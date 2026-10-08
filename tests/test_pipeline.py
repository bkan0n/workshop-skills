import importlib.util
import hashlib
import io
import json
import shutil
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from validate import metadata, validate_links, validate_coverage
from package import archive_bytes, package_files, verify_freshness, build
from release import verify_artifacts

spec=importlib.util.spec_from_file_location('refresh_wiki',Path(__file__).resolve().parents[1]/'scripts/refresh-wiki.py')
refresh=importlib.util.module_from_spec(spec)
spec.loader.exec_module(refresh)


class PipelineTests(unittest.TestCase):
    def test_companion_links_only_allowed_from_overpy(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            for skill in ('overwatch-workshop','overpy'):
                (root/'skills'/skill).mkdir(parents=True)
                (root/'skills'/skill/'SKILL.md').write_text('# Skill\n')
            opy=root/'skills/overpy/SKILL.md'
            opy.write_text('[Workshop](../overwatch-workshop/SKILL.md)\n')
            self.assertEqual(validate_links(root),[])
            native=root/'skills/overwatch-workshop/SKILL.md'
            native.write_text('[OverPy](../overpy/SKILL.md)\n')
            self.assertTrue(any('permitted' in e for e in validate_links(root)))
            opy.write_text('[Missing](references/absent.md)\n')
            self.assertTrue(any('missing' in e for e in validate_links(root)))

    def test_anchor_validation(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);p=root/'skills/overwatch-workshop';p.mkdir(parents=True)
            (p/'SKILL.md').write_text('[Claim](ref.md#claim-1)\n')
            (p/'ref.md').write_text('<a id="claim-1"></a>\n# Fact\n')
            self.assertEqual(validate_links(root,('overwatch-workshop',)),[])
            (p/'ref.md').write_text('# Different\n')
            self.assertTrue(any('anchor' in e for e in validate_links(root,('overwatch-workshop',))))

    def test_yaml_metadata_duplicate_and_nesting(self):
        fields=metadata('---\nname: overpy\ndescription: >\n  A folded description\nmetadata:\n  workshop-skills-version: "0.1.0"\n---\n')
        self.assertEqual(fields['description'],'A folded description')
        self.assertEqual(fields['metadata.workshop-skills-version'],'0.1.0')
        with self.assertRaisesRegex(ValueError,'Duplicate'):
            metadata('---\nname: one\nname: two\n---\n')

    def test_missing_note_is_not_covered_by_article_signature(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            files={
                'docs/research/workshop-wiki-survey-2026-10-07/article-ledger.json':[{'id':1,'source_content_sha256':'hash','important_information':['Useful quirk']}],
                'sources/wiki-content.json':{'articles':[{'id':1,'source_content_sha256':'hash','disposition':'catalog-covered','notes':[]}]},
                'coverage/wiki-coverage.json':{'articles':[{'id':1}]}}
            for filename,value in files.items():
                p=root/filename;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(value))
            errors,_=validate_coverage(root)
            self.assertTrue(any('missing or duplicate survey notes' in e for e in errors))

    def test_archive_bytes_ignore_input_order_and_have_fixed_modes(self):
        first=archive_bytes({'b.txt':b'b','a.txt':b'a'})
        self.assertEqual(first,archive_bytes({'a.txt':b'a','b.txt':b'b'}))
        with zipfile.ZipFile(io.BytesIO(first)) as z:
            self.assertEqual(z.namelist(),['a.txt','b.txt'])
            self.assertEqual(z.getinfo('a.txt').date_time,(1980,1,1,0,0,0))
            self.assertEqual(z.getinfo('a.txt').external_attr>>16,0o100644)
        with self.assertRaisesRegex(ValueError,'Unsafe'):
            archive_bytes({'../escape':b'x'})

    def test_failed_snapshot_cannot_imply_deleted_articles(self):
        old=[{'id':1,'title':'One','content_sha256':'a'}]
        with self.assertRaisesRegex(ValueError,'incomplete'):
            refresh.review_queue(old,[],{'articles':[]},{'article_count':0})
        with self.assertRaisesRegex(ValueError,'terminal'):
            refresh.review_queue(old,old,{'articles':[]},{'article_count':1,'populated_pages':2,'first_empty_page':2})

    def test_changed_signature_only_article_routes_to_catalog(self):
        old=[{'id':1,'title':'One','content_sha256':'a'}]
        new=[{'id':1,'title':'One','content_sha256':'b'}]
        corpus={'articles':[{'id':1,'notes':[],'catalog_destination':'skills/example.md'}]}
        q=refresh.review_queue(old,new,corpus,{'article_count':1,'populated_pages':1,'first_empty_page':2,'fetched_at':'date'})
        self.assertEqual(q['changes'][0]['references_to_review'],['skills/example.md'])
        self.assertFalse(q['curated_files_modified'])

    def test_metadata_changes_route_related_claims_and_table_parts(self):
        old=[{'id':1,'title':'Old','content_sha256':'a'}]
        new=[{'id':1,'title':'New','content_sha256':'a'}]
        corpus={'articles':[{'id':1,'notes':[{'destination':'claim.md','related_destinations':['helper.md']}],'tables':['data.md']}]}
        tables=[{'source_article_id':1,'destination':'data.md','tables':[{'destination':'data/map.md'}]}]
        q=refresh.review_queue(old,new,corpus,{'article_count':1,'populated_pages':1,'first_empty_page':2,'fetched_at':'date'},tables)
        self.assertEqual(q['changes'][0]['changed_fields'],['title'])
        self.assertEqual(q['changes'][0]['references_to_review'],['claim.md','data.md','data/map.md','helper.md'])

    def test_release_checks_files_against_checkout_not_self_asserted_manifest(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder).resolve()
            for name in ('overwatch-workshop','overpy'):
                dest=root/'skills'/name;dest.mkdir(parents=True)
                (dest/'SKILL.md').write_text('Required content for '+name)
            for name in ('LICENSE','THIRD_PARTY_NOTICES.md','INSTALL.md'):
                (root/name).write_text(name)
            (root/'sources').mkdir();(root/'sources/lock.json').write_text('{"release":"0.1.0"}')
            (root/'dist').mkdir()
            checks=[]
            for kind,skills in [('workshop',('overwatch-workshop',)),('workshop-overpy',('overwatch-workshop','overpy'))]:
                file=root/'dist'/f'{kind}-skills-0.1.0.zip'
                file.write_bytes(archive_bytes(package_files(root,skills,{'commit':'abc','dirty':False},'0.1.0',{'release':'0.1.0'})))
                checks.append(f'{hashlib.sha256(file.read_bytes()).hexdigest()}  {file.name}\n')
            (root/'dist/SHA256SUMS').write_text(''.join(checks))
            self.assertEqual(len(verify_artifacts('v0.1.0','abc',root)),2)
            file=root/'dist/workshop-skills-0.1.0.zip'
            fake={'version':'0.1.0','repository':{'commit':'abc','dirty':False},'source_locks':{'release':'0.1.0'},'files':{}}
            file.write_bytes(archive_bytes({'RELEASE.json':json.dumps(fake).encode()}))
            checks[0]=f'{hashlib.sha256(file.read_bytes()).hexdigest()}  {file.name}\n'
            (root/'dist/SHA256SUMS').write_text(''.join(checks))
            with self.assertRaisesRegex(ValueError,'differs from the files'):
                verify_artifacts('v0.1.0','abc',root)

    def test_build_rejects_changed_generated_prose_without_raw_archive(self):
        source=Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder).resolve()
            for name in ('skills','sources','coverage'):
                shutil.copytree(source/name,root/name)
            for name in ('scripts/generate-api.mjs','scripts/generate-wiki.py','docs/research/workshop-wiki-survey-2026-10-07/article-ledger.json'):
                target=root/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source/name,target)
            verify_freshness(root)
            article=root/'skills/overwatch-workshop/references/wiki/articles/4480.md'
            article.write_text(article.read_text()+'Unreviewed mutation.\n')
            with self.assertRaisesRegex(ValueError,'Generated content is stale'):
                build(root)


if __name__=='__main__':
    unittest.main()

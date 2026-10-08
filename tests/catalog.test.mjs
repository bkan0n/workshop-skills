import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import {pathToFileURL} from 'node:url';
import { normalize, publicCallable, callableSignature, defaultValue, buildOutputs } from '../scripts/generate-api.mjs';

const snapshot=JSON.parse(fs.readFileSync(new URL('../sources/overpy-api.json',import.meta.url),'utf8'));

test('public surface excludes implementation forms but preserves member calls',()=>{
  assert.equal(publicCallable('__add__',{}),false);
  assert.equal(publicCallable('temporary',{hideFromAutocomplete:true}),false);
  assert.equal(publicCallable('.getHealth',{}),true);
  assert.equal(publicCallable('__',{}),true);
  assert.equal(publicCallable('___',{}),true);
  assert.equal(publicCallable('random.choice',{}),false); // supplied by the module catalog
});

test('member receiver is removed once and optional defaults remain language-specific',()=>{
  const entry={class:'Player','en-US':'Example',args:[{name:'player',type:'Player'},{name:'mode',type:'Wait',default:'IGNORE_CONDITION'}]};
  assert.equal(callableSignature('.example',entry,'overpy',snapshot.data),'<Player>.example(mode=Wait.IGNORE_CONDITION)');
  assert.equal(callableSignature('.example',entry,'workshop',snapshot.data),'Example(player, mode)');
});

test('normalization preserves English facts while removing translations and functions',()=>{
  assert.deepEqual(normalize({'fr-FR':'Bonjour','en-US':'Hello',nested:{description:{'en-US':'Fact'},value:0},fn:()=>0}),{'en-US':'Hello',nested:{description:{'en-US':'Fact'},value:0}});
});

test('source-expression and literal-enum defaults are not JSON strings',()=>{
  assert.equal(defaultValue({type:'Color',default:'WHITE'},snapshot.data),'Color.WHITE');
  assert.equal(defaultValue({type:'Team',default:'ALL'},snapshot.data),'Team.ALL');
  assert.equal(defaultValue({type:['Player',{Array:'Player'}],default:'getAllPlayers()'},snapshot.data),'getAllPlayers()');
  assert.equal(defaultValue({type:'unsigned float',default:'Math.INFINITY'},snapshot.data),'Math.INFINITY');
  assert.equal(defaultValue({type:'Team',default:'TEAM'},snapshot.data),null);
  assert.equal(defaultValue({type:'Lambda',default:'<current array element>'},snapshot.data),null);
});

test('catalog preserves native internal operations without advertising them as OverPy calls',()=>{
  const files=buildOutputs(snapshot);
  const native=files.get('skills/overwatch-workshop/references/api/values/add.md');
  assert.ok(native?.includes('Add('));
  assert.ok(![...files.keys()].some(file=>file==='skills/overpy/references/api/values/add.md'));
  const method=files.get('skills/overpy/references/api/values/member-get-health.md');
  assert.ok(method.includes('<Player>.getHealth()'));
  assert.ok(method.includes('overwatch-workshop/references/api/values/health.md'));
  for(const file of ['translate','translate-without-player-var','deferred-translation']) assert.ok(files.has(`skills/overpy/references/api/functions/${file}.md`));
  assert.ok(files.get('skills/overwatch-workshop/references/api/constants/beam.md').includes('Requires extension `beamEffects`'));
  assert.ok(files.get('skills/overwatch-workshop/references/api/constants/color.md').includes('OverPy-only alias'));
  assert.ok(files.get('skills/overpy/references/api/functions/sorted.md').includes('sorted(array, key=lambda item: item)'));
  assert.ok(files.get('skills/overpy/references/api/functions/member-format.md').includes('format(value, ...)'));
  assert.ok(files.get('skills/overwatch-workshop/references/api/settings/heroes-ana.md').includes('`heroes.<team>.ana`'));
});

test('no overwrite on native label collisions',()=>{
  const changed=structuredClone(snapshot);
  changed.data.actionKw.fake=structuredClone(changed.data.actionKw.wait);
  assert.throws(()=>buildOutputs(changed),/collision/);
});

test('task routers offer small usage groups and retain alphabetical lookup',()=>{
  const files=buildOutputs(snapshot);
  for(const skill of ['overwatch-workshop','overpy']) {
    const base=`skills/${skill}/references/api`;
    const router=files.get(`${base}/usage/index.md`);
    assert.ok(router, `${skill} has a usage router`);
    assert.ok(router.length < 4000, 'router stays small enough to select a task');
    assert.match(router,/State and arrays/);
    assert.match(router,/Combat and abilities/);
    assert.ok(!router.includes('getHealth('), 'router does not dump signatures');
    assert.match(files.get(`${base}/index.md`),/usage\/index\.md/);
    assert.ok(files.has(`${base}/actions/index.md`));
  }
  assert.match(files.get('skills/overwatch-workshop/references/api/usage/combat-abilities.md'),/\[Health\]\(\.\.\/values\/health\.md\)/);
  assert.match(files.get('skills/overpy/references/api/usage/combat-abilities.md'),/member-get-health\.md/);
  assert.match(files.get('skills/overpy/references/api/usage/math-random.md'),/\.\.\/modules\/random-uniform\.md/);
  assert.match(files.get('skills/overpy/references/api/usage/math-random.md'),/\.\.\/functions\/log\.md/);
  assert.match(files.get('skills/overpy/references/api/usage/state-arrays.md'),/\.\.\/functions\/tabular\.md/);
  assert.match(files.get('skills/overpy/references/api/usage/debugging.md'),/\.\.\/macros\/print\.md/);
});

test('every callable has one usage route that resolves to its exact local entry',()=>{
  const files=buildOutputs(snapshot);
  for(const skill of ['overwatch-workshop','overpy']) {
    const base=`skills/${skill}/references/api`;
    const expected=[...files.keys()].filter(file=>new RegExp(`^${base}/(actions|values|functions|macros|modules|members)/[^/]+\\.md$`).test(file)&&!/^index(?:-[a-z0-9]|-symbols)?\.md$/.test(path.posix.basename(file)));
    const reached=[];
    for(const [file,body] of files) {
      if(!file.startsWith(`${base}/usage/`)||file.endsWith('/index.md'))continue;
      for(const match of body.matchAll(/\]\((\.\.\/[^)]+)\)/g)) {
        const target=path.posix.normalize(path.posix.join(path.posix.dirname(file),match[1]));
        assert.ok(files.has(target),`${file} links to existing ${target}`);
        reached.push(target);
      }
    }
    assert.deepEqual(reached.sort(),expected.sort());
  }
});

test('new or removed source callables require explicit usage classification review',()=>{
  const added=structuredClone(snapshot);
  added.data.opyFuncs.newCallable={args:[],description:'Newly introduced source function'};
  assert.throws(()=>buildOutputs(added),/Unclassified callable.*opyFuncs\.newCallable/);
  const removed=structuredClone(snapshot);
  delete removed.data.opyFuncs.debug;
  assert.throws(()=>buildOutputs(removed),/Stale usage assignment.*opyFuncs\.debug/);
});

test('small snapshot fixtures can supply reviewed usage assignments',()=>{
  const fixture={data:Object.fromEntries(Object.keys(snapshot.data).map(key=>[key,{}]))};
  fixture.data.actionKw.wait=snapshot.data.actionKw.wait;
  const group={id:'timing-control',title:'Timing and control',description:'Wait and sequence actions.',entries:{actionKw:['wait']}};
  const files=buildOutputs(fixture,{usageGroups:[group]});
  assert.match(files.get('skills/overwatch-workshop/references/api/usage/timing-control.md'),/wait\.md/);
  assert.throws(()=>buildOutputs(fixture,{usageGroups:[group,{...group,id:'duplicate'}]}),/assigned more than once.*actionKw\.wait/);
});

test('source article reading links resolve to the locally bundled full archive',()=>{
  const files=buildOutputs(snapshot);
  for(const file of ['skills/overpy/references/api/constants/texture.md','skills/overpy/references/api/directives/setup-tags.md']) {
    const body=files.get(file);
    assert.ok(body.includes('overwatch-workshop/references/wiki/archive/9562.md'), file);
    assert.ok(!body.includes('https://workshop.codes'), 'Workshop article reading stays offline');
  }
});

test('catalog generation needs only tracked sources, without an ignored archive checkout',async()=>{
  const root=fs.mkdtempSync(path.join(os.tmpdir(),'workshop-catalog-'));
  try {
    fs.mkdirSync(path.join(root,'scripts'));
    fs.mkdirSync(path.join(root,'sources'));
    for(const file of ['scripts/generate-api.mjs','sources/api-usage.json','sources/wiki-articles.json']) {
      fs.copyFileSync(new URL(`../${file}`,import.meta.url),path.join(root,file));
    }
    assert.equal(fs.existsSync(path.join(root,'archive')),false);
    const generator=await import(pathToFileURL(path.join(root,'scripts/generate-api.mjs')).href);
    const files=generator.buildOutputs(snapshot);
    assert.match(files.get('skills/overpy/references/api/constants/texture.md'),/wiki\/archive\/9562\.md/);
  } finally {
    fs.rmSync(root,{recursive:true,force:true});
  }
});

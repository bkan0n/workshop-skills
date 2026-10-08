import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
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

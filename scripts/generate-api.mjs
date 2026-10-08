#!/usr/bin/env node
/** Deterministic Markdown catalogs from reviewed, English-only OverPy exports. */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const SNAPSHOT = 'sources/overpy-api.json';
const COMMIT = '5a7d0e294b8cad73b9701987bb584d0551d7fa4d';
const SOURCE = `https://github.com/Zezombye/overpy/tree/${COMMIT}/src`;
const WORKSHOP = 'skills/overwatch-workshop/references/api';
const OVERPY = 'skills/overpy/references/api';
const USAGE = 'sources/api-usage.json';
const GROUPS = ['actionKw', 'valueFuncKw', 'constantValues', 'annotations', 'eventKw', 'eventTeamKw', 'eventSlotKw', 'eventPlayerKw', 'heroKw', 'mapKw', 'opyFuncs', 'opyMemberFuncs', 'opyKeywords', 'opyConstants', 'opyModules', 'opyMacros', 'preprocessingDirectives', 'customGameSettingsSchema'];
const compare = (a, b) => a < b ? -1 : a > b ? 1 : 0;
export const slug = value => value.replace(/([a-z0-9])([A-Z])/g, '$1-$2').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'symbol';
export const internal = key => key.startsWith('__') && key.endsWith('__') && !['__','___'].includes(key);
const functionSlug = key => ({'_':'translate','__':'translate-without-player-var','___':'deferred-translation'})[key] || slug(key);
export const publicCallable = (key, value) => !internal(key) && !value.hideFromAutocomplete && (!key.includes('.') || key.startsWith('.'));
export function normalize(value) {
  if (Array.isArray(value)) return value.map(normalize);
  if (value && typeof value === 'object') return Object.fromEntries(Object.keys(value).sort(compare)
    .filter(key => (!/^[a-z]{2}-[A-Z]{2}$/.test(key) || key === 'en-US') && !['guid'].includes(key) && typeof value[key] !== 'function')
    .map(key => [key, normalize(value[key])]));
  return value;
}
const json = value => JSON.stringify(value, null, 2) + '\n';
const description = value => (typeof value === 'string' ? value : value?.['en-US'] || '')
  .replaceAll('__extensionDescription__', 'Compile the project to obtain its extension-point usage; this catalog has no project-specific totals.')
  .replaceAll('__iconDescription__', 'Icon appearance is not bundled; this entry identifies the symbol only.');
const safe = value => String(value ?? '').replaceAll('|', '\\|').replaceAll('\n', ' ');
export function typeName(value) {
  if (Array.isArray(value)) return value.map(typeName).join(' | ');
  if (value && typeof value === 'object') return Object.entries(value).map(([k,v]) => `${k}<${typeName(v)}>`).join(' | ');
  return String(value ?? 'not specified');
}
export function defaultValue(arg, data) {
  if (typeof arg.default === 'string') {
    const values = data.constantValues[arg.type] || data.constantValues[arg.type + 'Literal'] || data.opyConstants[arg.type];
    if (values) return Object.hasOwn(values, arg.default) ? `${arg.type.replace(/Literal$/, '')}.${arg.default}` : null;
    if (/^<.*>$/.test(arg.default)) return null; // human metadata label, not an expression
    return arg.default; // upstream stores source expressions, not JSON string literals
  }
  return JSON.stringify(arg.default);
}
function sourceFooter(sourceFile = '') {
  return `\nSource: [OverPy 9.7.17](${SOURCE}${sourceFile ? '/' + sourceFile : ''}). Generated from pinned initialized exports.\n`;
}
export function callableSignature(key, value, dialect, data) {
  if (dialect === 'overpy' && key === 'sorted') return 'sorted(array, key=lambda item: item)';
  if (dialect === 'overpy' && key === '.format') return '<String>.format(value, ...)';
  let args = value.args;
  let name = dialect === 'workshop' ? value['en-US'] : key;
  if (dialect === 'overpy' && key.startsWith('.')) {
    name = `<${value.class || typeName(args?.[0]?.type) || 'receiver'}>${key}`;
    args = args?.slice(1);
  }
  if (args === null || args === undefined) return name;
  if (dialect === 'workshop' && args.length === 0) return name;
  return `${name}(${args.map(arg => arg.name + (dialect === 'overpy' && arg.default !== undefined ? (defaultValue(arg,data) === null ? '?' : '=' + defaultValue(arg, data)) : '')).join(', ')})`;
}
function defaultNote(arg, data) {
  if (arg.default === undefined) return '';
  const value = defaultValue(arg,data);
  if (value !== null) return ` Default: \`${safe(value)}\`.`;
  if (/^<.*>$/.test(String(arg.default))) return ` Optional; upstream describes the omitted expression as \`${safe(arg.default)}\`. This label is not literal source syntax.`;
  return ` Upstream marks this optional but its default \`${safe(arg.default)}\` does not match the declared enum. Supply a valid explicit argument; do not copy that default as source.`;
}
function parameterTable(args, dialect, data, includeMeaning = true) {
  if (!args?.length) return '';
  return '\n| Argument | Type | ' + (includeMeaning ? 'Meaning' : 'OverPy') + (dialect === 'overpy' ? ' / default' : '') + ' |\n| --- | --- | --- |\n' + args.map(arg => `| \`${arg.name}\` | \`${safe(typeName(arg.type))}\` | ${includeMeaning ? safe(description(arg.description)) : ''}${dialect === 'overpy' ? defaultNote(arg,data) : ''} |`).join('\n') + '\n';
}
export function buildOutputs(snapshot, {usageGroups, articleLinks} = {}) {
  const data = snapshot.data;
  const output = new Map();
  const mappings = [];
  const usageEntries = [];
  usageGroups ??= JSON.parse(fs.readFileSync(path.join(ROOT,USAGE),'utf8')).groups;
  articleLinks ??= JSON.parse(fs.readFileSync(path.join(ROOT,'sources/wiki-articles.json'),'utf8')).articles;
  const articlesBySlug = new Map(articleLinks.flatMap(article=>[[String(article.id),article],[article.slug,article]]));
  const corpusPath=path.join(ROOT,'sources/wiki-content.json');
  if(fs.existsSync(corpusPath))for(const record of JSON.parse(fs.readFileSync(corpusPath,'utf8')).articles){
    const target=articlesBySlug.get(String(record.source_revision_id ?? record.id)) ?? {id:record.id,title:record.title};
    for(const alias of [...(record.source_slugs ?? []),...(record.revision_ids ?? []).map(String)]){
      if(!articlesBySlug.has(alias))articlesBySlug.set(alias,target);
    }
  }
  const addMapping = (sourceGroup, record) => {
    mappings.push(record);
    usageEntries.push({...record, sourceGroup});
  };
  const set = (file, content) => {
    if (output.has(file)) throw new Error(`Catalog path collision: ${file}`);
    content = content.replace(/https:\/\/workshop\.codes\/wiki\/articles\/([a-zA-Z0-9_-]+)/g,(_,slug)=>{
      const article=articlesBySlug.get(slug);
      if(!article)throw new Error(`No bundled article for Workshop reading link: ${slug}`);
      const target=path.posix.relative(path.posix.dirname(file),`skills/overwatch-workshop/references/wiki/archive/${article.id}.md`);
      return `[${article.title.replaceAll('[','\\[').replaceAll(']','\\]')}](${target})`;
    });
    output.set(file, content.split('\n').map(line => line.trimEnd()).join('\n').trimEnd() + '\n');
  };
  function index(base, title, entries, intro = '') {
    const sorted = entries.sort((a,b) => compare(a.label, b.label));
    const render = list => list.map(item => `- [${item.label.replaceAll('[','\\[').replaceAll(']','\\]')}](${item.file})`).join('\n');
    if (sorted.length <= 65) set(`${base}/index.md`, `# ${title}\n\n${intro}\n\n${render(sorted)}`);
    else {
      const buckets = new Map();
      for (const item of sorted) {
        const letter = item.label.replace(/^[^A-Za-z0-9]+/, '').charAt(0).toUpperCase();
        const bucket = /[A-Z0-9]/.test(letter) ? letter : 'Symbols';
        if (!buckets.has(bucket)) buckets.set(bucket, []);
        buckets.get(bucket).push(item);
      }
      const links=[];
      for (const [bucket, items] of [...buckets].sort(([a],[b])=>compare(a,b))) {
        const file = `index-${bucket.toLowerCase()}.md`;
        set(`${base}/${file}`, `# ${title}: ${bucket}\n\n${render(items)}`);
        links.push(`- [${bucket}](${file}) — ${items.length} entries`);
      }
      set(`${base}/index.md`, `# ${title}\n\n${intro}\n\nChoose the first letter; read only the matching entry.\n\n${links.join('\n')}`);
    }
  }
  for (const [group, folder] of [['actionKw','actions'],['valueFuncKw','values']]) {
    const entries=[];
    for (const [key,value] of Object.entries(data[group])) {
      if (!value['en-US']) throw new Error(`No native label for ${group}.${key}`);
      const file = `${slug(value['en-US'])}.md`;
      const signature = callableSignature(key,value,'workshop',data);
      const text = `# ${value['en-US']}\n\nNative Workshop ${folder === 'actions' ? 'action' : 'value'}. Signature labels below describe argument order; replace them with expressions.\n\n\`${signature}\`\n\n${description(value.description)}\n${parameterTable(value.args,'workshop',data)}\n${value.return ? `Returns: \`${typeName(value.return)}\`. Types are OverPy's model of native inputs.\n` : ''}${value.extension ? `Requires the \`${value.extension}\` extension.\n` : ''}${sourceFooter(`data/${folder}.ts`)}`;
      set(`${WORKSHOP}/${folder}/${file}`,text);
      entries.push({label:value['en-US'],file});
      addMapping(group,{dialect:'workshop',kind:folder,key,name:value['en-US'],path:`${WORKSHOP}/${folder}/${file}`});
    }
    index(`${WORKSHOP}/${folder}`,`Native Workshop ${folder}`,entries,'English names from pinned compiler data; dated semantic exceptions are in the topic guides and wiki supplements.');
  }
  for (const [group,folder] of [['actionKw','actions'],['valueFuncKw','values'],['opyFuncs','functions'],['opyMacros','macros']]) {
    const entries=[];
    for (const [key,value] of Object.entries(data[group])) {
      if (!publicCallable(key,value)) continue;
      const file = `${key.startsWith('.') ? 'member-' : ''}${functionSlug(key)}.md`;
      const signature=callableSignature(key,value,'overpy',data);
      const receiver=key.startsWith('.') ? `Receiver: \`${value.class || typeName(value.args?.[0]?.type)}\`. The receiver supplies the first compiler argument.\n` : '';
      let args=key.startsWith('.') ? value.args?.slice(1) : value.args;
      if(key==='sorted')args=args.map((arg,i)=>i===1?{...arg,name:'key',default:'lambda item: item'}:arg);
      const native=value['en-US'] ? `Native operation: [${value['en-US']}](../../../../overwatch-workshop/references/api/${folder}/${slug(value['en-US'])}.md).\n` : '';
      set(`${OVERPY}/${folder}/${file}`,`# ${key.startsWith('.') ? 'receiver' : ''}${key}\n\n\`${signature}\`\n\n${receiver}\n${native ? 'Runtime meaning and argument semantics are documented in the native operation linked below.' : description(value.description)}\n${parameterTable(args,'overpy',data,!native)}\n${value.return ? `Returns: \`${typeName(value.return)}\`.\n` : ''}${native}${value.macro ? '\nMacro expansion (compiler implementation; not a second runtime function):\n\n```opy\n' + value.macro.trim() + '\n```\n' : ''}${sourceFooter()}`);
      entries.push({label:key.startsWith('.') ? `receiver${key}` : key,file});
      addMapping(group,{dialect:'overpy',kind:folder,key,name:signature,path:`${OVERPY}/${folder}/${file}`});
    }
    index(`${OVERPY}/${folder}`,`OverPy ${folder}`,entries,'Optional defaults belong to OverPy. Check the Workshop topic guide when runtime semantics matter.');
  }
  const moduleEntries=[];
  for(const [moduleName,module] of Object.entries(data.opyModules)) for(const [key,value] of Object.entries(module)) {
    if(key==='description'||!value||typeof value!=='object'||!publicCallable(key,value)) continue;
    const name=`${moduleName}.${key}`,file=`${slug(name)}.md`;
    set(`${OVERPY}/modules/${file}`,`# ${name}\n\n\`${callableSignature(name,value,'overpy',data)}\`\n\n${description(value.description)}\n${parameterTable(value.args,'overpy',data)}\nReturns: \`${typeName(value.return)}\`.${sourceFooter('data/opy/modules.ts')}`);
    moduleEntries.push({label:name,file});
    addMapping('opyModules',{dialect:'overpy',kind:'modules',key:name,name:callableSignature(name,value,'overpy',data),path:`${OVERPY}/modules/${file}`});
  }
  index(`${OVERPY}/modules`,'OverPy modules',moduleEntries);
  const memberEntries=[];
  for(const [key,value] of Object.entries(data.opyMemberFuncs)) {
    if(!publicCallable(key,value))continue;
    const file=`${slug(key)}.md`;
    set(`${OVERPY}/members/${file}`,`# ${value.class}.${key}\n\n\`<${value.class}>.${key}${Array.isArray(value.args) ? '('+value.args.map(a=>a.name).join(', ')+')' : ''}\`\n\n${description(value.description)}\n${parameterTable(value.args,'overpy',data)}\nReturns: \`${typeName(value.return)}\`.${sourceFooter('data/opy/memberFunctions.ts')}`);
    memberEntries.push({label:`${value.class}.${key}`,file});
    addMapping('opyMemberFuncs',{dialect:'overpy',kind:'members',key,name:`${value.class}.${key}`,path:`${OVERPY}/members/${file}`});
  }
  index(`${OVERPY}/members`,'Additional member properties',memberEntries,'Player member functions are listed with actions/values/macros.');
  for(const [group,folder,prefix] of [['annotations','annotations',''],['preprocessingDirectives','directives','#!'],['opyKeywords','keywords','']]) {
    const entries=[];
    for(const [key,value] of Object.entries(data[group])) {
      if(internal(key)||value.hideFromAutocomplete)continue;
      const file=`${slug(key)}.md`;
      let text=`# ${prefix}${key}\n\n${description(value.description)}\n`;
      if(value.args) text+=parameterTable(value.args,'overpy',data);
      for(const arg of value.args??[])if(arg.values)text+=`\n\`${arg.name}\` choices: ${arg.values.filter(x=>!internal(x)).map(x=>'`'+x+'`').join(', ')}.\n`;
      if(value.snippet)text+=`\nEditor snippet template (dollar placeholders are not source syntax):\n\n\`\`\`text\n${value.snippet}\n\`\`\`\n`;
      set(`${OVERPY}/${folder}/${file}`,text+sourceFooter());entries.push({label:prefix+key,file});
    }
    index(`${OVERPY}/${folder}`,`OverPy ${folder}`,entries);
  }
  for(const [group,base] of [['constantValues',WORKSHOP],['opyConstants',OVERPY]]) {
    const entries=[];
    for(const [key,values] of Object.entries(data[group])) {
      const name=key.replace(/Literal$/,''),file=`${slug(name)}.md`;
      const items=Object.entries(values).filter(([k,v])=>k!=='description'&&v&&typeof v==='object'&&!v.onlyInOw1);
      const native=group==='constantValues';
      const rows=items.map(([k,v])=>{
        const notes=[description(v.description).replace(/<tx[^>]*>/g,tag=>'`'+tag+'`')];
        if(v.onlyInOverpy)notes.push('OverPy-only alias; not a direct native enum choice.');
        if(['red','green','blue'].every(channel=>typeof v[channel]==='number'))notes.push(`RGB channels: ${v.red}, ${v.green}, ${v.blue}.`);
        if(v.extension)notes.push(`Requires extension \`${v.extension}\`.`);
        return `| ${native? (v.onlyInOverpy?'OverPy-only alias':'`'+safe(v['en-US']||'(no native label)')+'`')+' | ':''}${internal(key)? 'Use the native choice' : '`'+safe(name+'.'+k)+'`'} | ${safe(notes.filter(Boolean).join(' '))} |`;
      }).join('\n');
      set(`${base}/constants/${file}`,`# ${name}\n\n${description(values.description)}\n\n${internal(key)? 'Compiler enum name is internal; use the native choices in the appropriate action field.\n' : ''}${items.some(([,v])=>v.extension)? '\nExtension costs and activation: [settings schema]('+(native?'../settings/extensions.md':'../../../../overwatch-workshop/references/api/settings/extensions.md')+').\n':''}\n| ${native?'Native English choice | ':''}OverPy symbol | Note |\n| ${native?'--- | ':''}--- | --- |\n${rows}\n${sourceFooter()}`);
      entries.push({label:name,file});
    }
    index(`${base}/constants`,group==='constantValues'?'Workshop choices and OverPy enum spellings':'OverPy helper constants',entries);
  }
  const events=[];
  for(const [key,value] of Object.entries(data.eventKw)) {
    const file=slug(value['en-US'])+'.md';
    set(`${WORKSHOP}/events/${file}`,`# ${value['en-US']}\n\nNative event: \`${value['en-US']}\`.\n\nOverPy event key: \`${key}\`${internal(key)? ' (internal; declare a subroutine instead of using this as a public @Event value)' : ''}.\n\nRead [event context and triggering](../../execution.md) before choosing context values. Exact event names do not establish which values are available.\n${sourceFooter()}`);
    events.push({label:value['en-US'],file});
  }
  index(`${WORKSHOP}/events`,'Workshop events',events);
  for(const [group,title]of [['eventTeamKw','Team filters'],['eventPlayerKw','Player and hero filters'],['heroKw','Heroes'],['mapKw','Maps']]) {
    const folder=slug(group),entries=[];
    for(const [key,value]of Object.entries(data[group])) {
      const file=slug(key)+'.md';
      const detail=Object.fromEntries(Object.entries(value).filter(([k])=>k!=='en-US'));
      set(`${WORKSHOP}/${folder}/${file}`,`# ${value['en-US']||key}\n\nCompiler key: \`${key}\`; native English label: \`${value['en-US']||'not specified'}\`.\n\n${Object.keys(detail).length?'Pinned metadata (data, not source code):\n\n```json\n'+JSON.stringify(detail,null,2)+'\n```\n':''}${sourceFooter()}`);
      entries.push({label:value['en-US']||key,file});
    }
    index(`${WORKSHOP}/${folder}`,title,entries,'Pinned OverPy names; consult the bundled wiki for hero and map behavior.');
  }
  const settingsEntries=[];
  for(const [category,schema]of Object.entries(data.customGameSettingsSchema)) {
    const parts=['heroes','gamemodes'].includes(category) ? Object.entries(schema.values||{}).map(([key,value])=>[`${category}.${key}`,value]) : [[category,schema]];
    for(const [key,value]of parts) {
      const file=slug(key)+'.md';
      const teamContext=category==='heroes'? '\nHero settings require a team wrapper: `heroes.<team>.'+key.split('.').slice(1).join('.')+'`. Replace `<team>` with '+Object.keys(schema.teams).map(t=>'`'+t+'`').join(', ')+'. Native team labels: '+Object.entries(schema.teams).map(([k,v])=>'`'+k+'` = '+v['en-US']).join('; ')+'. The heading identifies a schema fragment, not a complete object path.\n' : '';
      set(`${WORKSHOP}/settings/${file}`,`# Settings: ${key}\n\nNormalized schema from the pinned compiler. Keys describe the OverPy settings object; \`en-US\` fields give native labels. This JSON is reference data, not a pasteable preset. \`values\` describes nested choices or accepted types; internal type tokens are compiler constraints. Keep unspecified settings from the user's preset.\n${teamContext}\n\`\`\`json\n${JSON.stringify(value,null,2)}\n\`\`\`\n${sourceFooter()}`);
      settingsEntries.push({label:key,file});
    }
  }
  index(`${WORKSHOP}/settings`,'Custom-game settings schema',settingsEntries,'Read only the relevant mode, hero, or lobby section. The schema describes compiler inputs; consult the bundled wiki for settings behavior.');
  const callableIds = new Set(usageEntries.map(entry=>`${entry.sourceGroup}.${entry.key}`));
  const assignments = new Map();
  const groupIds = new Set();
  for(const group of usageGroups) {
    if(!/^[a-z][a-z0-9-]*$/.test(group.id)||groupIds.has(group.id))throw new Error(`Invalid or duplicate usage group: ${group.id}`);
    groupIds.add(group.id);
    for(const [sourceGroup,keys] of Object.entries(group.entries)) for(const key of keys) {
      const id=`${sourceGroup}.${key}`;
      if(assignments.has(id))throw new Error(`Callable assigned more than once: ${id}`);
      if(!callableIds.has(id))throw new Error(`Stale usage assignment: ${id}`);
      assignments.set(id,group.id);
    }
  }
  for(const id of callableIds)if(!assignments.has(id))throw new Error(`Unclassified callable: ${id}; review ${USAGE} before publishing the new snapshot`);
  for(const [dialect,base] of [['workshop',WORKSHOP],['overpy',OVERPY]]) {
    const links=[];
    for(const group of usageGroups) {
      const entries=usageEntries.filter(entry=>entry.dialect===dialect&&assignments.get(`${entry.sourceGroup}.${entry.key}`)===group.id);
      if(!entries.length)continue;
      const label=entry=>dialect==='workshop'?entry.name:entry.kind==='members'?entry.name:entry.key.startsWith('.')?`receiver${entry.key}`:entry.key;
      const sections=[];
      for(const kind of ['actions','values','functions','macros','modules','members']) {
        const items=entries.filter(entry=>entry.kind===kind).sort((a,b)=>compare(label(a),label(b)));
        if(items.length)sections.push(`## ${kind.charAt(0).toUpperCase()+kind.slice(1)}\n\n${items.map(entry=>`- [${label(entry)}](${path.posix.relative(`${base}/usage`,entry.path)})`).join('\n')}`);
      }
      set(`${base}/usage/${group.id}.md`,`# ${group.title}\n\n${group.description}\n\nChoose the matching name, then read that entry only. [Browse tasks](index.md).\n\n${sections.join('\n\n')}`);
      links.push(`- [${group.title}](${group.id}.md) — ${group.description}`);
    }
    set(`${base}/usage/index.md`,`# ${dialect==='workshop'?'Workshop':'OverPy'} functions by task\n\nChoose the task you are implementing, read its group, then open only the relevant exact entries. Do not load every group or the whole catalog. For an already-known name, use the [alphabetical indexes](../index.md).\n\n${links.join('\n')}`);
  }
  set(`${WORKSHOP}/index.md`, `# Exact Workshop reference\n\nPinned to OverPy 9.7.17, English output. Use the [foundation router](../foundation.md) for behavior and [functions by task](usage/index.md) to find relevant operations. Use the alphabetical indexes below for an already-known name. Argument types describe compiler syntax; runtime behavior follows the bundled wiki articles.\n\n- [Actions](actions/index.md)\n- [Values](values/index.md)\n- [Events](events/index.md)\n- [Constants and choices](constants/index.md)\n- [Custom-game settings](settings/index.md)\n- [Event team filters](event-team-kw/index.md)\n- [Event player/hero filters](event-player-kw/index.md)\n- [Heroes](hero-kw/index.md)\n- [Maps](map-kw/index.md)\n\nFor source-reported exceptions and absent APIs, consult [wiki supplements](../wiki/index.md). The catalogs do not replace those notes.\n${sourceFooter()}`);
  set(`${OVERPY}/index.md`, `# Exact OverPy reference\n\nPinned to OverPy 9.7.17. Names and defaults follow the public completion surface; internal compiler identifiers are excluded. Use [functions by task](usage/index.md) to find relevant operations, or the alphabetical indexes below for an already-known name. Read only the matching entry. Angle-bracket receivers and parameter names are explanatory placeholders.\n\n- [Actions / player methods](actions/index.md)\n- [Values / player methods](values/index.md)\n- [Language functions](functions/index.md)\n- [Macros](macros/index.md)\n- [Modules](modules/index.md)\n- [Vector member properties](members/index.md)\n- [Keywords](keywords/index.md)\n- [Rule annotations](annotations/index.md)\n- [Preprocessing directives](directives/index.md)\n- [Helper constants](constants/index.md)\n- [Shared native constants and OverPy spellings](../../../overwatch-workshop/references/api/constants/index.md)\n- [Events](../../../overwatch-workshop/references/api/events/index.md)\n- [Settings schema](../../../overwatch-workshop/references/api/settings/index.md)\n\nOperators and syntax forms use the [language guide](../language.md), not internal names from compiler maps.\n${sourceFooter()}`);
  output.set('sources/api-map.json',json(mappings));
  const ledgerPath=path.join(ROOT,'docs/research/workshop-wiki-survey-2026-10-07/article-ledger.json');
  if(fs.existsSync(ledgerPath)) {
    const canonical = text => text.toLowerCase().replace(/[^a-z0-9]/g,'');
    const native = new Map(mappings.filter(x=>x.dialect==='workshop').map(x=>[canonical(x.name),x.path]));
    const wikiMap=Object.fromEntries(JSON.parse(fs.readFileSync(ledgerPath,'utf8')).filter(x=>native.has(canonical(x.title))).sort((a,b)=>a.id-b.id).map(x=>[String(x.id),native.get(canonical(x.title))]));
    output.set('sources/wiki-api-map.json',json(wikiMap));
  }
  return output;
}

async function main() {
  const check=process.argv.includes('--check');
  if(process.argv.includes('--snapshot')) {
    if(check) throw new Error('--snapshot mutates source data; cannot be combined with --check');
    const require=createRequire(import.meta.url),opy=require('overpy'),pkg=require('overpy/package.json');
    if(pkg.version!=='9.7.17')throw new Error(`Expected pinned OverPy 9.7.17, got ${pkg.version}`);
    await opy.readyPromise;
    for(const group of GROUPS)if(!opy[group]||!Object.keys(opy[group]).length)throw new Error(`Missing initialized export ${group}`);
    const lock=JSON.parse(fs.readFileSync(path.join(ROOT,'package-lock.json'),'utf8')).packages['node_modules/overpy'];
    const snapshot={schema_version:1,overpy_version:pkg.version,source_commit:COMMIT,package_integrity:lock.integrity,data:Object.fromEntries(GROUPS.map(group=>[group,normalize(opy[group])]))};
    fs.mkdirSync(path.join(ROOT,'sources'),{recursive:true});fs.writeFileSync(path.join(ROOT,SNAPSHOT),json(snapshot));
  }
  const snapshot=JSON.parse(fs.readFileSync(path.join(ROOT,SNAPSHOT),'utf8'));
  if(process.argv.includes('--verify-runtime')) {
    const require=createRequire(import.meta.url),opy=require('overpy'),pkg=require('overpy/package.json');
    await opy.readyPromise;
    const actual=Object.fromEntries(GROUPS.map(group=>[group,normalize(opy[group])]));
    if(pkg.version!==snapshot.overpy_version||json(actual)!==json(snapshot.data))throw new Error('Installed initialized OverPy exports differ from the checked-in source snapshot');
  }
  const outputs=buildOutputs(snapshot), errors=[];
  for(const [file,content]of outputs) {
    const dest=path.join(ROOT,file);
    if(check) {if(!fs.existsSync(dest)||fs.readFileSync(dest,'utf8')!==content)errors.push(file);}
    else {fs.mkdirSync(path.dirname(dest),{recursive:true});fs.writeFileSync(dest,content);}
  }
  for(const base of [WORKSHOP,OVERPY]) if(fs.existsSync(path.join(ROOT,base))) for(const entry of fs.readdirSync(path.join(ROOT,base),{recursive:true,withFileTypes:true})) {
    if(!entry.isFile())continue;
    const file=path.relative(ROOT,path.join(entry.parentPath,entry.name)).split(path.sep).join('/');
    if(!outputs.has(file)) {if(check)errors.push(`stale: ${file}`);else fs.unlinkSync(path.join(ROOT,file));}
  }
  if(errors.length)throw new Error(`Catalog drift: ${errors.slice(0,20).join(', ')}${errors.length>20?' ...':''}`);
  console.log(JSON.stringify({mode:check?'check':'generate',files:outputs.size,snapshot_sha256:crypto.createHash('sha256').update(fs.readFileSync(path.join(ROOT,SNAPSHOT))).digest('hex')}));
}
if(process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) main().catch(error=>{console.error(error.message);process.exitCode=1;});

#!/usr/bin/env python3
"""Read-only bounded legacy discovery; does not import or run legacy code."""
import collections, datetime, hashlib, json, os, pathlib, stat

ROOT = pathlib.Path('/Users/Shared/old/projects')
OUT = pathlib.Path('/Users/Shared/agent-org/factory/reports/legacy-retirement')
PRUNE = {'.git','node_modules','.venv','venv','__pycache__','.next','.cache','dist','build','target','.turbo','.ruff_cache','.pytest_cache','.mypy_cache','.svelte-kit','.nuxt','vendor'}
MAX_HASH = 32 * 1024 * 1024
totals, candidates, exclusions, symlinks = [], [], [], []
for top in sorted(ROOT.iterdir()):
    if top.is_symlink():
        symlinks.append({'path':str(top.relative_to(ROOT)), 'target':os.readlink(top), 'followed':False}); continue
    if not top.is_dir(): continue
    c = collections.Counter(); ext = collections.Counter(); hidden = collections.Counter()
    def error(e): exclusions.append({'path':os.path.relpath(e.filename,ROOT),'reason':type(e).__name__})
    for directory, dirs, files in os.walk(top, followlinks=False, onerror=error):
        c['directories'] += 1
        for name in list(dirs):
            p = pathlib.Path(directory)/name
            if name in PRUNE or p.is_symlink():
                dirs.remove(name)
                exclusion={'path':str(p.relative_to(ROOT)), 'reason':'symlink-not-followed' if p.is_symlink() else 'dependency-git-build-cache-directory'}
                if p.is_symlink():exclusion['target']=os.readlink(p)
                exclusions.append(exclusion)
                c['pruned_directories'] += 1
        for name in sorted(files):
            p = pathlib.Path(directory)/name; rel = p.relative_to(ROOT); suffix=p.suffix.lower()
            c['files'] += 1; ext[suffix] += 1
            if any(x.startswith('.') for x in rel.parts[1:]): c['hidden_path_files'] += 1
            if p.is_symlink():
                symlinks.append({'path':str(rel),'target':os.readlink(p),'followed':False});continue
            # Broad candidate discovery; content is never persisted by this script.
            isdoc = suffix in {'.md','.mdx','.rst','.txt'}
            isdata = suffix in {'.json','.jsonl','.ndjson','.csv','.tsv'} and any(k in str(rel).lower() for k in ('factory','artifact','evidence','eval','metric','telemetr','report','lesson','run','orchestrator','.local','ledger'))
            if not (isdoc or isdata): continue
            try:
                st=p.stat()
                if not stat.S_ISREG(st.st_mode):
                    exclusions.append({'path':str(rel),'reason':'special-file-not-opened'});continue
                r={'path':str(rel),'bytes':st.st_size,'kind':'document' if isdoc else 'data'}
                if st.st_size <= MAX_HASH:
                    h=hashlib.sha256()
                    with p.open('rb') as f:
                        for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
                    r['sha256']=h.hexdigest();c['hashed_candidates']+=1
                else:r['excluded_content']='over-32-MiB';c['oversize_candidates']+=1
                candidates.append(r)
            except OSError as e:error(e)
    totals.append({'project':top.name,**c,'extensions':dict(ext)})
    print(top.name,dict(c),flush=True)
groups=collections.defaultdict(list)
for r in candidates:
    if 'sha256' in r:groups[r['sha256']].append(r['path'])
summary={'observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'root':str(ROOT),'method':'os.walk no ignore rules, no symlink traversal; metadata and bounded sha256 only','hash_limit_bytes':MAX_HASH,'pruned_directory_names':sorted(PRUNE),'projects':totals,'symlinks':symlinks,'exclusions':exclusions,'candidate_count':len(candidates),'unique_candidate_hashes':len(groups),'duplicate_candidate_instances':sum(len(x)-1 for x in groups.values()),'not_claimed':'No exhaustive semantic reading, raw backup, Git preservation, or deletion readiness.'}
(OUT/'project-learning-inventory.json').write_text(json.dumps(summary,indent=2)+'\n')
with (OUT/'project-learning-sources.jsonl').open('w') as f:
    for r in candidates:f.write(json.dumps(r)+'\n')
(OUT/'project-learning-duplicates.json').write_text(json.dumps({h:ps for h,ps in groups.items() if len(ps)>1},indent=2)+'\n')

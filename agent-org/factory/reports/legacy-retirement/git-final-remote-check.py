import json,subprocess,os,datetime,concurrent.futures
from pathlib import Path
OUT=Path('/Users/Shared/agent-org/factory/reports/legacy-retirement');ENV=dict(os.environ,GIT_TERMINAL_PROMPT='0',GIT_OPTIONAL_LOCKS='0')
a=json.loads((OUT/'git-primary-inventory.json').read_text());b=json.loads((OUT/'git-remote-refs.json').read_text());waived={u['path'] for r in b['remotes'] if r['code'] for u in r['users']};remaining={r['path'] for r in a['repositories']} - waived
urls={r['url'] for r in b['remotes'] if any(u['path'] in remaining for u in r['users'])};rows=[]
def check(url):
 r=subprocess.run(['git','ls-remote',url],capture_output=True,text=True,env=ENV,timeout=60);return {'url':url,'code':r.returncode,'refs':r.stdout,'error':r.stderr}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 for r in ex.map(check,sorted(urls)):rows.append(r);print(r['code'],r['url'],len(r['refs'].splitlines()),flush=True)
(OUT/'git-remote-refs-final.json').write_text(json.dumps({'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'waived_paths':sorted(waived),'remaining_paths':sorted(remaining),'remotes':rows},indent=2))

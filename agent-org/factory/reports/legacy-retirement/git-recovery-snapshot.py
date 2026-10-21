"""Build inert Markdown recovery records; never execute recovered source."""
from pathlib import Path
import json,hashlib,base64,subprocess,re,stat
out=Path('/Users/Shared/agent-org/factory/reports/legacy-retirement');root=Path('/Users/Shared/old')
sets=[('onboarding',root/'projects/onboarding',None,None),('ollama-metered-source',root/'projects/competition/.local/ollama-metered-source',['llm/llama_server.go','server/routes.go','llm/ff_usage.go','LICENSE'],'cf2a313a298066d572c36812e5ad30a21c0db13b')]
summary=[]
for name,src,selected,base in sets:
 paths=selected or [str(p.relative_to(src)) for p in sorted(src.rglob('*')) if p.is_file() and not p.is_symlink()];records=[]
 for rel in paths:
  p=src/rel;data=p.read_bytes()
  if re.search(rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\bgh[pousr]_[A-Za-z0-9]{30,}|\bAKIA[A-Z0-9]{16}\b|\bsk-(?:proj-)?[A-Za-z0-9_-]{40,}',data):raise RuntimeError('Potential secret; refusing '+str(p))
  records.append({'path':rel,'mode':oct(stat.S_IMODE(p.stat().st_mode)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'base64':base64.b64encode(data).decode()})
 if base:
  data=subprocess.check_output(['git','-C',str(src),'diff','--binary','HEAD','--','llm/llama_server.go','server/routes.go']);records.append({'path':'tracked-changes.patch','mode':'0o644','bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'base64':base64.b64encode(data).decode()})
 manifest={'format':'inert-source-recovery-v1','source':str(src),'baseline_commit':base,'files':records}
 body=f'''# Inert historical recovery snapshot: {name}

- Target System: cross_boundary
- Change Classification: cross_boundary
- Authorized Scope: Read named legacy source; preserve reviewed inert source evidence in agent-org; no execution or installation
- Affected Paths or Resources: This Markdown artifact and named source hashes
- Owning Role: Coordinator
- Related Requirements: none
- Related Tasks: TASK-000029, TASK-000033
- Approval Requirements: APP-000010

This is an archival payload, not installed organization tooling or an adopted workflow. No enclosed program was run. Preserve original file bytes/modes by decoding the records below into a separately authorized empty recovery directory and checking SHA-256. Reject absolute/traversal paths before restoring. Do not execute recovered scripts merely to verify preservation.

'''
 if base:body+=f'The original repository is Ollama; baseline `{base}`. The three Go files preserve local telemetry instrumentation including an untracked file. The patch records the two tracked changes, and LICENSE preserves attribution. This small snapshot is carried with learning evidence rather than publishing custom changes to the upstream Ollama project. It is not a complete Ollama repository backup.\n\n'
 else:body+='This standalone GitHub setup wizard had no Git repository/remote. Its three files are preserved here so the legacy directory is no longer their sole recovery location. It is not activated as the current organization enrollment workflow.\n\n'
 body+='A bounded high-confidence token/private-key scan found no matches. This is not a comprehensive secret detector; source was inspected for its intended purpose.\n\n```json\n'+json.dumps(manifest,indent=2)+'\n```\n'
 target=out/f'git-recovery-{name}.md';target.write_text(body)
 loaded=json.loads(target.read_text().split('```json\n',1)[1].split('\n```',1)[0])
 for r in loaded['files']:
  decoded=base64.b64decode(r['base64'],validate=True);assert len(decoded)==r['bytes'] and hashlib.sha256(decoded).hexdigest()==r['sha256']
 summary.append({'artifact':str(target),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'files':len(records),'payload_bytes':sum(r['bytes'] for r in records),'round_trip_verified':True})
(out/'git-recovery-snapshot-verification.json').write_text(json.dumps(summary,indent=2));print(summary)

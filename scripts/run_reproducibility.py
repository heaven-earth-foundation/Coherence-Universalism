#!/usr/bin/env python3
"""Run all six shipped numerical suites in isolation and compare saved JSON results.

No missing suite is skipped. A process exit without a newly generated result fails.
Scientific values, booleans, text, model versions and seeds are compared; only the
explicit machine-environment/hash fields below are excluded. This checks the
published constructions, not empirical validity or all historical audit scripts.
"""
from __future__ import annotations
import argparse,hashlib,json,math,shutil,subprocess,sys,tempfile,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SUITE=[
 ('Physics','evidence/03_Physics/A6_1_reproducibility_package','CU_Physics_A6_1_reproducibility.py','CU_Physics_A6_1_verification_results.json'),
 ('Biology','evidence/04_Biology/C1_1_reproducibility_package','CU_Biology_C1_1_reproducibility.py','CU_Biology_C1_1_verification_results.json'),
 ('Ethics','evidence/08_Ethics','CU_Ethics_v0.10_PC1_Reproducibility.py','CU_Ethics_G1_1_verification_results.json'),
 ('Artificial Intelligence','evidence/09_Artificial_Intelligence','CU_AI_v0.10_PC1_Reproducibility.py','CU_AI_v0.10_PC1_Verification_Results.json'),
 ('Denying Knowledge','evidence/10_Denying_Knowledge','Denying_Knowledge_v0.10_PC2_Logic_Regression.py','Denying_Knowledge_v0.10_PC2_Logic_Results.json'),
 ('Non-Egoic Mind','evidence/11_Non_Egoic_Artificial_Mind','Non_Egoic_Mind_v0.10_RC1_Reproducibility.py','Non_Egoic_Mind_v0.10_RC1_Verification_Results.json'),
]
IGNORED={
 '/metadata/platform','/metadata/python','/metadata/numpy','/metadata/scipy',
 '/metadata/script_sha256','/software/python','/software/numpy',
 '/runtime/platform','/runtime/python','/content_sha256_without_hash_field',
}
def differences(new,old,path=''):
    if path in IGNORED:return []
    out=[]
    if isinstance(new,dict) and isinstance(old,dict):
        for key in sorted(set(new)|set(old)):
            p=path+'/'+key
            if key not in new or key not in old:out.append(p+': missing key')
            else:out.extend(differences(new[key],old[key],p))
    elif isinstance(new,list) and isinstance(old,list):
        if len(new)!=len(old):out.append(path+': list length mismatch')
        else:
            for i,(a,b) in enumerate(zip(new,old)):out.extend(differences(a,b,f'{path}/{i}'))
    elif isinstance(new,bool) or isinstance(old,bool):
        if type(new) is not type(old) or new!=old:out.append(path+': boolean mismatch')
    elif isinstance(new,(float,int)) and isinstance(old,(float,int)):
        if not math.isfinite(new) or not math.isfinite(old) or not math.isclose(new,old,rel_tol=1e-9,abs_tol=1e-9):out.append(f'{path}: {new!r} != {old!r}')
    elif type(new) is not type(old) or new!=old:out.append(f'{path}: {new!r} != {old!r}')
    return out

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--report',type=Path,help='Optional JSON report path outside the frozen repository')
    ap.add_argument('--timeout',type=int,default=600,help='Per-suite timeout in seconds')
    args=ap.parse_args();records=[]
    for label,rel,script,result in SUITE:
        src=ROOT/rel;entry={'suite':label,'script':str(Path(rel)/script),'result':str(Path(rel)/result)}
        t=time.monotonic();print('RUN',label,flush=True)
        try:
            for name in [script,result]:
                if not (src/name).is_file():raise FileNotFoundError(str(src/name))
            entry['script_sha256']=hashlib.sha256((src/script).read_bytes()).hexdigest()
            with tempfile.TemporaryDirectory(prefix='cu_repro_') as tmp:
                work=Path(tmp)/'run';shutil.copytree(src,work)
                (work/result).unlink()
                cp=subprocess.run([sys.executable,'-I',script],cwd=work,capture_output=True,text=True,timeout=args.timeout)
                entry['exit_code']=cp.returncode;entry['stdout']=cp.stdout;entry['stderr']=cp.stderr
                if cp.returncode:raise RuntimeError(f'exit {cp.returncode}: {cp.stderr[-1000:]}')
                if not (work/result).is_file():raise RuntimeError('Expected result was not regenerated')
                new=json.loads((work/result).read_text());old=json.loads((src/result).read_text())
                diff=differences(new,old)
                if new.get('overall_pass') is False:diff.append('overall_pass is false')
                if 'regression_checks' in new and not all(v is True for v in new['regression_checks'].values()):diff.append('A regression check failed')
                entry['differences']=diff;entry['pass']=not diff
                entry['regenerated_sha256']=hashlib.sha256((work/result).read_bytes()).hexdigest()
        except (OSError,ValueError,RuntimeError,subprocess.TimeoutExpired) as e:
            entry['pass']=False;entry['error']=str(e)
        entry['seconds']=round(time.monotonic()-t,3);records.append(entry)
        print(('PASS' if entry['pass'] else 'FAIL'),label,entry.get('error',entry.get('differences',[])),flush=True)
    passed=sum(x['pass'] for x in records);report={'required_suites':len(SUITE),'executed_suites':len(records),'passed':passed,'failed':len(records)-passed,'ignored_json_paths':sorted(IGNORED),'relative_tolerance':1e-9,'absolute_tolerance':1e-9,'suites':records}
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    print(f'OVERALL: {passed}/{len(SUITE)} suites PASS; {len(records)-passed} FAIL; 0 SKIP',flush=True)
    return int(passed!=len(SUITE))
if __name__=='__main__':raise SystemExit(main())

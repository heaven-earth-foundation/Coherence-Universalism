#!/usr/bin/env python3
"""Run all six shipped numerical suites in isolation and compare saved JSON results.

No missing suite is skipped. A process exit without a newly generated result fails.
Scientific values, booleans, text, model versions and seeds are compared; only the
explicit machine-environment/hash fields below are excluded. Physics diagnostic
coordinates and derived refinement ratios have documented, path-specific numeric
tolerances plus consistency checks. No scientific result field is omitted.
This checks the
published constructions, not empirical validity or all historical audit scripts.
"""
from __future__ import annotations
import argparse,hashlib,json,math,os,platform,re,shutil,subprocess,sys,tempfile,time
from importlib.metadata import version as package_version
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
# Default comparisons are unchanged; the two exceptions are diagnostics, not
# exact/root-based constants or mathematical pass/fail assertions.
DEFAULT_REL_TOL = 1e-9
DEFAULT_ABS_TOL = 1e-9
SCAN_COORD_ABS_TOL = 5e-8
REFINEMENT_REL_TOL = 1e-7
SCAN_COORD_PATTERN = re.compile(
    r"^/fisher_absolute_constants/(?:"
    r"all_reduced_cases/(?:norm_A|norm_B|Pi_F)/[0-5]|"
    r"sup_(?:norm_A|norm_B|Pi_F)/scan_argmax"
    r")/(?:a|b|total_mass_a)$"
)
REFINEMENT_PATTERN = re.compile(
    r"^/madelung/continuity_median_refinement_factors/[01]$"
)

def numeric_tolerance(path: str, suite: str | None = None):
    if suite == "Physics" and SCAN_COORD_PATTERN.fullmatch(path):
        return 0.0, SCAN_COORD_ABS_TOL, "bounded-optimizer coordinate"
    if suite == "Physics" and REFINEMENT_PATTERN.fullmatch(path):
        return REFINEMENT_REL_TOL, DEFAULT_ABS_TOL, "derived refinement ratio"
    return DEFAULT_REL_TOL, DEFAULT_ABS_TOL, "default"


def differences(new, old, path='', *, suite=None, accepted_variations=None):
    if path in IGNORED:
        return []
    out=[]
    if isinstance(new,dict) and isinstance(old,dict):
        for key in sorted(set(new)|set(old)):
            p=path+'/'+key
            if key not in new or key not in old:
                out.append(p+': missing key')
            else:
                out.extend(differences(new[key],old[key],p,suite=suite,
                                       accepted_variations=accepted_variations))
    elif isinstance(new,list) and isinstance(old,list):
        if len(new)!=len(old):
            out.append(path+': list length mismatch')
        else:
            for i,(a,b) in enumerate(zip(new,old)):
                out.extend(differences(a,b,f'{path}/{i}',suite=suite,
                                       accepted_variations=accepted_variations))
    elif isinstance(new,bool) or isinstance(old,bool):
        if type(new) is not type(old) or new!=old:
            out.append(path+': boolean mismatch')
    elif isinstance(new,int) and isinstance(old,int):
        if new!=old:
            out.append(f'{path}: integer mismatch {new!r} != {old!r}')
    elif isinstance(new,(float,int)) and isinstance(old,(float,int)):
        rel_tol,abs_tol,policy=numeric_tolerance(path,suite)
        if not math.isfinite(new) or not math.isfinite(old):
            out.append(f'{path}: non-finite value {new!r} != {old!r}')
        elif not math.isclose(new,old,rel_tol=rel_tol,abs_tol=abs_tol):
            out.append(f'{path}: {new!r} != {old!r}')
        elif policy != "default" and not math.isclose(
                new,old,rel_tol=DEFAULT_REL_TOL,abs_tol=DEFAULT_ABS_TOL):
            if accepted_variations is not None:
                accepted_variations.append({
                    'path':path,'new':new,'saved':old,'absolute_difference':abs(new-old),
                    'relative_tolerance':rel_tol,'absolute_tolerance':abs_tol,'policy':policy,
                })
    elif type(new) is not type(old) or new!=old:
        out.append(f'{path}: {new!r} != {old!r}')
    return out


def physics_consistency(result):
    """Additional checks on the diagnostic families with wider tolerances.

    Probability normalization and each reported objective must agree internally.
    The two-level objective formulas follow directly from the shipped definitions:
    norm(A)=2|a-b|sqrt(z(1-z)); norm(B)=|log(a/b)|sqrt(z(1-z));
    Pi_F=2z(1-z)(a-b)log(a/b). Refined-grid ratios must agree with their
    actual raw medians; the raw medians still use the original default comparison.
    """
    out=[]
    def close(actual,expected,label):
        if not math.isfinite(actual) or not math.isfinite(expected) or not math.isclose(
                actual,expected,rel_tol=1e-12,abs_tol=1e-12):
            out.append(f'{label}: inconsistent {actual!r} != {expected!r}')
    try:
        data=result['fisher_absolute_constants']
        for kind in ('norm_A','norm_B','Pi_F'):
            rows=data['all_reduced_cases'][kind]
            indexed=[(f'all_reduced_cases/{kind}/{i}',row) for i,row in enumerate(rows)]
            indexed += [(f'sup_{kind}/scan_argmax',data[f'sup_{kind}']['scan_argmax']),
                        (f'sup_{kind}/argmax',data[f'sup_{kind}']['argmax'])]
            for label,row in indexed:
                k,m=row['support_size'],row['multiplicity_a']
                a,b,z=row['a'],row['b'],row['total_mass_a']
                if type(k) is not int or type(m) is not int or not (2<=k<=4 and 1<=m<k):
                    out.append(f'{label}: invalid support or multiplicity'); continue
                if not all(type(v) in (float,int) and math.isfinite(v) and 0<v<1 for v in (a,b,z)):
                    out.append(f'{label}: invalid probability'); continue
                close(m*a,z,label+'/m*a')
                close((k-m)*b,1-z,label+'/(k-m)*b')
                close(m*a+(k-m)*b,1.0,label+'/normalization')
                spread=math.sqrt(z*(1-z)); log_ratio=math.log(a/b)
                objective={'norm_A':2*abs(a-b)*spread,
                           'norm_B':abs(log_ratio)*spread,
                           'Pi_F':2*z*(1-z)*(a-b)*log_ratio}[kind]
                close(row['value'],objective,label+'/objective')
        medians=[row['continuity_median'] for row in result['madelung']['grid_rows']]
        ratios=result['madelung']['continuity_median_refinement_factors']
        if len(medians)!=3 or len(ratios)!=2:
            out.append('madelung: expected three grids and two ratios')
        elif not all(type(v) in (float,int) and math.isfinite(v) and v>0 for v in medians):
            out.append('madelung: nonpositive or non-finite residual median')
        else:
            for i,ratio in enumerate(ratios):
                close(ratio,medians[i]/medians[i+1],f'madelung/refinement_ratio/{i}')
    except (KeyError,TypeError,IndexError,ValueError,ZeroDivisionError,OverflowError) as exc:
        out.append(f'Physics diagnostic consistency error: {exc}')
    return out


def environment_record():
    packages={}
    for name in ('numpy','scipy','sympy'):
        try: packages[name]=package_version(name)
        except Exception: packages[name]='not available'
    return {'python':sys.version,'platform':platform.platform(),'packages':packages,
            'cpu_dispatch_overrides':{key:os.environ[key] for key in
                ('NPY_DISABLE_CPU_FEATURES','OPENBLAS_CORETYPE','OPENBLAS_NUM_THREADS')
                if key in os.environ}}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--report',type=Path,help='Optional JSON report path outside the frozen repository')
    ap.add_argument('--timeout',type=int,default=600,help='Per-suite timeout in seconds')
    args=ap.parse_args();records=[]
    if args.timeout <= 0: ap.error('--timeout must be positive')
    environment=environment_record()
    print('ENVIRONMENT',json.dumps(environment,sort_keys=True),flush=True)
    # The regression tests are required, not optional. They import this module
    # without invoking main, so there is no recursive execution.
    test_script=ROOT/'scripts'/'test_reproducibility_portability.py'
    if not test_script.is_file():
        print('FAIL comparator self-tests: required test file missing',flush=True)
        return 1
    test_run=subprocess.run([sys.executable,'-I',str(test_script)],capture_output=True,text=True)
    if test_run.returncode:
        print('FAIL comparator self-tests',test_run.stdout,test_run.stderr,flush=True)
        return 1
    print('PASS comparator self-tests\n'+test_run.stderr.strip(),flush=True)
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
                accepted=[]
                diff=differences(new,old,suite=label,accepted_variations=accepted)
                if label=='Physics': diff.extend(physics_consistency(new))
                entry['accepted_portability_variations']=accepted
                for variation in accepted:
                    print('PORTABILITY',label,json.dumps(variation,sort_keys=True),flush=True)
                if new.get('overall_pass') is False:diff.append('overall_pass is false')
                if 'regression_checks' in new and not all(v is True for v in new['regression_checks'].values()):diff.append('A regression check failed')
                entry['differences']=diff;entry['pass']=not diff
                entry['regenerated_sha256']=hashlib.sha256((work/result).read_bytes()).hexdigest()
        except (OSError,ValueError,TypeError,KeyError,AttributeError,OverflowError,RuntimeError,subprocess.TimeoutExpired) as e:
            entry['pass']=False;entry['error']=str(e)
        entry['seconds']=round(time.monotonic()-t,3);records.append(entry)
        print(('PASS' if entry['pass'] else 'FAIL'),label,entry.get('error',entry.get('differences',[])),flush=True)
    passed=sum(x['pass'] for x in records);report={'required_suites':len(SUITE),'executed_suites':len(records),'passed':passed,'failed':len(records)-passed,'ignored_json_paths':sorted(IGNORED),'relative_tolerance':DEFAULT_REL_TOL,'absolute_tolerance':DEFAULT_ABS_TOL,
        'environment':environment,'comparison_policy':'physics-portability-2026-10-19',
        'path_specific_tolerances':[
          {'suite':'Physics','pattern':SCAN_COORD_PATTERN.pattern,'relative_tolerance':0.0,'absolute_tolerance':SCAN_COORD_ABS_TOL},
          {'suite':'Physics','pattern':REFINEMENT_PATTERN.pattern,'relative_tolerance':REFINEMENT_REL_TOL,'absolute_tolerance':DEFAULT_ABS_TOL}],
        'comparator_self_tests':{'returncode':test_run.returncode,'output':test_run.stderr},'suites':records}
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    print(f'OVERALL: {passed}/{len(SUITE)} suites PASS; {len(records)-passed} FAIL; 0 SKIP',flush=True)
    return int(passed!=len(SUITE))
if __name__=='__main__':raise SystemExit(main())

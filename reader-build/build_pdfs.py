#!/usr/bin/env python3
"""Build the eleven paper PDFs directly from unchanged release Markdown math.
Requires Pandoc and XeLaTeX with standard TeX packages and Liberation/DejaVu fonts.
Does not bundle fonts. Output contains PDFs, editable TeX and build logs.
"""
from __future__ import annotations
import argparse, concurrent.futures, hashlib, json, shutil, subprocess
from pathlib import Path

def run(cmd: list[str], cwd: Path, log: Path) -> None:
    result=subprocess.run(cmd,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    with log.open('a',encoding='utf-8') as stream: stream.write(result.stdout)
    if result.returncode: raise RuntimeError(f'{cmd[0]} exited {result.returncode}; see {log}')

def build(src: Path, repo: Path, out: Path) -> dict:
    target=out/src.stem; target.mkdir(parents=True,exist_ok=True)
    log=target/'build.log'; log.write_text('',encoding='utf-8')
    tex=target/(src.stem+'.tex')
    reader='markdown+tex_math_single_backslash+autolink_bare_uris-yaml_metadata_block-multiline_tables-simple_tables-grid_tables'
    cmd=['pandoc',str(src),'--from='+reader,'--to=latex','--standalone',
         '--metadata=lang:en-US','-V','mainfont=Liberation Serif','-V','sansfont=Liberation Sans',
         '-V','monofont=DejaVu Sans Mono','-V','fontsize=11pt','-V','geometry:margin=0.8in',
         '-V','colorlinks=true','-V','linkcolor=blue','-V','urlcolor=blue',
         '--include-in-header='+str(repo/'reader-build/header.tex'),
         '--lua-filter='+str(repo/'reader-build/fit-display.lua'),
         '--resource-path='+str(src.parent)+':'+str(repo),'-o',str(tex)]
    run(cmd,repo,log)
    for _ in range(2):
        run(['xelatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error',tex.name],target,log)
    pdf=tex.with_suffix('.pdf')
    if not pdf.exists(): raise RuntimeError('No PDF produced: '+str(src))
    return {'file':src.name,'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
            'pdf':str(pdf),'tex':str(tex),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
            'status':'PASS'}

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[1]); ap.add_argument('--out',type=Path,required=True); ap.add_argument('--jobs',type=int,default=2)
    a=ap.parse_args();a.repo=a.repo.resolve();a.out=a.out.resolve();a.out.mkdir(parents=True,exist_ok=True)
    for program in ('pandoc','xelatex'):
        if not shutil.which(program): raise SystemExit('Required program missing: '+program)
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.jobs) as executor:
        futures={executor.submit(build,p,a.repo,a.out):p for p in sorted((a.repo/'papers').glob('*.md'))}
        for future in concurrent.futures.as_completed(futures):
            p=futures[future]
            try: row=future.result()
            except Exception as exc: row={'file':p.name,'status':'FAIL','error':str(exc)}
            results.append(row);print(row['status'],p.name,flush=True)
            (a.out/'BUILD_REPORT.json').write_text(json.dumps(sorted(results,key=lambda r:r['file']),indent=2),encoding='utf-8')
    return int(any(r['status']!='PASS' for r in results))
if __name__=='__main__':raise SystemExit(main())

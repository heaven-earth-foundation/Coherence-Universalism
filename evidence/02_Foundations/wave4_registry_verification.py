#!/usr/bin/env python3
"""Wave 4 registry and stage verification for CU Foundations."""
import csv, json, pathlib, re
root = pathlib.Path(__file__).resolve().parents[2]
reg = list(csv.DictReader((root / 'registries' / 'CU_v0.10_Normalized_Principle_Registry_Wave4_v0.1.csv').open(encoding='utf-8')))
stages = list(csv.DictReader((root / 'registries' / 'CU_v0.10_Normalized_64_Stage_Status_Registry_Wave4_v0.1.csv').open(encoding='utf-8')))
fd = (root / 'manuscripts' / '02_CU_Foundations_v0.10_RC3_Methodological_Spine_Propagation_Draft.md').read_text(encoding='utf-8')
me = (root / 'manuscripts' / '01_CU_Metaphysics_Epistemology_v0.10_RC3_Methodological_Spine_Propagation_Draft.md').read_text(encoding='utf-8')
checks = {
    'principle_records_226': len(reg) == 226,
    'principle_ids_unique': len({r['id'] for r in reg}) == len(reg),
    'stage_records_64': len(stages) == 64,
    'stage_numbers_unique': len({r['stage'] for r in stages}) == 64,
    'foundations_has_wave4_supplement_link': '02_Foundations_Technical_Supplement_Wave4.md' in fd,
    'stage_64_repaired_in_both': 'interpretive recognition' in fd.lower() and 'interpretive recognition' in me.lower(),
}
for k, v in checks.items(): print(k, 'PASS' if v else 'FAIL')
if not all(checks.values()): raise SystemExit(1)

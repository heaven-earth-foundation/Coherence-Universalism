#!/usr/bin/env python3
"""Regression tests for the October 2026 Physics portability comparison policy.

Run directly, or automatically through run_reproducibility.py. These tests never
write to scientific evidence. OBSERVED contains the ten comparisons copied from
the user's GitHub Actions failure log, not a reconstruction of the entire run.
"""
from __future__ import annotations
import copy
import importlib.util
import json
import math
from pathlib import Path
import sys
import unittest

sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cu_reproduction_runner',HERE/'run_reproducibility.py')
runner=importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)
ROOT=HERE.parent
EXPECTED=ROOT/'evidence/03_Physics/A6_1_reproducibility_package/CU_Physics_A6_1_verification_results.json'
PREFIX='/fisher_absolute_constants/all_reduced_cases/'
OBSERVED=[
 (PREFIX+'Pi_F/2/a',0.07898715745126184,0.07898715628074739),
 (PREFIX+'Pi_F/2/b',0.8420256850974763,0.8420256874385053),
 (PREFIX+'Pi_F/2/total_mass_a',0.15797431490252367,0.15797431256149477),
 (PREFIX+'norm_A/4/a',0.07322330558105744,0.07322330335374634),
 (PREFIX+'norm_A/4/b',0.42677669441894256,0.4267766966462537),
 (PREFIX+'norm_A/4/total_mass_a',0.14644661116211488,0.14644660670749268),
 (PREFIX+'norm_A/5/a',0.06782161067294591,0.06782160966801526),
 (PREFIX+'norm_A/5/b',0.7965351679811623,0.7965351709959543),
 (PREFIX+'norm_A/5/total_mass_a',0.20346483201883775,0.20346482900404578),
 ('/madelung/continuity_median_refinement_factors/1',3.992793520818326,3.9927935536960173),
]

def lookup(obj,path):
    for part in path.strip('/').split('/'):
        obj=obj[int(part)] if isinstance(obj,list) else obj[part]
    return obj

class ComparisonContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved=json.loads(EXPECTED.read_text(encoding='utf-8'))

    def test_01_original_policy_rejects_all_ten_logged_comparisons(self):
        for path,new,old in OBSERVED:
            with self.subTest(path=path):
                self.assertEqual(lookup(self.saved,path),old)
                self.assertTrue(runner.differences(new,old,path))

    def test_02_scoped_policy_accepts_and_reports_all_ten(self):
        accepted=[]
        for path,new,old in OBSERVED:
            self.assertEqual(runner.differences(new,old,path,suite='Physics',accepted_variations=accepted),[])
        self.assertEqual(len(accepted),10)

    def test_03_other_suites_do_not_receive_relaxed_tolerances(self):
        for suite in ('Biology','Ethics','Artificial Intelligence','Denying Knowledge','Non-Egoic Mind'):
            for path,new,old in OBSERVED:
                with self.subTest(suite=suite,path=path):
                    self.assertTrue(runner.differences(new,old,path,suite=suite))

    def test_04_large_coordinate_errors_still_fail(self):
        for path,_,old in OBSERVED[:9]:
            self.assertTrue(runner.differences(old+1e-5,old,path,suite='Physics'))

    def test_05_large_ratio_errors_still_fail(self):
        path,_,old=OBSERVED[-1]
        self.assertTrue(runner.differences(old+0.001,old,path,suite='Physics'))

    def test_06_objective_values_remain_strict(self):
        for kind in ('norm_A','norm_B','Pi_F'):
            path=PREFIX+kind+'/4/value'; old=lookup(self.saved,path)
            self.assertTrue(runner.differences(old+1e-8,old,path,suite='Physics'))

    def test_07_exact_and_root_based_argmaxes_remain_strict(self):
        for kind in ('norm_A','norm_B','Pi_F'):
            for field in ('a','b','total_mass_a'):
                path=f'/fisher_absolute_constants/sup_{kind}/argmax/{field}'
                old=lookup(self.saved,path)
                self.assertTrue(runner.differences(old+1e-8,old,path,suite='Physics'))

    def test_08_booleans_strings_integers_and_shapes_remain_checked(self):
        for new,old in [(False,True),(1,True),('changed','original'),(10**12+1,10**12),([1],[1,2]),({}, {'x':1})]:
            with self.subTest(new=new,old=old):
                self.assertTrue(runner.differences(new,old,suite='Physics'))

    def test_09_nonfinite_values_fail_even_in_relaxed_paths(self):
        for path,_,old in OBSERVED:
            for bad in (math.nan,math.inf,-math.inf):
                self.assertTrue(runner.differences(bad,old,path,suite='Physics'))
        self.assertTrue(runner.differences(math.nan,math.nan,OBSERVED[0][0],suite='Physics'))

    def test_10_saved_physics_passes_consistency_checks(self):
        self.assertEqual(runner.physics_consistency(self.saved),[])

    def test_11_small_but_inconsistent_probability_is_rejected(self):
        new=copy.deepcopy(self.saved)
        new['fisher_absolute_constants']['all_reduced_cases']['norm_A'][4]['a']+=1e-8
        self.assertEqual(runner.differences(new,self.saved,suite='Physics'),[])
        self.assertTrue(runner.physics_consistency(new))

    def test_12_inconsistent_objective_is_rejected(self):
        new=copy.deepcopy(self.saved)
        new['fisher_absolute_constants']['all_reduced_cases']['norm_A'][4]['value']+=1e-10
        self.assertEqual(runner.differences(new,self.saved,suite='Physics'),[])
        self.assertTrue(runner.physics_consistency(new))

    def test_13_ratio_cannot_change_without_its_inputs(self):
        new=copy.deepcopy(self.saved)
        new['madelung']['continuity_median_refinement_factors'][1]=OBSERVED[-1][1]
        self.assertEqual(runner.differences(new,self.saved,suite='Physics'),[])
        self.assertTrue(runner.physics_consistency(new))

    def test_14_reported_coordinates_are_normalized_and_objective_consistent(self):
        new=copy.deepcopy(self.saved)
        for path,value,_ in OBSERVED[:9]:
            parts=path.strip('/').split('/'); node=new
            for key in parts[:-1]: node=node[int(key)] if isinstance(node,list) else node[key]
            node[parts[-1]]=value
        self.assertEqual(runner.physics_consistency(new),[])

    def test_15_consistent_ratio_fixture_passes(self):
        # Synthetic consistency fixture, NOT the complete GitHub output. The
        # local CPU-dispatch reproduction is a separate documented experiment.
        new=copy.deepcopy(self.saved)
        med=new['madelung']['grid_rows']; ratio=OBSERVED[-1][1]
        med[2]['continuity_median']=med[1]['continuity_median']/ratio
        new['madelung']['continuity_median_refinement_factors'][1]=ratio
        self.assertEqual(runner.differences(new,self.saved,suite='Physics'),[])
        self.assertEqual(runner.physics_consistency(new),[])

    def test_16_wrong_paths_receive_no_exception(self):
        for path in (PREFIX+'norm_A/6/a',PREFIX+'other/0/a',
                     '/madelung/continuity_median_refinement_factors/2',
                     '/madelung/grid_rows/2/continuity_median'):
            self.assertEqual(runner.numeric_tolerance(path,'Physics')[:2],(1e-9,1e-9))

    def test_17_explicit_environment_exclusions_unchanged(self):
        expected={'/metadata/platform','/metadata/python','/metadata/numpy','/metadata/scipy',
                  '/metadata/script_sha256','/software/python','/software/numpy',
                  '/runtime/platform','/runtime/python','/content_sha256_without_hash_field'}
        self.assertEqual(runner.IGNORED,expected)
        self.assertEqual(len(runner.SUITE),6)

    def test_18_missing_consistency_fields_fail(self):
        self.assertTrue(runner.physics_consistency({}))
        new=copy.deepcopy(self.saved)
        del new['madelung']['grid_rows'][0]['continuity_median']
        self.assertTrue(runner.physics_consistency(new))

if __name__=='__main__':
    unittest.main(verbosity=1)

"""Test demographic identity, benefit indexation and reproducibility."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('ageing_case', ROOT / 'examples/ageing-fiscal/model.py')
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)


class AgeingCase(unittest.TestCase):
    def test_percent_ratio_convention(self):
        self.assertAlmostEqual(model.mechanical_burden(80, .75, .3), 32)

    def test_productivity_cancels_under_full_indexation(self):
        baseline = model.mechanical_burden(80, .75, .3)
        self.assertAlmostEqual(model.mechanical_burden(80, .75, .3, .1, True), baseline)
        self.assertLess(model.mechanical_burden(80, .75, .3, .1, False), baseline)

    def test_employment_and_benefit_sensitivities(self):
        baseline = model.mechanical_burden(80, .75, .3)
        self.assertAlmostEqual(model.mechanical_burden(80, .8, .3), 30)
        self.assertAlmostEqual(model.mechanical_burden(80, .75, .27), .9 * baseline)

    def test_invalid_denominators_rejected(self):
        for employment, prod in [(0, 0), (1.1, 0), (.75, -1)]:
            with self.assertRaises(ValueError): model.mechanical_burden(80, employment, .3, prod)

    def test_archived_results_reproduce(self):
        p = subprocess.run([sys.executable, 'examples/ageing-fiscal/model.py', '--check'], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)


if __name__ == '__main__': unittest.main()

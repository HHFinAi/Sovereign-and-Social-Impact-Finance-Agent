import unittest
from sf_agent.analytics import debt_path,swap_value,blended_loss_allocation,outcome_payment,mobilisation_ratio
from sf_agent.validation import DataError

class SovereignArithmetic(unittest.TestCase):
    def test_stable_debt(self): self.assertEqual(debt_path(.6,[.05],[.05],[0],[0],0,[0]),[.6,.6])
    def test_primary_surplus_sign(self): self.assertAlmostEqual(debt_path(.6,[.05],[.05],[.02],[0],0,[0])[-1],.58)
    def test_fx_opening_principal(self): self.assertAlmostEqual(debt_path(.6,[0],[0],[0],[0],.5,[.2])[-1],.66)
    def test_stock_flow_adjustment(self): self.assertEqual(debt_path(.6,[0],[0],[0],[.1],0,[0])[-1],.7)
    def test_series_length_mismatch(self):
        with self.assertRaises(DataError): debt_path(.6,[.05,.05],[.05],[0],[0],0,[0])
    def test_negative_gdp_denominator(self):
        with self.assertRaises(DataError): debt_path(.6,[0],[-1],[0],[0],0,[0])
    def test_net_assets_not_clamped(self):
        with self.assertRaises(DataError): debt_path(.1,[0],[0],[.5],[0],0,[0])
    def test_swap_net_not_face_value(self):
        r=swap_value([0,100],[0,80],[0,10],[2,0],.1)
        self.assertAlmostEqual(r['pv_debt_service_relief'],20/1.1);self.assertAlmostEqual(r['net_fiscal_savings'],10/1.1-2)
    def test_swap_can_destroy_fiscal_value(self): self.assertLess(swap_value([0,100],[0,95],[0,10],[2,0],0)['net_fiscal_savings'],0)
    def test_swap_full_horizon_required(self):
        with self.assertRaises(DataError): swap_value([0,100],[0,80,20],[0,10],[2,0],.1)
    def test_loss_waterfall_conserves_loss(self):
        r=blended_loss_allocation(100,20,.5,30);self.assertEqual(r,{'first_loss_absorbed':20,'guarantee_payment':30,'residual_investor_loss':50});self.assertEqual(sum(r.values()),100)
    def test_first_loss_smaller_than_capacity(self): self.assertEqual(blended_loss_allocation(10,20,.5,30)['residual_investor_loss'],0)
    def test_outcome_payment_cap(self): self.assertEqual(outcome_payment(100,10,500),500)
    def test_mobilisation(self): self.assertEqual(mobilisation_ratio(80,20),4)
    def test_no_concessional_denominator(self):
        with self.assertRaises(DataError): mobilisation_ratio(80,0)
if __name__=='__main__': unittest.main()

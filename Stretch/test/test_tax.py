import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tax import tax_calculator

def test_tax_earnings_below_12000():
  assert tax_calculator(11500) == 0
  
def test_tax_earnings_between_12000And36000():
  assert tax_calculator(31500) == 6300

def test_tax_earnings_above_36000():
  assert tax_calculator(41500) == 8300

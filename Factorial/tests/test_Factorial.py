

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from factorial import recur_factorial

def test_factorial_one():
  assert recur_factorial(1) == 1

def test_factorial_8():
  assert recur_factorial(8) == 40320

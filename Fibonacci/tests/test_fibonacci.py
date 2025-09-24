import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fibonacci import fibonacci_recursive
import pytest

def test_fibonacci_recursive_zero():
  assert fibonacci_recursive(0) == 0

def test_fibonacci_recursive_one():
  assert fibonacci_recursive(1) == 1

def test_fibonacci_recursive_two():
  assert fibonacci_recursive(2) == 1

def test_fibonacci_recursive_three():
  assert fibonacci_recursive(3) == 2

def test_fibonacci_recursive_five():
  assert fibonacci_recursive(5) == 5

def test_fibonacci_recursive_ten():
  assert fibonacci_recursive(10) == 55

def test_fibonacci_recursive_negative():
  assert fibonacci_recursive(-5) == 0

def test_fibonacci_recursive_large():
  assert fibonacci_recursive(15) == 610
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from multiply import multiply

def test_multiply_two_positive_numbers():
    assert multiply(2, 3) == 6

def test_multiply_positive_and_negative_number():
    assert multiply(2, -3)  == -6

def test_multiply_two_negative_numbers():
    assert multiply(-3, -2)  == 6

def test_multiply_by_zero():
    assert multiply(5, 0) == 0

def test_multiply_one_and_number():
    assert multiply(5, 1) == 5
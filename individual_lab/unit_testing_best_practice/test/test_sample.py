import os
import sys
# Always run from unit_testing_best_practice/test
sys.path += ['../src'] 

from test import sample

def test_answer():
    assert sample.func(3) == 5 

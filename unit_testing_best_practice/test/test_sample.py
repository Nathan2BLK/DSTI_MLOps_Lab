import os
import sys

# Get the current script's directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))

# Add the parent directory to sys.path
sys.path.insert(0, parent_directory)

# Import the module from the parent directory
from src import sample

def test_answer():
    assert sample.func(3) == 5 

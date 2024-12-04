#test binary string to decimal value


import sys
import os

# Append the BASE_cons directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'BASE_cons')))

# Now you can import binary_string_to_decimal from BASE_cons
from binary_string_to_decimal import binarystr_decimal  # Replace with the actual class or function name


import unittest
import binary_string_to_decimal

class Test_My_String(unittest.TestCase):
    def test_stringLength(self):
        self.assertEqual(binary_string_to_decimal.binarystr_decimal('test'), 4)
                         
                         #stringLength('test'), 4)



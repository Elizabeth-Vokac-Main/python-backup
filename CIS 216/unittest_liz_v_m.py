#unittest - Unit testing framework

import unittest
import math

class TestMathMethods(unittest.TestCase):

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(celsius_to_kelvin(0), 273.15)
        self.assertAlmostEqual(celsius_to_kelvin(500), 773.15)
        self.assertAlmostEqual(celsius_to_kelvin(-273.15), 0)

    def test_pythagorean_hypot(self):
        self.assertEqual(pythagorean_hypot(5, 12), 13)
        self.assertEqual(pythagorean_hypot(3, 4), 5)
        self.assertEqual(pythagorean_hypot(7, 24), 25)

class TestStringMethods(unittest.TestCase):

    def test_mirror_function(self):
        self.assertEqual(mirror_function('321'), '123321')
        self.assertEqual(mirror_function('abc') , 'cbaabc')
        self.assertEqual(mirror_function('X Y'), 'Y XX Y')
        

def celsius_to_kelvin(c_float):
    if c_float >= -273.15:
        k_float = c_float + 273.15
        print(k_float)
        return k_float
    else:
        print('Enter a number greater than or equal to -273.15')
        
def pythagorean_hypot(int1, int2):
    if int1 > 0 and int2 > 0:
        hypotenuse = math.sqrt((int1 * int1) + (int2 * int2))
        return hypotenuse
    else:
        print('Enter numbers greater than zero. ')


def mirror_function(string):
    mirror = ''
    for j in range(-1, -len(string) - 1, -1):
        mirror += string[j]
    
    palindrome = mirror + string
    return palindrome
    

if __name__ == '__main__':
    unittest.main()
    


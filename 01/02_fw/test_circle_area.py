import unittest
from circle import circle_area
from math import pi

class TestCircleLength(unittest.TestCase):

    def test_number(self):
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(1), 2*pi*1)
        self.assertEqual(circle_area(5), 2*pi*5)
        self.assertEqual(circle_area(1.2), 2*pi*1.2)

    def test_values(self):
        self.assertRaises(ValueError, circle_area, -6.8)
        self.assertRaises(ValueError, circle_area, -1)

    def test_types(self):
        self.assertRaises(TypeError, circle_area, 5+2j)
        self.assertRaises(TypeError, circle_area, 'text')
        self.assertRaises(TypeError, circle_area, [12, 3]) 
        self.assertRaises(TypeError, circle_area, [12])
        self.assertRaises(TypeError, circle_area, [4, 23])
        self.assertRaises(TypeError, circle_area, False) 
        self.assertRaises(TypeError, circle_area, True) 

         
if __name__ == '__main__':
    unittest.main() 
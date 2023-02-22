import unittest
from circle_length import circle_length
from math import pi

# Создаем класс для тестирования ф-ии, который
# наследуется от класса TestCase
class TestCircleLength(unittest.TestCase):

    # assertEqual - ф-ия, которая отслеживает равенство
    def test_area(self):
        self.assertEqual(circle_length(3), pi*3*2)
        self.assertEqual(circle_length(1), 2*pi)
        self.assertEqual(circle_length(0), 0)
        self.assertEqual(circle_length(2.5), pi*2.5*2)

    # Проверим, выбрасывается ли исключение для отрицательных радиусов
    def test_values(self):
        self.assertRaises(ValueError, circle_length, -2)
        self.assertRaises(ValueError, circle_length, -1)

    # Проверим, выбрасывается ли исключение о несовместимости типов
    def test_types(self):
        self.assertRaises(TypeError, circle_length, 5+2j)
        self.assertRaises(TypeError, circle_length, 'five')
        self.assertRaises(TypeError, circle_length, [16, 22])
        self.assertRaises(TypeError, circle_length, [42])
        self.assertRaises(TypeError, circle_length, True) 

         
if __name__ == '__main__':
    unittest.main() 
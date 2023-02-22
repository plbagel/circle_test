from circle import circle_area
from math import pi

def test_area_int():
    if circle_area(3) == pi*3**2:
        print("Test circle_area(int) is OK")
    else:
        print("Test circle_area(int) is FAIL")

def test_area_one():
    if circle_area(1) == pi:
        print("Test circle_area(1) is OK")
    else:
        print("Test circle_area(1) is FAIL")

def test_area_zero():
    if circle_area(0) == 0:
        print("Test circle_area(0) is OK")
    else:
        print("Test circle_area(0) is FAIL")

def test_area_float():
    if circle_area(2.5) == pi*2.5**2:
        print("Test circle_area(float) is OK")
    else:
        print("Test circle_area(float) is FAIL")

test_area_int()
test_area_one()
test_area_zero()
test_area_float()
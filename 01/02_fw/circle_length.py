from math import pi

def circle_length(radius):
    if type(radius) not in [int, float]:
        raise TypeError(("Radius must be non-negative real number only"))
    if radius < 0:
        raise ValueError("Radius can't be negative")
    return 2*pi*radius
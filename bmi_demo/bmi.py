import math

def calculate_bmi(weight, height):
    assert weight > 0
    assert height > 0
    precise_value = weight / (math.pow(height, 2))
    return math.ceil(precise_value)
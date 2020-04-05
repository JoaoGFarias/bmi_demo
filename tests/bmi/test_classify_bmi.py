from bmi_demo.bmi import classify_bmi

def test_normal_bmi():
    assert classify_bmi(weight = 80, height = 1.80) == "normal"


def test_underweight_bmi():
    assert classify_bmi(weight = 20, height = 1.80) == "underweight"

def test_overweight_bmi():
    assert classify_bmi(weight = 200, height = 1.80) == "overweight"
from bmi_demo.bmi import calculate_bmi
import pytest

def test_valid_inputs():
    assert calculate_bmi(weight = 80, height = 1.80) == 25

def test_invalid_weight():
    with pytest.raises(AssertionError):
        calculate_bmi(weight = 0, height = 1.80)
    with pytest.raises(AssertionError):
        assert calculate_bmi(weight = -1, height = 1.80)

def test_invalid_weight():
    with pytest.raises(AssertionError):
        assert calculate_bmi(weight = 80, height = 0)
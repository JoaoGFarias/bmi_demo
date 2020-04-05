
import re

import pytest
import typer
import re

from bmi_demo.cli import calculate, classify
from bmi_demo.bmi import calculate_bmi, classify_bmi


def test_calculate(capsys):
    height=1.80
    weight=80
    
    calculate(weight = weight, height = height)
    
    stdout = capsys.readouterr().out

    assert str(calculate_bmi(weight = weight, height = height)) in stdout


def test_classify(capsys):
    height=1.80
    weight=80
    
    classify(weight = weight, height = height)
    
    stdout = capsys.readouterr().out
    assert str(classify_bmi(weight = weight, height = height)) in stdout
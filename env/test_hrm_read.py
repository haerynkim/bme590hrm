#This code tests my functions in the file hrm_read.py
from hrm_read import voltage_extremes
import pytest

@pytest.mark.parametrize("candidate, expected", [
    ([1, 5, 100], (1,100))
    ([8, 9, 10, 11], (8,11))
    ([-100, 9, 7, 65, 1], (-100, 65))
])

def test_voltage_extremes(candidate, expected):
    response = voltage_extremes(candidate)
    assert response == expected

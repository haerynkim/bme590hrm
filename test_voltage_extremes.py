from hrm_read import voltage_extremes
import pytest
import numpy

@pytest.mark.parametrize("candidate, expected", [
    (numpy.array([1, 5, 100]), (1,100)),
    (numpy.array([8, 9, 10, 11]), (8,11)),
    (numpy.array([-100, 9, 7, 65, 1]), (-100, 65))
])

def test_voltage_extremes(candidate, expected):
    """
    This test checks if a tuple containing the correct minimum and maximum value of a numpy array is returned.
    """
    response = voltage_extremes(candidate)
    assert response == expected
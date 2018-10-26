from hrm_read import duration
import pytest
import numpy


@pytest.mark.parametrize("candidate, expected", [
    (numpy.array([1, 2, 3, 4, 5, 6]), 5.0),
    (numpy.array([3, 6, 12, 15, 18, 2, 9]), 6.0),
    (numpy.array([7, 6, 212, 90, 8]), 1.0)
])
def test_duration(candidate, expected):
    """
    This test checks if the function returns a float value that is the difference between the last and first element of
    the numpy array.
    """
    response = duration(candidate)
    assert response == expected

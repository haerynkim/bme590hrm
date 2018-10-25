from hrm_read import duration
import pytest

@pytest.mark.parametrize("candidate, expected", [
    ([1, 2, 3, 4, 5, 6], 5.0),
    ([3, 6, 12, 15, 18, 2, 9], 6.0),
    ([7, 6, 212, 90, 8], 1.0)
])

def test_duration(candidate, expected):
    response = duration(candidate)
    assert response == expected
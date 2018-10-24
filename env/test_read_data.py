#This code tests my function read_data in the file hrm_read.py
from hrm_read import read_data


@pytest.mark.parametrize("candidate, expected1, expected2", [
    (dummy file, val1, val2)
])

def test_read_data(candidate, expected1, expected2):
    response1, response2 = read_data(candidate)
    assert response1 == expected1
    assert response2 == expected2
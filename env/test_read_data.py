#This code tests my function read_data in the file hrm_read.py
import pytest
from hrm_read import read_data

@pytest.fixture
def file_loader():
    """Loads data from locally available test data"""

    def _loader(filename):
        fileread = numpy.genfromtxt(filename, delimiter=',')
    return fileread

#@pytest.mark.parametrize("candidate, expected1, expected2", [
#    (dummy file, val1, val2)
#])

def test_read_data(candidate, expected, file_loader):
    response1, response2 = read_data('env/ECGdata/test_data1.csv')
    t, V = file_loader()[:,0], file_loader()[:,1]
    assert response1 == t
    assert response2 == V
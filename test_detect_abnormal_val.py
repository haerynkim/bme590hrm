import pytest
import numpy
from detect_abnormal_val import detect_abnormal_val

def test_detect_abnormal_val():
    with pytest.raises(ValueError):
        detect_abnormal_val(numpy.array([-250, 100]), 200)
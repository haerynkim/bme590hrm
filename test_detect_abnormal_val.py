import pytest
import numpy
from detect_abnormal_val import detect_abnormal_val


def test_detect_abnormal_val():
    """
    This test checks if a ValueError is raised if any value in the input numpy array is greater in magnitude than a
    user-specified value.
    """
    with pytest.raises(ValueError):
        detect_abnormal_val(numpy.array([-250, 100]), 200)

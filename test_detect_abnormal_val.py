import pytest

def test_detect_abnormal_val():
    with pytest.raises(ValueError):
        detect_abnormal_val([-250], 200)
from functions.hrm_read import read_data

def test_read_data():
    """
    This test checks if the two columns of the test data have been read in correctly via spot-testing.
    """
    t, V= read_data('./ECGdata/test_data1.csv')
    assert t[0] == 0
    assert V[0] == -0.145
    assert t[9999] == 27.775
    assert V[9999] == 0.72
    assert len(t) == 10000
    assert len(V) == 10000

from find_peak import find_peak

def test_find_peak():
    b, nb = find_peak([0,0,0,0,5,0,7,8.9,3,1,1,2,0.5], thres=0.8, min_dist=0.1)
    assert [7]
    assert nb == 1
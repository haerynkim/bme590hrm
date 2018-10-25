import pytest
from cross_corr import cross_corr
import numpy

x = numpy.linspace(0.5*numpy.pi, 1.5*numpy.pi, 15)
x2 = [18.00751528, 15.85091013, 12.74821481, 8.84938525, 4.34429888, -0.54676661, -5.58417895, -10.5209674,
      -11.86736426, -12.95560465, -13.72549351, -14.13279923, -14.15147163, -13.77494825, -13.01648336]

y = [0, 0.5, 0.5, 0.5, 0]
y2 = [9.87463956e-01, 1.43794839e+00, 1.32886413e+00, 1.15314508e+00,
        9.19602512e-01, 6.39947237e-01, 3.28202337e-01, 1.66533454e-16,
        -3.28202337e-01, -6.39947237e-01, -9.19602512e-01, -1.15314508e+00,
        -1.32886413e+00, -1.43794839e+00, -9.87463956e-01]
@pytest.mark.parametrize("candidate, expected", [
    (x, x2),
    (y, y2)
])

def test_cross_corr(candidate, expected):
    response = cross_corr(candidate, startpi = 0.5*numpy.pi, endpi = 1.5*numpy.pi, intrp=15)
    numpy.testing.assert_array_almost_equal(response, expected)

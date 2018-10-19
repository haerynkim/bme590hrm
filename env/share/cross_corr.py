import numpy

def cross_corr(a, b, mode):
    correlate = numpy.correlate(a, b, mode)
    return correlate
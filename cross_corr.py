import numpy

def cross_corr(vol, startpi = 0.5*numpy.pi, endpi = 1.5*numpy.pi, intrp=15):
    """This function will generate a sine wave given an array of intrp number of elements
    from start to end point and cross-correlate the voltage array with this sine wave.
    It returns a numpy array of correlation coefficients.

    :param vol: array
    :param startpi: float, starting point of sine wave
    :param endpi: float, end point of sine wave
    :param intrp: int total number of points interpolated between starting point and end point
    :return:
    """
    t = numpy.linspace(startpi, endpi, intrp)
    qrs_filter = numpy.sin(t)
    correlate = numpy.correlate(qrs_filter, vol, mode="same")
    return correlate
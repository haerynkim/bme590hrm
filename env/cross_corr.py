import numpy
import matplotlib
import matplotlib.pyplot as plt
import peakutils

def cross_corr(vol, startpi = 0.5*numpy.pi, endpi = 1.5*numpy.pi, intrp=15):
    t = numpy.linspace(startpi, endpi, intrp)
    qrs_filter = numpy.sin(t)
    correlate = numpy.correlate(qrs_filter, vol, mode="same")
    return correlate
import numpy as np
import peakutils
import scipy

def find_peak(corr, thres=0.8, min_dist=0.1):
    """
    This function finds the local maxima given an array.

    :param corr: list
    :return: list
    """
    cb = np.array(corr)
    beats = peakutils.indexes(cb, thres, min_dist)
    #num_beats = len(beats)
    return beats
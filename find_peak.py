import numpy as np
import peakutils


def find_peak(corr, thres=0.5, min_dist=0.1):
    """
    This function finds the peaks of a given an array, given parameters like threshold (default 0.5) and minimum
    distance between peaks (default 0.1). It will return the indexes at which these peaks happened, and the number of
    peaks that were detected.

    :param corr: numpy.ndarray
    :param thres: float
    :param min_dist: float
    :return: beatidx: 'numpy.ndarray', num_beats: 'int'
    """
    cb = np.array(corr)
    beatidx = peakutils.indexes(cb, thres, min_dist)
    num_beats = len(beatidx)
    return beatidx, num_beats

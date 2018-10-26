from warnings import warn
import numpy
from hrm_read import read_data
from find_peak import find_peak

def read_bpm(time, voltage, starttime=0, endtime=20):
    """ This function calculates the average heart rate over user-specified integer number of seconds and returns
    value as a float. If user inputs a float as arguments, the function will generate a warning.

    :param time: numpy.ndarray
    :param voltage: numpy.ndarray
    :param starttime: int
    :param endtime: int
    :return: float
    """
    if type(starttime) != int or type(endtime) != int:
        warn("System expects integers for starttime or endtime. Program will round down to nearest integer.")
        if starttime < 0.5 or endtime < 0.5:
            starttime = round(starttime)
            endtime = round(endtime)
        else:
            starttime = round(starttime-0.5)
            endtime = round(endtime-0.5)
    if (starttime in time) == True and (endtime in time) == True:
            startidx = numpy.where(time==starttime)[0][0]
            endidx = numpy.where(time==endtime)[0][0]
            time = time[startidx:endidx]
            voltage = voltage[startidx:endidx]
            peakidx, numpeak = find_peak(voltage, thres=0.5, min_dist=0.1)
            peaktimes = time[peakidx]
            rr_int = [t - s for s, t in zip(peaktimes, peaktimes[1:])]
            rr_avg = sum(rr_int) / float(len(rr_int))
            mean_hr_bpm = 60 / rr_avg
    else:
        warn("Input values are out of range of data. Program will continue by calculating mean heart rate of entire array.")
        peakidx_def, numpeak_def = find_peak(voltage, thres=0.5, min_dist=0.1)
        peaktimes_def = time[peakidx_def]
        rr_int_def = [t - s for s, t in zip(peaktimes_def, peaktimes_def[1:])]
        rr_avg_def = sum(rr_int_def) / float(len(rr_int_def))
        mean_hr_bpm = 60 / rr_avg_def
    return float(mean_hr_bpm)
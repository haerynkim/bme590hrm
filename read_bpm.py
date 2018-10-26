from warnings import warn
import numpy
from hrm_read import read_data
from find_peak import find_peak

def read_bpm(filename, starttime=0, endtime=20):
    """ This function calculates the average heart rate over user-specified integer number of seconds and returns
    value as a float. If user inputs a float as arguments, the function will generate a warning.

    :param filename: .csv file
    :param starttime: int
    :param endtime: int
    :return: float
    """
    time, voltage = read_data(filename)
    if type(starttime) != int or type(endtime) != int:
        warn("System expects integers for starttime or endtime.")
        starttime = round(starttime)
        endtime = round(endtime)
    startidx = numpy.where(time==starttime)[0][0]
    endidx = numpy.where(time==endtime)[0][0]
    time = time[startidx:endidx+1]
    voltage = voltage[startidx:endidx+1]
    peakidx, numpeak = find_peak(voltage, thres=0.5, min_dist=0.1)
    peaktimes = time[peakidx]
    rr_int = [t-s for s, t in zip(peaktimes, peaktimes[1:])]
    rr_avg = sum(rr_int) / float(len(rr_int))
    mean_hr_bpm = 60/rr_avg
    return float(mean_hr_bpm)
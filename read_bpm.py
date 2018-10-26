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
        warn("System expects integers for starttime or endtime.")
        starttime = round(starttime)
        endtime = round(endtime)
    if (starttime in time) == True and (endtime in time) == True:
    startidx = numpy.where(time==starttime)[0][0]
    endidx = numpy.where(time==endtime)[0][0]
    else:
        print('Pick a different parameter for either starttime or endtime.')
    time = time[startidx:endidx+1]
    voltage = voltage[startidx:endidx+1]
    peakidx, numpeak = find_peak(voltage, thres=0.5, min_dist=0.1)
    peaktimes = time[peakidx]
    rr_int = [t-s for s, t in zip(peaktimes, peaktimes[1:])]
    rr_avg = sum(rr_int) / float(len(rr_int))
    mean_hr_bpm = 60/rr_avg
    return float(mean_hr_bpm)

if __name__ == "__main__":
    t, V = read_data("ECGdata/test_data31.csv")
    bpm = read_bpm(t,V,0.0,15.0)
    print(bpm)
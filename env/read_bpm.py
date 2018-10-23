from hrm_read import read_data
from find_peak import find_peak

def read_bpm(filename, starttime=0, endtime=20):
    """ This function calculates the average heart rate over user-specified number of minutes.

    :param filename: .csv file
    :return:
    """
    time, voltage = read_data(filename)
    #if user_min < 0 or user_min >
    startidx = time.index(starttime)
    endidx = time.index(endtime)
    time = time[startidx:endidx]
    voltage = voltage[startidx:endidx]
    peakidx = find_peak(voltage, thres=0.8, min_dist=0.1)
    peaktimes = time[peakidx]
    rr_int = [t-s for s, t in zip(peaktimes, peaktimes[1:])]
    rr_avg = sum(rr_int) / float(len(rr_int))
    mean_hr_bpm = 60/rr_avg
    return mean_hr_bpm
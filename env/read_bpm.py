from hrm_read import read_data
from find_peak import find_peak

def read_bpm(filename, default_min=20):
    """ This function calculates the average heart rate over user-specified number of minutes.

    :param filename: .csv file
    :return:
    """
    time, voltage = read_data(filename)
    try:
        user_sec = input("Input number of seconds you want to average heart rate over (input integer value.)")
    except SyntaxError:
        user_sec = None
    if user_sec is None:
        user_sec = default_min
    if type(user_sec) is not int:
        raise TypeError("Inputs must be python integers.") #I want this later to try rounding up.
        # How to default?
    #if user_min < 0 or user_min >
    idx = time.index(user_sec)
    time = time[:idx]
    voltage = voltage[:idx]
    peakidx = find_peak(voltage, thres=0.8, min_dist=0.1)
    peaktimes = time[peakidx]
    rr_int = [t-s for s, t in zip(peaktimes, peaktimes[1:])]
    rr_avg = sum(rr_int) / float(len(rr_int))
    mean_hr_bpm = 60/rr_avg
    return mean_hr_bpm
import matplotlib.pyplot as plt
from cross_corr import cross_corr
from hrm_read import read_data
from find_peak import find_peak
from read_bpm import read_bpm

filename = '/Users/haerynkim/PycharmProjects/bme590hrm/env/ECGdata/test_data1.csv'

def main(filename, ):
    time, voltage = read_data(filename)
    mean_hr_bpm = read_bpm(filename, default_min=20)
    correlate = cross_corr(voltage, startpoint = 0.5*numpy.pi, endpoint = 1.5*numpy.pi, intrp=15)
    peaktime = find_peak(voltage, thres=0.8, min_dist=0.1)


if __name__ == '__main__':


    #r_r = peaktime[6]-peaktime[5] #time between fifth and sixth peak
    #qrs = voltage[int :int((peaktime[5]+peaktime[6])/2)]
    #print(correlate[find_peak(correlate)])
    #print(qrs)

    plt.figure(1)
    plt.plot(correlate, 'g:', find_peak(correlate), correlate[find_peak(correlate)], 'bo')
    #plt.plot(qrs)
    plt.show()
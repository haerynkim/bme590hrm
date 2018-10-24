import matplotlib.pyplot as plt
from hrm_read import voltage_extremes
from cross_corr import cross_corr
from hrm_read import read_data
from hrm_read import duration
from hrm_read import voltage_extremes
from find_peak import find_peak
from read_bpm import read_bpm
from dictionary import create_dictionary
from dictionary import add_to_dictionary
from write_json import write_json

filename = 'ECGdata/test_data1.csv'

def main(filename):
    time, voltage = read_data(filename)
    mean_hr_bpm = read_bpm(filename, starttime=0, endtime=20)
    correlate = cross_corr(voltage, startpi = 0.5*numpy.pi, endpi = 1.5*numpy.pi, intrp=15)
    beats, num_beats = find_peak(correlate, thres=0.8, min_dist=0.1)
    voltage_extremes = voltage_extremes(voltage)
    duration = duration(time)
    metrics = create_dictionary()
    metrics = add_to_dictionary(metrics, 'mean_hr_bpm', mean_hr_bpm)
    metrics = add_to_dictionary(metrics, 'voltage_extremes', voltage_extremes)
    metrics = add_to_dictionary(metrics, 'duration', duration)
    metrics = add_to_dictionary(metrics, 'num_beats', num_beats)
    metrics = add_to_dictionary(metrics, 'beats', beats)
    #outfile = write_json(filename, metrics)
    #return outfile

if __name__ == '__main__':
    main(filename)


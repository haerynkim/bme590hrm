import sys
from cross_corr import cross_corr
from hrm_read import read_data
from hrm_read import duration
from hrm_read import voltage_extremes
from find_peak import find_peak
from read_bpm import read_bpm
from dictionary import add_to_dictionary
from write_json import write_json
from detect_abnormal_val import detect_abnormal_val
import numpy

def main(filename):
    time, voltage = read_data(filename)
    try:
        detect_abnormal_val(voltage, abs_range=200)
    except ValueError:
        sys.exit('Voltage out of this world. Consult doctor immediately.')
    mean_hr_bpm = read_bpm(time, voltage, starttime=0, endtime=20)
    correlate = cross_corr(voltage, startpi=0.5 * numpy.pi, endpi=1.5 * numpy.pi, intrp=15)
    beatidx, num_beats = find_peak(correlate, thres=0.5, min_dist=0.1)
    beats = time[beatidx]
    voltage_extremes = voltage_extremes(voltage)
    duration = duration(time)
    metrics = dict()
    metrics = add_to_dictionary(metrics, 'mean_hr_bpm', mean_hr_bpm)
    metrics = add_to_dictionary(metrics, 'voltage_extremes', voltage_extremes)
    metrics = add_to_dictionary(metrics, 'duration', duration)
    metrics = add_to_dictionary(metrics, 'num_beats', num_beats)
    metrics = add_to_dictionary(metrics, 'beats', beats)
    write_json(filename, metrics)


if __name__ == '__main__':
    filename = 'ECGdata/test_data31.csv'
    main(filename)

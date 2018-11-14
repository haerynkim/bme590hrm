import sys
from functions.cross_corr import cross_corr
from functions.hrm_read import read_data
from functions.hrm_read import duration
from functions.hrm_read import voltage_extremes
from functions.find_peak import find_peak
from functions.read_bpm import read_bpm
from functions.dictionary import add_to_dictionary
from functions.write_json import write_json
from functions.detect_abnormal_val import detect_abnormal_val
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
    minmax = voltage_extremes(voltage)
    dur = duration(time)
    metrics = dict()
    metrics = add_to_dictionary(metrics, 'mean_hr_bpm', mean_hr_bpm)
    metrics = add_to_dictionary(metrics, 'voltage_extremes', minmax)
    metrics = add_to_dictionary(metrics, 'duration', dur)
    metrics = add_to_dictionary(metrics, 'num_beats', num_beats)
    metrics = add_to_dictionary(metrics, 'beats', beats)
    write_json(filename, metrics)


if __name__ == '__main__':
    filename = 'ECGdata/test_data1.csv'
    main(filename)

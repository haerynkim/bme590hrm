import numpy

def read_data(filename):
    """ This function reads a .csv file and extracts time and voltage arrays.

    :param filename: .csv
    :return: lists
    """
    data = numpy.genfromtxt(filename, delimiter=',')
    time = data[:, 0]
    voltage = data[:, 1]
    return time, voltage

def voltage_extremes(V):
    """ This function returns the max and min voltages found from a voltage array in a tuple form.

    :param V: list
    :return: tuple

    later: add test to see if voltage_extreme returns tuple. add exceptions to see if a list is passed as input.
    """
    maxV = max(V)
    minV = min(V)
    return (minV,maxV)

def duration(t):
    """ This function returns a float that represents the duration of the ECG strip.

    :param t: list
    :return: float

    add test that checks if t is list
    """
    dur = t[-1] - t[0]
    return float(dur)
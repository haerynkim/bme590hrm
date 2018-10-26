import numpy


def read_data(filename):
    """ This function reads a .csv file and extracts time and voltage arrays. The 'numpy.genfromtxt' function is a
    robust mechanism that internally screens for strings and missing values and leaves those rows out from the numpy
    arrays that are returned.

    :param filename: .csv file
    :return: time: numpy.ndarray, voltage: numpy.ndarray
    """
    data = numpy.genfromtxt(filename, delimiter=',')
    time = data[:, 0]
    voltage = data[:, 1]
    return time, voltage


def voltage_extremes(V):
    """ This function returns the minimum and maximum voltages found from a voltage array in a tuple form.

    :param V: numpy.ndarray
    :return: tuple (minimum voltage, maximum voltage)
    """
    maxV = numpy.amax(V)
    minV = numpy.amin(V)
    return (minV, maxV)


def duration(t):
    """ This function returns a float that represents the duration of the ECG strip.

    :param t: numpy.ndarray
    :return: float
    """
    dur = t[-1] - t[0]
    return float(dur)

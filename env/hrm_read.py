import numpy

def read_data(filename):
    """ This function returns time and voltage arrays from an input file.
    """
    data = numpy.genfromtxt(filename, delimiter=',')
    time = data[:, 0]
    voltage = data[:, 1]
    return time, voltage
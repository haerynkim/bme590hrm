import numpy

def read_data(filename):
    """ This function returns time and voltage arrays from an input file.
    """
    data = numpy.genfromtxt(filename, delimiter=',')
    time = data[:, 0]
    voltage = data[:, 1]
    return time, voltage

def voltage_extreme(V):
    """ This function returns the max and min voltages found from a voltage array in a tuple form.
        :param V:
    :return:


    later: add test to see if voltage_extreme returns tuple. add exceptions to see if a list is passed as input.
    """
    maxV = max(V)
    minV = min(V)
    return tuple([minV,maxV])
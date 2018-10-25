def detect_abnormal_val(V, abs_range=200):
    """This function will see if any value in numpy array V exceeds the range of a user-
    specified value (integer value, defaulted to 200).

    :param V: numpy ndarray
    :param abs_range: int
    :return: numpy ndarray
    """
    for i in V.absolute:
        if i >= abs_range:
            print('Voltage values out of this world. Consult doctor immediately.')
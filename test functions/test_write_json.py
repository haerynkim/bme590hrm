import os
import pytest
from functions.write_json import write_json


@pytest.fixture
def mktmpdir(tmpdir_factory):
    """ This creates a temporary directory for unit tests.
    
    :param tmpdir_factory: directory
    :return: tmpdir
    """
    tmpdir = tmpdir_factory.mktemp('tmp')
    return tmpdir


@pytest.fixture
def pathfile(mktmpdir):
    """
    This creates a .csv file in the temporary directory, mkrmpdir, and returns the file's pathway.
    """
    file = mktmpdir.join('/emptyfile.csv')
    path = file.strpath
    return path


def test_write_json(pathfile, mktmpdir):
    """ This function tests if the write_json function generates a json file after being passed a
    path in a temp directory and writes the sample dictionary in that path.

    :param pathfile: pytest fixture that points to specific file's path in temporary directory
    :param mktmpdir: pytest fixture that points to temporary directory
    """
    sampledict = {
        'This': 9,
        'Is': 8,
        'Hard': 7
    }
    write_json(pathfile, sampledict)
    assert os.path.exists('emptyfile.json') == True

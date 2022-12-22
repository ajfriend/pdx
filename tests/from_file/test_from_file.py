import pdx
import os

def get_absolute_filename(local_filename):
    s = os.path.dirname(os.path.realpath(__file__)) + '/' + local_filename
    return s

def test_from_file():
    iris = pdx.data.get_iris()

    expected = {'setosa': 50, 'versicolor': 50, 'virginica': 50}

    f = get_absolute_filename('short.sql')
    assert iris.sql(f).cols2dict() == expected

    f = get_absolute_filename('long.sql')
    assert pdx.sql(f, tbl=iris).cols2dict() == expected

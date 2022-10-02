from pandas.core.base import PandasObject

from . import _query

def _insist_single_row(df):
    if len(df) != 1:
        raise ValueError(f'DataFrame has {len(df)} rows, but should only have 1.')

def _insist_single_col(df):
    if len(df.columns) != 1:
        raise ValueError(f'DataFrame has {len(df.columns)} columns, but should only have 1.')

def _insist_single_row_or_col(df):
    if len(df.columns) == 1 or len(df) == 1:
        pass
    else:
        raise ValueError(f'DataFrame should have a single row or column, but has shape f{df.shape}')


def _sql(df, s='', tbl_name='tbl'):
    """ Run a SQL query against Pandas DataFrame.

    DataFrame will be referred to by string given in `tbl_name`.

    Examples
    --------
    >>> df.sql('select * from tbl')
    >>> df.sql('select * from new_tbl', tbl_name='new_tbl')

    """
    if not s:
        s = f'select * from {tbl_name}'

    tables = {tbl_name: df}

    return _query.sql(s, **tables)


def _prql(df, s='', tbl_name='tbl'):
    s = f'from {tbl_name}\n' + s
    tables = {tbl_name: df}

    return _query.prql(s, **tables)


def _as_list(df):
    """Transform a df with one row or one column to a list"""
    if len(df.columns) == 1:
        col = df.columns[0]
        out = list(df[col])
    elif len(df) == 1:
        out = list(df.loc[0])
    else:
        raise ValueError(f'DataFrame should have a single row or column, but has shape f{df.shape}')

    return out


def _as_dict(df):
    """Transform a df with one row to a dict
    """
    _insist_single_row(df)

    out = dict(df.iloc[0])

    return out

def _as_item(df):
    """Transform a df with one row and one column to single element"""
    _insist_single_row(df)
    _insist_single_col(df)

    out = _as_list(df)[0]

    return out


def _cols2dict(df):
    cols = df.columns

    if len(cols) != 2:
        raise ValueError(f'DataFrame should have 2 columns, but has {len(df.columns)}.')

    k = cols[0]
    v = cols[1]

    k = df[k]
    v = df[v]

    out = dict(zip(k, v))

    return out


PandasObject.sql = _sql
PandasObject.pdx_sql = _sql

PandasObject.prql = _prql
PandasObject.pdx_prql = _prql

PandasObject.as_list = _as_list
PandasObject.aslist = _as_list

PandasObject.as_dict = _as_dict
PandasObject.asdict = _as_dict

PandasObject.as_item = _as_item
PandasObject.asitem = _as_item

PandasObject.cols2dict = _cols2dict

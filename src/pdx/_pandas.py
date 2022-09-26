from pandas.core.base import PandasObject

from . import _query

def _insist_single_row(df):
    if len(df) != 1:
        raise ValueError(f'DataFrame has {len(df)} rows, but should only have 1.')

def _insist_single_col(df):
    if len(df.columns) != 1:
        raise ValueError(f'DataFrame has {len(df.columns)} columns, but should only have 1.')



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
    """Transform a df with one column to a list"""
    _insist_single_col(df)

    col = df.columns[0]
    out = list(df[col])

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


PandasObject.sql = _sql
PandasObject.pdx_sql = _sql

PandasObject.prql = _prql
PandasObject.pdx_prql = _prql

PandasObject.as_list = _as_list
PandasObject.as_dict = _as_dict
PandasObject.as_item = _as_item

from pandas.core.base import PandasObject

from ._query import query, pqrl_to_sql

def _sql(df, s=None, tbl_name='tbl'):
    """ Run a SQL query against Pandas DataFrame.

    DataFrame will be referred to by string given in `tbl_name`.

    Examples
    --------
    >>> df.sql('select * from tbl')
    >>> df.sql('select * from new_tbl', tbl_name='new_tbl')

    """
    if s is None:
        s = f'select * from {tbl_name}'

    tables = {tbl_name: df}

    return query(s, **tables)

def _prql(df, s='', tbl_name='tbl', show_queries=False):
    s = f'from {tbl_name}\n' + s

    s = pqrl_to_sql(s, show_queries=show_queries)

    return _sql(df, s, tbl_name=tbl_name)


def _insist_single_row(df):
    if len(df) != 1:
        raise ValueError(f'DataFrame has {len(df)} rows, but should only have 1.')

def _insist_single_col(df):
    if len(df.columns) != 1:
        raise ValueError(f'DataFrame has {len(df.columns)} columns, but should only have 1.')


def _df_as_list(df):
    """Transform a df with one column to a list"""
    _insist_single_col(df)

    col = df.columns[0]
    out = list(df[col])

    return out

def _df_as_dict(df):
    """Transform a df with one row to a dict
    """
    _insist_single_row(df)

    out = dict(df.iloc[0])

    return out

def _df_as_item(df):
    """Transform a df with one row and one column to single element"""
    _insist_single_row(df)
    _insist_single_col(df)

    out = _df_as_list(df)[0]

    return out


PandasObject.sql = _sql
PandasObject.prql = _prql
PandasObject.as_list = _df_as_list
PandasObject.as_dict = _df_as_dict
PandasObject.as_item = _df_as_item

# class _pdq:
#     as_list = df_as_list
#     as_dict = df_as_dict
#     as_item = df_as_item

# PandasObject.pqd = _pdq


# todo: maybe also supply these functions so they can be called
# directly, not needing to be methods of the dataframe

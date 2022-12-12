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
    """ Run a DuckDB SQL query against Pandas DataFrame.

    DataFrame will be referred to by string given in `tbl_name`.
    The query starts with a `from {table_name}` clause.
    Since DuckDB 0.6, the `select` clause is optional, defaulting to `select *`.

    Examples
    --------

    ```
    df.sql('select col_a where col_b > 0')
    ```

    is equivalent to the query

    ```
    select
        col_a
    from
        tbl
    where
        col_b > 0
    ```


    `df.sql('where col_b > 0')` is equivalent to

    ```
    select
        *
    from
        tbl
    where
        col_b > 0
    ```

    Note that `df.sql()` is equivalent to

    ```
    select * from tbl
    ```
    """

    s = f'from {tbl_name}\n' + s
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
PandasObject.prql = _prql

PandasObject.aslist = _as_list
PandasObject.asdict = _as_dict
PandasObject.asitem = _as_item
PandasObject.cols2dict = _cols2dict

import pandas

from . import _query

def _insist_single_row(df):
    if len(df) != 1:
        raise ValueError(f'DataFrame has {len(df)} rows, but should only have 1.')

def _insist_single_col(df):
    if len(df.columns) != 1:
        raise ValueError(f'DataFrame has {len(df.columns)} columns, but should only have 1.')


@pandas.api.extensions.register_dataframe_accessor('pdq')
class PDQAccessor:
    def __init__(self, pandas_obj):
        self._df = pandas_obj

    def sql(self, s='', tbl_name='tbl'):
        """ Run a SQL query against Pandas DataFrame.

        DataFrame will be referred to by string given in `tbl_name`.

        Examples
        --------
        >>> df.sql('select * from tbl')
        >>> df.sql('select * from new_tbl', tbl_name='new_tbl')

        """
        if not s:
            s = f'select * from {tbl_name}'

        tables = {tbl_name: self._df}

        return _query.sql(s, **tables)

    def prql(self, s='', tbl_name='tbl'):
        s = f'from {tbl_name}\n' + s
        tables = {tbl_name: self._df}

        return _query.prql(s, **tables)

    def as_list(self):
        """Transform a df with one column to a list"""
        df = self._df
        _insist_single_col(df)

        col = df.columns[0]
        out = list(df[col])

        return out

    def as_dict(self):
        """Transform a df with one row to a dict
        """
        df = self._df
        _insist_single_row(df)

        out = dict(df.iloc[0])

        return out

    def as_item(self):
        """Transform a df with one row and one column to single element"""
        df = self._df
        _insist_single_row(df)
        _insist_single_col(df)

        col = df.columns[0]
        out = list(df[col])
        out = out[0]

        return out


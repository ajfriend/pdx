from pandas.core.base import PandasObject

from .query import dquery, pqrl_to_sql

def _sql(df, s=None, tbl_name='tbl', _single_row_as_dict_=True):
    if s is None:
        s = f'select * from {tbl_name}'

    tables = {tbl_name: df}

    return dquery(s, _single_row_as_dict_=_single_row_as_dict_, **tables)


def _prql(df, s, tbl_name='tbl', _single_row_as_dict_=True, show_queries=False):
    s = f'from {tbl_name}\n' + s

    s = pqrl_to_sql(s, show_queries=show_queries)

    return _sql(df, s, tbl_name=tbl_name, _single_row_as_dict_=_single_row_as_dict_)


PandasObject.sql = _sql
PandasObject.prql = _prql


# todo: maybe also supply these functions so they can be called
# directly, not needing to be methods of the dataframe

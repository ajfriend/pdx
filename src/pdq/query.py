import duckdb
import prql_python as prql

def dquery(
    query_string,
    _single_row_as_dict_=True,
    **dfs_for_query,
):
    con = duckdb.connect(database=':memory:')
    for tbl_name, df in dfs_for_query.items():
        con.register(tbl_name, df)

    out = con.execute(query_string).df()

    if _single_row_as_dict_ and len(out) == 1:
        out = dict(out.iloc[0])

    return out


def pqrl_to_sql(s, show_queries=False):
    if show_queries:
        print(s)

    s = prql.to_sql(s)

    if show_queries:
        print(s)

    return s

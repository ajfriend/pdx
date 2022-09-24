import duckdb
import prql_python as prql

def dquery(
    query_string,
    **dfs_for_query,
):
    con = duckdb.connect(database=':memory:')
    for tbl_name, df in dfs_for_query.items():
        con.register(tbl_name, df)

    out = con.execute(query_string).df()

    return out


def pqrl_to_sql(s, show_queries=False):
    if show_queries:
        print(s)

    s = prql.to_sql(s)

    if show_queries:
        print(s)

    return s

import duckdb
import os

def save(filename, **dfs):
    try:
        os.remove(filename)
    except OSError:
        pass

    config = {'enable_external_access': False}
    con = duckdb.connect(database=filename, config=config)

    for tbl_name, df in dfs.items():
        temp_df_name = '__tmp_duckdb__' + tbl_name
        con.register(temp_df_name, df)
        con.execute(f'create table {tbl_name} as select * from {temp_df_name}')

    con.close()


def load(filename):
    config = {'enable_external_access': False}
    con = duckdb.connect(database=filename, config=config, read_only=True)

    tbl_names = list(con.execute('show tables;').df()['name'])

    dfs = {
        tbl_name: con.execute(f'select * from {tbl_name}').df()
        for tbl_name in tbl_names
    }

    con.close()

    return dfs

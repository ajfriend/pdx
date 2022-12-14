# PDX: Helper functions to run SQL on Pandas DataFrames

```shell
pip install git+https://github.com/ajfriend/pdx
```

- powered by [DuckDB](https://duckdb.org/) and [PRQL](https://prql-lang.org/)
- [Apache Arrow and the "10 Things I Hate About pandas"](https://wesmckinney.com/blog/apache-arrow-pandas-internals/)

Check out the [example notebook folder](notebooks).

## Useful stuff

- `pdx.get_params(query_string)`
- `df.sql(query_string)`
- `df.prql(query_string)`
- duckdb save/load
  - `pdx.save(filename, tbl1=df1, tbl2=df2)`
  - `pdx.load(filename) -> dict(table_name: dataframe)`

## For bleeding edge DuckDB

```
git clone https://github.com/duckdb/duckdb.git
cd duckdb
../env/bin/pip install -e tools/pythonpkg --verbose
```

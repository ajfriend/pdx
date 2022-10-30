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

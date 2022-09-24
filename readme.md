# todo

- add a method to pandas dataframes
    + `df.sql('...')`
    + `df.prql('...')`


# thoughts

- i dunno. maybe the default duckdb is pretty good
    + https://duckdb.org/2021/05/14/sql-on-pandas.html
    + except, i dont' know if i like the implicit namespace stuff they're doing

https://gist.github.com/ajfriend/6942bdd4a9eb31861f7dfab471f411fb


- also, maybe the whole relational API is pretty good?
    + https://duckdb.org/2021/05/14/sql-on-pandas.html

# idea: garbage-collected, duckdb-backed pandas replacement

- avoids marshalling back and forth to pandas
- lets users use natural python interface, instead


# viewers/editors

- https://duckdb.org/docs/guides/data_viewers/tad
    + https://www.tadviewer.com/
- https://duckdb.org/docs/guides/sql_editors/dbeaver


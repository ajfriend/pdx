import pdx
from pytest import approx


def test_from_first_sql():
    iris = pdx.data.get_iris()

    foo = lambda s: iris.sql(s).asitem()

    assert (
        foo('select avg(sepal_length)')
        ==
        approx(5.843333333333335)
    )

    assert (
        foo('select avg(sepal_length) where sepal_length < 6.0')
        ==
        approx(5.224096385542169)
    )

    assert (
        foo('select avg(sepal_length) where sepal_length > 6.0')
        ==
        approx(6.670491803278686)
    )


def test_from_first_prql():
    iris = pdx.data.get_iris()

    foo = lambda s: iris.prql(s).asitem()

    assert (
        foo('aggregate [average sepal_length]')
        ==
        approx(5.843333333333335)
    )

    assert (
        foo("""
            filter sepal_length < 6.0
            aggregate [average sepal_length]
        """)
        ==
        approx(5.224096385542169)
    )

    assert (
        foo("""
            filter sepal_length > 6.0
            aggregate [average sepal_length]
        """)
        ==
        approx(6.670491803278686)
    )

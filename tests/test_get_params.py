import pdx

def test_one():
    s = """
    select
        *
    from
        tbl
    where
        datestr = {{datestr}}
    """

    params = pdx.get_params(s)

    expected = {
        'datestr': ...,
    }

    assert params == expected


def test_two():
    s = """
    {{datestr}} {{param1}} {{param2}} {{param3}}
    """

    params = pdx.get_params(s)

    expected = {
        'datestr': ...,
        'param1': ...,
        'param2': ...,
        'param3': ...,
    }

    assert params == expected

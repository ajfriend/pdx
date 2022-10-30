from jinja2 import Environment, meta


def _get_jinja_params(s):
    env = Environment()
    ast = env.parse(s)
    var_names = meta.find_undeclared_variables(ast)
    var_names = sorted(var_names)

    return var_names


def get_params(s):
    var_names = _get_jinja_params(s)

    out = {
        name: ...
        for name in var_names
    }

    return out

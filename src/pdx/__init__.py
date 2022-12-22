from ._query import (
    sql,
    prql,
    pqrl_to_sql,
)

from . import _pandas # triggers pandas monkeypatching
from . import _data as data
from ._io import save, load

import importlib.metadata
__version__ = importlib.metadata.version(__package__ or __name__)

from ._query import (
    sql,
    prql,
    pqrl_to_sql,
)

from . import _pandas # triggers pandas monkeypatching

try: # dumb hack to get this to work on 3.7 today
    from . import _data as data
except:
    pass
    
from ._io import save, load

try: # dumb hack to get this to work on 3.7 today
    import importlib.metadata
    __version__ = importlib.metadata.version(__package__ or __name__)
except:
    __version__ = '0.4.0'

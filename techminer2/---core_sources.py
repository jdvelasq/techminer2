"""
Core Sources
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> core_sources(directory)
   Num Sources        %  ...  Tot Documents Bradford's Group
0            1   1.49 %  ...         5.32 %                1
1            2   2.99 %  ...        13.83 %                1
2            4   5.97 %  ...         26.6 %                1
3            9  13.43 %  ...        45.74 %                2
4           51  76.12 %  ...        100.0 %                3
<BLANKLINE>
[5 rows x 9 columns]

>>> from pprint import pprint
>>> columns = core_sources(directory).columns.to_list()
>>> pprint(columns)
['Num Sources',
 '%',
 'Acum Num Sources',
 '% Acum',
 'Documents published',
 'Tot Documents published',
 'Num Documents',
 'Tot Documents',
 "Bradford's Group"]

"""

import numpy as np
import pandas as pd

from ._read_records import read_records
from .explode import explode

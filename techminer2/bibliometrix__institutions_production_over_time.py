"""
Institutions' Production over Time
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__institutions_production_over_time.html"

>>> from techminer2 import bibliometrix__institutions_production_over_time
>>> pot = bibliometrix__institutions_production_over_time(
...    top_n=10, 
...    directory=directory,
... )

>>> pot.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__institutions_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> pot.documents_per_institution_.head()
                                institutions  ...                           doi
0                 University of Johannesburg  ...    10.1057/S41261-020-00134-0
1  ---Indian Institute of Management Lucknow  ...    10.1057/S41261-020-00127-Z
2                           Ahlia University  ...  10.1007/978-981-15-3383-9_32
3                Conventional Wholesale Bank  ...  10.1007/978-981-15-3383-9_32
4                  Mendel University in Brno  ...   10.1007/978-3-030-62796-6_9
<BLANKLINE>
[5 rows x 7 columns]

>>> pot.production_per_year_.head()
                                                         OCC  ...  local_citations_per_year
institutions                                       year       ...                          
---3PB                                             2022    1  ...                     0.000
---ABES Engineering College                        2021    1  ...                     0.000
---AML Forensic library KPMG Luxembourg Societe... 2020    1  ...                     0.333
---Audencia PRES LUNAM                             2018    1  ...                     0.600
---BITS Pilani                                     2020    1  ...                     0.000
<BLANKLINE>
[5 rows x 7 columns]


"""
from dataclasses import dataclass

from .bibliometrix__production_over_time import bibliometrix__production_over_time
from .column_indicators_by_year import column_indicators_by_year
from .documents_per import documents_per


@dataclass(init=False)
class _Results:
    plot_ = None
    production_per_year_ = None
    documents_per_institution_ = None


def bibliometrix__institutions_production_over_time(
    top_n=10,
    directory="./",
):
    """Institution production over time."""

    results = _Results()
    results.plot_ = bibliometrix__production_over_time(
        column="institutions",
        top_n=top_n,
        directory=directory,
        title="Institutions' production over time",
    )
    results.documents_per_institution_ = documents_per(
        column="institutions",
        directory=directory,
    )
    results.production_per_year_ = column_indicators_by_year(
        "institutions",
        directory=directory,
    )

    return results

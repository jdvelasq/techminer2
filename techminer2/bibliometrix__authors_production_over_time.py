"""
Authors' Production over Time
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__authors_production_over_time.html"


>>> from techminer2 import bibliometrix__authors_production_over_time
>>> pot = bibliometrix__authors_production_over_time(
...    top_n=10, 
...    directory=directory,
... )

>>> pot.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__authors_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>



>>> pot.documents_per_author_.head()
        authors  ...                           doi
0   von Solms J  ...    10.1057/S41261-020-00134-0
1   Dashottar S  ...    10.1057/S41261-020-00127-Z
2  Srivastava V  ...    10.1057/S41261-020-00127-Z
3       Turki M  ...  10.1007/978-981-15-3383-9_32
4      Hamdan A  ...  10.1007/978-981-15-3383-9_32
<BLANKLINE>
[5 rows x 7 columns]


>>> pot.production_per_year_.head()
                   OCC  ...  local_citations_per_year
authors      year       ...                          
Abdullah Y   2022    1  ...                     0.000
Abi-Lahoud E 2018    1  ...                     0.000
Ajmi JA      2021    1  ...                     0.500
Al Haider N  2020    1  ...                     0.333
Alam TM      2021    1  ...                     0.000
<BLANKLINE>
[5 rows x 7 columns]



"""
from .bibliometrix__production_over_time import bibliometrix__production_over_time
from .column_indicators_by_year import column_indicators_by_year
from .documents_per import documents_per


class _Result:
    def __init__(self):
        self.plot_ = None
        self.production_per_year_ = None
        self.documents_per_author_ = None


def bibliometrix__authors_production_over_time(
    top_n=10,
    directory="./",
):
    """Author production over time."""

    result = _Result()
    result.plot_ = bibliometrix__production_over_time(
        column="authors",
        top_n=top_n,
        directory=directory,
        title="Authors' Production over Time",
    )
    result.documents_per_author_ = documents_per(
        column="authors",
        directory=directory,
    )

    result.production_per_year_ = column_indicators_by_year(
        "authors",
        directory=directory,
    )

    return result

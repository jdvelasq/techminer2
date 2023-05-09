"""
Source Impact
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__source_impact.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.sources.source_impact(
...     impact_measure='h_index',
...     topics_length=20, 
...     directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__source_impact.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()
                  Source Abbr  ...  Avg Global Citations
0                J BANK REGUL  ...                  17.5
1              J FINANC CRIME  ...                   6.5
2  LECT NOTES BUS INF PROCESS  ...                   2.0
3            ADELAIDE LAW REV  ...                   5.0
4        J FINANCIAL DATA SCI  ...                   5.0
<BLANKLINE>
[5 rows x 10 columns]

"""
from .._impact import _impact


def source_impact(
    impact_measure="h_index",
    topics_length=20,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Plots the selected impact measure by source."""

    return _impact(
        criterion="source_abbr",
        impact_measure=impact_measure,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        title="Source Local Impact by " + impact_measure.replace("_", " ").title(),
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

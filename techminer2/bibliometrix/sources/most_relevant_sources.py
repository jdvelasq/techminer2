"""
Most Relevant Sources
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_relevant_sources.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.sources.most_relevant_sources(
...     directory=directory,
...     topics_length=20,
...     plot="cleveland",
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__most_relevant_sources.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
source_abbr
J BANK REGUL                                                  2
J FINANC CRIME                                                2
FOSTER INNOV AND COMPET WITH FINTECH, REGTECH, AND SUPTECH    2
STUD COMPUT INTELL                                            2
ROUTLEDGE HANDB OF FINANCIAL TECHNOLOGY AND LAW               2
Name: OCC, dtype: int64

"""
from ...vantagepoint.report.chart import chart


def most_relevant_sources(
    directory="./",
    topics_length=20,
    topic_min_occ=None,
    topic_min_citations=None,
    plot="cleveland",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Most Relevant Sources."""

    return chart(
        criterion="source_abbr",
        directory=directory,
        database=database,
        metric="OCC",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=None,
        title="Most Relevant Sources",
        plot=plot,
        **filters,
    )

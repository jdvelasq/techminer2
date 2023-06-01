"""
Most Global Cited Sources
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_global_cited_sources.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.sources.most_global_cited_sources(
...     directory=directory,
...     topics_length=20,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__most_global_cited_sources.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
source_abbr
J ECON BUS                       153
NORTHWEST J INTL LAW BUS         150
J BANK REGUL                      35
PALGRAVE STUD DIGIT BUS ENABL     33
DUKE LAW J                        30
Name: global_citations, dtype: int64


>>> print(r.prompt_)
Analyze the table below, which provides bibliographic indicators for a collection of research articles. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| source_abbr                   |   global_citations |
|:------------------------------|-------------------:|
| J ECON BUS                    |                153 |
| NORTHWEST J INTL LAW BUS      |                150 |
| J BANK REGUL                  |                 35 |
| PALGRAVE STUD DIGIT BUS ENABL |                 33 |
| DUKE LAW J                    |                 30 |
| J RISK FINANC                 |                 21 |
| J MONEY LAUND CTRL            |                 14 |
| J FINANC CRIME                |                 13 |
| FIN INNOV                     |                 13 |
| ICEIS - PROC INT CONF ENTERP  |                 12 |
| HELIYON                       |                 11 |
| HANDB OF BLOCKCHAIN, DIGIT FI |                 11 |
| J RISK MANG FIN INST          |                  8 |
| ADV INTELL SYS COMPUT         |                  7 |
| INTELL SYST ACCOUNT FIN MANAG |                  5 |
| J FIN DATA SCI                |                  5 |
| ADELAIDE LAW REV              |                  5 |
| UNIV NEW SOUTH WALES LAW J    |                  4 |
| LECT NOTES DATA ENG COMMUN TE |                  4 |
| J ANTITRUST ENFORC            |                  3 |
<BLANKLINE>
<BLANKLINE>




"""
from ...vantagepoint.analyze import list_view
from ..utils import bbx_generic_indicators_by_item


def most_global_cited_sources(
    plot="cleveland_chart",
    x_label=None,
    y_label=None,
    directory="./",
    topics_length=20,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    custom_topics=None,
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Most global cited sources."""

    return bbx_generic_indicators_by_item(
        fnc_view=list_view,
        field="source_abbr",
        metric="global_citations",
        plot=plot,
        x_label=x_label,
        y_label=y_label,
        title="Most Global Cited Sources",
        root_dir=directory,
        top_n=topics_length,
        occ_range=topic_min_occ,
        topic_max_occ=topic_max_occ,
        gc_range=topic_min_citations,
        topic_max_citations=topic_max_citations,
        custom_items=custom_topics,
        database=database,
        year_filter=start_year,
        cited_by_filter=end_year,
        **filters,
    )

"""
Most Local Cited Sources (from reference lists)
===============================================================================



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_local_cited_sources.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.sources.most_local_cited_sources(
...     topics_length=20,
...     directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__most_local_cited_sources.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
source_abbr
J ECON BUS                       17
PALGRAVE STUD DIGIT BUS ENABL    14
J BANK REGUL                      9
J RISK FINANC                     8
J RISK MANG FIN INST              5
Name: local_citations, dtype: int64

>>> print(r.prompt_)
Analyze the table below, which provides bibliographic indicators for a collection of research articles. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| source_abbr                   |   local_citations |
|:------------------------------|------------------:|
| J ECON BUS                    |                17 |
| PALGRAVE STUD DIGIT BUS ENABL |                14 |
| J BANK REGUL                  |                 9 |
| J RISK FINANC                 |                 8 |
| J RISK MANG FIN INST          |                 5 |
| J FINANC CRIME                |                 4 |
| HELIYON                       |                 4 |
| J MONEY LAUND CTRL            |                 3 |
| ICEIS - PROC INT CONF ENTERP  |                 3 |
| HANDB OF BLOCKCHAIN, DIGIT FI |                 3 |
| INTELL SYST ACCOUNT FIN MANAG |                 3 |
| UNIV NEW SOUTH WALES LAW J    |                 3 |
| J ANTITRUST ENFORC            |                 3 |
| CEUR WKSHP PROC               |                 3 |
| PROC - IEEE WORLD CONGR SERV, |                 2 |
| FRONTIER ARTIF INTELL         |                 2 |
| FIN INNOV                     |                 1 |
| ADV INTELL SYS COMPUT         |                 1 |
| J FIN DATA SCI                |                 1 |
| ADELAIDE LAW REV              |                 1 |
<BLANKLINE>
<BLANKLINE>


"""
from ..bibliometric_indicators_by_topic import bibliometric_indicators_by_topic


def most_local_cited_sources(
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
    """Most local cited sources."""

    return bibliometric_indicators_by_topic(
        criterion="source_abbr",
        metric="local_citations",
        plot=plot,
        x_label=x_label,
        y_label=y_label,
        title="Most Local Cited Sources",
        directory=directory,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        custom_topics=custom_topics,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

"""
Most Global Cited Sources (GPT)
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
J ECON BUS                                  153
NORTHWEST J INTL LAW BUS                    150
J BANK REGUL                                 35
PALGRAVE STUD DIGIT BUS ENABLING TECHNOL     33
DUKE LAW J                                   30
Name: global_citations, dtype: int64


>>> print(r.prompt_)
Analyze the table below, which provides bibliographic indicators for a collection of research articles. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| source_abbr                                                                                   |   global_citations |
|:----------------------------------------------------------------------------------------------|-------------------:|
| J ECON BUS                                                                                    |                153 |
| NORTHWEST J INTL LAW BUS                                                                      |                150 |
| J BANK REGUL                                                                                  |                 35 |
| PALGRAVE STUD DIGIT BUS ENABLING TECHNOL                                                      |                 33 |
| DUKE LAW J                                                                                    |                 30 |
| J RISK FINANC                                                                                 |                 21 |
| J MONEY LAUND CONTROL                                                                         |                 14 |
| J FINANC CRIME                                                                                |                 13 |
| FINANCIAL INNOV                                                                               |                 13 |
| ICEIS - PROC INT CONF ENTERP INF SYST                                                         |                 12 |
| HELIYON                                                                                       |                 11 |
| HANDB OF BLOCKCHAIN, DIGIT FINANC, AND INCL, VOL 1: CRYPTOCURR, FINTECH, INSURTECH, AND REGUL |                 11 |
| J RISK MANG FINANCIAL INST                                                                    |                  8 |
| ADV INTELL SYS COMPUT                                                                         |                  7 |
| INTELL SYST ACCOUNT FINANCE MANAG                                                             |                  5 |
| J FINANCIAL DATA SCI                                                                          |                  5 |
| ADELAIDE LAW REV                                                                              |                  5 |
| UNIV NEW SOUTH WALES LAW J                                                                    |                  4 |
| LECTURE NOTES DATA ENG COMMUN TECH                                                            |                  4 |
| J ANTITRUST ENFORC                                                                            |                  3 |
<BLANKLINE>
<BLANKLINE>



"""
from ... import vantagepoint


def most_global_cited_sources(
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

    obj = vantagepoint.analyze.extract_topics(
        criterion="source_abbr",
        directory=directory,
        database=database,
        metric="global_citations",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        custom_topics=custom_topics,
        **filters,
    )

    chart = vantagepoint.report.cleveland_chart(
        obj,
        title="Most Global Cited Sources",
        x_label="Global Citations",
        y_label="SOURCE ABBR",
    )

    return chart

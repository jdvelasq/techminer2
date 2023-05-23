"""
Most Frequent Sources
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_frequent_sources.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.sources.most_frequent_sources(
...     directory=directory,
...     topics_length=20,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__most_frequent_sources.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
source_abbr
J BANK REGUL                                                  2
J FINANC CRIME                                                2
FOSTER INNOV AND COMPET WITH FINTECH, REGTECH, AND SUPTECH    2
STUD COMPUT INTELL                                            2
ROUTLEDGE HANDB OF FINANCIAL TECHNOLOGY AND LAW               2
Name: OCC, dtype: int64

>>> print(r.prompt_)
Analyze the table below, which provides bibliographic indicators for a collection of research articles. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| source_abbr                                                                                   |   OCC |
|:----------------------------------------------------------------------------------------------|------:|
| J BANK REGUL                                                                                  |     2 |
| J FINANC CRIME                                                                                |     2 |
| FOSTER INNOV AND COMPET WITH FINTECH, REGTECH, AND SUPTECH                                    |     2 |
| STUD COMPUT INTELL                                                                            |     2 |
| ROUTLEDGE HANDB OF FINANCIAL TECHNOLOGY AND LAW                                               |     2 |
| INT CONF INF TECHNOL SYST INNOV, ICITSI - PROC                                                |     2 |
| J ECON BUS                                                                                    |     1 |
| NORTHWEST J INTL LAW BUS                                                                      |     1 |
| PALGRAVE STUD DIGIT BUS ENABLING TECHNOL                                                      |     1 |
| DUKE LAW J                                                                                    |     1 |
| J RISK FINANC                                                                                 |     1 |
| J MONEY LAUND CONTROL                                                                         |     1 |
| FINANCIAL INNOV                                                                               |     1 |
| ICEIS - PROC INT CONF ENTERP INF SYST                                                         |     1 |
| HELIYON                                                                                       |     1 |
| HANDB OF BLOCKCHAIN, DIGIT FINANC, AND INCL, VOL 1: CRYPTOCURR, FINTECH, INSURTECH, AND REGUL |     1 |
| J RISK MANG FINANCIAL INST                                                                    |     1 |
| ADV INTELL SYS COMPUT                                                                         |     1 |
| INTELL SYST ACCOUNT FINANCE MANAG                                                             |     1 |
| J FINANCIAL DATA SCI                                                                          |     1 |
<BLANKLINE>
<BLANKLINE>


"""
from ... import vantagepoint


def most_frequent_sources(
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
    """Most Relevant Sources."""

    obj = vantagepoint.analyze.extract_topics(
        criterion="source_abbr",
        directory=directory,
        database=database,
        metric="OCC",
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
        title="Most Frequent Sources",
        x_label="OCC",
        y_label="SOURCES",
    )

    return chart

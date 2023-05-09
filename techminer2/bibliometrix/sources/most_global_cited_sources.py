"""
Most Global Cited Sources
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_global_cited_sources.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.sources.most_global_cited_sources(
...     directory=directory,
...     topics_length=20,
...     plot="cleveland",
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
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top 20 cited document sources with highest number of total citations in the dataset ('global_citations' column). Use the information in the table to draw conclusions about the impact and relevance of the reseach published by the source in the dataset. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
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
<BLANKLINE>

"""
from ...vantagepoint.report.chart import chart


def most_global_cited_sources(
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
    """Most global cited sources."""

    obj = chart(
        criterion="source_abbr",
        directory=directory,
        database=database,
        metric="global_citations",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=None,
        title="Most Global Cited Sources",
        plot=plot,
        **filters,
    )

    obj.prompt_ = _create_prompt(obj.table_)

    return obj


def _create_prompt(table):
    return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on top {table.shape[0]} cited document sources with highest \
number of total citations in the dataset ('global_citations' column). Use the \
information in the table to draw conclusions about the impact and relevance of \
the reseach published by the source in the dataset. In your analysis, be sure \
to describe in a clear and concise way, any findings or any patterns you \
observe, and identify any outliers or anomalies in the data. \
Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}


"""

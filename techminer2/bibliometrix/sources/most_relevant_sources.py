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

>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top 20 document sources with highest number of documents ('OCC' indicates 'occurrences'). Use the the information in the table to draw conclusions about the document production by source. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
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
<BLANKLINE>

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

    obj = chart(
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

    obj.prompt_ = _create_prompt("Source", obj.table_)

    return obj


def _create_prompt(criterion, table):
    return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on top {table.shape[0]} document sources with highest \
number of documents ('OCC' indicates 'occurrences'). Use the the information \
in the table to draw conclusions about the document production by source. In \
your analysis, be sure to describe in a clear and concise way, any findings or \
any patterns you observe, and identify any outliers or anomalies in the data. \
Limit your description to one \
paragraph with no more than 250 words.

{table.to_markdown()}


"""

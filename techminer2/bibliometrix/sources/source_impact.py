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


>>> print(r.table_.head().to_markdown())
| source_abbr                   |   OCC |   Global Citations |   First Pb Year |   Age |   H-Index |   G-Index |   M-Index |   Global Citations Per Year |   Avg Global Citations |
|:------------------------------|------:|-------------------:|----------------:|------:|----------:|----------:|----------:|----------------------------:|-----------------------:|
| J BANK REGUL                  |     2 |                 35 |            2020 |     4 |         2 |         2 |      0.5  |                        8.75 |                   17.5 |
| J FINANC CRIME                |     2 |                 13 |            2020 |     4 |         2 |         1 |      0.5  |                        3.25 |                    6.5 |
| J ECON BUS                    |     1 |                153 |            2018 |     6 |         1 |         1 |      0.17 |                       25.5  |                  153   |
| NORTHWEST J INTL LAW BUS      |     1 |                150 |            2017 |     7 |         1 |         1 |      0.14 |                       21.43 |                  150   |
| PALGRAVE STUD DIGIT BUS ENABL |     1 |                 33 |            2019 |     5 |         1 |         1 |      0.2  |                        6.6  |                   33   |


>>> print(r.prompt_)
The table below provides data on top 20 sources with the highest H-Index. 'OCC' represents the number of documents published by the source in the dataset. Use the information in the table to draw conclusions about the impact and productivity of the document source. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
| source_abbr                   |   OCC |   Global Citations |   First Pb Year |   Age |   H-Index |   G-Index |   M-Index |   Global Citations Per Year |   Avg Global Citations |
|:------------------------------|------:|-------------------:|----------------:|------:|----------:|----------:|----------:|----------------------------:|-----------------------:|
| J BANK REGUL                  |     2 |                 35 |            2020 |     4 |         2 |         2 |      0.5  |                        8.75 |                   17.5 |
| J FINANC CRIME                |     2 |                 13 |            2020 |     4 |         2 |         1 |      0.5  |                        3.25 |                    6.5 |
| J ECON BUS                    |     1 |                153 |            2018 |     6 |         1 |         1 |      0.17 |                       25.5  |                  153   |
| NORTHWEST J INTL LAW BUS      |     1 |                150 |            2017 |     7 |         1 |         1 |      0.14 |                       21.43 |                  150   |
| PALGRAVE STUD DIGIT BUS ENABL |     1 |                 33 |            2019 |     5 |         1 |         1 |      0.2  |                        6.6  |                   33   |
| DUKE LAW J                    |     1 |                 30 |            2016 |     8 |         1 |         1 |      0.12 |                        3.75 |                   30   |
| J RISK FINANC                 |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                   21   |
| J MONEY LAUND CTRL            |     1 |                 14 |            2020 |     4 |         1 |         1 |      0.25 |                        3.5  |                   14   |
| FIN INNOV                     |     1 |                 13 |            2022 |     2 |         1 |         1 |      0.5  |                        6.5  |                   13   |
| ICEIS - PROC INT CONF ENTERP  |     1 |                 12 |            2020 |     4 |         1 |         1 |      0.25 |                        3    |                   12   |
| HANDB OF BLOCKCHAIN, DIGIT FI |     1 |                 11 |            2017 |     7 |         1 |         1 |      0.14 |                        1.57 |                   11   |
| HELIYON                       |     1 |                 11 |            2020 |     4 |         1 |         1 |      0.25 |                        2.75 |                   11   |
| J RISK MANG FIN INST          |     1 |                  8 |            2018 |     6 |         1 |         1 |      0.17 |                        1.33 |                    8   |
| ADV INTELL SYS COMPUT         |     1 |                  7 |            2021 |     3 |         1 |         1 |      0.33 |                        2.33 |                    7   |
| ADELAIDE LAW REV              |     1 |                  5 |            2020 |     4 |         1 |         1 |      0.25 |                        1.25 |                    5   |
| INTELL SYST ACCOUNT FIN MANAG |     1 |                  5 |            2020 |     4 |         1 |         1 |      0.25 |                        1.25 |                    5   |
| J FIN DATA SCI                |     1 |                  5 |            2019 |     5 |         1 |         1 |      0.2  |                        1    |                    5   |
| LECT NOTES DATA ENG COMMUN TE |     1 |                  4 |            2020 |     4 |         1 |         1 |      0.25 |                        1    |                    4   |
| UNIV NEW SOUTH WALES LAW J    |     1 |                  4 |            2020 |     4 |         1 |         1 |      0.25 |                        1    |                    4   |
| EUR J RISK REGUL              |     1 |                  3 |            2022 |     2 |         1 |         1 |      0.5  |                        1.5  |                    3   |
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>


"""
from ..criterion_impact import criterion_impact


def source_impact(
    impact_measure="h_index",
    topics_length=20,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    custom_topics=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Plots the selected impact measure by source."""

    obj = criterion_impact(
        criterion="source_abbr",
        metric=impact_measure,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        custom_topics=custom_topics,
        directory=directory,
        title="Source Local Impact by "
        + impact_measure.replace("_", " ").title(),
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    obj.prompt_ = _create_prompt(obj.table_, impact_measure)

    return obj


def _create_prompt(table, impact_measure):
    return f"""\
The table \
below provides data on top {table.shape[0]} sources with the highest \
{impact_measure.replace("_", "-").title()}. 'OCC' represents the number of \
documents published by the source in the dataset. Use the information in the \
table to draw conclusions about the impact and productivity of the document \
source. In your analysis, be sure to describe in a clear and concise way, any \
findings or any patterns you observe, and identify any outliers or anomalies in \
the data. Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}


"""

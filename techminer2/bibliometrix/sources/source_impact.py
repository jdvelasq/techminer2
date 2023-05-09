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

>>> print(r.prompt_)
<BLANKLINE>
Act as a researcher realizing a bibliometric analysis. 
<BLANKLINE>
The following table contains the top 20 Source Abbr 
with more H Index in the given bibliographic dataset.
<BLANKLINE>
| Source Abbr                              |   Occ |   Global Citations |   First Pb Year |   Age |   H Index |   G Index |   M Index |   Global Citations Per Year |   Avg Global Citations |
|:-----------------------------------------|------:|-------------------:|----------------:|------:|----------:|----------:|----------:|----------------------------:|-----------------------:|
| J BANK REGUL                             |     2 |                 35 |            2020 |     4 |         2 |         2 |      0.5  |                        8.75 |                   17.5 |
| J FINANC CRIME                           |     2 |                 13 |            2020 |     4 |         2 |         1 |      0.5  |                        3.25 |                    6.5 |
| LECT NOTES BUS INF PROCESS               |     1 |                  2 |            2021 |     3 |         1 |         1 |      0.33 |                        0.67 |                    2   |
| ADELAIDE LAW REV                         |     1 |                  5 |            2020 |     4 |         1 |         1 |      0.25 |                        1.25 |                    5   |
| J FINANCIAL DATA SCI                     |     1 |                  5 |            2019 |     5 |         1 |         1 |      0.2  |                        1    |                    5   |
| J IND BUS ECON                           |     1 |                  1 |            2022 |     2 |         1 |         1 |      0.5  |                        0.5  |                    1   |
| J MONEY LAUND CONTROL                    |     1 |                 14 |            2020 |     4 |         1 |         1 |      0.25 |                        3.5  |                   14   |
| J RISK FINANC                            |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                   21   |
| J RISK MANG FINANCIAL INST               |     1 |                  8 |            2018 |     6 |         1 |         1 |      0.17 |                        1.33 |                    8   |
| ACM INT CONF PROC SER                    |     1 |                  2 |            2021 |     3 |         1 |         1 |      0.33 |                        0.67 |                    2   |
| J ANTITRUST ENFORC                       |     1 |                  3 |            2021 |     3 |         1 |         1 |      0.33 |                        1    |                    3   |
| LECTURE NOTES DATA ENG COMMUN TECH       |     1 |                  4 |            2020 |     4 |         1 |         1 |      0.25 |                        1    |                    4   |
| NORTHWEST J INTL LAW BUS                 |     1 |                150 |            2017 |     7 |         1 |         1 |      0.14 |                       21.43 |                  150   |
| PALGRAVE STUD DIGIT BUS ENABLING TECHNOL |     1 |                 33 |            2019 |     5 |         1 |         1 |      0.2  |                        6.6  |                   33   |
| PROC - IEEE WORLD CONGR SERV, SERVICES   |     1 |                  3 |            2019 |     5 |         1 |         1 |      0.2  |                        0.6  |                    3   |
| PROC EUR CONF INNOV ENTREPREN, ECIE      |     1 |                  1 |            2020 |     4 |         1 |         1 |      0.25 |                        0.25 |                    1   |
| PROC INT CONF ELECTRON BUS (ICEB)        |     1 |                  1 |            2017 |     7 |         1 |         1 |      0.14 |                        0.14 |                    1   |
| STUD COMPUT INTELL                       |     2 |                  1 |            2021 |     3 |         1 |         1 |      0.33 |                        0.33 |                    0.5 |
| LECT NOTES NETWORKS SYST                 |     1 |                  1 |            2022 |     2 |         1 |         1 |      0.5  |                        0.5  |                    1   |
| J ECON BUS                               |     1 |                153 |            2018 |     6 |         1 |         1 |      0.17 |                       25.5  |                  153   |
<BLANKLINE>
Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice in the previous table. 
<BLANKLINE>
Limit your description to a paragraph with no more than 250 words.    
<BLANKLINE>
<BLANKLINE>


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

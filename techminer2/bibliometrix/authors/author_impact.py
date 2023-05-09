"""
Author Impact
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__author_impact.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.authors.author_impact(
...     impact_measure='h_index',
...     topics_length=20,
...     directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__author_impact.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()
      Authors  Occ  ...  Global Citations Per Year  Avg Global Citations
0    Arner DW    3  ...                      26.43                 61.67
1  Buckley RP    3  ...                      26.43                 61.67
2      Ryan P    2  ...                       3.50                  7.00
3     Singh C    2  ...                       4.25                  8.50
4     Crane M    2  ...                       3.50                  7.00
<BLANKLINE>
[5 rows x 10 columns]


>>> print(r.prompt_)
<BLANKLINE>
Act as a researcher realizing a bibliometric analysis. 
<BLANKLINE>
The following table contains the top 20 Authors 
with more H Index in the given bibliographic dataset.
<BLANKLINE>
| Authors         |   Occ |   Global Citations |   First Pb Year |   Age |   H Index |   G Index |   M Index |   Global Citations Per Year |   Avg Global Citations |
|:----------------|------:|-------------------:|----------------:|------:|----------:|----------:|----------:|----------------------------:|-----------------------:|
| Arner DW        |     3 |                185 |            2017 |     7 |         3 |         3 |      0.43 |                       26.43 |                  61.67 |
| Buckley RP      |     3 |                185 |            2017 |     7 |         3 |         3 |      0.43 |                       26.43 |                  61.67 |
| Ryan P          |     2 |                 14 |            2020 |     4 |         2 |         1 |      0.5  |                        3.5  |                   7    |
| Singh C         |     2 |                 17 |            2020 |     4 |         2 |         1 |      0.5  |                        4.25 |                   8.5  |
| Crane M         |     2 |                 14 |            2020 |     4 |         2 |         1 |      0.5  |                        3.5  |                   7    |
| Lin W           |     2 |                 17 |            2020 |     4 |         2 |         1 |      0.5  |                        4.25 |                   8.5  |
| Barberis JN     |     2 |                161 |            2017 |     7 |         2 |         2 |      0.29 |                       23    |                  80.5  |
| Hamdan A        |     2 |                 18 |            2020 |     4 |         2 |         2 |      0.5  |                        4.5  |                   9    |
| Turki M         |     2 |                 18 |            2020 |     4 |         2 |         2 |      0.5  |                        4.5  |                   9    |
| Butler T/1      |     2 |                 41 |            2018 |     6 |         2 |         2 |      0.33 |                        6.83 |                  20.5  |
| Brennan R       |     2 |                 14 |            2020 |     4 |         2 |         1 |      0.5  |                        3.5  |                   7    |
| Rabbani MR      |     1 |                  1 |            2022 |     2 |         1 |         1 |      0.5  |                        0.5  |                   1    |
| Potapenko L     |     1 |                  4 |            2020 |     4 |         1 |         1 |      0.25 |                        1    |                   4    |
| Pantielieieva N |     1 |                  4 |            2020 |     4 |         1 |         1 |      0.25 |                        1    |                   4    |
| OBrien L        |     1 |                 33 |            2019 |     5 |         1 |         1 |      0.2  |                        6.6  |                  33    |
| Nicholls R      |     1 |                  3 |            2021 |     3 |         1 |         1 |      0.33 |                        1    |                   3    |
| Abdullah Y      |     1 |                  1 |            2022 |     2 |         1 |         1 |      0.5  |                        0.5  |                   1    |
| Nasir F         |     1 |                  3 |            2019 |     5 |         1 |         1 |      0.2  |                        0.6  |                   3    |
| Narang S        |     1 |                  1 |            2020 |     4 |         1 |         1 |      0.25 |                        0.25 |                   1    |
| Razzaque A      |     1 |                  7 |            2021 |     3 |         1 |         1 |      0.33 |                        2.33 |                   7    |
<BLANKLINE>
Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice in the previous table. 
<BLANKLINE>
Limit your description to a paragraph with no more than 250 words.    
<BLANKLINE>
<BLANKLINE>


"""
from .._impact import _impact


def author_impact(
    impact_measure="h_index",
    topics_length=20,
    topic_min_occ=0,
    topic_min_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Plots the selected impact measure by author."""

    return _impact(
        criterion="authors",
        impact_measure=impact_measure,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        title="Author Local Impact by " + impact_measure.replace("_", " ").title(),
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

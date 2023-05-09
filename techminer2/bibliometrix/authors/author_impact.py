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


>>> print(r.table_.head().to_markdown())
|    | Authors     |   OCC |   Global Citations |   First Pb Year |   Age |   H-Index |   G-Index |   M-Index |   Global Citations Per Year |   Avg Global Citations |
|---:|:------------|------:|-------------------:|----------------:|------:|----------:|----------:|----------:|----------------------------:|-----------------------:|
|  0 | Arner DW    |     3 |                185 |            2017 |     7 |         3 |         3 |      0.43 |                       26.43 |                  61.67 |
|  1 | Buckley RP  |     3 |                185 |            2017 |     7 |         3 |         3 |      0.43 |                       26.43 |                  61.67 |
|  2 | Barberis JN |     2 |                161 |            2017 |     7 |         2 |         2 |      0.29 |                       23    |                  80.5  |
|  3 | Butler T/1  |     2 |                 41 |            2018 |     6 |         2 |         2 |      0.33 |                        6.83 |                  20.5  |
|  4 | Hamdan A    |     2 |                 18 |            2020 |     4 |         2 |         2 |      0.5  |                        4.5  |                   9    |

>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top 20 authors with the highest H-Index. 'OCC' represents the number of documents published by the author in the dataset. Use the information in the table to draw conclusions about the impact and productivity of the author. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
|    | Authors           |   OCC |   Global Citations |   First Pb Year |   Age |   H-Index |   G-Index |   M-Index |   Global Citations Per Year |   Avg Global Citations |
|---:|:------------------|------:|-------------------:|----------------:|------:|----------:|----------:|----------:|----------------------------:|-----------------------:|
|  0 | Arner DW          |     3 |                185 |            2017 |     7 |         3 |         3 |      0.43 |                       26.43 |                  61.67 |
|  1 | Buckley RP        |     3 |                185 |            2017 |     7 |         3 |         3 |      0.43 |                       26.43 |                  61.67 |
|  2 | Barberis JN       |     2 |                161 |            2017 |     7 |         2 |         2 |      0.29 |                       23    |                  80.5  |
|  3 | Butler T/1        |     2 |                 41 |            2018 |     6 |         2 |         2 |      0.33 |                        6.83 |                  20.5  |
|  4 | Hamdan A          |     2 |                 18 |            2020 |     4 |         2 |         2 |      0.5  |                        4.5  |                   9    |
|  5 | Turki M           |     2 |                 18 |            2020 |     4 |         2 |         2 |      0.5  |                        4.5  |                   9    |
|  6 | Lin W             |     2 |                 17 |            2020 |     4 |         2 |         1 |      0.5  |                        4.25 |                   8.5  |
|  7 | Singh C           |     2 |                 17 |            2020 |     4 |         2 |         1 |      0.5  |                        4.25 |                   8.5  |
|  8 | Brennan R         |     2 |                 14 |            2020 |     4 |         2 |         1 |      0.5  |                        3.5  |                   7    |
|  9 | Crane M           |     2 |                 14 |            2020 |     4 |         2 |         1 |      0.5  |                        3.5  |                   7    |
| 10 | Ryan P            |     2 |                 14 |            2020 |     4 |         2 |         1 |      0.5  |                        3.5  |                   7    |
| 11 | Anagnostopoulos I |     1 |                153 |            2018 |     6 |         1 |         1 |      0.17 |                       25.5  |                 153    |
| 12 | OBrien L          |     1 |                 33 |            2019 |     5 |         1 |         1 |      0.2  |                        6.6  |                  33    |
| 13 | Baxter LG         |     1 |                 30 |            2016 |     8 |         1 |         1 |      0.12 |                        3.75 |                  30    |
| 14 | Weber RH          |     1 |                 24 |            2020 |     4 |         1 |         1 |      0.25 |                        6    |                  24    |
| 15 | Zetzsche DA       |     1 |                 24 |            2020 |     4 |         1 |         1 |      0.25 |                        6    |                  24    |
| 16 | Breymann W        |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
| 17 | Gross FJ          |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
| 18 | Kavassalis P      |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
| 19 | Saxton K          |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
<BLANKLINE>
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

    obj = _impact(
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

    obj.prompt_ = _create_prompt(obj.table_, impact_measure)

    return obj


def _create_prompt(table, impact_measure):
    return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on top {table.shape[0]} authors with the highest \
{impact_measure.replace("_", "-").title()}. 'OCC' represents the number of \
documents published by the author in the dataset. Use the information in the \
table to draw conclusions about the impact and productivity of the author. \
In your analysis, be sure to describe in a clear and concise way, any \
findings or any patterns you observe, and identify any outliers or anomalies in \
the data. Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}


"""

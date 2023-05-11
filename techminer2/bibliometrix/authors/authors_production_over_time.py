"""
Authors' Production over Time
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__authors_production_over_time.html"


>>> from techminer2 import bibliometrix
>>> r = bibliometrix.authors.authors_production_over_time(
...    topics_length=10,
...    directory=directory,
... )

>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__authors_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>



>>> print(r.documents_per_author_.head().to_markdown())
|    | authors     | title                                                                                        |   year | source_title                                   |   global_citations |   local_citations | doi                           |
|---:|:------------|:---------------------------------------------------------------------------------------------|-------:|:-----------------------------------------------|-------------------:|------------------:|:------------------------------|
|  0 | Teichmann F | RegTech  Potential benefits and challenges for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  1 | Boticiu SR  | RegTech  Potential benefits and challenges for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  2 | Sergi BS    | RegTech  Potential benefits and challenges for businesses                                    |   2023 | Technology in Society                          |                  0 |                 0 | 10.1016/J.TECHSOC.2022.102150 |
|  3 | Lan G       | Costs of voting and firm performance: Evidence from RegTech adoption in Chinese listed firms |   2023 | Research in International Business and Finance |                  0 |                 0 | 10.1016/J.RIBAF.2022.101868   |
|  4 | Li D/1      | Costs of voting and firm performance: Evidence from RegTech adoption in Chinese listed firms |   2023 | Research in International Business and Finance |                  0 |                 0 | 10.1016/J.RIBAF.2022.101868   |


>>> print(r.production_per_year_.head().to_markdown())
|                             |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|:----------------------------|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
| ('Abdullah Y', 2022)        |     1 |         1 |                  1 |                 0 |     2 |                       0.5   |                      0     |
| ('Ajmi JA', 2021)           |     1 |         1 |                  7 |                 1 |     3 |                       2.333 |                      0.333 |
| ('Anagnostopoulos I', 2018) |     1 |         1 |                153 |                17 |     6 |                      25.5   |                      2.833 |
| ('Anasweh M', 2020)         |     1 |         1 |                 11 |                 4 |     4 |                       2.75  |                      1     |
| ('Arman AA', 2022)          |     2 |         2 |                  0 |                 0 |     2 |                       0     |                      0     |



>>> print(r.table_.to_markdown())
|    | Authors          |   Year |   OCC |   cum_OCC |   Global Citations |   Local Citations |   Age |   Global Citations Per Year |   Local Citations Per Year |
|---:|:-----------------|-------:|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
|  0 | Arner DW 3:185   |   2017 |     2 |         2 |                161 |                 3 |     7 |                      23     |                      0.429 |
|  1 | Buckley RP 3:185 |   2017 |     2 |         2 |                161 |                 3 |     7 |                      23     |                      0.429 |
|  2 | Arner DW 3:185   |   2020 |     1 |         3 |                 24 |                 5 |     4 |                       6     |                      1.25  |
|  3 | Buckley RP 3:185 |   2020 |     1 |         3 |                 24 |                 5 |     4 |                       6     |                      1.25  |
|  4 | Butler T/1 2:041 |   2019 |     1 |         2 |                 33 |                14 |     5 |                       6.6   |                      2.8   |
|  5 | Lin W 2:017      |   2020 |     1 |         1 |                 14 |                 3 |     4 |                       3.5   |                      0.75  |
|  6 | Singh C 2:017    |   2020 |     1 |         1 |                 14 |                 3 |     4 |                       3.5   |                      0.75  |
|  7 | Brennan R 2:014  |   2020 |     1 |         1 |                 12 |                 3 |     4 |                       3     |                      0.75  |
|  8 | Crane M 2:014    |   2020 |     1 |         1 |                 12 |                 3 |     4 |                       3     |                      0.75  |
|  9 | Hamdan A 2:018   |   2020 |     1 |         1 |                 11 |                 4 |     4 |                       2.75  |                      1     |
| 10 | Sarea A 2:012    |   2020 |     1 |         1 |                 11 |                 4 |     4 |                       2.75  |                      1     |
| 11 | Butler T/1 2:041 |   2018 |     1 |         1 |                  8 |                 5 |     6 |                       1.333 |                      0.833 |
| 12 | Hamdan A 2:018   |   2021 |     1 |         2 |                  7 |                 1 |     3 |                       2.333 |                      0.333 |
| 13 | Lin W 2:017      |   2022 |     1 |         2 |                  3 |                 1 |     2 |                       1.5   |                      0.5   |
| 14 | Singh C 2:017    |   2022 |     1 |         2 |                  3 |                 1 |     2 |                       1.5   |                      0.5   |
| 15 | Brennan R 2:014  |   2021 |     1 |         2 |                  2 |                 0 |     3 |                       0.667 |                      0     |
| 16 | Crane M 2:014    |   2021 |     1 |         2 |                  2 |                 0 |     3 |                       0.667 |                      0     |
| 17 | Grassi L 2:002   |   2020 |     1 |         1 |                  1 |                 0 |     4 |                       0.25  |                      0     |
| 18 | Grassi L 2:002   |   2022 |     1 |         2 |                  1 |                 0 |     2 |                       0.5   |                      0     |
| 19 | Sarea A 2:012    |   2022 |     1 |         2 |                  1 |                 0 |     2 |                       0.5   |                      0     |


>>> print(r.production_.head().to_markdown())
| Authors          |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |
|:-----------------|-------:|-------:|-------:|-------:|-------:|-------:|
| Arner DW 3:185   |      2 |      0 |      0 |      1 |      0 |      0 |
| Brennan R 2:014  |      0 |      0 |      0 |      1 |      1 |      0 |
| Buckley RP 3:185 |      2 |      0 |      0 |      1 |      0 |      0 |
| Butler T/1 2:041 |      0 |      1 |      1 |      0 |      0 |      0 |
| Crane M 2:014    |      0 |      0 |      0 |      1 |      1 |      0 |



>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on document production by year per author for the top 10 most productive authors in the dataset. Use the information in the table to draw conclusions about the productivity per year of the authors. The final part of the author name contains two numbers separated by a colon. The first is the total number of documents of the author, and the second is the total number of citations of the author. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
| Authors          |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |
|:-----------------|-------:|-------:|-------:|-------:|-------:|-------:|
| Arner DW 3:185   |      2 |      0 |      0 |      1 |      0 |      0 |
| Brennan R 2:014  |      0 |      0 |      0 |      1 |      1 |      0 |
| Buckley RP 3:185 |      2 |      0 |      0 |      1 |      0 |      0 |
| Butler T/1 2:041 |      0 |      1 |      1 |      0 |      0 |      0 |
| Crane M 2:014    |      0 |      0 |      0 |      1 |      1 |      0 |
| Grassi L 2:002   |      0 |      0 |      0 |      1 |      0 |      1 |
| Hamdan A 2:018   |      0 |      0 |      0 |      1 |      1 |      0 |
| Lin W 2:017      |      0 |      0 |      0 |      1 |      0 |      1 |
| Sarea A 2:012    |      0 |      0 |      0 |      1 |      0 |      1 |
| Singh C 2:017    |      0 |      0 |      0 |      1 |      0 |      1 |
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>

"""
from ...techminer.indicators.indicators_by_topic_per_year import (
    indicators_by_topic_per_year,
)
from .._documents_per import _documents_per
from .._production_over_time import _production_over_time


def authors_production_over_time(
    topics_length=10,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Authors production over time."""

    results = _production_over_time(
        criterion="authors",
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        title="Authors' production over time",
        metric="OCC",
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    results.documents_per_author_ = _documents_per(
        criterion="authors",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    results.production_per_year_ = indicators_by_topic_per_year(
        criterion="authors",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    table = results.table_.copy()
    table = table[["Authors", "Year", "OCC"]]
    table = table.pivot(index="Authors", columns="Year", values="OCC")
    table = table.fillna(0)
    results.production_ = table
    results.prompt_ = _create_prompt(table)

    return results


def _create_prompt(table):
    return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on document production by year per author for the top {table.shape[0]} \
most productive authors in the dataset. Use the information in the table to \
draw conclusions about the productivity per year of the authors. The final \
part of the author name contains two numbers separated by a colon. The first \
is the total number of documents of the author, and the second is the total \
number of citations of the author. \
In your analysis, be sure to describe in a clear and concise way, any findings \
or any patterns you observe, and identify any outliers or anomalies in the \
data. Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}


"""

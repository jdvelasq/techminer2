# flake8: noqa
"""
Average Citations per Year
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/examples/average_citations_per_year.html"

>>> import techminer2plus
>>> r = techminer2plus.examples.overview.average_citations_per_year(root_dir)
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/examples/average_citations_per_year.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> print(r.table_.head().to_markdown())
|   year |   OCC |   cum_OCC |   local_citations |   global_citations |   citable_years |   mean_global_citations |   cum_global_citations |   mean_global_citations_per_year |   mean_local_citations |   cum_local_citations |   mean_local_citations_per_year |
|-------:|------:|----------:|------------------:|-------------------:|----------------:|------------------------:|-----------------------:|---------------------------------:|-----------------------:|----------------------:|--------------------------------:|
|   2016 |     1 |         1 |                 0 |                 30 |               8 |                30       |                     30 |                             3.75 |                0       |                     0 |                            0    |
|   2017 |     4 |         5 |                 3 |                162 |               7 |                40.5     |                    192 |                             5.79 |                0.75    |                     3 |                            0.11 |
|   2018 |     3 |         8 |                30 |                182 |               6 |                60.6667  |                    374 |                            10.11 |               10       |                    33 |                            1.67 |
|   2019 |     6 |        14 |                19 |                 47 |               5 |                 7.83333 |                    421 |                             1.57 |                3.16667 |                    52 |                            0.63 |
|   2020 |    14 |        28 |                29 |                 93 |               4 |                 6.64286 |                    514 |                             1.66 |                2.07143 |                    81 |                            0.52 |


>>> print(r.prompt_)
The table below provides data on the average citations per year of the \\
dataset. Use the the information in the table to draw conclusions about the \\
impact per year. In your analysis, be sure to describe in a clear and \\
concise way, any trends or patterns you observe, and identify any outliers \\
or anomalies in the data. Limit your description to one paragraph with no \\
more than 250 words.
<BLANKLINE>
Table:
```
|   year |   mean_global_citations |   global_citations |
|-------:|------------------------:|-------------------:|
|   2016 |                30       |                 30 |
|   2017 |                40.5     |                162 |
|   2018 |                60.6667  |                182 |
|   2019 |                 7.83333 |                 47 |
|   2020 |                 6.64286 |                 93 |
|   2021 |                 2.7     |                 27 |
|   2022 |                 1.83333 |                 22 |
|   2023 |                 0       |                  0 |
```
<BLANKLINE>



# pylint: disable=line-too-long
"""
from ...classes import IndicatorByYearChart
from ...prompts import format_prompt_for_tables
from ...query import indicators_by_year, indicators_by_year_plot


def average_citations_per_year(
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Average citations per year.

    Args:
        root_dir (str, optional): root directory. Defaults to "./".
        database (str, optional): database name. Defaults to "documents".
        year_filter (tuple, optional): Year filter. Defaults to None.
        cited_by_filter (tuple, optional): Cited by filter. Defaults to None.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.


    Returns:
        IndicatorByYearChart: A chart containing the average citations per year.

    """

    def generate_chatgpt_prompt(table):
        """Generates prompt for analysis of the average citations per year."""

        main_text = (
            "The table below provides data on the average citations per year "
            "of the dataset. Use the the information in the table to draw "
            "conclusions about the impact per year. In your analysis, be "
            "sure to describe in a clear and concise way, any trends or "
            "patterns you observe, and identify any outliers or anomalies "
            "in the data. Limit your description to one paragraph with no "
            "more than 250 words."
        )
        table_text = table.to_markdown()
        return format_prompt_for_tables(main_text, table_text)

    #
    # Main code
    #

    indicators = indicators_by_year(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    results = IndicatorByYearChart()
    results.table_ = indicators
    results.plot_ = indicators_by_year_plot(
        indicators,
        metric="mean_global_citations",
        title="Average Citations per Year",
    )
    results.prompt_ = generate_chatgpt_prompt(
        indicators[["mean_global_citations", "global_citations"]]
    )

    return results

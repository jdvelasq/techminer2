# flake8: noqa
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=missing-docstring
# pylint: disable=invalid-name
"""
.. _average_citations_per_year_prompt:

Average Citations per Year Prompt
===============================================================================

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"
>>> prompt = tm2p.average_citations_per_year_prompt(
...     root_dir=root_dir,
... )
>>> print(prompt)
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


"""
from .format_prompt_for_dataframes import format_prompt_for_dataframes
from .global_indicators_by_year_table import global_indicators_by_year_table


def average_citations_per_year_prompt(
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Makes a time line plot for indicators."""

    df = global_indicators_by_year_table(
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    main_text = (
        "The table below provides data on the average citations per year "
        "of the dataset. Use the the information in the table to draw "
        "conclusions about the impact per year. In your analysis, be "
        "sure to describe in a clear and concise way, any trends or "
        "patterns you observe, and identify any outliers or anomalies "
        "in the data. Limit your description to one paragraph with no "
        "more than 250 words."
    )

    table_text = df[
        ["mean_global_citations", "global_citations"]
    ].to_markdown()

    return format_prompt_for_dataframes(main_text, table_text)

# flake8: noqa
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=missing-docstring
# pylint: disable=invalid-name
"""
.. _records_by_year_prompt:

Records by Year Prompt
===============================================================================

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"
>>> prompt = tm2p.records_by_year_prompt(
...     root_dir=root_dir,
... )
>>> print(prompt)
The table below, delimited by triple backticks, provides data on the annual \\
scientific production in a bibliographic database. Use the table to draw \\
conclusions about annual research productivity and the cumulative \\
productivity. The column 'OCC' is the number of documents published in a \\
given year. The column 'cum_OCC' is the cumulative number of documents \\
published up to a given year. The information in the table is used to \\
create a line plot of number of publications per year. In your analysis, be \\
sure to describe in a clear and concise way, any trends or patterns you \\
observe, and identify any outliers or anomalies in the data. Limit your \\
description to one paragraph with no more than 250 words.
<BLANKLINE>
Table:
```
|   year |   OCC |   cum_OCC |
|-------:|------:|----------:|
|   2016 |     1 |         1 |
|   2017 |     4 |         5 |
|   2018 |     3 |         8 |
|   2019 |     6 |        14 |
|   2020 |    14 |        28 |
|   2021 |    10 |        38 |
|   2022 |    12 |        50 |
|   2023 |     2 |        52 |
```
<BLANKLINE>




"""
from .format_prompt_for_dataframes import format_prompt_for_dataframes
from .global_indicators_by_year import global_indicators_by_year


def records_by_year_prompt(
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Makes a time line plot for indicators."""

    df = global_indicators_by_year(
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    main_text = (
        "The table below, delimited by triple backticks, provides data on "
        "the annual scientific production in a bibliographic database. Use "
        "the table to draw conclusions about annual research productivity "
        "and the cumulative productivity. The column 'OCC' is the number of "
        "documents published in a given year. The column 'cum_OCC' is "
        "the cumulative number of documents published up to a given year. "
        "The information in the table is used to create a line plot of "
        "number of publications per year. In your analysis, be sure to "
        "describe in a clear and concise way, any trends or patterns you "
        "observe, and identify any outliers or anomalies in the data. Limit "
        "your description to one paragraph with no more than 250 words."
    )

    table_text = df[["OCC", "cum_OCC"]].to_markdown()

    return format_prompt_for_dataframes(main_text, table_text)

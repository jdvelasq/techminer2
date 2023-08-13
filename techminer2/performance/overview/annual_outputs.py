# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _tm2.performance.overview.annual_outputs:

Annual Outputs
===============================================================================


>>> from techminer2.performance.overview import annual_outputs
>>> metrics = annual_outputs(
...     #
...     # TABLE PARAMS:
...     selected_columns=[
...         "OCC",
...         "global_citations",
...         "mean_global_citations",
...         "mean_global_citations_per_year",
...     ],
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )


>>> print(metrics.df_.to_markdown())
|   year |   OCC |   global_citations |   mean_global_citations |   mean_global_citations_per_year |
|-------:|------:|-------------------:|------------------------:|---------------------------------:|
|   2016 |     1 |                 30 |                30       |                             3.75 |
|   2017 |     4 |                162 |                40.5     |                             5.79 |
|   2018 |     3 |                182 |                60.6667  |                            10.11 |
|   2019 |     6 |                 47 |                 7.83333 |                             1.57 |
|   2020 |    14 |                 93 |                 6.64286 |                             1.66 |
|   2021 |    10 |                 27 |                 2.7     |                             0.9  |
|   2022 |    12 |                 22 |                 1.83333 |                             0.92 |
|   2023 |     2 |                  0 |                 0       |                             0    |



>>> print(metrics.df_.T.to_markdown())
|                                |   2016 |   2017 |     2018 |     2019 |     2020 |   2021 |     2022 |   2023 |
|:-------------------------------|-------:|-------:|---------:|---------:|---------:|-------:|---------:|-------:|
| OCC                            |   1    |   4    |   3      |  6       | 14       |   10   | 12       |      2 |
| global_citations               |  30    | 162    | 182      | 47       | 93       |   27   | 22       |      0 |
| mean_global_citations          |  30    |  40.5  |  60.6667 |  7.83333 |  6.64286 |    2.7 |  1.83333 |      0 |
| mean_global_citations_per_year |   3.75 |   5.79 |  10.11   |  1.57    |  1.66    |    0.9 |  0.92    |      0 |



>>> print(metrics.prompt_)
Your task is to generate a short summary for a research paper about the \\
annual performance metrics of a bibliographic dataset. The table below \\
provides data on: the number of publications per yeear (OCC); the number of \\
citations per year (global_citations); the average number of citations per \\
document for each year (mean_global_citations); the average number of \\
citations per document divided by the age of the documents \\
(mean_global_citations_per_year);  Use the the information in the table to \\
draw conclusions about the impact per year. In your analysis, be sure to \\
describe in a clear and concise way, any trends or patterns you observe, \\
and identify any outliers or anomalies  in the data. Limit your description \\
to one paragraph with no more than 250 words.
<BLANKLINE>
Table:
```
|   year |   OCC |   global_citations |   mean_global_citations |   mean_global_citations_per_year |
|-------:|------:|-------------------:|------------------------:|---------------------------------:|
|   2016 |     1 |                 30 |                30       |                             3.75 |
|   2017 |     4 |                162 |                40.5     |                             5.79 |
|   2018 |     3 |                182 |                60.6667  |                            10.11 |
|   2019 |     6 |                 47 |                 7.83333 |                             1.57 |
|   2020 |    14 |                 93 |                 6.64286 |                             1.66 |
|   2021 |    10 |                 27 |                 2.7     |                             0.9  |
|   2022 |    12 |                 22 |                 1.83333 |                             0.92 |
|   2023 |     2 |                  0 |                 0       |                             0    |
```
<BLANKLINE>


"""
from dataclasses import dataclass

import pandas as pd

from ...format_prompt_for_dataframes import format_prompt_for_dataframes
from ._compute_metrics_per_year import compute_metrics_per_year


def annual_outputs(
    #
    # TABLE PARAMS:
    selected_columns=None,
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Global citations per year.

    :meta private:
    """

    #
    # Compute metrics per year
    data_frame = compute_metrics_per_year(
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    #
    # Select only columns existent in the data frame
    if selected_columns is None:
        selected_columns = data_frame.columns.copy()
    else:
        selected_columns = [col for col in selected_columns if col in data_frame.columns]
    data_frame = data_frame[selected_columns]

    @dataclass
    class Result:
        df_: pd.DataFrame = data_frame[selected_columns]
        prompt_: str = _generate_prompt(data_frame)

    return Result()


def _generate_prompt(data_frame: pd.DataFrame) -> str:
    main_text = (
        "Your task is to generate a short summary for a research paper about "
        "the annual performance metrics of a bibliographic dataset. The table "
        "below provides data on: "
    )

    for col in data_frame.columns:
        if col == "OCC":
            main_text += "the number of publications per yeear (OCC); "
        if col == "cum_OCC":
            main_text += "the cummulative number of publications per yeear (OCC); "
        if col == "local_citations":
            main_text += "the number of local citations per year (local_citations); "
        if col == "global_citations":
            main_text += "the number of citations per year (global_citations); "
        if col == "citable_years":
            main_text += "the number of citable years (citable_years); "
        if col == "mean_global_citations":
            main_text += "the average number of citations per document for each year (mean_global_citations); "
        if col == "cum_global_citations":
            main_text += "the cummulative number of citations per document for each year (cum_global_citations); "
        if col == "mean_global_citations_per_year":
            main_text += "the average number of citations per document divided by the age of the documents (mean_global_citations_per_year); "
        if col == "mean_local_citations":
            main_text += "the average number of local citations per document for each year (mean_local_citations); "
        if col == "cum_local_citations":
            main_text += "the cummulative number of local citations per document for each year (cum_local_citations); "
        if col == "mean_local_citations_per_year":
            main_text += "the average number of local citations per document divided by the age of the documents (mean_local_citations_per_year); "

    main_text += (
        " Use the the information in the table "
        "to draw conclusions about the impact per year. In your analysis, be "
        "sure to describe in a clear and concise way, any trends or patterns "
        "you observe, and identify any outliers or anomalies  in the data. "
        "Limit your description to one paragraph with no more than 250 words. "
    )

    table_text = data_frame.to_markdown()

    return format_prompt_for_dataframes(main_text, table_text)

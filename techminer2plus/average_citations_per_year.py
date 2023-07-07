# flake8: noqa
# pylint: disable=line-too-long
"""
.. _average_citations_per_year:

Average Citations per Year
===============================================================================


* Preparation

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

* Object oriented interface

>>> average_citations_per_year = (
...     tm2p.records(root_dir=root_dir)
...     .average_citations_per_year()
... )
>>> average_citations_per_year
AverageCitationsPerYear(root_dir='data/regtech/', database='main',
    year_filter=(None, None), cited_by_filter=(None, None), filters={})


* Functional interface

>>> average_citations_per_year = tm2p.average_citations_per_year(
...     root_dir=root_dir,
... )
>>> average_citations_per_year
AverageCitationsPerYear(root_dir='data/regtech/', database='main',
    year_filter=(None, None), cited_by_filter=(None, None), filters={})


* Results

>>> average_citations_per_year.fig_.write_html("sphinx/_static/average_citations_per_year.html")

.. raw:: html

    <iframe src="../../../_static/average_citations_per_year.html"  height="600px" width="100%" frameBorder="0"></iframe>

    

>>> print(average_citations_per_year.df_.head().to_markdown())
|   year |   OCC |   cum_OCC |   local_citations |   global_citations |   citable_years |   mean_global_citations |   cum_global_citations |   mean_global_citations_per_year |   mean_local_citations |   cum_local_citations |   mean_local_citations_per_year |
|-------:|------:|----------:|------------------:|-------------------:|----------------:|------------------------:|-----------------------:|---------------------------------:|-----------------------:|----------------------:|--------------------------------:|
|   2016 |     1 |         1 |                 0 |                 30 |               8 |                30       |                     30 |                             3.75 |                0       |                     0 |                            0    |
|   2017 |     4 |         5 |                 3 |                162 |               7 |                40.5     |                    192 |                             5.79 |                0.75    |                     3 |                            0.11 |
|   2018 |     3 |         8 |                30 |                182 |               6 |                60.6667  |                    374 |                            10.11 |               10       |                    33 |                            1.67 |
|   2019 |     6 |        14 |                19 |                 47 |               5 |                 7.83333 |                    421 |                             1.57 |                3.16667 |                    52 |                            0.63 |
|   2020 |    14 |        28 |                29 |                 93 |               4 |                 6.64286 |                    514 |                             1.66 |                2.07143 |                    81 |                            0.52 |


>>> print(average_citations_per_year.prompt_)
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
import textwrap
from dataclasses import dataclass
from dataclasses import field as datafield

import pandas as pd
import plotly.graph_objects as go

from ._chatbot import format_chatbot_prompt_for_df
from ._metrics_lib import global_indicators_by_year, indicators_by_year_plot


# pylint: disable=too-many-instance-attributes
@dataclass
class AverageCitationsPerYear:
    """Average Citations per Year.

    :meta private:
    """

    #
    # RESULTS:
    df_: pd.DataFrame
    fig_: go.Figure
    prompt_: str
    #
    # PARAMS:
    root_dir: str = "./"
    database: str = "main"
    year_filter: tuple = (None, None)
    cited_by_filter: tuple = (None, None)
    filters: dict = datafield(default_factory=dict)

    def __post_init__(self):
        if self.filters is None:
            self.filters = {}

    def __repr__(self):
        text = (
            "AverageCitationsPerYear("
            f"root_dir='{self.root_dir}'"
            f", database='{self.database}'"
            f", year_filter={self.year_filter}"
            f", cited_by_filter={self.cited_by_filter}"
            f", filters={self.filters}"
            ")"
        )
        text = textwrap.fill(text, width=75, subsequent_indent="    ")
        return text


def average_citations_per_year(
    title: str = "Average Citations per Year",
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Average citations per year."""

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
        return format_chatbot_prompt_for_df(main_text, table_text)

    #
    # Main code
    #

    indicators = global_indicators_by_year(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    fig = indicators_by_year_plot(
        indicators,
        metric="mean_global_citations",
        title=title,
    )

    prompt = generate_chatgpt_prompt(
        indicators[["mean_global_citations", "global_citations"]]
    )

    return AverageCitationsPerYear(
        #
        # RESULTS:
        df_=indicators,
        fig_=fig,
        prompt_=prompt,
        #
        # PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

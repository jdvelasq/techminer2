# flake8: noqa
# pylint: disable=line-too-long
"""
.. _annual_scientific_production:

Annual Scientific Production
===============================================================================


* Preparation

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

* Object oriented interface


>>> annual_scientific_production = (
...     tm2p.records(root_dir=root_dir)
...     .annual_scientific_production()
... )
>>> annual_scientific_production
AnnualScientificProduction(root_dir='data/regtech/', database='main',
    year_filter=(None, None), cited_by_filter=(None, None), filters={})


* Functional interface

>>> annual_scientific_production = tm2p.annual_scientific_production(
...     root_dir=root_dir,
... )
>>> annual_scientific_production
AnnualScientificProduction(root_dir='data/regtech/', database='main',
    year_filter=(None, None), cited_by_filter=(None, None), filters={})



* Results

>>> annual_scientific_production.fig_.write_html("sphinx/_static/annual_scientific_production.html")

.. raw:: html

    <iframe src="../../../_static/annual_scientific_production.html"  height="600px" width="100%" frameBorder="0"></iframe>


>>> annual_scientific_production.df_.head()
      OCC  cum_OCC  ...  cum_local_citations  mean_local_citations_per_year
year                ...                                                    
2016    1        1  ...                  0.0                           0.00
2017    4        5  ...                  3.0                           0.11
2018    3        8  ...                 33.0                           1.67
2019    6       14  ...                 52.0                           0.63
2020   14       28  ...                 81.0                           0.52
<BLANKLINE>
[5 rows x 11 columns]


>>> print(annual_scientific_production.prompt_)
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
import textwrap
from dataclasses import dataclass
from dataclasses import field as datafield

import pandas as pd
import plotly.graph_objects as go

from ._chatbot import format_chatbot_prompt_for_df
from ._metrics_lib import indicators_by_year, indicators_by_year_plot


# pylint: disable=too-many-instance-attributes
@dataclass
class AnnualScientificProduction:
    """Annual scientific production."""

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
            "AnnualScientificProduction("
            f"root_dir='{self.root_dir}'"
            f", database='{self.database}'"
            f", year_filter={self.year_filter}"
            f", cited_by_filter={self.cited_by_filter}"
            f", filters={self.filters}"
            ")"
        )
        text = textwrap.fill(text, width=75, subsequent_indent="    ")
        return text


def annual_scientific_production(
    title: str = "Annual Scientific Production",
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Computes annual scientific production (number of documents per year).

    Args:
        root_dir (str, optional): Root directory. Defaults to "./".
        database (str, optional): Database name. Defaults to "documents".
        year_filter (tuple, optional): Year filter. Defaults to None.
        cited_by_filter (tuple, optional): Cited by filter. Defaults to None.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.

    Returns:
        :class:`IndicatorByYearChart`: A :class:`IndicatorByYearChart` instance.


    """

    def generate_chatgpt_prompt(table):
        """Generates the prompt for annual_scientific_production."""

        main_text = (
            "The table below, delimited by triple backticks, provides data on the annual scientific "
            "production in a bibliographic database. Use the table to draw conclusions about annual "
            "research productivity and the cumulative productivity. The "
            "column 'OCC' is the number of documents published in a given "
            "year. The column 'cum_OCC' is the cumulative number of "
            "documents published up to a given year. The information in the "
            "table is used to create a line plot of number of publications "
            "per year. In your analysis, be sure to describe in a clear and "
            "concise way, any trends or patterns you observe, and identify "
            "any outliers or anomalies in the data. Limit your description "
            "to one paragraph with no more than 250 words."
        )

        table_text = table.to_markdown()
        return format_chatbot_prompt_for_df(main_text, table_text)

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

    fig = indicators_by_year_plot(
        indicators,
        metric="OCC",
        title=title,
    )

    prompt = generate_chatgpt_prompt(indicators[["OCC", "cum_OCC"]])

    return AnnualScientificProduction(
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

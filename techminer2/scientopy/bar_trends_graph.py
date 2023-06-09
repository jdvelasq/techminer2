# flake8: noqa
"""
Bar Trends Graph
===============================================================================

ScientoPy Bar Trends


**Basic Usage.**

>>> from techminer2 import scientopy
>>> root_dir = "data/regtech/"

>>> file_name = "sphinx/_static/scientpy__bar_trends-1.html"
>>> r = scientopy.bar_trends_graph(
...     field="author_keywords",
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientpy__bar_trends-1.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()
                    OCC  Before 2022  Between 2022-2023
author_keywords                                        
REGTECH              28           20                  8
FINTECH              12           10                  2
COMPLIANCE            7            5                  2
REGULATION            5            4                  1
FINANCIAL_SERVICES    4            3                  1


>>> print(r.prompt_)
Your task is to generate a short analysis for a scientific research paper. Analyze the table below, delimited by triple backticks, in at most 100 words, for the occurrences per year of different items of the field 'author_keywords' and years in the columns. 
<BLANKLINE>
Table:
```
| author_keywords                 |   OCC |   Before 2022 |   Between 2022-2023 |
|:--------------------------------|------:|--------------:|--------------------:|
| REGTECH                         |    28 |            20 |                   8 |
| FINTECH                         |    12 |            10 |                   2 |
| COMPLIANCE                      |     7 |             5 |                   2 |
| REGULATION                      |     5 |             4 |                   1 |
| FINANCIAL_SERVICES              |     4 |             3 |                   1 |
| FINANCIAL_REGULATION            |     4 |             2 |                   2 |
| REGULATORY_TECHNOLOGY (REGTECH) |     4 |             3 |                   1 |
| ARTIFICIAL_INTELLIGENCE         |     4 |             3 |                   1 |
| ANTI_MONEY_LAUNDERING           |     4 |             4 |                   0 |
| RISK_MANAGEMENT                 |     3 |             2 |                   1 |
| INNOVATION                      |     3 |             2 |                   1 |
| REGULATORY_TECHNOLOGY           |     3 |             2 |                   1 |
| BLOCKCHAIN                      |     3 |             3 |                   0 |
| SUPTECH                         |     3 |             1 |                   2 |
| DATA_PROTECTION                 |     2 |             1 |                   1 |
| SMART_CONTRACT                  |     2 |             2 |                   0 |
| CHARITYTECH                     |     2 |             1 |                   1 |
| ENGLISH_LAW                     |     2 |             1 |                   1 |
| ACCOUNTABILITY                  |     2 |             2 |                   0 |
| DATA_PROTECTION_OFFICER         |     2 |             2 |                   0 |
```
<BLANKLINE>

**Time Filter.**

>>> file_name = "sphinx/_static/scientpy__bar_trends-3.html"
>>> r = scientopy.bar_trends_graph(
...     field="author_keywords",
...     year_filter=(2018, 2021),
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientpy__bar_trends-3.html" height="800px" width="100%" frameBorder="0"></iframe>

>>> r.table_.head()
                       OCC  Before 2020  Between 2020-2021
author_keywords                                           
REGTECH                 18            7                 11
FINTECH                 10            6                  4
COMPLIANCE               5            1                  4
REGULATION               4            2                  2
ANTI_MONEY_LAUNDERING    4            0                  4



**Custom Topics Extraction.**

>>> file_name = "sphinx/_static/scientpy__bar_trends-4.html"
>>> from techminer2 import scientopy
>>> r = scientopy.bar_trends_graph(
...     field="author_keywords",
...     custom_items=[
...         "FINTECH",
...         "BLOCKCHAIN",
...         "FINANCIAL_REGULATION",
...         "MACHINE_LEARNING",
...         "BIG_DATA",
...         "CRYPTOCURRENCY",
...     ],
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientpy__bar_trends-4.html" height="800px" width="100%" frameBorder="0"></iframe>




>>> file_name = "sphinx/_static/scientpy__bar_trends-5.html"
>>> r = scientopy.bar_trends_graph(
...     field="author_keywords",
...     is_trend_analysis=True,
...     year_filter=(2018, 2021),
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientpy__bar_trends-5.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()    
                                 OCC  Before 2020  Between 2020-2021
author_keywords                                                     
ANTI_MONEY_LAUNDERING              4            0                  4
REGULATORY_TECHNOLOGY (REGTECH)    3            0                  3
REGULATION                         4            2                  2
ACCOUNTABILITY                     2            0                  2
DATA_PROTECTION_OFFICER            2            0                  2




>>> print(r.prompt_)
Your task is to generate a short analysis for a scientific research paper. Analyze the table below, delimited by triple backticks, in at most 100 words, for the occurrences per year of different items of the field 'author_keywords' and years in the columns. 
<BLANKLINE>
Table:
```
| author_keywords                 |   OCC |   Before 2020 |   Between 2020-2021 |
|:--------------------------------|------:|--------------:|--------------------:|
| ANTI_MONEY_LAUNDERING           |     4 |             0 |                   4 |
| REGULATORY_TECHNOLOGY (REGTECH) |     3 |             0 |                   3 |
| REGULATION                      |     4 |             2 |                   2 |
| ACCOUNTABILITY                  |     2 |             0 |                   2 |
| DATA_PROTECTION_OFFICER         |     2 |             0 |                   2 |
| GDPR                            |     2 |             0 |                   2 |
| INNOVATION                      |     2 |             0 |                   2 |
| REGULATORY_TECHNOLOGY           |     2 |             0 |                   2 |
| CORONAVIRUS                     |     1 |             0 |                   1 |
| DIGITAL_TECHNOLOGIES            |     1 |             0 |                   1 |
| REGULATIONS_AND_COMPLIANCE      |     1 |             0 |                   1 |
| SMART_TREASURY                  |     1 |             0 |                   1 |
| BAHRAIN                         |     1 |             0 |                   1 |
| ANTITRUST                       |     1 |             0 |                   1 |
| COMPETITION_LAW                 |     1 |             0 |                   1 |
| RESALE_PRICE_MAINTENANCE        |     1 |             0 |                   1 |
| VERTICAL_PRICE_FIXING           |     1 |             0 |                   1 |
| ANOMALY_DETECTION               |     1 |             0 |                   1 |
| CLASSIFICATION                  |     1 |             0 |                   1 |
| DATA_ANALYSIS                   |     1 |             0 |                   1 |
```
<BLANKLINE>



# pylint: disable=line-too-long
"""

import plotly.express as px

from ..classes import ScientoPyGraph
from ..item_utils import generate_custom_items
from ..sort_utils import sort_indicators_by_metric
from ..techminer.indicators.growth_indicators_by_field import (
    growth_indicators_by_field,
)
from ..vantagepoint.report import bar_chart
from .common import PROMPT, get_default_indicators, get_trend_indicators


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def bar_trends_graph(
    field,
    # Specific params:
    time_window=2,
    is_trend_analysis=False,
    title=None,
    field_label=None,
    n_words=100,
    # Item filters:
    top_n=20,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """ScientoPy Bar Trend."""

    if is_trend_analysis:
        return trend_analysis_bar_trends_graph(
            field=field,
            # Specific params:
            time_window=time_window,
            title=title,
            field_label=field_label,
            n_words=n_words,
            # Item filters:
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
            custom_items=custom_items,
            # Database params:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

    return default_bar_trends_graph(
        field=field,
        # Specific params:
        time_window=time_window,
        title=title,
        field_label=field_label,
        n_words=n_words,
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )


PROMPT = """\
Your task is to generate a short analysis for a scientific research paper. \
Analyze the table below, delimited by triple backticks, in at most {n_words} \
words, for the occurrences per year of different items of the field \
'{field}' and years in the columns. 
"""


def default_bar_trends_graph(
    field,
    # Specific params:
    time_window,
    title,
    field_label,
    n_words,
    # Item filters:
    top_n,
    occ_range,
    gc_range,
    custom_items,
    # Database params:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    """Creates a bar trend graph."""

    indicators = get_default_indicators(
        field=field,
        # Specific params:
        time_window=time_window,
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    occ = indicators.columns[0]
    before = indicators.columns[1]
    between = indicators.columns[2]

    indicators = indicators[[occ, before, between]]
    table = indicators.copy()
    indicators[field] = indicators.index

    indicators = indicators.reset_index(drop=True)
    indicators = indicators.melt(id_vars=field, value_vars=[before, between])
    indicators = indicators.rename(
        columns={
            field: field.replace("_", " ").title(),
            "variable": "Period",
            "value": "Num Documents",
        }
    )

    obj = ScientoPyGraph()
    obj.table_ = table
    obj.plot_ = _make_plot(
        indicators, field, before, between, title, field_label
    )
    obj.prompt_ = (
        PROMPT.format(
            field=field, before=before, between=between, n_words=n_words
        )
        + f"\nTable:\n```\n{table.to_markdown()}\n```\n"
    )

    return obj


def trend_analysis_bar_trends_graph(
    field,
    # Specific params:
    time_window,
    title,
    field_label,
    n_words,
    # Item filters:
    top_n,
    occ_range,
    gc_range,
    custom_items,
    # Database params:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    """Creates a bar trend graph."""

    indicators = get_trend_indicators(
        field=field,
        # Specific params:
        time_window=time_window,
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    occ = indicators.columns[0]
    before = indicators.columns[1]
    between = indicators.columns[2]

    indicators = indicators[[occ, before, between]]
    table = indicators.copy()
    indicators[field] = indicators.index

    indicators = indicators.reset_index(drop=True)
    indicators = indicators.melt(id_vars=field, value_vars=[before, between])
    indicators = indicators.rename(
        columns={
            field: field.replace("_", " ").title(),
            "variable": "Period",
            "value": "Num Documents",
        }
    )

    obj = ScientoPyGraph()
    obj.table_ = table
    obj.plot_ = _make_plot(
        indicators, field, before, between, title, field_label
    )
    obj.prompt_ = (
        PROMPT.format(
            field=field, before=before, between=between, n_words=n_words
        )
        + f"\nTable:\n```\n{table.to_markdown()}\n```\n"
    )

    return obj


def _make_plot(indicators, criterion, col0, col1, title, field_label):
    fig = px.bar(
        indicators,
        x="Num Documents",
        y=criterion.replace("_", " ").title(),
        color="Period",
        title=title,
        hover_data=["Num Documents"],
        orientation="h",
        color_discrete_map={
            col0: "#8da4b4",
            col1: "#556f81",
        },
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
        title=field_label,
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="gray",
        griddash="dot",
    )

    return fig

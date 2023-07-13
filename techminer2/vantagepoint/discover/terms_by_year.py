# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _terms_by_year:

Terms by Year
===============================================================================

>>> from techminer2 import vantagepoint
>>> root_dir = "data/regtech/"
>>> terms_by_year = vantagepoint.discover.terms_by_year(
...     root_dir=root_dir,
...     field="author_keywords",
...     top_n=10,
... )
>>> terms_by_year.df_
year                            2017  2018  2019  2020  2021  2022  2023
author_keywords                                                         
REGTECH 28:329                     2     3     4     8     3     6     2
FINTECH 12:249                     0     2     4     3     1     2     0
REGULATORY_TECHNOLOGY 07:037       0     0     0     2     3     2     0
COMPLIANCE 07:030                  0     0     1     3     1     1     1
REGULATION 05:164                  0     2     0     1     1     1     0
ANTI_MONEY_LAUNDERING 05:034       0     0     0     2     3     0     0
FINANCIAL_SERVICES 04:168          1     1     0     1     0     1     0
FINANCIAL_REGULATION 04:035        1     0     0     1     0     2     0
ARTIFICIAL_INTELLIGENCE 04:023     0     0     1     2     0     1     0
RISK_MANAGEMENT 03:014             0     1     0     1     0     1     0

>>> terms_by_year.fig_.write_html("sphinx/_static/terms_by_year_0.html")

.. raw:: html

    <iframe src="../../../../_static/terms_by_year_0.html" height="800px" width="100%" frameBorder="0"></iframe>

    
>>> print(terms_by_year.prompt_)
Your task is to generate an analysis about the  occurrences by year of the \\
'author_keywords' in a scientific bibliography database. Summarize the \\
table below, delimited by triple backticks, identify any notable patterns, \\
trends, or outliers in the data, and disc  uss their implications for the \\
research field. Be sure to provide a concise summary of your findings in no \\
more than 150 words.
<BLANKLINE>
Table:
```
| author_keywords                |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329                 |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| FINTECH 12:249                 |      0 |      2 |      4 |      3 |      1 |      2 |      0 |
| REGULATORY_TECHNOLOGY 07:037   |      0 |      0 |      0 |      2 |      3 |      2 |      0 |
| COMPLIANCE 07:030              |      0 |      0 |      1 |      3 |      1 |      1 |      1 |
| REGULATION 05:164              |      0 |      2 |      0 |      1 |      1 |      1 |      0 |
| ANTI_MONEY_LAUNDERING 05:034   |      0 |      0 |      0 |      2 |      3 |      0 |      0 |
| FINANCIAL_SERVICES 04:168      |      1 |      1 |      0 |      1 |      0 |      1 |      0 |
| FINANCIAL_REGULATION 04:035    |      1 |      0 |      0 |      1 |      0 |      2 |      0 |
| ARTIFICIAL_INTELLIGENCE 04:023 |      0 |      0 |      1 |      2 |      0 |      1 |      0 |
| RISK_MANAGEMENT 03:014         |      0 |      1 |      0 |      1 |      0 |      1 |      0 |
```
<BLANKLINE>


>>> terms_by_year = vantagepoint.discover.terms_by_year(
...     root_dir=root_dir,
...     field="author_keywords",
...     top_n=10,
...     cumulative=True,
... )
>>> terms_by_year.df_
year                            2017  2018  2019  2020  2021  2022  2023
author_keywords                                                         
REGTECH 28:329                     2     5     9    17    20    26    28
FINTECH 12:249                     0     2     6     9    10    12    12
REGULATORY_TECHNOLOGY 07:037       0     0     0     2     5     7     7
COMPLIANCE 07:030                  0     0     1     4     5     6     7
REGULATION 05:164                  0     2     2     3     4     5     5
ANTI_MONEY_LAUNDERING 05:034       0     0     0     2     5     5     5
FINANCIAL_SERVICES 04:168          1     2     2     3     3     4     4
FINANCIAL_REGULATION 04:035        1     1     1     2     2     4     4
ARTIFICIAL_INTELLIGENCE 04:023     0     0     1     3     3     4     4
RISK_MANAGEMENT 03:014             0     1     1     2     2     3     3

>>> terms_by_year.fig_.write_html("sphinx/_static/terms_by_year_1.html")

.. raw:: html

    <iframe src="../../../../_static/terms_by_year_1.html" height="800px" width="100%" frameBorder="0"></iframe>

>>> print(terms_by_year.prompt_)    
Your task is to generate an analysis about the cumulative occurrences by \\
year of the 'author_keywords' in a scientific bibliography database. \\
Summarize the table below, delimited by triple backticks, identify any \\
notable patterns, trends, or outliers in the data, and disc  uss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| author_keywords                |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329                 |      2 |      5 |      9 |     17 |     20 |     26 |     28 |
| FINTECH 12:249                 |      0 |      2 |      6 |      9 |     10 |     12 |     12 |
| REGULATORY_TECHNOLOGY 07:037   |      0 |      0 |      0 |      2 |      5 |      7 |      7 |
| COMPLIANCE 07:030              |      0 |      0 |      1 |      4 |      5 |      6 |      7 |
| REGULATION 05:164              |      0 |      2 |      2 |      3 |      4 |      5 |      5 |
| ANTI_MONEY_LAUNDERING 05:034   |      0 |      0 |      0 |      2 |      5 |      5 |      5 |
| FINANCIAL_SERVICES 04:168      |      1 |      2 |      2 |      3 |      3 |      4 |      4 |
| FINANCIAL_REGULATION 04:035    |      1 |      1 |      1 |      2 |      2 |      4 |      4 |
| ARTIFICIAL_INTELLIGENCE 04:023 |      0 |      0 |      1 |      3 |      3 |      4 |      4 |
| RISK_MANAGEMENT 03:014         |      0 |      1 |      1 |      2 |      2 |      3 |      3 |
```
<BLANKLINE>

>>> print(terms_by_year.metrics_.head(20).to_markdown())
|    | author_keywords       |   year |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|---:|:----------------------|-------:|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
|  0 | REGTECH               |   2017 |     2 |         2 |                 12 |                 3 |     7 |                       1.714 |                      0.429 |
|  1 | REGTECH               |   2018 |     3 |         5 |                182 |                30 |     6 |                      30.333 |                      5     |
|  2 | REGTECH               |   2019 |     4 |         9 |                 42 |                18 |     5 |                       8.4   |                      3.6   |
|  3 | REGTECH               |   2020 |     8 |        17 |                 67 |                17 |     4 |                      16.75  |                      4.25  |
|  4 | REGTECH               |   2021 |     3 |        20 |                  6 |                 4 |     3 |                       2     |                      1.333 |
|  5 | REGTECH               |   2022 |     6 |        26 |                 20 |                 2 |     2 |                      10     |                      1     |
|  6 | REGTECH               |   2023 |     2 |        28 |                  0 |                 0 |     1 |                       0     |                      0     |
|  7 | FINTECH               |   2018 |     2 |         2 |                161 |                22 |     6 |                      26.833 |                      3.667 |
|  8 | FINTECH               |   2019 |     4 |         6 |                 42 |                18 |     5 |                       8.4   |                      3.6   |
|  9 | FINTECH               |   2020 |     3 |         9 |                 29 |                 5 |     4 |                       7.25  |                      1.25  |
| 10 | FINTECH               |   2021 |     1 |        10 |                  3 |                 3 |     3 |                       1     |                      1     |
| 11 | FINTECH               |   2022 |     2 |        12 |                 14 |                 1 |     2 |                       7     |                      0.5   |
| 12 | REGULATORY_TECHNOLOGY |   2020 |     2 |         2 |                 16 |                 7 |     4 |                       4     |                      1.75  |
| 13 | REGULATORY_TECHNOLOGY |   2021 |     3 |         5 |                 19 |                 6 |     3 |                       6.333 |                      2     |
| 14 | REGULATORY_TECHNOLOGY |   2022 |     2 |         7 |                  2 |                 1 |     2 |                       1     |                      0.5   |
| 15 | COMPLIANCE            |   2019 |     1 |         1 |                  3 |                 0 |     5 |                       0.6   |                      0     |
| 16 | COMPLIANCE            |   2020 |     3 |         4 |                 24 |                 9 |     4 |                       6     |                      2.25  |
| 17 | COMPLIANCE            |   2021 |     1 |         5 |                  2 |                 0 |     3 |                       0.667 |                      0     |
| 18 | COMPLIANCE            |   2022 |     1 |         6 |                  1 |                 0 |     2 |                       0.5   |                      0     |
| 19 | COMPLIANCE            |   2023 |     1 |         7 |                  0 |                 0 |     1 |                       0     |                      0     |

>>> print(terms_by_year.documents_.head().to_markdown())
|    | author_keywords    | title                                                   |   year | source_title                                                   |   global_citations |   local_citations | doi                            |
|---:|:-------------------|:--------------------------------------------------------|-------:|:---------------------------------------------------------------|-------------------:|------------------:|:-------------------------------|
|  0 | FINANCIAL_SERVICES | FINTECH and REGTECH: impact on regulators and BANKS     |   2018 | Journal of Economics and Business                              |                153 |                17 | 10.1016/J.JECONBUS.2018.07.003 |
|  1 | FINTECH            | FINTECH and REGTECH: impact on regulators and BANKS     |   2018 | Journal of Economics and Business                              |                153 |                17 | 10.1016/J.JECONBUS.2018.07.003 |
|  2 | REGTECH            | FINTECH and REGTECH: impact on regulators and BANKS     |   2018 | Journal of Economics and Business                              |                153 |                17 | 10.1016/J.JECONBUS.2018.07.003 |
|  3 | REGULATION         | FINTECH and REGTECH: impact on regulators and BANKS     |   2018 | Journal of Economics and Business                              |                153 |                17 | 10.1016/J.JECONBUS.2018.07.003 |
|  4 | FINTECH            | understanding REGTECH for digital REGULATORY_COMPLIANCE |   2019 | Palgrave Studies in Digital Business and Enabling Technologies |                 33 |                14 | 10.1007/978-3-030-02330-0_6    |


"""
from dataclasses import dataclass

import plotly.express as px

from ..._counters_lib import add_counters_to_frame_axis
from ..._filtering_lib import generate_custom_items
from ..._sorting_lib import sort_indicators_by_metric
from ...format_prompt_for_dataframes import format_prompt_for_dataframes
from ...techminer.metrics.global_indicators_by_field import (
    global_indicators_by_field,
)
from ...techminer.metrics.global_metrics_by_field_per_year import (
    global_metrics_by_field_per_year,
)
from ...techminer.metrics.items_occurrences_by_year import (
    items_occurrences_by_year,
)
from ...techminer.reports.documents_per_item import documents_per_item

COLOR = "#556f81"
TEXTLEN = 40


def terms_by_year(
    #
    # PARAMS:
    field,
    cumulative=False,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    # pylint: disable=line-too-long
    """Computes a table with the number of occurrences of each term by year."""

    data_frame = __table(
        #
        # PARAMS:
        field=field,
        cumulative=cumulative,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    prompt = __prompt(data_frame, field, cumulative)

    fig = __gantt(data_frame, field, title=None)

    metrics = __metrics(
        items=data_frame.index.tolist(),
        field=field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    documents = __documents(
        items=data_frame.index.tolist(),
        field=field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    @dataclass
    class Results:
        df_ = data_frame
        prompt_ = prompt
        fig_ = fig
        metrics_ = metrics
        documents_ = documents

    return Results()


def __table(
    #
    # PARAMS:
    field,
    cumulative,
    #
    # ITEM FILTERS:
    top_n,
    occ_range,
    gc_range,
    custom_items,
    #
    # DATABASE PARAMS:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    descriptors_by_year = items_occurrences_by_year(
        field=field,
        cumulative=cumulative,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    if custom_items is None:
        indicators = global_indicators_by_field(
            field=field,
            #
            # DATABASE PARAMS:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

        indicators = sort_indicators_by_metric(indicators, metric="OCC")

        custom_items = generate_custom_items(
            indicators=indicators,
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
        )

    descriptors_by_year = descriptors_by_year[
        descriptors_by_year.index.isin(custom_items)
    ]

    descriptors_by_year = descriptors_by_year.loc[custom_items, :]

    descriptors_by_year = add_counters_to_frame_axis(
        descriptors_by_year,
        axis=0,
        field=field,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return descriptors_by_year


def __prompt(data_frame, field, cumulative):
    main_text = (
        "Your task is to generate an analysis about the "
        f"{'cumulative' if cumulative else ''} occurrences by year "
        f"of the '{field}' in a scientific bibliography database. "
        "Summarize the table below, delimited by triple backticks, "
        "identify any notable patterns, trends, or outliers in the data, "
        "and disc  uss their implications for the research field. Be sure "
        "to provide a concise summary of your findings in no more than "
        "150 words."
    )

    return format_prompt_for_dataframes(main_text, data_frame.to_markdown())


def __gantt(
    data_frame,
    field,
    title=None,
):
    # pylint: disable=line-too-long
    """Computes a table with the number of occurrences of each term by year."""

    data_frame = data_frame.copy()
    data_frame["RANKING"] = range(1, len(data_frame) + 1)
    data_frame = data_frame.melt(
        value_name="OCC",
        var_name="column",
        ignore_index=False,
        id_vars=["RANKING"],
    )

    data_frame = data_frame[data_frame.OCC > 0]
    data_frame = data_frame.sort_values(by=["RANKING"], ascending=True)
    data_frame = data_frame.drop(columns=["RANKING"])

    data_frame = data_frame.rename(columns={"column": "Year"})
    data_frame = data_frame.reset_index()

    fig = px.scatter(
        data_frame,
        x="Year",
        y=field,
        size="OCC",
        hover_data=data_frame.columns.to_list(),
        title=title,
        color=field,
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        showlegend=False,
        xaxis_title=None,
        yaxis_title=field.replace("_", " ").upper(),
    )
    fig.update_traces(
        marker={
            "line": {"color": "white", "width": 0.5},
            "opacity": 1.0,
        },
        marker_color=COLOR,
        mode="lines+markers",
        line={"width": 2, "color": COLOR},
    )
    fig.update_xaxes(
        linecolor="white",
        linewidth=1,
        gridcolor="gray",
        griddash="dot",
        tickangle=270,
        dtick=1.0,
    )
    fig.update_yaxes(
        linecolor="white",
        linewidth=1,
        gridcolor="gray",
        griddash="dot",
    )

    return fig


def __metrics(
    items,
    field,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Creates a rank chart."""

    items = items.copy()
    items = [" ".join(item.split(" ")[:-1]) for item in items]

    data_frame = global_metrics_by_field_per_year(
        field=field,
        as_index=False,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    data_frame = data_frame[data_frame[field].isin(items)]

    data_frame["TOTAL_OCC"] = data_frame.groupby(field)["OCC"].transform("sum")
    data_frame["TOTAL_GC"] = data_frame.groupby(field)[
        "global_citations"
    ].transform("sum")
    data_frame["TOTAL_LC"] = data_frame.groupby(field)[
        "local_citations"
    ].transform("sum")
    data_frame = data_frame.sort_values(
        ["TOTAL_OCC", "TOTAL_GC", "TOTAL_LC", field, "year"],
        ascending=[False, False, False, True, True],
    )
    data_frame = data_frame.drop(columns=["TOTAL_OCC", "TOTAL_GC", "TOTAL_LC"])
    data_frame = data_frame.reset_index(drop=True)

    return data_frame


def __documents(
    items,
    field,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    items = items.copy()
    items = [" ".join(item.split(" ")[:-1]) for item in items]

    documents = documents_per_item(
        field=field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    documents = documents[documents[field].isin(items)]
    documents = documents.sort_values(
        ["global_citations", "local_citations", "year", "title"],
        ascending=[False, False, True, True],
    )
    documents = documents.reset_index(drop=True)

    return documents

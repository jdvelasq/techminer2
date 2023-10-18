# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Terms by Year
===============================================================================

>>> from techminer2.analyze import terms_by_year
>>> terms = terms_by_year(
...     #
...     # PARAMS:
...     field="author_keywords",
...     cumulative=False,
...     #
...     # CHART PARAMS:
...     title=None,
...     #
...     # ITEM FILTERS:
...     top_n=10,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> terms.df_
year                          2015  2016  2017  2018  2019
author_keywords                                           
FINTECH 31:5168                  0     5     8    12     6
INNOVATION 07:0911               0     3     3     1     0
FINANCIAL_SERVICES 04:0667       0     1     0     3     0
FINANCIAL_TECHNOLOGY 04:0551     0     0     1     1     2
BUSINESS 03:0896                 0     0     0     3     0
SHADOW_BANKING 03:0643           0     0     0     2     1
FINANCIAL_INCLUSION 03:0590      0     1     2     0     0
CASE_STUDIES 03:0442             0     0     1     1     1
DIGITALIZATION 03:0434           0     2     1     0     0
BANKING 03:0375                  0     1     2     0     0



>>> terms.fig_.write_html("sphinx/_static/analyze/terms_by_year_0.html")

.. raw:: html

    <iframe src="../../../_static/analyze/terms_by_year_0.html" 
    height="800px" width="100%" frameBorder="0"></iframe>

    
>>> print(terms.prompt_) # doctest: +ELLIPSIS
Your task is ...



>>> terms = terms_by_year(
...     #
...     # PARAMS:
...     field="author_keywords",
...     cumulative=True,
...     #
...     # CHART PARAMS:
...     title=None,
...     #
...     # ITEM FILTERS:
...     top_n=10,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> terms.df_
year                          2015  2016  2017  2018  2019
author_keywords                                           
FINTECH 31:5168                  0     5    13    25    31
INNOVATION 07:0911               0     3     6     7     7
FINANCIAL_SERVICES 04:0667       0     1     1     4     4
FINANCIAL_TECHNOLOGY 04:0551     0     0     1     2     4
BUSINESS 03:0896                 0     0     0     3     3
SHADOW_BANKING 03:0643           0     0     0     2     3
FINANCIAL_INCLUSION 03:0590      0     1     3     3     3
CASE_STUDIES 03:0442             0     0     1     2     3
DIGITALIZATION 03:0434           0     2     3     3     3
BANKING 03:0375                  0     1     3     3     3


>>> terms.fig_.write_html("sphinx/_static/analyze/terms_by_year_1.html")

.. raw:: html

    <iframe src="../../../_static/performance/plots/terms_by_year_1.html" 
    height="800px" width="100%" frameBorder="0"></iframe>

>>> print(terms.prompt_) # doctest: +ELLIPSIS    
Your task is ...



>>> print(terms.metrics_.head(20).to_markdown())
|    | author_keywords      |   year |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|---:|:---------------------|-------:|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
|  0 | FINTECH              |   2016 |     5 |         5 |                498 |                 6 |     4 |                     124.5   |                      1.5   |
|  1 | FINTECH              |   2017 |     8 |        13 |               1572 |                11 |     3 |                     524     |                      3.667 |
|  2 | FINTECH              |   2018 |    12 |        25 |               2338 |                 9 |     2 |                    1169     |                      4.5   |
|  3 | FINTECH              |   2019 |     6 |        31 |                760 |                 1 |     1 |                     760     |                      1     |
|  4 | INNOVATION           |   2016 |     3 |         3 |                407 |                 3 |     4 |                     101.75  |                      0.75  |
|  5 | INNOVATION           |   2017 |     3 |         6 |                402 |                 2 |     3 |                     134     |                      0.667 |
|  6 | INNOVATION           |   2018 |     1 |         7 |                102 |                 0 |     2 |                      51     |                      0     |
|  7 | FINANCIAL_SERVICES   |   2016 |     1 |         1 |                226 |                 0 |     4 |                      56.5   |                      0     |
|  8 | FINANCIAL_SERVICES   |   2018 |     3 |         4 |                441 |                 1 |     2 |                     220.5   |                      0.5   |
|  9 | FINANCIAL_TECHNOLOGY |   2017 |     1 |         1 |                253 |                 1 |     3 |                      84.333 |                      0.333 |
| 10 | FINANCIAL_TECHNOLOGY |   2018 |     1 |         2 |                137 |                 0 |     2 |                      68.5   |                      0     |
| 11 | FINANCIAL_TECHNOLOGY |   2019 |     2 |         4 |                161 |                 0 |     1 |                     161     |                      0     |
| 12 | BUSINESS             |   2018 |     3 |         3 |                896 |                 3 |     2 |                     448     |                      1.5   |
| 13 | SHADOW_BANKING       |   2018 |     2 |         2 |                546 |                 2 |     2 |                     273     |                      1     |
| 14 | SHADOW_BANKING       |   2019 |     1 |         3 |                 97 |                 0 |     1 |                      97     |                      0     |
| 15 | FINANCIAL_INCLUSION  |   2016 |     1 |         1 |                 96 |                 1 |     4 |                      24     |                      0.25  |
| 16 | FINANCIAL_INCLUSION  |   2017 |     2 |         3 |                494 |                 4 |     3 |                     164.667 |                      1.333 |
| 17 | CASE_STUDIES         |   2017 |     1 |         1 |                180 |                 2 |     3 |                      60     |                      0.667 |
| 18 | CASE_STUDIES         |   2018 |     1 |         2 |                102 |                 0 |     2 |                      51     |                      0     |
| 19 | CASE_STUDIES         |   2019 |     1 |         3 |                160 |                 0 |     1 |                     160     |                      0     |



>>> print(terms.documents_.head().to_markdown())
|    | author_keywords   | document_title                                                               |   year | source_title                   |   global_citations |   local_citations | doi                           |
|---:|:------------------|:-----------------------------------------------------------------------------|-------:|:-------------------------------|-------------------:|------------------:|:------------------------------|
|  0 | BUSINESS          | FINTECH: ECOSYSTEM, BUSINESS_MODELS, INVESTMENT_DECISIONS, and CHALLENGES    |   2018 | Business Horizons              |                557 |                 2 | 10.1016/J.BUSHOR.2017.09.003  |
|  1 | FINTECH           | FINTECH: ECOSYSTEM, BUSINESS_MODELS, INVESTMENT_DECISIONS, and CHALLENGES    |   2018 | Business Horizons              |                557 |                 2 | 10.1016/J.BUSHOR.2017.09.003  |
|  2 | FINTECH           | DIGITAL_FINANCE and FINTECH: CURRENT_RESEARCH and FUTURE_RESEARCH_DIRECTIONS |   2017 | Journal of Business Economics  |                489 |                 4 | 10.1007/S11573-017-0852-X     |
|  3 | FINTECH           | FINTECH, REGULATORY_ARBITRAGE, and the RISE of SHADOW_BANKS                  |   2018 | Journal of Financial Economics |                390 |                 0 | 10.1016/J.JFINECO.2018.03.011 |
|  4 | SHADOW_BANKING    | FINTECH, REGULATORY_ARBITRAGE, and the RISE of SHADOW_BANKS                  |   2018 | Journal of Financial Economics |                390 |                 0 | 10.1016/J.JFINECO.2018.03.011 |


"""
from dataclasses import dataclass

import plotly.express as px

from .._common._counters_lib import add_counters_to_frame_axis
from .._common._filtering_lib import generate_custom_items
from .._common._sorting_lib import sort_indicators_by_metric
from .._common.format_prompt_for_dataframes import format_prompt_for_dataframes
from ..indicators.global_indicators_by_field import global_indicators_by_field
from ..indicators.global_metrics_by_field_per_year import (
    global_metrics_by_field_per_year,
)
from ..indicators.items_occurrences_by_year import items_occurrences_by_year
from .documents_per_item import documents_per_item

COLOR = "#465c6b"
TEXTLEN = 40


def terms_by_year(
    #
    # PARAMS:
    field,
    cumulative=False,
    #
    # CHART PARAMS:
    title=None,
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
    """Computes a table with the number of occurrences of each term by year.

    :meta private:
    """

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

    fig = __gantt(data_frame, field, title)

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
            metric="OCC",
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
    title,
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
    data_frame["TOTAL_GC"] = data_frame.groupby(field)["global_citations"].transform(
        "sum"
    )
    data_frame["TOTAL_LC"] = data_frame.groupby(field)["local_citations"].transform(
        "sum"
    )
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
        ["global_citations", "local_citations", "year", "document_title"],
        ascending=[False, False, True, True],
    )
    documents = documents.reset_index(drop=True)

    return documents

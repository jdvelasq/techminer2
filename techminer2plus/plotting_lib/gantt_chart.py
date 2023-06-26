# flake8: noqa
"""
Gantt Chart
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/report/gantt_chart.html"

>>> import techminer2plus
>>> data = techminer2plus.analyze.terms_by_year(
...    field='author_keywords',
...    top_n=20,
...    root_dir=root_dir,
... )
>>> chart = techminer2plus.report.gantt_chart(data)
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/report/gantt_chart.html" height="800px" width="100%" frameBorder="0"></iframe>

    
>>> chart.table_.head(10)
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




>>> print(chart.prompt_)
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
| INNOVATION 03:012              |      0 |      0 |      0 |      1 |      1 |      1 |      0 |
| BLOCKCHAIN 03:005              |      1 |      0 |      1 |      0 |      1 |      0 |      0 |
| SUPTECH 03:004                 |      0 |      0 |      1 |      0 |      0 |      2 |      0 |
| SEMANTIC_TECHNOLOGIES 02:041   |      0 |      1 |      1 |      0 |      0 |      0 |      0 |
| DATA_PROTECTION 02:027         |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| SMART_CONTRACTS 02:022         |      1 |      1 |      0 |      0 |      0 |      0 |      0 |
| CHARITYTECH 02:017             |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| ENGLISH_LAW 02:017             |      0 |      0 |      0 |      1 |      0 |      1 |      0 |
| ACCOUNTABILITY 02:014          |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
| DATA_PROTECTION_OFFICER 02:014 |      0 |      0 |      0 |      1 |      1 |      0 |      0 |
```
<BLANKLINE>

# pylint: disable=line-too-long    
"""
import textwrap

import plotly.express as px

# from ..analyze import terms_by_year
# from ..classes import BasicChart

COLOR = "#556f81"
TEXTLEN = 40


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def gantt_chart(
    obj=None,
    #
    # Gantt params:
    title=None,
    #
    # Terms by year params:
    field=None,
    # Table params:
    cumulative=False,
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database filters:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Creates a Gantt Chart from a terms by year table."""

    def compute_obj(obj):
        """Compute the object if it is not already computed."""
        if obj is None:
            return terms_by_year(
                field=field,
                # Table params:
                cumulative=cumulative,
                # Item filters:
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
                custom_items=custom_items,
                # Database filters:
                root_dir=root_dir,
                database=database,
                year_filter=year_filter,
                cited_by_filter=cited_by_filter,
                **filters,
            )
        else:
            return obj

    def compute_table(obj):
        """Melt the data"""

        table = obj.table_.copy()
        table["RANKING"] = range(1, len(table) + 1)
        table = table.melt(
            value_name="OCC",
            var_name="column",
            ignore_index=False,
            id_vars=["RANKING"],
        )

        table = table[table.OCC > 0]
        table = table.sort_values(by=["RANKING"], ascending=True)
        table = table.drop(columns=["RANKING"])

        table = table.rename(columns={"column": "Year"})
        table = table.reset_index()

        return table

    def create_fig(table, criterion, metric, title):
        """Create the figure"""

        fig = px.scatter(
            table,
            x="Year",
            y=criterion,
            size=metric,
            hover_data=table.columns.to_list(),
            title=title,
            color=criterion,
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            showlegend=False,
            xaxis_title=None,
            yaxis_title=criterion.replace("_", " ").upper(),
        )
        fig.update_traces(
            marker={
                # "line": {"color": COLOR, "width": 1},
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

    #
    # Main code:
    #
    if title is None:
        title = "Gantt Chart"

    obj = compute_obj(obj)
    table = compute_table(obj)
    fig = create_fig(table, obj.field_, obj.metric_, title)

    chart = BasicChart()
    chart.plot_ = fig
    chart.table_ = obj.table_
    chart.prompt_ = obj.prompt_

    return chart

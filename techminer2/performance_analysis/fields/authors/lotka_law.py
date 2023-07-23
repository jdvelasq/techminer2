# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Lotka's Law
===============================================================================


>>> from techminer2.performance_analysis.fields.authors import lotka_law
>>> lotka = lotka_law(
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=None,
...     cited_by_filter=None,
... )
>>> lotka.fig_.write_html("sphinx/_static/performance_analysis/fields/authors/lotka_law.html")

.. raw:: html

    <iframe src="../../../../_static/performance_analysis/fields/authors/lotka_law.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> print(lotka.df_.to_markdown())
|    |   Documents Written |   Num Authors |   Proportion of Authors |   Theoretical Num Authors |   Prop Theoretical Authors |
|---:|--------------------:|--------------:|------------------------:|--------------------------:|---------------------------:|
|  0 |                   1 |            87 |                   0.853 |                    87     |                      0.735 |
|  1 |                   2 |            13 |                   0.127 |                    21.75  |                      0.184 |
|  2 |                   3 |             2 |                   0.02  |                     9.667 |                      0.082 |


"""
from dataclasses import dataclass

import plotly.graph_objects as go


def lotka_law(
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Lotka's Law

    :meta private:
    """

    table = __core_authors_table(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    fig = __plot_lotka_law(table)

    @dataclass
    class Results:
        df_ = table
        fig_ = fig

    return Results()


def __plot_lotka_law(indicators):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=indicators["Documents Written"],
            y=indicators["Proportion of Authors"],
            fill="tozeroy",
            name="Real",
            opacity=0.5,
            marker_color="darkslategray",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=indicators["Documents Written"],
            y=indicators["Prop Theoretical Authors"],
            fill="tozeroy",
            name="Theoretical",
            opacity=0.5,
            marker_color="lightgrey",
        )
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title="Author Productivity through Lotka's Law",
    )

    fig.update_traces(
        marker=dict(
            size=7,
            line=dict(color="darkslategray", width=2),
        ),
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        title="Documents Written",
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        title="Proportion of Authors",
    )

    return fig


def __core_authors_table(
    #
    # DATABASE PARAMS:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    from ....techminer.metrics.global_indicators_by_field import global_indicators_by_field

    #
    # Part 1: Computes the number of written documents per number of authors.
    #         Read as: "178 authors write only 1 document and 1 author writes 7 documents"
    #
    #    Documents Written  Num Authors
    # 0                  1          178
    # 1                  2            9
    # 2                  3            2
    # 3                  4            2
    # 4                  6            1
    # 5                  7            1
    #
    indicators = global_indicators_by_field(
        field="authors",
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    indicators = indicators[["OCC"]]
    indicators = indicators.groupby(["OCC"], as_index=False).size()
    indicators.columns = ["Documents Written", "Num Authors"]
    indicators = indicators.sort_values(by="Documents Written", ascending=True)
    indicators = indicators.reset_index(drop=True)
    indicators = indicators[["Documents Written", "Num Authors"]]
    indicators["Proportion of Authors"] = (
        indicators["Num Authors"].map(lambda x: x / indicators["Num Authors"].sum()).round(3)
    )

    #
    # Part 2: Computes the theoretical number of authors
    #
    total_authors = indicators["Num Authors"].max()
    indicators["Theoretical Num Authors"] = (
        indicators["Documents Written"].map(lambda x: total_authors / float(x * x)).round(3)
    )
    total_theoretical_num_authors = indicators["Theoretical Num Authors"].sum()
    indicators["Prop Theoretical Authors"] = (
        indicators["Theoretical Num Authors"]
        .map(lambda x: x / total_theoretical_num_authors)
        .round(3)
    )

    return indicators

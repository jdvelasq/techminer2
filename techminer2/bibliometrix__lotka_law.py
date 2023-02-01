"""
Lotka's Law
===============================================================================



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__lotka_law.html"

>>> from techminer2 import bibliometrix__lotka_law
>>> bibliometrix__lotka_law(directory=directory).plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__lotka_law.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> bibliometrix__lotka_law(directory=directory).table_
   Documents Written  ...  Prop Theoretical Authors
0                  1  ...                     0.679
1                  2  ...                     0.170
2                  3  ...                     0.075
3                  4  ...                     0.042
4                  6  ...                     0.019
5                  7  ...                     0.014
<BLANKLINE>
[6 rows x 5 columns]

"""
from dataclasses import dataclass

import plotly.graph_objects as go

from .techminer2.indicators.tm2__indicators_by_topic import tm2__indicators_by_topic


@dataclass(init=False)
class _Results:
    plot_: None
    table_: None


def bibliometrix__lotka_law(
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Lotka's Law"""

    results = _Results()
    results.table_ = _core_authors(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    results.plot_ = _plot_lotka_law(results.table_)
    return results


def _plot_lotka_law(indicators):

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


def _core_authors(
    directory,
    database,
    start_year,
    end_year,
    **filters,
):

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
    indicators = tm2__indicators_by_topic(
        criterion="authors",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    indicators = indicators[["OCC"]]
    indicators = indicators.groupby(["OCC"], as_index=False).size()
    indicators.columns = ["Documents Written", "Num Authors"]
    indicators = indicators.sort_values(by="Documents Written", ascending=True)
    indicators = indicators.reset_index(drop=True)
    indicators = indicators[["Documents Written", "Num Authors"]]
    indicators["Proportion of Authors"] = (
        indicators["Num Authors"]
        .map(lambda x: x / indicators["Num Authors"].sum())
        .round(3)
    )

    #
    # Part 2: Computes the theoretical number of authors
    #
    total_authors = indicators["Num Authors"].max()
    indicators["Theoretical Num Authors"] = (
        indicators["Documents Written"]
        .map(lambda x: total_authors / float(x * x))
        .round(3)
    )
    total_theoretical_num_authors = indicators["Theoretical Num Authors"].sum()
    indicators["Prop Theoretical Authors"] = (
        indicators["Theoretical Num Authors"]
        .map(lambda x: x / total_theoretical_num_authors)
        .round(3)
    )

    return indicators

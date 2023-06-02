# flake8: noqa
"""
Bubble Chart
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__bubble_chart.html"


>>> from techminer2 import vantagepoint
>>> matrix = vantagepoint.analyze.co_occ_matrix(
...    columns='author_keywords',
...    col_occ_range=(4, None),
...    root_dir=root_dir,
... )

>>> chart = vantagepoint.report.bubble_chart(matrix)
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__bubble_chart.html" height="800px" width="100%" frameBorder="0"></iframe>

>>> chart.table_.head()
                 row             column  VALUE
0     regtech 28:329     regtech 28:329     28
1     fintech 12:249     fintech 12:249     12
2     fintech 12:249     regtech 28:329     12
3     regtech 28:329     fintech 12:249     12
4  compliance 07:030  compliance 07:030      7

>>> print(chart.prompt_)
Analyze the table below which contains values of co-occurrence (OCC) for the 'author_keywords' field in a bibliographic dataset. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row                            |   regtech 28:329 |   fintech 12:249 |   regulatory technology 07:037 |   compliance 07:030 |   regulation 05:164 |   financial services 04:168 |   financial regulation 04:035 |   artificial intelligence 04:023 |
|:-------------------------------|-----------------:|-----------------:|-------------------------------:|--------------------:|--------------------:|----------------------------:|------------------------------:|---------------------------------:|
| regtech 28:329                 |               28 |               12 |                              2 |                   7 |                   4 |                           3 |                             2 |                                2 |
| fintech 12:249                 |               12 |               12 |                              1 |                   2 |                   4 |                           2 |                             1 |                                1 |
| regulatory technology 07:037   |                2 |                1 |                              7 |                   1 |                   1 |                           0 |                             0 |                                1 |
| compliance 07:030              |                7 |                2 |                              1 |                   7 |                   1 |                           0 |                             0 |                                1 |
| regulation 05:164              |                4 |                4 |                              1 |                   1 |                   5 |                           1 |                             0 |                                0 |
| financial services 04:168      |                3 |                2 |                              0 |                   0 |                   1 |                           4 |                             2 |                                0 |
| financial regulation 04:035    |                2 |                1 |                              0 |                   0 |                   0 |                           2 |                             4 |                                0 |
| artificial intelligence 04:023 |                2 |                1 |                              1 |                   1 |                   0 |                           0 |                             0 |                                4 |
<BLANKLINE>
<BLANKLINE>

"""
import plotly.express as px

from ...classes import BasicChart


def bubble_chart(
    obj,
    title=None,
):
    """Makes a bubble chart."""

    matrix = obj.matrix_.copy()
    matrix = matrix.melt(
        value_name="VALUE", var_name="column", ignore_index=False
    )
    matrix = matrix.reset_index()
    matrix = matrix.rename(columns={"index": "row"})
    matrix = matrix.sort_values(
        by=["VALUE", "row", "column"], ascending=[False, True, True]
    )
    matrix = matrix.reset_index(drop=True)

    fig = px.scatter(
        matrix,
        x="row",
        y="column",
        size="VALUE",
        hover_data=matrix.columns.to_list(),
        title=title,
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        showlegend=False,
        yaxis_title=None,
        xaxis_title=None,
        margin=dict(l=1, r=1, t=1, b=1),
    )
    fig.update_traces(
        marker=dict(
            line=dict(
                color="black",
                width=2,
            ),
        ),
        marker_color="darkslategray",
        mode="markers",
    )
    fig.update_xaxes(
        side="top",
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
        autorange="reversed",
    )

    result = BasicChart()
    result.plot_ = fig
    result.table_ = matrix
    result.prompt_ = obj.prompt_

    return result

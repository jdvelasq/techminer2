# flake8: noqa
"""
.. _pie_chart:

Pie Chart
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/pie_chart.html"

>>> import techminer2plus
>>> itemslist = techminer2plus.list_items(
...    field='author_keywords',
...    root_dir=root_dir,
...    top_n=20,
... )
>>> chart = techminer2plus.pie_chart(itemslist, title="Most Frequent Author Keywords")
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/pie_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> chart.table_.head()
author_keywords
REGTECH                  28
FINTECH                  12
REGULATORY_TECHNOLOGY     7
COMPLIANCE                7
REGULATION                5
Name: OCC, dtype: int64




# pylint: disable=line-too-long
"""
from dataclasses import dataclass

import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


@dataclass
class PieChart:
    """Bar Chart.

    :meta private:
    """

    plot_: go.Figure
    table_: pd.DataFrame


def pie_chart(
    itemslist=None,
    title=None,
    hole=0.4,
):
    """Creates a pie chart.

    Args:
        obj (vantagepoint.analyze.list_view): A list view object.
        title (str, optional): Title. Defaults to None.
        hole (float, optional): Hole size. Defaults to 0.4.

    Returns:
        BasicChart: A BasicChart object.


    """

    fig = px.pie(
        itemslist.items_list_,
        values=itemslist.metric_,
        names=itemslist.items_list_.index.to_list(),
        hole=hole,
        hover_data=itemslist.items_list_.columns.to_list(),
        title=title if title is not None else "",
    )
    fig.update_traces(textinfo="percent+value")
    fig.update_layout(legend={"y": 0.5})

    return PieChart(
        plot_=fig,
        table_=itemslist.items_list_[itemslist.metric_],
    )

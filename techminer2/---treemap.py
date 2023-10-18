# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""
Treemap
===============================================================================


# >>> from techminer2.visualize import treemap
# >>> import techminer2plus
# >>> itemslist = techminer2plus.list_items(
# ...    field='author_keywords',
# ...    top_n=20,
# ...    root_dir=root_dir,
# ... )
# >>> chart = treemap(itemslist, title="Most Frequent Author Keywords")
# >>> chart.plot_.write_html(file_name)

# .. raw:: html

#     <iframe src="../_static/treemap.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from dataclasses import dataclass

import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


@dataclass
class Treemap:
    """Bar Chart.

    :meta private:
    """

    plot_: go.Figure
    table_: pd.DataFrame


def treemap(
    itemslist=None,
    title=None,
):
    """Creates a treemap.

    Args:
        obj (vantagepoint.analyze.list_view): A list view object.
        title (str, optional): Title. Defaults to None.

    Returns:
        BasicChart: A basic chart object.


    """
    fig = go.Figure()
    fig.add_trace(
        go.Treemap(
            labels=itemslist.df_.index,
            parents=[""] * len(itemslist.df_),
            values=itemslist.df_[itemslist.metric_],
            textinfo="label+value",
        )
    )
    fig.update_traces(marker={"cornerradius": 5})
    fig.update_layout(
        showlegend=False,
        margin={"t": 30, "l": 0, "r": 0, "b": 0},
        title=title if title is not None else "",
    )

    # Change the colors of the treemap white
    fig.update_traces(
        marker={"line": {"color": "darkslategray", "width": 1}},
        marker_colors=["white"] * len(itemslist.df_),
    )

    # Change the font size of the labels
    fig.update_traces(textfont_size=12)

    return Treemap(
        plot_=fig,
        table_=itemslist.df_[itemslist.metric_],
    )

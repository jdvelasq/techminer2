# flake8: noqa
"""
Treemap
===============================================================================



Example
-------------------------------------------------------------------------------


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__treemap.html"

>>> from techminer2 import vantagepoint
>>> obj = vantagepoint.analyze.list_view(
...    field='author_keywords',
...    root_dir=root_dir,
... )
>>> chart = vantagepoint.report.treemap(obj, title="Most Frequent Author Keywords")
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__treemap.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> chart.table_.head()    
author_keywords
regtech                  28
fintech                  12
regulatory technology     7
compliance                7
regulation                5
Name: OCC, dtype: int64

>>> print(chart.prompt_)
Analyze the table below, which provides bibliometric indicators for the field 'author_keywords' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| author_keywords         |   OCC |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |
|:------------------------|------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|
| regtech                 |    28 |                329 |                74 |                           11.75 |                           2.64 |
| fintech                 |    12 |                249 |                49 |                           20.75 |                           4.08 |
| regulatory technology   |     7 |                 37 |                14 |                            5.29 |                           2    |
| compliance              |     7 |                 30 |                 9 |                            4.29 |                           1.29 |
| regulation              |     5 |                164 |                22 |                           32.8  |                           4.4  |
| financial services      |     4 |                168 |                20 |                           42    |                           5    |
| financial regulation    |     4 |                 35 |                 8 |                            8.75 |                           2    |
| artificial intelligence |     4 |                 23 |                 6 |                            5.75 |                           1.5  |
| anti-money laundering   |     3 |                 21 |                 4 |                            7    |                           1.33 |
| risk management         |     3 |                 14 |                 8 |                            4.67 |                           2.67 |
<BLANKLINE>
<BLANKLINE>



# pylint: disable=line-too-long
"""
import plotly.graph_objs as go

from ...check_params import check_listview
from ...classes import BasicChart


def treemap(
    obj,
    title=None,
):
    """Creates a treemap.

    Args:
        obj (vantagepoint.analyze.list_view): A list view object.
        title (str, optional): Title. Defaults to None.

    Returns:
        BasicChart: A basic chart object.


    """

    def create_plot():
        """Creates a plotly treemap."""

        fig = go.Figure()
        fig.add_trace(
            go.Treemap(
                labels=obj.table_.index,
                parents=[""] * len(obj.table_),
                values=obj.table_[obj.metric_],
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
            marker_colors=["white"] * len(obj.table_),
        )

        # Change the font size of the labels
        fig.update_traces(textfont_size=12)

        return fig

    #
    # Main code:
    #

    check_listview(obj)

    chart = BasicChart()
    chart.plot_ = create_plot()
    chart.table_ = obj.table_[obj.metric_]
    chart.prompt_ = obj.prompt_

    return chart

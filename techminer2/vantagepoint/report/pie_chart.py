# flake8: noqa
"""
Pie Chart
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__pie_chart.html"

>>> from techminer2 import vantagepoint
>>> obj = vantagepoint.analyze.list_view(
...    field='author_keywords',
...    root_dir=root_dir,
...    top_n=10,
... )
>>> chart = vantagepoint.report.pie_chart(obj, title="Most Frequent Author Keywords")
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__pie_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

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
import plotly.express as px

from ...classes import BasicChart
from ...utils import check_listview


def pie_chart(
    obj,
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

    def create_plot():
        """Creates plotly figure"""

        fig = px.pie(
            obj.table_,
            values=obj.metric_,
            names=obj.table_.index.to_list(),
            hole=hole,
            hover_data=obj.table_.columns.to_list(),
            title=title if title is not None else "",
        )
        fig.update_traces(textinfo="percent+value")
        fig.update_layout(legend={"y": 0.5})

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

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Word Cloud
===============================================================================

>>> from techminer2.visualize.basic_charts.word_cloud import WordCloud
>>> plot = (
...     WordCloud()
...     .set_item_params(
...         field="title_nlp_phrases",
...         top_n=80,
...         occ_range=(None, None),
...         gc_range=(None, None),
...         custom_terms=None,
...     ).set_chart_params(
...         width=400, 
...         height=400,
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).build(metric="OCC")
... )
>>> # plot.save("sphinx/images/visualize/basic_charts/word_cloud.png")

.. image:: /images/visualize/basic_charts/word_cloud.png
    :width: 900px
    :align: center

"""
from dataclasses import dataclass

import numpy as np
from wordcloud import WordCloud as WordCloudExternal  # type: ignore

from ...analyze.metrics.performance_metrics_frame import performance_metrics_frame
from ...internals.params.database_params import DatabaseParams, DatabaseParamsMixin
from ...internals.params.item_params import ItemParams, ItemParamsMixin


@dataclass
class ChartParams:
    """:meta private:"""

    width: float = 400
    height: float = 400


class WordCloud(
    ItemParamsMixin,
    DatabaseParamsMixin,
):
    """:meta private:"""

    def __init__(self):
        self.chart_params = ChartParams()
        self.database_params = DatabaseParams()
        self.item_params = ItemParams()

    def set_chart_params(self, **kwars):
        for key, value in kwars.items():
            if hasattr(self.chart_params, key):
                setattr(self.chart_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for ChartParams: {key}")
        return self

    def build(self, metric: str = "OCC"):

        width = self.chart_params.width
        height = self.chart_params.height

        data_frame = performance_metrics_frame(
            metric=metric,
            **self.item_params.__dict__,
            **self.database_params.__dict__,
        )

        x_mask, y_mask = np.ogrid[:300, :300]
        mask = (x_mask - 150) ** 2 + (y_mask - 150) ** 2 > 130**2  #  type: ignore
        mask = 255 * mask.astype(int)  #  type: ignore

        wordcloud = WordCloudExternal(
            background_color="white",
            repeat=True,
            mask=mask,
            width=width,
            height=height,
        )

        text = dict(
            zip(
                data_frame.index,
                data_frame[metric],
            )
        )
        wordcloud.generate_from_frequencies(text)
        wordcloud.recolor(color_func=lambda word, **kwargs: "black")

        fig = wordcloud.to_image()

        return fig

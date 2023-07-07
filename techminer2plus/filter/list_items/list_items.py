# flake8: noqa
# pylint: disable=line-too-long
"""
.. _list_items:

List Items
===============================================================================




"""
import textwrap
from dataclasses import dataclass
from dataclasses import field as datafield
from typing import Optional

import pandas as pd

from ..._chatbot import format_chatbot_prompt_for_df
from ..._filtering_lib import generate_custom_items
from ..._metrics_lib import indicators_by_field
from ..._sorting_lib import sort_indicators_by_metric
from ...bar_chart import bar_chart
from ...cleveland_dot_chart import cleveland_dot_chart
from ...column_chart import column_chart
from ...line_chart import line_chart
from ...pie_chart import pie_chart
from ...ranking_chart import ranking_chart
from ...word_cloud import word_cloud
from ...world_map import world_map


# pylint: disable=too-many-instance-attributes
@dataclass
class ListItems:
    """List items."""

    #
    # DATA:
    records: pd.DataFrame
    stopwords: list

    #
    # PARAMS:
    field: str
    metric: str = "OCC"
    #
    # ITEM FILTERS:
    top_n: Optional[int] = None
    occ_range: tuple = (None, None)
    gc_range: tuple = (None, None)
    custom_items: list = datafield(default_factory=list)

    #
    # RESULTS:
    df_: pd.DataFrame = pd.DataFrame()
    prompt_: str = ""

    def __repr__(self):
        text = (
            "ListItems("
            f"field='{self.field}'"
            f", metric='{self.metric}'"
            f", top_n={self.top_n}"
            f", occ_range={self.occ_range}"
            f", gc_range={self.gc_range}"
            f", custom_items={self.custom_items}"
            ")"
        )

        return textwrap.fill(text, width=80, subsequent_indent="    ")

    def bar_chart(self, title=None, metric_label=None, field_label=None):
        """Bar chart interface."""

        return bar_chart(
            #
            # CHART PARAMS:
            self,
            title=title,
            metric_label=metric_label,
            field_label=field_label,
        )

    def cleveland_dot_chart(
        self, title=None, metric_label=None, field_label=None
    ):
        """Column chart interface."""

        return cleveland_dot_chart(
            #
            # CHART PARAMS:
            self,
            title=title,
            metric_label=metric_label,
            field_label=field_label,
        )

    def column_chart(self, title=None, metric_label=None, field_label=None):
        """Column chart interface."""

        return column_chart(
            #
            # CHART PARAMS:
            self,
            title=title,
            metric_label=metric_label,
            field_label=field_label,
        )

    def line_chart(self, title=None, metric_label=None, field_label=None):
        """Column chart interface."""

        return line_chart(
            #
            # CHART PARAMS:
            self,
            title=title,
            metric_label=metric_label,
            field_label=field_label,
        )

    def pie_chart(self, title=None, hole=0.4):
        """Column chart interface."""
        return pie_chart(
            #
            # CHART PARAMS:
            self,
            title=title,
            hole=hole,
        )

    def word_cloud(self, title=None, figsize=(10, 10)):
        """Word cloud interface."""
        return word_cloud(
            list_items=self,
            title=title,
            figsize=figsize,
        )

    def world_map(self, colormap="Blues", title=None):
        """World map interface."""
        return world_map(
            list_items=self,
            colormap=colormap,
            title=title,
        )

    # pylint: disable=too-many-arguments
    def ranking_chart(
        self,
        title=None,
        field_label=None,
        metric_label=None,
        textfont_size=10,
        marker_size=7,
        line_color="black",
        line_width=1.5,
        yshift=4,
    ):
        """World map interface."""
        return ranking_chart(
            list_items=self,
            title=title,
            field_label=field_label,
            metric_label=metric_label,
            textfont_size=textfont_size,
            marker_size=marker_size,
            line_color=line_color,
            line_width=line_width,
            yshift=yshift,
        )


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def list_items(
    #
    # ITEMS PARAMS:
    field,
    records,
    metric="OCC",
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
):
    """Returns a ItemList object with the extracted items of database field."""

    # pylint: disable=line-too-long
    def generate_prompt(field, metric, table):
        """Returns the prompt to be used in the chatbot."""

        main_text = (
            "Your task is to generate an analysis about the bibliometric indicators of the "
            f"'{field}' field in a scientific bibliography database. Summarize the table below, "
            f"sorted by the '{metric}' metric, and delimited by triple backticks, identify "
            "any notable patterns, trends, or outliers in the data, and discuss their "
            "implications for the research field. Be sure to provide a concise summary "
            "of your findings in no more than 150 words."
        )
        return format_chatbot_prompt_for_df(main_text, table.to_markdown())

    data_frame = indicators_by_field(
        field=field,
        records=records,
    )

    data_frame = sort_indicators_by_metric(data_frame, metric)

    if custom_items is None:
        if metric == "OCCGC":
            custom_items_occ = generate_custom_items(
                indicators=sort_indicators_by_metric(data_frame, "OCC"),
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

            custom_items_gc = generate_custom_items(
                indicators=sort_indicators_by_metric(
                    data_frame, "global_citations"
                ),
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

            custom_items = custom_items_occ[:]
            custom_items += [
                item
                for item in custom_items_gc
                if item not in custom_items_occ
            ]

        else:
            custom_items = generate_custom_items(
                indicators=data_frame,
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

    data_frame = data_frame[data_frame.index.isin(custom_items)]

    metric = "OCC" if metric == "OCCGC" else metric

    prompt = generate_prompt(field, metric, data_frame)

    return ListItems(
        #
        # PARAMETERS:
        field=field,
        metric=metric,
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # RESULTS:
        df_=data_frame,
        prompt_=prompt,
    )

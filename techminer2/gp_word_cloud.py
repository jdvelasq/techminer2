# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from wordcloud import WordCloud

from .performance_analysis.performance_metrics import performance_metrics


def gp_word_cloud(
    #
    # ITEMS PARAMS:
    field,
    metric="OCC",
    #
    # CHART PARAMS:
    width=400,
    height=400,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Creates a word cloud.

    :meta private:
    """

    items = performance_metrics(
        #
        # ITEMS PARAMS:
        field=field,
        metric=metric,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    data_frame = items.df_.copy()

    x_mask, y_mask = np.ogrid[:300, :300]
    mask = (x_mask - 150) ** 2 + (y_mask - 150) ** 2 > 130**2
    mask = 255 * mask.astype(int)

    wordcloud = WordCloud(
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

    # fig = Figure(figsize=figsize)
    # ax_ = fig.add_subplot(111)
    # ax_.imshow(wordcloud, interpolation="bilinear")
    # ax_.axis("off")
    # if title is not None:
    #     ax_.set_title(title)
    # fig.tight_layout(pad=0)
    # items.fig_ = fig

    items.fig_ = wordcloud.to_image()

    return items

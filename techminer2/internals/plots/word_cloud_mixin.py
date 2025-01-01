# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Word Cloud Mixin."""

from dataclasses import dataclass

import numpy as np
from wordcloud import WordCloud as WordCloudExternal  # type: ignore


@dataclass
class WordCloudParams:
    """:meta private:"""

    width: float = 400
    height: float = 400


class WordCloudMixin:

    def set_plot_params(self, **kwars):
        for key, value in kwars.items():
            if hasattr(self.plot_params, key):
                setattr(self.plot_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for WordCloudParams: {key}")
        return self

    def build_word_cloud(self, dataframe, values_col):

        width = self.plot_params.width
        height = self.plot_params.height

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
                dataframe.index,
                dataframe[values_col],
            )
        )
        wordcloud.generate_from_frequencies(text)
        wordcloud.recolor(color_func=lambda word, **kwargs: "black")

        fig = wordcloud.to_image()

        return fig

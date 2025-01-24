# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-few-public-methods
"""Word Cloud Mixin."""

import numpy as np
from wordcloud import WordCloud as WordCloudExternal  # type: ignore


class WordCloudMixin:

    def build_word_cloud(self, data_frame):

        width = self.params.width
        height = self.params.height

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
                data_frame[self.params.terms_order_by],
            )
        )
        wordcloud.generate_from_frequencies(text)
        wordcloud.recolor(color_func=lambda word, **kwargs: "black")

        fig = wordcloud.to_image()

        return fig

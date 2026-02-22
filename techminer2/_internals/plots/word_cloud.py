import numpy as np
from wordcloud import WordCloud as WordCloudExternal  # type: ignore


def word_cloud(params, dataframe):

    width = params.plot_width
    height = params.plot_height

    x_mask, y_mask = np.ogrid[:300, :300]
    mask = (x_mask - 150) ** 2 + (y_mask - 150) ** 2 > 130**2
    mask = 255 * mask.astype(int)

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
            dataframe[params.items_order_by.value],
        )
    )
    wordcloud.generate_from_frequencies(text)
    wordcloud.recolor(color_func=lambda word, **kwargs: "black")

    fig = wordcloud.to_image()

    return fig

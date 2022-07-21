"""
Top Trending Topics
===============================================================================

Extract and plot the top trending topics for the selected column using the 
average growth rate.



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/scientopy__top_trending_topics.html"

>>> from techminer2 import scientopy__top_trending_topics
>>> scientopy__top_trending_topics(
...     column="author_keywords",
...     top_n=20,
...     directory=directory,
... ).plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__top_trending_topics.html" height="600px" width="100%" frameBorder="0"></iframe>



>>> scientopy__top_trending_topics(
...     column='author_keywords',
...     directory=directory,
...     top_n=20,
... ).table_.head()
                     author_keywords  Average Growth Rate
0   wealthtech (wealth + technology)                  0.5
1                        text mining                  0.5
2   edutech (education + technology)                  0.5
3                           business                  0.5
4  register of processing activities                  0.5



"""
from dataclasses import dataclass

from .bar_px import bar_px
from .growth_indicators import growth_indicators


@dataclass(init=False)
class _Results:
    plot_: None
    table_: None


def scientopy__top_trending_topics(
    column,
    top_n=20,
    time_window=2,
    directory="./",
):

    indicators = growth_indicators(column, time_window=time_window, directory=directory)
    indicators = indicators.reset_index()
    indicators = indicators[[column, "average_growth_rate"]]
    indicators = indicators.sort_values("average_growth_rate", ascending=False)
    indicators = indicators.reset_index(drop=True)
    indicators = indicators.rename(
        columns={"average_growth_rate": "Average Growth Rate"}
    )

    results = _Results()
    results.table_ = indicators.copy()

    indicators = indicators.head(top_n)

    results.plot_ = bar_px(
        dataframe=indicators,
        x_label="Average Growth Rate",
        y_label=column,
        title="Top Trending Topics",
    )

    return results

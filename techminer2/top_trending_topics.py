"""
Top Trending Topics
===============================================================================

Extract and plot the top trending topics for the selected column using the 
average growth rate.


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/top_trending_topics.png"
>>> top_trending_topics(
...     column="author_keywords", 
...     top_n=20,
...     directory=directory,
... ).savefig(file_name)

.. image:: images/top_trending_topics.png
    :width: 700px
    :align: center


>>> top_trending_topics(
...     column='author_keywords',
...     directory=directory,
...     plot=False,
... ).head()
fintech                   21.5
financial technologies     4.0
financial inclusion        4.0
covid-19                   3.0
regulation                 2.5
Name: average_growth_rate, dtype: float64

"""

from .growth_indicators import growth_indicators
from .plots.bar_plot import bar_plot


def top_trending_topics(
    column,
    top_n=20,
    time_window=2,
    figsize=(6, 6),
    directory="./",
    plot=True,
):

    indicators = growth_indicators(column, time_window=time_window, directory=directory)
    indicators = indicators.average_growth_rate
    indicators = indicators.sort_values(ascending=False)

    if plot is False:
        return indicators

    indicators = indicators.head(top_n)

    return _hbar_chart(
        indicators,
        title="Top Trending Topics",
        xlabel="Average Growth Rate",
        ylabel=column,
        figsize=figsize,
    )

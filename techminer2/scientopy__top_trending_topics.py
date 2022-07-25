"""
Top Trending Topics
===============================================================================

Extract and plot the top trending topics for the selected column using the 
average growth rate.



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/scientopy__top_trending_topics.html"

>>> from techminer2 import scientopy__top_trending_topics
>>> scientopy__top_trending_topics(
...     criterion="author_keywords",
...     topics_length=20,
...     directory=directory,
...     start_year=2018,
...     end_year=2021,
... ).plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__top_trending_topics.html" height="600px" width="100%" frameBorder="0"></iframe>



>>> scientopy__top_trending_topics(
...     criterion='author_keywords',
...     directory=directory,
...     topics_length=20,
...     start_year=2018,
...     end_year=2021,
... ).table_.head()
           author_keywords  Average Growth Rate
0    regulatory technology                  2.0
1     financial technology                  1.0
2  artificial intelligence                  1.0
3                  regtech                  0.5
4               regulation                  0.5



"""
from dataclasses import dataclass

from techminer2.scientopy__bar import _filter_indicators

from ._indicators.growth_indicators_by_topic import growth_indicators_by_topic
from ._px.bar_px import bar_px


@dataclass(init=False)
class _Results:
    plot_: None
    table_: None


def scientopy__top_trending_topics(
    criterion,
    topics_length=20,
    time_window=2,
    directory="./",
    database="documents",
    custom_topics=None,
    start_year=None,
    end_year=None,
    **filters,
):
    """Top trending topics."""

    indicators = growth_indicators_by_topic(
        criterion,
        time_window=time_window,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    indicators = _filter_indicators(
        indicators=indicators,
        topics_length=topics_length,
        custom_topics=custom_topics,
    )

    indicators = indicators.reset_index()
    indicators = indicators[[criterion, "average_growth_rate"]]
    indicators = indicators.sort_values("average_growth_rate", ascending=False)
    indicators = indicators.reset_index(drop=True)
    indicators = indicators.rename(
        columns={"average_growth_rate": "Average Growth Rate"}
    )

    results = _Results()
    results.table_ = indicators.copy()

    indicators = indicators.head(topics_length)

    results.plot_ = bar_px(
        dataframe=indicators,
        x_label="Average Growth Rate",
        y_label=criterion,
        title="Top Trending Topics",
    )

    return results

"""
Top Trending Topics
===============================================================================

Extract and plot the top trending topics for the selected column using the 
average growth rate.



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/scientopy__top_trending_topics.html"

>>> from techminer2 import scientopy
>>> scientopy.top_trending_topics(
...     criterion="author_keywords",
...     topics_length=5,
...     directory=directory,
...     start_year=2018,
...     end_year=2021,
... ).plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__top_trending_topics.html" height="600px" width="100%" frameBorder="0"></iframe>



>>> scientopy.top_trending_topics(
...     criterion='author_keywords',
...     directory=directory,
...     topics_length=5,
...     start_year=2018,
...     end_year=2021,
... ).table_.head()
         author_keywords  Average Growth Rate
0  regulatory technology                  1.5
1  anti-money laundering                  1.0
2             regulation                  0.5
3         accountability                  0.5
4                   gdpr                  0.5



"""
from dataclasses import dataclass

from techminer2.scientopy.bar import _filter_indicators_by_custom_topics

from .._px.bar_px import bar_px
from ..tm2__growth_indicators_by_topic import tm2__growth_indicators_by_topic


@dataclass(init=False)
class _Results:
    plot_: None
    table_: None


def top_trending_topics(
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

    growth_indicators = tm2__growth_indicators_by_topic(
        criterion=criterion,
        time_window=time_window,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    growth_indicators = growth_indicators.sort_values(
        by=["average_growth_rate", "OCC", "global_citations"],
        ascending=[False, False, False],
    )

    growth_indicators = _filter_indicators_by_custom_topics(
        indicators=growth_indicators,
        topics_length=topics_length,
        custom_topics=custom_topics,
    )

    growth_indicators = growth_indicators.sort_values(
        by=["OCC", "global_citations", "average_growth_rate"],
        ascending=[False, False, False],
    )

    growth_indicators = growth_indicators.reset_index()
    growth_indicators = growth_indicators[[criterion, "average_growth_rate"]]
    growth_indicators = growth_indicators.sort_values(
        "average_growth_rate", ascending=False
    )
    growth_indicators = growth_indicators.reset_index(drop=True)
    growth_indicators = growth_indicators.rename(
        columns={"average_growth_rate": "Average Growth Rate"}
    )

    results = _Results()
    results.table_ = growth_indicators.copy()

    growth_indicators = growth_indicators.head(topics_length)

    results.plot_ = bar_px(
        dataframe=growth_indicators,
        x_label="Average Growth Rate",
        y_label=criterion,
        title="Top Trending Topics",
    )

    return results

"""
Top Trending Topics
===============================================================================

Extract and plot the top trending topics for the selected column using the 
average growth rate.



>>> directory = "data/regtech/"
>>> from techminer2 import scientopy

>>> file_name = "sphinx/_static/scientopy__top_trending_topics.html"
>>> r = scientopy.top_trending_topics(
...     criterion="author_keywords",
...     topics_length=5,
...     directory=directory,
...     start_year=2018,
...     end_year=2021,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__top_trending_topics.html" height="600px" width="100%" frameBorder="0"></iframe>



>>> r.table_.head()
         author_keywords  Average Growth Rate
0  regulatory technology                  1.5
1  anti-money laundering                  1.0
2             regulation                  0.5
3         accountability                  0.5
4                   gdpr                  0.5


>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top 5 'author_keywords' with the highest average growth rate in the dataset. Use the information in the table to draw conclusions about growth trends of the 'author_keywords'. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
|    | author_keywords       |   Average Growth Rate |
|---:|:----------------------|----------------------:|
|  0 | regulatory technology |                   1.5 |
|  1 | anti-money laundering |                   1   |
|  2 | regulation            |                   0.5 |
|  3 | accountability        |                   0.5 |
|  4 | gdpr                  |                   0.5 |
<BLANKLINE>
<BLANKLINE>

"""
from dataclasses import dataclass

from techminer2.scientopy.bar import _filter_indicators_by_custom_topics

from .._px.bar_px import bar_px
from ..techminer.indicators.growth_indicators_by_topic import growth_indicators_by_topic


@dataclass(init=False)
class _Results:
    plot_: None
    table_: None
    prompt_: None


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

    growth_indicators = growth_indicators_by_topic(
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
    results.table_ = growth_indicators.head(topics_length)
    results.plot_ = bar_px(
        dataframe=results.table_,
        x_label="Average Growth Rate",
        y_label=criterion,
        title="Top Trending Topics",
    )
    results.prompt_ = _create_prompt(results.table_, criterion)

    return results


def _create_prompt(table, criterion):
    return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. \
The table below provides data on top {int(table.shape[0])} '{criterion}' \
with the highest average growth rate in the dataset. \
Use the information in the table to draw conclusions about growth trends of the '{criterion}'. \
In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you \
observe, and identify any outliers or anomalies in the data. \
Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}

"""

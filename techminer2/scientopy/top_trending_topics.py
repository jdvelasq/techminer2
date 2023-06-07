# flake8: noqa
"""
Top Trending Topics
===============================================================================

Extract and plot the top trending topics for the selected column using the 
average growth rate.



>>> root_dir = "data/regtech/"
>>> from techminer2 import scientopy

>>> file_name = "sphinx/_static/scientopy__top_trending_topics.html"
>>> r = scientopy.top_trending_topics(
...     field="author_keywords",
...     top_n=5,
...     root_dir=root_dir,
...     year_filter=(2018, 2021),
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__top_trending_topics.html" height="600px" width="100%" frameBorder="0"></iframe>



>>> r.table_.head()
                   author_keywords  Average Growth Rate
0            ANTI_MONEY_LAUNDERING                  1.5
1  REGULATORY_TECHNOLOGY (REGTECH)                  1.0
2                       REGULATION                  0.5
3                   ACCOUNTABILITY                  0.5
4                             GDPR                  0.5


>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top 5 'author_keywords' with the highest average growth rate in the dataset. Use the information in the table to draw conclusions about growth trends of the 'author_keywords'. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
|    | author_keywords                 |   Average Growth Rate |
|---:|:--------------------------------|----------------------:|
|  0 | ANTI_MONEY_LAUNDERING           |                   1.5 |
|  1 | REGULATORY_TECHNOLOGY (REGTECH) |                   1   |
|  2 | REGULATION                      |                   0.5 |
|  3 | ACCOUNTABILITY                  |                   0.5 |
|  4 | GDPR                            |                   0.5 |
<BLANKLINE>
<BLANKLINE>



# pylint: disable=line-too-long
"""
from dataclasses import dataclass

from techminer2.scientopy.bar import _filter_indicators_by_custom_topics

from .._px.bar_px import bar_px
from ..techminer.indicators.growth_indicators_by_topic import (
    growth_indicators_by_topic,
)


@dataclass(init=False)
class _Results:
    plot_: None
    table_: None
    prompt_: None


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def top_trending_topics(
    field,
    # Specific params:
    time_window=2,
    # Item filters:
    top_n=20,
    custom_items=None,
    # Database params:
    root_dir="./",
    database="documents",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Top trending topics."""

    growth_indicators = growth_indicators_by_topic(
        field=field,
        time_window=time_window,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    growth_indicators = growth_indicators.sort_values(
        by=["average_growth_rate", "OCC", "global_citations"],
        ascending=[False, False, False],
    )

    growth_indicators = _filter_indicators_by_custom_topics(
        indicators=growth_indicators,
        topics_length=top_n,
        custom_topics=custom_items,
    )

    growth_indicators = growth_indicators.sort_values(
        by=["OCC", "global_citations", "average_growth_rate"],
        ascending=[False, False, False],
    )

    growth_indicators = growth_indicators.reset_index()
    growth_indicators = growth_indicators[[field, "average_growth_rate"]]
    growth_indicators = growth_indicators.sort_values(
        "average_growth_rate", ascending=False
    )
    growth_indicators = growth_indicators.reset_index(drop=True)
    growth_indicators = growth_indicators.rename(
        columns={"average_growth_rate": "Average Growth Rate"}
    )

    results = _Results()
    results.table_ = growth_indicators.head(top_n)
    results.plot_ = bar_px(
        dataframe=results.table_,
        x_label="Average Growth Rate",
        y_label=field,
        title="Top Trending Topics",
    )
    results.prompt_ = _create_prompt(results.table_, field)

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

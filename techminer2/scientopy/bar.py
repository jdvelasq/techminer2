"""
Bar
===============================================================================






**Basic Usage.**

>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/scientopy__bar-1.html"

>>> from techminer2 import scientopy
>>> scientopy.bar(
...    criterion='author_keywords',
...    directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-1.html" height="600px" width="100%" frameBorder="0"></iframe>


**Time Filter.**

>>> file_name = "sphinx/_static/scientopy__bar-3.html"
>>> from techminer2 import scientopy
>>> scientopy.bar(
...     criterion='author_keywords',
...     start_year=2018,
...     end_year=2021,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-3.html" height="600px" width="100%" frameBorder="0"></iframe>


**Custom Topics Extraction.**

>>> file_name = "sphinx/_static/scientopy__bar-4.html"
>>> from techminer2 import scientopy
>>> scientopy.bar(
...     criterion='author_keywords',
...     custom_topics=[
...         "fintech", 
...         "blockchain", 
...         "financial regulation", 
...         "machine learning",
...         "big data",
...         "cryptocurrency",
...     ],
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-4.html" height="600px" width="100%" frameBorder="0"></iframe>



**Filters.**

>>> file_name = "sphinx/_static/scientopy__bar-5.html"
>>> from techminer2 import scientopy
>>> scientopy.bar(
...     criterion='countries',
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-5.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> file_name = "sphinx/_static/scientopy__bar-6.html"
>>> from techminer2 import scientopy
>>> scientopy.bar(
...     criterion='countries',
...     directory=directory,
...     countries=['Australia', 'United Kingdom', 'United States'],
... ).write_html(file_name)



.. raw:: html

    <iframe src="../_static/scientopy__bar-6.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> file_name = "sphinx/_static/scientopy__bar-7.html"
>>> from techminer2 import scientopy
>>> scientopy.bar(
...     criterion='author_keywords',
...     directory=directory,
...     topics_length=5,
...     trend_analysis=True,
...     start_year=2018,
...     end_year=2021,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-7.html" height="600px" width="100%" frameBorder="0"></iframe>



"""
from .._plots.bar_plot import bar_plot
from ..tm2.indicators.tm2__growth_indicators_by_topic import (
    tm2__growth_indicators_by_topic,
)


def bar(
    criterion,
    time_window=2,
    topics_length=20,
    custom_topics=None,
    trend_analysis=False,
    title=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """ScientoPy Bar Plot."""

    growth_indicators = tm2__growth_indicators_by_topic(
        criterion=criterion,
        time_window=time_window,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    if trend_analysis is True:
        growth_indicators = growth_indicators.sort_values(
            by=["average_growth_rate", "OCC", "global_citations"],
            ascending=[False, False, False],
        )
    else:
        growth_indicators = growth_indicators.sort_values(
            by=["OCC", "global_citations", "average_growth_rate"],
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

    return bar_plot(
        dataframe=growth_indicators,
        metric="OCC",
        title=title,
    )


def _filter_indicators_by_custom_topics(indicators, topics_length, custom_topics):
    indicators = indicators.copy()
    if custom_topics is not None:
        custom_topics = [
            topic for topic in custom_topics if topic in indicators.index.tolist()
        ]
    else:
        custom_topics = indicators.index.copy()
        custom_topics = custom_topics[:topics_length]

    indicators = indicators.loc[custom_topics, :]

    return indicators

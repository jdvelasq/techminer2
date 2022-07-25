"""
Bar
===============================================================================


**Basic Usage.**

>>> directory = "data/regtech/"

>>> file_name = "sphinx/_static/scientopy__bar-1.html"
>>> from techminer2 import scientopy__bar
>>> scientopy__bar(
...    criterion='author_keywords',
...    directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-1.html" height="600px" width="100%" frameBorder="0"></iframe>


**Time Filter.**

>>> file_name = "sphinx/_static/scientopy__bar-3.html"
>>> from techminer2 import scientopy__bar
>>> scientopy__bar(
...     criterion='author_keywords',
...     start_year=2018,
...     end_year=2021,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-3.html" height="600px" width="100%" frameBorder="0"></iframe>


**Custom Topics Extraction.**

>>> file_name = "sphinx/_static/scientopy__bar-4.html"
>>> from techminer2 import scientopy__bar
>>> scientopy__bar(
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
>>> from techminer2 import scientopy__bar
>>> scientopy__bar(
...     criterion='countries',
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-5.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> file_name = "sphinx/_static/scientopy__bar-6.html"
>>> from techminer2 import scientopy__bar
>>> scientopy__bar(
...     criterion='countries',
...     directory=directory,
...     countries=['United States'],
... ).write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-6.html" height="600px" width="100%" frameBorder="0"></iframe>



"""
from ._indicators.indicators_by_topic import indicators_by_topic
from ._plots.bar_plot import bar_plot


def scientopy__bar(
    criterion,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    topics_length=20,
    custom_topics=None,
    title=None,
    **filters
):
    """ScientoPy Bar Plot."""

    indicators = indicators_by_topic(
        criterion=criterion,
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

    return bar_plot(
        dataframe=indicators,
        metric="OCC",
        title=title,
    )


def _filter_indicators(indicators, topics_length, custom_topics):
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

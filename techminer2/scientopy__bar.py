"""
Bar
===============================================================================


**Basic Usage.**

>>> directory = "data/regtech/"

>>> file_name = "sphinx/_static/scientopy__bar-1.html"
>>> from techminer2 import scientopy__bar
>>> scientopy__bar(
...    column='author_keywords',
...    directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-1.html" height="600px" width="100%" frameBorder="0"></iframe>


**'skip_first' argument.**

>>> file_name = "sphinx/_static/scientopy__bar-2.html"
>>> from techminer2 import scientopy__bar
>>> scientopy__bar(
...     column='author_keywords',
...     skip_first=2,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__bar-2.html" height="600px" width="100%" frameBorder="0"></iframe>


**Time Filter.**

>>> file_name = "sphinx/_static/scientopy__bar-3.html"
>>> from techminer2 import scientopy__bar
>>> scientopy__bar(
...     column='author_keywords',
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
...     column='author_keywords',
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


"""
from ._indicators.column_indicators import _column_indicators_from_records
from ._plots.bar_plot import bar_plot
from ._read_records import read_records


def scientopy__bar(
    column,
    start_year=None,
    end_year=None,
    topics_length=20,
    skip_first=0,
    custom_topics=None,
    title=None,
    directory="./",
    database="documents",
):
    """ScientoPy Bar Plot."""

    indicators = _compute_indicators(
        directory=directory,
        column=column,
        database=database,
        start_year=start_year,
        end_year=end_year,
    )

    indicators = _filter_indicators(
        indicators=indicators,
        topics_length=topics_length,
        skip_first=skip_first,
        custom_topics=custom_topics,
    )

    return bar_plot(
        dataframe=indicators,
        metric="OCC",
        title=title,
    )


def _filter_indicators(indicators, topics_length, skip_first, custom_topics):
    indicators = indicators.copy()
    if custom_topics is not None:
        custom_topics = [
            topic for topic in custom_topics if topic in indicators.index.tolist()
        ]
    else:
        custom_topics = indicators.index.copy()
        if skip_first > 0:
            custom_topics = custom_topics[skip_first:]
        custom_topics = custom_topics[:topics_length]

    indicators = indicators.loc[custom_topics, :]

    return indicators


def _compute_indicators(directory, column, database, start_year, end_year):
    indicators = read_records(directory=directory, database=database, use_filter=False)
    if start_year is not None:
        indicators = indicators[indicators.year >= start_year]
    if end_year is not None:
        indicators = indicators[indicators.year <= end_year]
    indicators = _column_indicators_from_records(column, indicators)
    return indicators

"""
Most Frequent Words
===============================================================================



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_frequent_words.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.words.most_frequent_words(
...     criterion="author_keywords",
...     directory=directory,
...     topics_length=20,
...     plot="cleveland",
...     database="documents",
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_frequent_words.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()
author_keywords
regtech                  12
regulatory technology     4
fintech                   3
financial regulation      3
sandbox                   2
Name: OCC, dtype: int64


>>> print(r.prompt_)
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top 20 author_keywords with highest frequency. The column 'OCC' represents the number of documents on which each item in 'author_keywords' appears. Use the the information in the table to draw conclusions about the frequency of the author_keywords. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
| author_keywords            |   OCC |
|:---------------------------|------:|
| regtech                    |    12 |
| regulatory technology      |     4 |
| fintech                    |     3 |
| financial regulation       |     3 |
| sandbox                    |     2 |
| innovation                 |     2 |
| financial services         |     2 |
| regulation                 |     2 |
| blockchain                 |     2 |
| reporting                  |     2 |
| suptech                    |     2 |
| compliance                 |     2 |
| china                      |     1 |
| financial development      |     1 |
| smart treasury             |     1 |
| regulations and compliance |     1 |
| coronavirus                |     1 |
| digital technologies       |     1 |
| resale price maintenance   |     1 |
| competition law            |     1 |
<BLANKLINE>
<BLANKLINE>


"""
from ...vantagepoint.report.chart import chart


def most_frequent_words(
    criterion="author_keywords",
    directory="./",
    topics_length=20,
    topic_min_occ=None,
    topic_min_citations=None,
    plot="cleveland",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Plots the number of documents by country using the specified plot."""

    obj = chart(
        criterion=criterion,
        directory=directory,
        database=database,
        metric="OCC",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=None,
        title="Most Frequent Keywords",
        plot=plot,
        **filters,
    )

    obj.prompt_ = _create_prompt(obj.table_, criterion)

    return obj


def _create_prompt(table, criterion):
    return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on top {table.shape[0]} {criterion} with highest \
frequency. The column 'OCC' represents the number of documents on which \
each item in '{criterion}' appears. \
Use the the information in the table to draw conclusions about the frequency \
of the {criterion}. In your analysis, be sure to describe in a clear and \
concise way, any findings or any patterns you observe, and identify any \
outliers or anomalies in the data. Limit your description to one paragraph \
with no more than 250 words.

{table.to_markdown()}

"""

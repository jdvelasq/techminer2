"""
Column chart
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__column_chart.html"

>>> from techminer2 import vantagepoint
>>> r = vantagepoint.report.column_chart(
...     criterion='author_keywords',
...     topics_length=15,
...     directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__column_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> print(r.prompt_)
<BLANKLINE>
Act as a researcher realizing a bibliometric analysis. Analyze the following 
table, which provides data corresponding to the top 15
author_keywords with more OCC in a given bibliographic dataset. 
<BLANKLINE>
- 'OCC' is the number of documents published.  
<BLANKLINE>
- 'local_citations' are the local citations in the dataset.
<BLANKLINE>
- 'global_citations' are the citations received 
<BLANKLINE>
| author_keywords         |   OCC |
|:------------------------|------:|
| regtech                 |    28 |
| fintech                 |    12 |
| regulatory technology   |     7 |
| compliance              |     7 |
| regulation              |     5 |
| financial services      |     4 |
| financial regulation    |     4 |
| artificial intelligence |     4 |
| anti-money laundering   |     3 |
| risk management         |     3 |
| innovation              |     3 |
| blockchain              |     3 |
| suptech                 |     3 |
| semantic technologies   |     2 |
| data protection         |     2 |
<BLANKLINE>
Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice. 
<BLANKLINE>
Limit your description to a paragraph with no more than 250 words.        
<BLANKLINE>
<BLANKLINE>


"""
from .chart import chart


def column_chart(
    criterion,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    topics_length=20,
    topic_min_occ=None,
    topic_min_citations=None,
    custom_topics=None,
    title=None,
    **filters
):
    """Plots a bar chart from a column of a dataframe."""

    return chart(
        criterion=criterion,
        directory=directory,
        database=database,
        metric="OCC",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=custom_topics,
        title=title,
        plot="column",
        **filters,
    )

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
regtech                  28
fintech                  12
regulatory technology     7
compliance                7
regulation                5
Name: OCC, dtype: int64

>>> print(r.prompt_)
<BLANKLINE>
Act as a researcher realizing a bibliometric analysis. Analyze the following 
table, which provides data corresponding to the top 20
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
| smart contracts         |     2 |
| charitytech             |     2 |
| english law             |     2 |
| gdpr                    |     2 |
| data protection officer |     2 |
<BLANKLINE>
Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice. 
<BLANKLINE>
Limit your description to a paragraph with no more than 250 words.        
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
        custom_topics=None,
        title="Most Frequent Keywords",
        plot=plot,
        **filters,
    )

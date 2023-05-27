"""
List View --- ChatGPT
===============================================================================


>>> root_dir = "data/regtech/"


>>> from techminer2 import vantagepoint
>>> r = vantagepoint.analyze.list_view(
...    criterion='author_keywords',
...    root_dir=root_dir,
... )
>>> r.table_.head()
                       OCC  ...  local_citations_per_document
author_keywords             ...                              
regtech                 28  ...                          2.64
fintech                 12  ...                          4.08
regulatory technology    7  ...                          2.00
compliance               7  ...                          1.29
regulation               5  ...                          4.40
<BLANKLINE>
[5 rows x 5 columns]



>>> print(r.table_.head().to_markdown())
| author_keywords       |   OCC |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |
|:----------------------|------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|
| regtech               |    28 |                329 |                74 |                           11.75 |                           2.64 |
| fintech               |    12 |                249 |                49 |                           20.75 |                           4.08 |
| regulatory technology |     7 |                 37 |                14 |                            5.29 |                           2    |
| compliance            |     7 |                 30 |                 9 |                            4.29 |                           1.29 |
| regulation            |     5 |                164 |                22 |                           32.8  |                           4.4  |

>>> print(r.prompt_)
Analyze the table below, which provides bibliographic indicators for a collection of research articles. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| author_keywords         |   OCC |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |
|:------------------------|------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|
| regtech                 |    28 |                329 |                74 |                           11.75 |                           2.64 |
| fintech                 |    12 |                249 |                49 |                           20.75 |                           4.08 |
| regulatory technology   |     7 |                 37 |                14 |                            5.29 |                           2    |
| compliance              |     7 |                 30 |                 9 |                            4.29 |                           1.29 |
| regulation              |     5 |                164 |                22 |                           32.8  |                           4.4  |
| financial services      |     4 |                168 |                20 |                           42    |                           5    |
| financial regulation    |     4 |                 35 |                 8 |                            8.75 |                           2    |
| artificial intelligence |     4 |                 23 |                 6 |                            5.75 |                           1.5  |
| anti-money laundering   |     3 |                 21 |                 4 |                            7    |                           1.33 |
| risk management         |     3 |                 14 |                 8 |                            4.67 |                           2.67 |
| innovation              |     3 |                 12 |                 4 |                            4    |                           1.33 |
| blockchain              |     3 |                  5 |                 0 |                            1.67 |                           0    |
| suptech                 |     3 |                  4 |                 2 |                            1.33 |                           0.67 |
| semantic technologies   |     2 |                 41 |                19 |                           20.5  |                           9.5  |
| data protection         |     2 |                 27 |                 5 |                           13.5  |                           2.5  |
| smart contracts         |     2 |                 22 |                 8 |                           11    |                           4    |
| charitytech             |     2 |                 17 |                 4 |                            8.5  |                           2    |
| english law             |     2 |                 17 |                 4 |                            8.5  |                           2    |
| gdpr                    |     2 |                 14 |                 3 |                            7    |                           1.5  |
| data protection officer |     2 |                 14 |                 3 |                            7    |                           1.5  |
<BLANKLINE>
<BLANKLINE>

"""


from ... import chatgpt, techminer
from ...classes import ListView
from ...custom_topics import generate_custom_topics
from ...sort_indicators import sort_indicators_by_metric


def list_view(
    criterion,
    root_dir="./",
    database="documents",
    metric="OCC",
    start_year=None,
    end_year=None,
    topics_length=20,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    custom_topics=None,
    **filters,
):
    """Returns a dataframe with the extracted topics.

    Args:
        criterion (str): Criterion to be used to extract the topics.
        root_dir (str): Root directory.
        database (str): Database name.
        metric (str): Metric to be used to sort the topics.
        start_year (int): Start year.
        end_year (int): End year.
        topics_length (int): Number of topics to be extracted.
        topic_min_occ (int): Minimum number of occurrences of the topic.
        topic_max_occ (int): Maximum number of occurrences of the topic.
        topic_min_citations (int): Minimum number of citations of the topic.
        topic_max_citations (int): Maximum number of citations of the topic.
        custom_topics (list): List of custom topics.
        **filters: Filters.

    Returns:
        A ListView object.

    """

    indicators = techminer.indicators.indicators_by_topic(
        criterion=criterion,
        root_dir=root_dir,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    indicators = sort_indicators_by_metric(indicators, metric)

    if custom_topics is None:
        custom_topics = generate_custom_topics(
            indicators=indicators,
            topics_length=topics_length,
            topic_min_occ=topic_min_occ,
            topic_max_occ=topic_max_occ,
            topic_min_citations=topic_min_citations,
            topic_max_citations=topic_max_citations,
        )

    indicators = indicators[indicators.index.isin(custom_topics)]

    results = ListView()
    results.table_ = indicators
    results.prompt_ = chatgpt.generate_prompt_bibliographic_indicators(
        results.table_
    )
    results.metric_ = metric
    results.criterion_ = criterion

    return results

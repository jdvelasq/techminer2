"""
Extract topics (equivalent to `List View` in VantagePoint).
===============================================================================


>>> directory = "data/regtech/"


>>> from techminer2 import vantagepoint
>>> r = vantagepoint.analyze.extract_topics(
...    criterion='author_keywords',
...    directory=directory,
... )
>>> r.table_.head()
                       OCC  ...  local_citations_per_document
author_keywords             ...                              
regtech                 28  ...                             2
fintech                 12  ...                             4
regulatory technology    7  ...                             2
compliance               7  ...                             1
regulation               5  ...                             4
<BLANKLINE>
[5 rows x 5 columns]



>>> print(r.table_.head().to_markdown())
| author_keywords       |   OCC |   local_citations |   global_citations |   global_citations_per_document |   local_citations_per_document |
|:----------------------|------:|------------------:|-------------------:|--------------------------------:|-------------------------------:|
| regtech               |    28 |                74 |                329 |                              11 |                              2 |
| fintech               |    12 |                49 |                249 |                              20 |                              4 |
| regulatory technology |     7 |                14 |                 37 |                               5 |                              2 |
| compliance            |     7 |                 9 |                 30 |                               4 |                              1 |
| regulation            |     5 |                22 |                164 |                              32 |                              4 |


>>> print(r.prompt_)
Analyze the table below, which provides bibliographic indicators for a collection of research articles. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| author_keywords         |   OCC |   local_citations |   global_citations |   global_citations_per_document |   local_citations_per_document |
|:------------------------|------:|------------------:|-------------------:|--------------------------------:|-------------------------------:|
| regtech                 |    28 |                74 |                329 |                              11 |                              2 |
| fintech                 |    12 |                49 |                249 |                              20 |                              4 |
| regulatory technology   |     7 |                14 |                 37 |                               5 |                              2 |
| compliance              |     7 |                 9 |                 30 |                               4 |                              1 |
| regulation              |     5 |                22 |                164 |                              32 |                              4 |
| financial services      |     4 |                20 |                168 |                              42 |                              5 |
| financial regulation    |     4 |                 8 |                 35 |                               8 |                              2 |
| artificial intelligence |     4 |                 6 |                 23 |                               5 |                              1 |
| anti-money laundering   |     3 |                 4 |                 21 |                               7 |                              1 |
| risk management         |     3 |                 8 |                 14 |                               4 |                              2 |
| innovation              |     3 |                 4 |                 12 |                               4 |                              1 |
| blockchain              |     3 |                 0 |                  5 |                               1 |                              0 |
| suptech                 |     3 |                 2 |                  4 |                               1 |                              0 |
| semantic technologies   |     2 |                19 |                 41 |                              20 |                              9 |
| data protection         |     2 |                 5 |                 27 |                              13 |                              2 |
| smart contracts         |     2 |                 8 |                 22 |                              11 |                              4 |
| charitytech             |     2 |                 4 |                 17 |                               8 |                              2 |
| english law             |     2 |                 4 |                 17 |                               8 |                              2 |
| gdpr                    |     2 |                 3 |                 14 |                               7 |                              1 |
| data protection officer |     2 |                 3 |                 14 |                               7 |                              1 |
<BLANKLINE>
<BLANKLINE>


"""
from dataclasses import dataclass

from ... import chatgpt, techminer


def extract_topics(
    criterion,
    directory="./",
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
    """Returns a dataframe with the topics extracted from the specified criterion.

    Parameters
    ----------
    criterion : str
        Criterion to be used to extract topics. Corresponds to one of columns of the database.

    directory : str
        Root directory of the project.

    database : ``{"documents", "references", "cited_by"}``, default="documents"``
        Name of the database to be used.

    metric :  ``{"OCC", "global_citations", "local_citations"}``, default="documents"``
        Metric to be used to sort the topics.

    start_year : int, optional
        Start year. Used to filter the database.

    end_year : int, optional
        End year. Used to filter the database.

    topics_length : int, default=20
        Number of topics to be extracted.

    topic_min_occ : int, optional
        Minimum number of occurrences of the topic.

    topic_max_occ : int, optional
        Maximum number of occurrences of the topic.

    topic_min_citations : int, optional
        Minimum number of citations of the topic.

    topic_max_citations : int, optional
        Maximum number of citations of the topic.

    custom_topics : list of str, optional
        List of topics to be extracted.

    filters : dictionary of ``{criterion : list of values}``, optional
        dictionary of filters to be applied to the database.

    Returns
    -------
    ExtractTopicsResult
        A dataclass with the following attributes:

        table_ : pandas.DataFrame
            Table with the extracted topics.

        prompt_ : str
            ChatGPT prompt to be used to generate the analysis report.

        metric_ : str
            Metric used to sort the topics.

    """

    indicators = techminer.indicators.indicators_by_topic(
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    indicators = _sort_indicators(indicators, metric)

    if custom_topics is None:
        custom_topics = _generate_custom_topics(
            topics_length,
            topic_min_occ,
            topic_max_occ,
            topic_min_citations,
            topic_max_citations,
            indicators,
        )
    else:
        custom_topics = _filter_custom_topics(indicators, custom_topics)

    indicators = indicators.loc[custom_topics, :]

    results = _ExtractTopicsResult()
    results.table_ = indicators
    results.prompt_ = chatgpt.generate_prompt(results.table_)
    results.metric_ = metric
    results.criterion_ = criterion

    return results


def _filter_custom_topics(indicators, custom_topics):
    custom_topics = [
        topic for topic in custom_topics if topic in indicators.index.tolist()
    ]
    return custom_topics


def _generate_custom_topics(
    topics_length,
    topic_min_occ,
    topic_max_occ,
    topic_min_citations,
    topic_max_citations,
    indicators,
):
    custom_topics = indicators.copy()
    if topic_min_occ is not None:
        custom_topics = custom_topics[custom_topics["OCC"] >= topic_min_occ]
    if topic_max_occ is not None:
        custom_topics = custom_topics[custom_topics["OCC"] <= topic_max_occ]
    if topic_min_citations is not None:
        custom_topics = custom_topics[
            custom_topics["global_citations"] >= topic_min_citations
        ]
    if topic_max_citations is not None:
        custom_topics = custom_topics[
            custom_topics["global_citations"] <= topic_max_citations
        ]
    custom_topics = custom_topics.index.copy()
    custom_topics = custom_topics[:topics_length]
    return custom_topics


# Sort the indicators dataframe based on the given metric (OCC, local_citations, or global_citations).
def _sort_indicators(indicators, metric):
    # Define the columns to sort by for each metric, and whether to sort ascending or descending.
    if metric == "OCC":
        columns = ["OCC", "global_citations", "local_citations"]
        ascending = [False, False, False]
    if metric == "global_citations":
        columns = ["global_citations", "local_citations", "OCC"]
        ascending = [False, False, False]
    if metric == "local_citations":
        columns = ["local_citations", "global_citations", "OCC"]
        ascending = [False, False, False]

    # Sort the indicators dataframe based on the given columns and sort order.
    indicators = indicators.sort_values(columns, ascending=ascending)

    return indicators


@dataclass(init=False)
class _ExtractTopicsResult:
    """Results of the extract_topics function."""

    table_: None  # pandas.DataFrame
    prompt_: None  # str
    metric_: None  # str
    criterion_: None  # str

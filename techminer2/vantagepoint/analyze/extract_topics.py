"""
Extract topics (equivalent to `List View` in VantagePoint).
===============================================================================


>>> directory = "data/regtech/"


>>> from techminer2 import vantagepoint
>>> r = vantagepoint.analyze.extract_topics(
...    criterion='author_keywords',
...    directory=directory,
... )
>>> r.head()
                       OCC  ...  local_citations_per_document
author_keywords             ...                              
regtech                 28  ...                             2
fintech                 12  ...                             4
regulatory technology    7  ...                             2
compliance               7  ...                             1
regulation               5  ...                             4
<BLANKLINE>
[5 rows x 5 columns]



>>> print(r.head().to_markdown())
| author_keywords       |   OCC |   local_citations |   global_citations |   global_citations_per_document |   local_citations_per_document |
|:----------------------|------:|------------------:|-------------------:|--------------------------------:|-------------------------------:|
| regtech               |    28 |                74 |                329 |                              11 |                              2 |
| fintech               |    12 |                49 |                249 |                              20 |                              4 |
| regulatory technology |     7 |                14 |                 37 |                               5 |                              2 |
| compliance            |     7 |                 9 |                 30 |                               4 |                              1 |
| regulation            |     5 |                22 |                164 |                              32 |                              4 |

"""
from ... import techminer


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
    """Creates a list of terms with indicators."""

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

    return indicators


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

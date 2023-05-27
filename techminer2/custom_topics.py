"""
Checks custom topics
"""


def generate_custom_topics(
    indicators,
    topics_length,
    topic_min_occ,
    topic_max_occ,
    topic_min_citations,
    topic_max_citations,
):
    """Generates custom topics from an indicators dataframe.

    Topics are obtained from the index of the indicators dataframe.

    Parameters
    ----------
    indicators : pandas.DataFrame
        Indicators dataframe.

    topics_length : int
        Number of topics to be returned.

    topic_min_occ : int
        Minimum number of occurrences of a topic.

    topic_max_occ : int
        Maximum number of occurrences of a topic.

    topic_min_citations : int
        Minimum number of citations of a topic.

    topic_max_citations : int
        Maximum number of citations of a topic.

    Returns
    -------
    custom_topics : list
        List of topics.

    """
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

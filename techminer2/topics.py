"""
Functions for topic selection.

"""


# pylint: disable=too-many-arguments
def filter_custom_topics_from_axis(dataframe, custom_topics, axis):
    """Filters custom topics from a dataframe axis."""

    if axis == 0:
        topics_list = dataframe.index.tolist()
    else:
        topics_list = dataframe.index.tolist()

    custom_topics = [topic for topic in custom_topics if topic in topics_list]

    return custom_topics


def filter_custom_topics_from_column(dataframe, col_name, custom_topics):
    """Filters custom topics from a dataframe column."""

    custom_topics = [
        topic
        for topic in custom_topics
        if topic in dataframe[col_name].drop_duplicates().tolist()
    ]

    return custom_topics


def generate_custom_topics(
    indicators,
    topics_length,
    topic_occ_min,
    topic_occ_max,
    topic_citations_min,
    topic_citations_max,
):
    """Generates custom topics from the index techminer indicators dataframe.

    Args:
        indicators (pandas.DataFrame): a dataframe with the techminer.indicators.
        topics_length (int): number of topics to be generated.
        topic_min_occ (int): minimum number of occurrences of the topic.
        topic_max_occ (int): maximum number of occurrences of the topic.
        topic_min_citations (int): minimum number of citations of the topic.
        topic_max_citations (int): maximum number of citations of the topic.

    Returns:
        A list of topics.

    """
    custom_topics = indicators.copy()

    if topic_occ_min is not None:
        custom_topics = custom_topics[custom_topics["OCC"] >= topic_occ_min]

    if topic_occ_max is not None:
        custom_topics = custom_topics[custom_topics["OCC"] <= topic_occ_max]

    if topic_citations_min is not None:
        custom_topics = custom_topics[
            custom_topics["global_citations"] >= topic_citations_min
        ]

    if topic_citations_max is not None:
        custom_topics = custom_topics[
            custom_topics["global_citations"] <= topic_citations_max
        ]

    custom_topics = custom_topics.index.copy()
    custom_topics = custom_topics[:topics_length]

    return custom_topics

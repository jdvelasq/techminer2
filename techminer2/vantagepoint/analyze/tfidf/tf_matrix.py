"""
TF Matrix
===============================================================================

>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.analyze.tfidf.tf_matrix(
...     criterion='authors', 
...     topic_min_occ=2, 
...     directory=directory,
... ).head()
authors                                             Arner DW 3:185  ...  Arman AA 2:000
article                                                             ...                
Arner DW, 2017, HANDB OF BLOCKCHAIN, DIGIT FINA...               1  ...               0
Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, ...               1  ...               0
Battanta L, 2020, PROC EUR CONF INNOV ENTREPREN...               0  ...               0
Buckley RP, 2020, J BANK REGUL, V21, P26                         1  ...               0
Butler T/1, 2018, J RISK MANG FINANCIAL INST, V...               0  ...               0
<BLANKLINE>
[5 rows x 15 columns]

"""
import numpy as np
import pandas as pd

from ...._items2counters import items2counters
from ...._load_stopwords import load_stopwords
from ...._read_records import read_records
from ....techminer.indicators.tm2__indicators_by_topic import tm2__indicators_by_topic

# pylint: disable=too-many-arguments


def tf_matrix(
    criterion,
    topics_length=None,
    topic_min_occ=None,
    topic_min_citations=None,
    custom_topics=None,
    scheme=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Computes TF Matrix."""

    # extracts filtered topics
    indicators = _compute_filter(
        criterion,
        topics_length,
        topic_min_occ,
        topic_min_citations,
        custom_topics,
        directory,
        database,
        start_year,
        end_year,
        **filters,
    )
    custom_topics = indicators.index.tolist()

    # apply stopwords
    custom_topics = [
        topic for topic in custom_topics if topic not in load_stopwords(directory)
    ]

    # compute TF matrix
    result = _create_tf_matrix(
        criterion,
        custom_topics,
        directory,
        database,
        start_year,
        end_year,
        **filters,
    )

    result = _rename_columns(
        result,
        criterion,
        directory,
        database,
        start_year,
        end_year,
        **filters,
    )

    result = _remove_rows_of_zeros(result)
    result = _apply_scheme(scheme, result)

    result = _sort_columns(result)

    return result


def _sort_columns(result):

    topics = pd.DataFrame({"topic": result.columns.tolist()})

    topics["OCC"] = topics.topic.str.split()
    topics["OCC"] = topics["OCC"].map(lambda x: x[-1])
    topics["OCC"] = topics["OCC"].str.split(":")
    topics["OCC"] = topics["OCC"].map(lambda x: x[0]).astype(int)

    topics["citations"] = topics.topic.str.split()
    topics["citations"] = topics["citations"].map(lambda x: x[-1])
    topics["citations"] = topics["citations"].str.split(":")
    topics["citations"] = topics["citations"].map(lambda x: x[1]).astype(int)

    topics = topics.sort_values(
        by=["OCC", "citations", "topic"], ascending=[False, False, True]
    )
    sorted_topics = topics.topic.tolist()
    result = result[sorted_topics]
    return result


def _apply_scheme(scheme, result):
    if scheme is None or scheme == "raw":
        result = result.astype(int)
    elif scheme == "binary":
        result = result.applymap(lambda w: 1 if w > 0 else 0)
    elif scheme == "log":
        result = result.applymap(lambda x: np.log(x) if x > 0 else 0)
    elif scheme == "sqrt":
        result = result.applymap(lambda x: np.sqrt(x) if x > 0 else 0)
    else:
        raise ValueError("scheme must be 'raw', 'binary', 'log' or 'sqrt'")
    return result


def _remove_rows_of_zeros(result):
    result = result.loc[(result != 0).any(axis=1)]
    return result


def _rename_columns(
    result,
    criterion,
    directory,
    database,
    start_year,
    end_year,
    **filters,
):
    items_dict = items2counters(
        column=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    result = result.rename(columns=items_dict)
    return result


def _create_tf_matrix(
    criterion,
    custom_topics,
    directory,
    database,
    start_year,
    end_year,
    **filters,
):
    records = read_records(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    records = records.reset_index()
    records = records[[criterion, "article"]].copy()
    records = records.dropna()
    records["OCC"] = 1
    records[criterion] = records[criterion].str.split(";")
    records = records.explode(criterion)
    records[criterion] = records[criterion].str.strip()
    records = records[records[criterion].isin(custom_topics)]

    grouped_records = records.groupby(["article", criterion], as_index=False).agg(
        {"OCC": np.sum}
    )

    result = pd.pivot(
        index="article",
        data=grouped_records,
        columns=criterion,
        values="OCC",
    )
    result = result.fillna(0)
    return result


def _compute_filter(
    criterion,
    topics_length,
    topic_min_occ,
    topic_min_citations,
    custom_topics,
    directory,
    database,
    start_year,
    end_year,
    **filters,
):
    """apply filter to topics"""
    indicators = tm2__indicators_by_topic(
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    if custom_topics is None:
        custom_topics = indicators.copy()
        if topic_min_occ is not None:
            custom_topics = custom_topics[custom_topics["OCC"] >= topic_min_occ]
        if topic_min_citations is not None:
            custom_topics = custom_topics[
                custom_topics["global_citations"] >= topic_min_citations
            ]
        custom_topics = custom_topics.index.copy()
        custom_topics = custom_topics[:topics_length]
    else:
        custom_topics = [
            topic for topic in custom_topics if topic in indicators.index.tolist()
        ]

    indicators = indicators.loc[custom_topics, :]
    return indicators

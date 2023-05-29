"""
TF Matrix --- ChatGPT
===============================================================================

>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> tf_matrix = vantagepoint.analyze.tf_matrix(
...     criterion='authors',
...     topic_min_occ=2,
...     root_dir=root_dir,
... )
>>> tf_matrix.table_.head()
authors                                             Arner DW 3:185  ...  Arman AA 2:000
article                                                             ...                
Arner DW, 2017, HANDB OF BLOCKCHAIN, DIGIT FI, ...               1  ...               0
Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, ...               1  ...               0
Battanta L, 2020, PROC EUR CONF INNOV ENTREPREN...               0  ...               0
Buckley RP, 2020, J BANK REGUL, V21, P26                         1  ...               0
Butler T/1, 2018, J RISK MANG FIN INST, V11, P19                 0  ...               0
<BLANKLINE>
[5 rows x 15 columns]


"""
import numpy as np
import pandas as pd

from ...classes import TFMatrix
from ...counters import add_counters_to_axis
from ...load_utils import load_stopwords
from ...record_utils import read_records
from ...techminer.indicators.indicators_by_topic import indicators_by_topic
from ...topics import generate_custom_topics


# pylint: disable=too-many-arguments
def tf_matrix(
    criterion,
    topics_length=None,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    custom_topics=None,
    scheme=None,
    root_dir="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Computes TF Matrix."""

    if scheme is None:
        scheme = "raw"

    indicators = indicators_by_topic(
        criterion=criterion,
        root_dir=root_dir,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

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

    custom_topics = indicators.index.tolist()

    # apply stopwords
    custom_topics = [
        topic
        for topic in custom_topics
        if topic not in load_stopwords(root_dir)
    ]

    # compute TF matrix
    result = _create_tf_matrix(
        criterion,
        custom_topics,
        root_dir,
        database,
        start_year,
        end_year,
        **filters,
    )

    result = add_counters_to_axis(
        dataframe=result,
        axis=1,
        criterion=criterion,
        root_dir=root_dir,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    result = _remove_rows_of_zeros(result)
    result = _apply_scheme(scheme, result)
    result = _sort_columns(result)

    tfmatrix_ = TFMatrix()
    tfmatrix_.table_ = result
    tfmatrix_.criterion_ = criterion
    tfmatrix_.scheme_ = scheme
    tfmatrix_.prompt_ = "TODO"

    return tfmatrix_


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
        root_dir=directory,
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

    grouped_records = records.groupby(
        ["article", criterion], as_index=False
    ).agg({"OCC": np.sum})

    result = pd.pivot(
        index="article",
        data=grouped_records,
        columns=criterion,
        values="OCC",
    )
    result = result.fillna(0)
    return result

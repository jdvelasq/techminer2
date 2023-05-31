# flake8: noqa
"""
TF Matrix --- ChatGPT
===============================================================================

>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> tf_matrix = vantagepoint.analyze.tf_matrix(
...     criterion='authors',
...     topic_occ_min=2,
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
from ...item_utils import generate_custom_items
from ...techminer.indicators.indicators_by_item import indicators_by_item
from ...utils.load_utils import load_stopwords
from ...utils.records import read_records


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def tf_matrix(
    criterion,
    topics_length=None,
    topic_occ_min=None,
    topic_occ_max=None,
    topic_citations_min=None,
    topic_citations_max=None,
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

    indicators = indicators_by_item(
        field=criterion,
        root_dir=root_dir,
        database=database,
        year_filter=start_year,
        cited_by_filter=end_year,
        **filters,
    )

    if custom_topics is None:
        custom_topics = generate_custom_items(
            indicators=indicators,
            top_n=topics_length,
            occ_range=topic_occ_min,
            topic_occ_max=topic_occ_max,
            gc_range=topic_citations_min,
            topic_citations_max=topic_citations_max,
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

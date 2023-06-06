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

# pylint: disable=line-too-long
"""
import numpy as np
import pandas as pd

from ...classes import TFMatrix
from ...counters import add_counters_to_axis
from ...item_utils import generate_custom_items
from ...load_utils import load_stopwords
from ...record_utils import read_records
from ...techminer.indicators.indicators_by_item import indicators_by_item


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def tf_matrix(
    field,
    scheme=None,
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database params:
    root_dir="./",
    database="documents",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Computes TF Matrix."""

    if scheme is None:
        scheme = "raw"

    indicators = indicators_by_item(
        field=field,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    if custom_items is None:
        custom_items = generate_custom_items(
            indicators=indicators,
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
        )

    indicators = indicators[indicators.index.isin(custom_items)]

    custom_items = indicators.index.tolist()

    # apply stopwords
    custom_items = [
        topic
        for topic in custom_items
        if topic not in load_stopwords(root_dir)
    ]

    # compute TF matrix
    result = _create_tf_matrix(
        field,
        custom_items,
        root_dir,
        database,
        year_filter,
        cited_by_filter,
        **filters,
    )

    result = add_counters_to_axis(
        dataframe=result,
        axis=1,
        field=field,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    result = _remove_rows_of_zeros(result)
    result = _apply_scheme(scheme, result)
    result = _sort_columns(result)

    tfmatrix_ = TFMatrix()
    tfmatrix_.table_ = result
    tfmatrix_.criterion_ = field
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
    field,
    custom_items,
    # Database params:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    records = records.reset_index()
    records = records[[field, "article"]].copy()
    records = records.dropna()
    records["OCC"] = 1
    records[field] = records[field].str.split(";")
    records = records.explode(field)
    records[field] = records[field].str.strip()
    records = records[records[field].isin(custom_items)]

    grouped_records = records.groupby(["article", field], as_index=False).agg(
        {"OCC": np.sum}
    )

    result = pd.pivot(
        index="article",
        data=grouped_records,
        columns=field,
        values="OCC",
    )
    result = result.fillna(0)
    return result

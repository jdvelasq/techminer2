# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _performance_analysis.tfidf:

TFIDF
===============================================================================


>>> from techminer2.performance_analysis import tfidf
>>> tfidf(
...     #
...     # TF PARAMS:
...     field='author_keywords',
...     is_binary=False,
...     cooc_within= 1,
...     #
...     # ITEM FILTERS:
...     top_n=50,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # TF-IDF parameters:
...     norm= None,
...     use_idf=False,
...     smooth_idf=False,
...     sublinear_tf=False,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head(20)
author_keywords                                     REGTECH 28:329  ...  MONEY_LAUNDERING 01:010
article                                                             ...                         
Anagnostopoulos I, 2018, J ECON BUS, V100, P7                    1  ...                        0
Arner DW, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, ...               1  ...                        0
Battanta L, 2020, PROC EUR CONF INNOV ENTREPREN...               1  ...                        0
Becker M, 2020, INTELL SYST ACCOUNT FINANCE M, ...               0  ...                        0
Buckley RP, 2020, J BANK REGUL, V21, P26                         1  ...                        0
Butler T, 2018, J RISK MANG FINANCIAL INST, V11...               1  ...                        0
Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85               1  ...                        0
Campbell-Verduyn M, 2022, NEW POLIT ECON                         0  ...                        0
Cruz Rambaud S, 2022, EUR J RISK REGUL, V13, P333                1  ...                        0
Firmansyah B, 2022, INT CONF INF TECHNOL SYST I...               1  ...                        0
Gasparri G, 2019, FRONTIER ARTIF INTELL, V2                      1  ...                        0
Ghanem S, 2021, STUD COMPUT INTELL, V954, P139                   1  ...                        0
Goul M, 2019, PROC - IEEE WORLD CONGR SERV,, P219                1  ...                        0
Grassi L, 2022, J IND BUS ECON, V49, P441                        1  ...                        0
Huang GKJ, 2017, PROC INT CONF ELECTRON BUS (I,...               1  ...                        0
Kavassalis P, 2018, J RISK FINANC, V19, P39                      1  ...                        0
Kera DR, 2021, EAI/SPRINGER INNO COMM COMP, P67                  0  ...                        0
Kristanto AD, 2022, INT CONF INF TECHNOL SYST I...               1  ...                        0
Kurum E, 2020, J FINANC CRIME                                    1  ...                        1
Lan G, 2023, RES INT BUS FINANC, V64                             1  ...                        0
<BLANKLINE>
[20 rows x 50 columns]


"""
from typing import Literal

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer

from .._counters_lib import add_counters_to_frame_axis
from .._filtering_lib import generate_custom_items
from .._read_records import read_records
from ..indicators.global_indicators_by_field import global_indicators_by_field


def tfidf(
    #
    # TF PARAMS:
    field: str,
    is_binary: bool = False,
    cooc_within: int = 1,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # TF-IDF parameters:
    norm: Literal["l1", "l2", None] = None,
    use_idf=False,
    smooth_idf=False,
    sublinear_tf=False,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Computes TF Matrix.

    :meta private:
    """

    indicators = global_indicators_by_field(
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
            metric="OCC",
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
        )

    indicators = indicators[indicators.index.isin(custom_items)]

    custom_items = indicators.index.tolist()

    # compute TF matrix
    result = _create_tf_matrix(
        field=field,
        cooc_within=cooc_within,
        custom_items=custom_items,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    if is_binary is True:
        result = result.applymap(lambda w: 1 if w > 0 else 0)

    if norm is not None or use_idf or smooth_idf or sublinear_tf:
        transformer = TfidfTransformer(
            norm=norm,
            use_idf=use_idf,
            smooth_idf=smooth_idf,
            sublinear_tf=sublinear_tf,
        )

        result = transformer.fit_transform(result)
    else:
        result = result.astype(int)

    result = add_counters_to_frame_axis(
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

    topics = topics.sort_values(by=["OCC", "citations", "topic"], ascending=[False, False, True])
    sorted_topics = topics.topic.tolist()
    result = result[sorted_topics]
    return result


def _remove_rows_of_zeros(result):
    result = result.loc[(result != 0).any(axis=1)]
    return result


def _create_tf_matrix(
    field,
    cooc_within,
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

    grouped_records = records.groupby(["article", field], as_index=False).agg({"OCC": np.sum})

    result = pd.pivot(
        index="article",
        data=grouped_records,
        columns=field,
        values="OCC",
    )
    result = result.loc[:, result.columns.isin(custom_items)]
    result = result.fillna(0)
    result = result.loc[(result.sum(axis=1) >= cooc_within)]

    return result

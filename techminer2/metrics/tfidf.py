# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
TFIDF
===============================================================================


>>> from techminer2.metrics import tfidf
>>> tfidf(
...     #
...     # TF PARAMS:
...     retain_counters=True,
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
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head()
author_keywords                                 FINTECH 31:5168  ...  BIG_DATA 01:0238
article                                                          ...                  
Anagnostopoulos I., 2018, J ECON BUS, V100, P7                1  ...                 0
Anshari M., 2019, ENERGY PROCEDIA, V156, P234                 0  ...                 0
Buchak G., 2018, J FINANC ECON, V130, P453                    1  ...                 0
Cai C.W., 2018, ACCOUNT FINANC, V58, P965                     1  ...                 0
Chen L., 2016, CHINA ECON J, V9, P225                         1  ...                 0
<BLANKLINE>
[5 rows x 50 columns]




"""
from typing import Literal

import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer  # type: ignore

from .._core.metrics.calculate_global_performance_metrics import calculate_global_performance_metrics
from .._core.metrics.extract_top_n_terms_by_metric import extract_top_n_terms_by_metric
from .._core.read_filtered_database import read_filtered_database
from ..helpers.helper_append_occurrences_and_citations_to_axis import helper_append_occurrences_and_citations_to_axis


def tfidf(
    #
    # TF PARAMS:
    field: str,
    retain_counters=True,
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
    sort_by=None,
    **filters,
):
    """Computes TF Matrix.

    :meta private:
    """

    indicators = calculate_global_performance_metrics(
        field=field,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=sort_by,
        **filters,
    )

    if custom_items is None:
        custom_items = extract_top_n_terms_by_metric(
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
        sort_by=sort_by,
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

    result = helper_append_occurrences_and_citations_to_axis(
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

    if retain_counters is False:
        result.columns = [" ".join(x.split()[:-1]) for x in result.columns]

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
    sort_by,
    **filters,
):
    records = read_filtered_database(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=sort_by,
        **filters,
    )

    records = records.reset_index()
    records = records[[field, "article"]].copy()
    records = records.dropna()
    records["OCC"] = 1
    records[field] = records[field].str.split(";")
    records = records.explode(field)
    records[field] = records[field].str.strip()

    grouped_records = records.groupby(["article", field], as_index=False).agg({"OCC": "sum"})

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

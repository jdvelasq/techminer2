# flake8: noqa
"""
TF Matrix
===============================================================================

>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> tf_matrix = techminer2plus.tfidf.tf_matrix(
...     field='author_keywords',
...     top_n=50,
...     root_dir=root_dir,
... )
>>> tf_matrix
TF-Matrix(field='author_keywords', scheme='raw', cooc_within=1, shape=(39,
    50))

>>> tf_matrix.table_.head(20)
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



# pylint: disable=line-too-long
"""
import textwrap
from dataclasses import dataclass

import numpy as np
import pandas as pd

from .counters_lib import add_counters_to_frame_axis
from .filtering_lib import generate_custom_items
from .metrics_lib import indicators_by_field
from .records import read_records


# pylint: disable=too-many-instance-attributes
@dataclass
class TFMatrix:
    """Term-frequency matrix.

    :meta private:
    """

    table_: pd.DataFrame
    prompt_: str
    #
    # Params:
    field_: str
    scheme_: str
    cooc_within_: int
    #
    # Item filters:
    top_n_: int
    occ_range_: tuple
    gc_range_: tuple
    custom_items_: list
    #
    # Database params:
    root_dir_: str
    database_: str
    year_filter_: tuple
    cited_by_filter_: tuple
    filters_: dict

    def __repr__(self):
        text = "TF-Matrix("
        text += f"field='{self.field_}'"
        text += f", scheme='{self.scheme_}'"
        text += f", cooc_within={self.cooc_within_}"
        text += f", shape={self.table_.shape}"
        text += ")"
        text = textwrap.fill(text, width=75, subsequent_indent="    ")
        return text


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def tf_matrix(
    field,
    scheme=None,
    cooc_within=1,
    #
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    #
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Computes TF Matrix."""

    if scheme is None:
        scheme = "raw"

    indicators = indicators_by_field(
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
    result = _apply_scheme(scheme, result)
    result = _sort_columns(result)

    return TFMatrix(
        #
        # Results:
        table_=result,
        prompt_="TODO",
        #
        # Params:
        field_=field,
        scheme_=scheme,
        cooc_within_=cooc_within,
        #
        # Item filters:
        top_n_=top_n,
        occ_range_=occ_range,
        gc_range_=gc_range,
        custom_items_=custom_items,
        #
        # Database params:
        root_dir_=root_dir,
        database_=database,
        year_filter_=year_filter,
        cited_by_filter_=cited_by_filter,
        filters_=filters,
    )


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

    grouped_records = records.groupby(["article", field], as_index=False).agg(
        {"OCC": np.sum}
    )

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

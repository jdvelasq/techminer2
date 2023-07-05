# flake8: noqa
"""
TF-IDF Matrix
===============================================================================



>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> tf_matrix = techminer2plus.tfidf.tf_matrix(
...     field='author_keywords',
...     top_n=50,
...     root_dir=root_dir,
... )
>>> tfidf_matrix = techminer2plus.tfidf.tf_idf_matrix(tf_matrix)
>>> tfidf_matrix
TFIDF-Matrix(field='author_keywords', scheme='raw', cooc_within=1,
    shape=(39, 50))

>>> tfidf_matrix.table_.head(20)
author_keywords                                     REGTECH 28:329  ...  MONEY_LAUNDERING 01:010
article                                                             ...                         
Anagnostopoulos I, 2018, J ECON BUS, V100, P7             0.176501  ...                 0.000000
Arner DW, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, ...        0.227986  ...                 0.000000
Battanta L, 2020, PROC EUR CONF INNOV ENTREPREN...        0.213136  ...                 0.000000
Becker M, 2020, INTELL SYST ACCOUNT FINANCE M, ...        0.000000  ...                 0.000000
Buckley RP, 2020, J BANK REGUL, V21, P26                  0.126899  ...                 0.000000
Butler T, 2018, J RISK MANG FINANCIAL INST, V11...        0.213136  ...                 0.000000
Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85        0.223027  ...                 0.000000
Campbell-Verduyn M, 2022, NEW POLIT ECON                  0.000000  ...                 0.000000
Cruz Rambaud S, 2022, EUR J RISK REGUL, V13, P333         0.345442  ...                 0.000000
Firmansyah B, 2022, INT CONF INF TECHNOL SYST I...        0.345442  ...                 0.000000
Gasparri G, 2019, FRONTIER ARTIF INTELL, V2               0.318989  ...                 0.000000
Ghanem S, 2021, STUD COMPUT INTELL, V954, P139            0.451820  ...                 0.000000
Goul M, 2019, PROC - IEEE WORLD CONGR SERV,, P219         0.528310  ...                 0.000000
Grassi L, 2022, J IND BUS ECON, V49, P441                 0.166539  ...                 0.000000
Huang GKJ, 2017, PROC INT CONF ELECTRON BUS (I,...        0.261489  ...                 0.000000
Kavassalis P, 2018, J RISK FINANC, V19, P39               0.193664  ...                 0.000000
Kera DR, 2021, EAI/SPRINGER INNO COMM COMP, P67           0.000000  ...                 0.000000
Kristanto AD, 2022, INT CONF INF TECHNOL SYST I...        0.371524  ...                 0.000000
Kurum E, 2020, J FINANC CRIME                             0.180890  ...                 0.546912
Lan G, 2023, RES INT BUS FINANC, V64                      1.000000  ...                 0.000000
<BLANKLINE>
[20 rows x 50 columns]


"""
import textwrap
from dataclasses import dataclass
from typing import Literal

import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer


# Analyze / Discover / Matrix / TF-IDF Matrix
@dataclass
class TFIDFMatrix:
    """Term-frequency IDF matrix."""

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
        text = "TFIDF-Matrix("
        text += f"field='{self.field_}'"
        text += f", scheme='{self.scheme_}'"
        text += f", cooc_within={self.cooc_within_}"
        text += f", shape={self.table_.shape}"
        text += ")"
        text = textwrap.fill(text, width=75, subsequent_indent="    ")
        return text


def tf_idf_matrix(
    tf_matrix,
    #
    # TF-IDF parameters:
    norm: Literal["l1", "l2", None] = "l2",
    use_idf=True,
    smooth_idf=True,
    sublinear_tf=False,
):
    """
    Compute TF-IDF matrix from a TF matrix.


    """
    if tf_matrix.scheme_ != "raw":
        raise ValueError("tf_matrix must be a raw TF matrix")

    transformer = TfidfTransformer(
        norm=norm,
        use_idf=use_idf,
        smooth_idf=smooth_idf,
        sublinear_tf=sublinear_tf,
    )

    transformed_matrix = transformer.fit_transform(tf_matrix.table_)
    table = pd.DataFrame(
        transformed_matrix.toarray(),
        columns=tf_matrix.table_.columns,
        index=tf_matrix.table_.index,
    )

    return TFIDFMatrix(
        #
        # Results:
        prompt_=tf_matrix.prompt_,
        table_=table,
        #
        # Params:
        field_=tf_matrix.field_,
        scheme_=tf_matrix.scheme_,
        cooc_within_=tf_matrix.cooc_within_,
        #
        # Item filters:
        top_n_=tf_matrix.top_n_,
        occ_range_=tf_matrix.occ_range_,
        gc_range_=tf_matrix.gc_range_,
        custom_items_=tf_matrix.custom_items_,
        #
        # Database params:
        root_dir_=tf_matrix.root_dir_,
        database_=tf_matrix.database_,
        year_filter_=tf_matrix.year_filter_,
        cited_by_filter_=tf_matrix.cited_by_filter_,
        filters_=tf_matrix.filters_,
    )

"""
TF Matrix (TODO:)
===============================================================================


>>> from techminer2 import vantagepoint__tf_matrix
>>> directory = "data/regtech/"

>>> vantagepoint__tf_matrix(
...     'authors', 
...     min_occ=2, 
...     directory=directory,
... ).head()
                                                    Arner DW 7:220  ...  Lin W 2:007
article                                                             ...             
Arner DW, 2017, HANDB OF BLOCKCHAIN, DIGIT FINA...               1  ...            0
Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, ...               1  ...            0
Arner DW, 2019, EUR BUS ORG LAW REV, V20, P55                    1  ...            0
Arner DW, 2020, EUR BUS ORG LAW REV, V21, P7                     1  ...            0
Barberis JN, 2016, NEW ECON WINDOWS, P69                         1  ...            0
<BLANKLINE>
[5 rows x 15 columns]

"""
import numpy as np
import pandas as pd

from ._items2counters import items2counters
from ._load_stopwords import load_stopwords
from ._read_records import read_records

# pylint: disable=too-many-arguments


def vantagepoint__tf_matrix(
    criterion,
    topics_length=None,
    topic_min_occ=None,
    topic_min_citations=None,
    scheme=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Computes TF Matrix."""

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
    records[criterion] = records[criterion].map(lambda x: [y.strip() for y in x])
    records = records.explode(criterion)
    grouped_records = records.groupby(["article", criterion], as_index=False).agg(
        {"OCC": np.sum}
    )

    result = pd.pivot(
        index="article",
        data=grouped_records,
        columns=criterion,
    )
    result = result.fillna(0)

    items_dict = items2counters(
        column=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    result = result.rename(columns=items_dict)

    ## filter columns
    selected_columns = result.columns
    if topic_min_occ is not None:
        selected_columns = [
            col
            for col in selected_columns
            if int(col.split()[-1].split(":")[0]) >= topic_min_occ
        ]
    if topic_min_citations is not None:
        selected_columns = [
            col
            for col in selected_columns
            if int(col.split()[-1].split(":")[0]) >= topic_min_citations
        ]

    # ----< Counts term occurrence >-------------------------------------------
    result.columns = [b for _, b in result.columns]
    terms = result.sum(axis=0)
    terms = terms.sort_values(ascending=False)
    if topic_min_occ is not None:
        terms = terms[terms >= topic_min_occ]
    if topic_min_citations is not None:
        terms = terms[terms <= topic_min_citations]
    terms = terms.drop(labels=load_stopwords(directory), errors="ignore")
    result = result.loc[:, terms.index]

    # ---< Remove rows with only zeros detected -------------------------------
    result = result.loc[(result != 0).any(axis=1)]

    # ----< Applies scheme >---------------------------------------------------
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

    result = result.sort_index(axis=0, ascending=True)

    return result

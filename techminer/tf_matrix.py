"""
TF (term-frecuency) Matrix
===============================================================================

"""
import numpy as np
import pandas as pd

from .utils import (
    explode,
    load_records_from_directory,
    load_stopwords_from_directory,
    map_,
)


def _tf_matrix_from_records(
    records,
    column,
    min_occurrence,
    max_occurrence,
    stopwords,
    scheme,
    sep,
):

    records = records[[column, "record_id"]].copy()
    records["value"] = 1.0
    records = explode(records, column, sep)

    grouped_records = records.groupby([column, "record_id"], as_index=False).agg(
        {"value": np.sum}
    )
    result = pd.pivot_table(
        data=grouped_records,
        index="record_id",
        columns=column,
        margins=False,
        fill_value=0.0,
    )
    result.columns = [b for _, b in result.columns]
    result = result.reset_index(drop=True)

    terms = result.sum(axis=0)
    terms = terms.sort_values(ascending=False)
    terms = terms[terms >= min_occurrence]
    terms = terms[terms <= max_occurrence]
    terms = terms.drop(labels=load_stopwords(stopwords), errors="ignore")
    result = result.loc[:, terms.index]

    # rows = result.sum(axis=1)
    # rows = rows[rows > 0]
    # result = result.loc[rows.index, :]

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


def _tf_matrix_from_directory(
    directory,
    column,
    min_occurrence,
    max_occurrence,
    stopwords,
    scheme,
    sep,
):
    return _tf_matrix_from_records(
        records=load_records(directory),
        column=column,
        min_occurrence=min_occurrence,
        max_occurrence=max_occurrence,
        stopwords=stopwords,
        scheme=scheme,
        sep=sep,
    )


def tf_matrix(
    directory_or_records,
    column,
    min_occurrence=1,
    max_occurrence=99999,
    stopwords=None,
    scheme=None,
    sep="; ",
):
    if isinstance(directory_or_records, str):
        return _tf_matrix_from_directory(
            directory=directory_or_records,
            column=column,
            min_occurrence=min_occurrence,
            max_occurrence=max_occurrence,
            stopwords=stopwords,
            scheme=scheme,
            sep=sep,
        )
    elif isinstance(directory_or_records, pd.DataFrame):
        return _tf_matrix_from_records(
            records=directory_or_records,
            column=column,
            min_occurrence=min_occurrence,
            max_occurrence=max_occurrence,
            stopwords=stopwords,
            scheme=scheme,
            sep=sep,
        )
    else:
        raise TypeError("directory_or_records must be a string or a pandas.DataFrame")

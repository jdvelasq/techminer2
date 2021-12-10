"""
Growth indicators
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> growth_indicators(directory, "author_keywords").head()
                        before 2020  ...  average_growth_rate
fintech                          42  ...                 21.5
financial technologies           11  ...                  4.0
blockchain                        9  ...                  1.0
innovation                        9  ...                 -1.0
financial service                 7  ...                  1.0
<BLANKLINE>
[5 rows x 4 columns]

"""
import numpy as np
import pandas as pd

from .utils import load_filtered_documents, load_stopwords


def _num_documents_per_period(documents, column, time_window=2, sep="; "):
    #
    # Computes the total number of documents published in each period
    #
    if time_window < 2:
        raise ValueError("Time window must be greater than 1")
    year_limit = documents.pub_year.max() - time_window + 1
    result = documents.copy()
    result.index = result.record_no
    result = result[[column, "pub_year"]].copy()
    result[column] = result[column].str.split(sep)
    result = result.explode(column)
    result = result.assign(
        before=result.pub_year.map(lambda x: 1 if x < year_limit else 0)
    )
    result = result.assign(
        between=result.pub_year.map(lambda x: 1 if x >= year_limit else 0)
    )
    result = result.groupby(column, as_index=False).agg(
        {"before": np.sum, "between": np.sum}
    )
    result = result.sort_values("before", ascending=False)
    result = result.set_index(column)

    return result


def _average_growth_rate(documents, column, time_window, sep="; "):
    #
    #         sum_{i=Y_start}^Y_end  Num_Documents[i] - Num_Documents[i-1]
    #  AGR = --------------------------------------------------------------
    #                          Y_end - Y_start + 1
    #
    #
    if time_window < 2:
        raise ValueError("Time window must be greater than 1")

    # first and last years in the time window
    first_year = documents.pub_year.max() - time_window
    last_year = documents.pub_year.max()

    # generates a table of term and year.
    result = documents.copy()
    result.index = result.record_no
    result = result[[column, "pub_year"]].copy()
    result[column] = result[column].str.split(sep)
    result = result.explode(column)
    result = result[(result.pub_year == first_year) | (result.pub_year == last_year)]
    result = result.assign(num_documents=1)

    #
    result = result.groupby([column, "pub_year"], as_index=False).agg(
        {"num_documents": np.sum}
    )
    result = result.pivot(index=column, columns="pub_year", values="num_documents")
    result = result.fillna(0)
    result = result.assign(
        average_growth_rate=(result.iloc[:, 1] - result.iloc[:, 0]) / time_window
    )
    result = result[["average_growth_rate"]]

    return result


def _average_documents_per_year(documents, column, time_window, sep="; "):
    #
    #         sum_{i=Y_start}^Y_end  Num_Documents[i]
    #  ADY = -----------------------------------------
    #                  Y_end - Y_start + 1
    #
    result = _num_documents_per_period(
        documents=documents, column=column, time_window=time_window, sep=sep
    )
    result = result.assign(average_documents_per_year=result.between / time_window)
    result = result[["average_documents_per_year"]]
    return result


def growth_indicators(column, sep="; ", time_window=2, directory="./"):

    documents = load_filtered_documents(directory)

    ndpp = _num_documents_per_period(
        documents=documents, column=column, time_window=time_window, sep=sep
    )
    adpy = _average_documents_per_year(
        documents=documents, column=column, time_window=time_window, sep=sep
    )
    agr = _average_growth_rate(
        documents=documents, column=column, time_window=time_window, sep=sep
    )
    result = pd.concat([ndpp, adpy, agr], axis="columns")

    year_limit = documents.pub_year.max() - time_window + 1
    result = result.rename(
        columns={
            "before": f"before {year_limit}",
            "between": f"between {year_limit}-{documents.pub_year.max()}",
        }
    )

    stopwords = load_stopwords(directory)
    result = result.drop(stopwords, axis=0)

    return result

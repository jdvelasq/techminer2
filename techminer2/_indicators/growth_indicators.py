"""
Growth Indicators
===============================================================================

>>> directory = "data/regtech/"

>>> from techminer2 import growth_indicators
>>> growth_indicators(column="author_keywords", directory=directory).head()
                         before 2021  ...  average_growth_rate
author_keywords                       ...                     
regtech                           50  ...                 -6.5
fintech                           32  ...                 -4.0
blockchain                        13  ...                 -1.5
compliance                        10  ...                 -2.5
artificial intelligence            8  ...                 -1.5
<BLANKLINE>
[5 rows x 4 columns]

"""
import numpy as np
import pandas as pd

from .._load_stopwords import load_stopwords
from .._read_records import read_records


def _occ_per_period(records, column, time_window=2, sep="; "):
    #
    # Computes the total number of documents published in each period
    #
    if time_window < 2:
        raise ValueError("Time window must be greater than 1")
    year_limit = records.year.max() - time_window + 1
    result = records.copy()
    result.index = result.article
    result = result[[column, "year"]].copy()
    result[column] = result[column].str.split(sep)
    result = result.explode(column)
    result = result.assign(before=result.year.map(lambda x: 1 if x < year_limit else 0))
    result = result.assign(
        between=result.year.map(lambda x: 1 if x >= year_limit else 0)
    )
    result = result.groupby(column, as_index=False).agg(
        {"before": np.sum, "between": np.sum}
    )
    result = result.sort_values("before", ascending=False)
    result = result.set_index(column)

    return result


def _average_growth_rate(records, column, time_window, sep="; "):
    #
    #         sum_{i=Y_start}^Y_end  Num_Documents[i] - Num_Documents[i-1]
    #  AGR = --------------------------------------------------------------
    #                          Y_end - Y_start + 1
    #
    #
    if time_window < 2:
        raise ValueError("Time window must be greater than 1")

    # first and last years in the time window
    first_year = records.year.max() - time_window
    last_year = records.year.max()

    # generates a table of term and year.
    result = records.copy()
    result.index = result.article
    result = result[[column, "year"]].copy()
    result[column] = result[column].str.split(sep)
    result = result.explode(column)
    result = result[(result.year == first_year) | (result.year == last_year)]
    result = result.assign(OCC=1)

    #
    result = result.groupby([column, "year"], as_index=False).agg({"OCC": np.sum})
    result = result.pivot(index=column, columns="year", values="OCC")
    result = result.fillna(0)
    result = result.assign(
        average_growth_rate=(result.iloc[:, 1] - result.iloc[:, 0]) / time_window
    )
    result = result[["average_growth_rate"]]

    return result


def _average_documents_per_year(records, column, time_window, sep="; "):
    #
    #         sum_{i=Y_start}^Y_end  Num_Documents[i]
    #  ADY = -----------------------------------------
    #                  Y_end - Y_start + 1
    #
    result = _occ_per_period(
        records=records, column=column, time_window=time_window, sep=sep
    )
    result = result.assign(average_documents_per_year=result.between / time_window)
    result = result[["average_documents_per_year"]]
    return result


def growth_indicators(
    column, sep="; ", time_window=2, directory="./", database="documents"
):
    """Computes growth indicators."""

    records = read_records(
        directory=directory, database=database, use_filter=(database == "documents")
    )

    ndpp = _occ_per_period(
        records=records, column=column, time_window=time_window, sep=sep
    )
    adpy = _average_documents_per_year(
        records=records, column=column, time_window=time_window, sep=sep
    )
    agr = _average_growth_rate(
        records=records, column=column, time_window=time_window, sep=sep
    )
    result = pd.concat([ndpp, adpy, agr], axis="columns")

    year_limit = records.year.max() - time_window + 1
    result = result.rename(
        columns={
            "before": f"Before {year_limit}",
            "between": f"Between {year_limit}-{records.year.max()}",
        }
    )

    stopwords = load_stopwords(directory)
    result = result.drop(stopwords, axis=0)

    return result

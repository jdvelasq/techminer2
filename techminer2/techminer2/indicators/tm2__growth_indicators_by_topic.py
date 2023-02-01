"""
Growth Indicators by Topic
===============================================================================

>>> directory = "data/regtech/"

>>> from techminer2.tm2__growth_indicators_by_topic import tm2__growth_indicators_by_topic
>>> tm2__growth_indicators_by_topic(
...     criterion="author_keywords", 
...     directory=directory,
... ).head()
                         Before 2021  ...  average_growth_rate
author_keywords                       ...                     
regtech                           49  ...                 -6.0
fintech                           32  ...                 -4.0
blockchain                        13  ...                 -1.5
artificial intelligence            8  ...                 -1.5
regulatory technology              6  ...                 -0.5
<BLANKLINE>
[5 rows x 6 columns]

>>> from pprint import pprint
>>> pprint(sorted(growth_indicators_by_topic('author_keywords',directory=directory).columns.to_list()))
['Before 2021',
 'Between 2021-2022',
 'OCC',
 'average_documents_per_year',
 'average_growth_rate',
 'global_citations']

"""
import numpy as np
import pandas as pd

from ..._load_stopwords import load_stopwords
from ..._read_records import read_records


def tm2__growth_indicators_by_topic(
    criterion,
    time_window=2,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Computes growth indicators."""

    records = read_records(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    return _growth_indicators_from_records(criterion, time_window, directory, records)


def _growth_indicators_from_records(column, time_window, directory, records):
    #
    ndpp = _occ_per_period(
        records=records,
        column=column,
        time_window=time_window,
    )
    adpy = _average_documents_per_year(
        records=records,
        column=column,
        time_window=time_window,
    )
    agr = _average_growth_rate(
        records=records,
        column=column,
        time_window=time_window,
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
    result = result.drop(stopwords, axis=0, errors="ignore")

    return result


def _occ_per_period(
    records,
    column,
    time_window=2,
):
    #
    # Computes the total number of documents published in each period
    #
    if time_window < 2:
        raise ValueError("Time window must be greater than 1")

    year_limit = records.year.max() - time_window + 1

    result = records.copy()
    result.index = result.article
    result = result[[column, "global_citations", "year"]].copy()

    result[column] = result[column].str.split(";")
    result = result.explode(column)
    result[column] = result[column].str.strip()

    result = result.assign(before=result.year.map(lambda x: 1 if x < year_limit else 0))

    result = result.assign(
        between=result.year.map(lambda x: 1 if x >= year_limit else 0)
    )

    result = result.groupby(column, as_index=False).agg(
        {"before": np.sum, "between": np.sum, "global_citations": np.sum}
    )

    result = result.assign(OCC=result.between + result.before)

    result = result.sort_values("OCC", ascending=False)
    result = result.set_index(column)

    return result


def _average_growth_rate(
    records,
    column,
    time_window,
):
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
    result[column] = result[column].str.split(";")
    result = result.explode(column)
    result[column] = result[column].str.strip()
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


def _average_documents_per_year(
    records,
    column,
    time_window,
):
    #
    #         sum_{i=Y_start}^Y_end  Num_Documents[i]
    #  ADY = -----------------------------------------
    #                  Y_end - Y_start + 1
    #
    result = _occ_per_period(
        records=records,
        column=column,
        time_window=time_window,
    )
    result = result.assign(average_documents_per_year=result.between / time_window)
    result = result[["average_documents_per_year"]]
    return result

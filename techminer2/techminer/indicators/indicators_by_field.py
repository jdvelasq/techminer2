# flake8: noqa
"""
Indicators by Field
===============================================================================


TechMiner2 computes three growth indicators for each item in a field (usually
keywords or noun phrases):

* Average growth rate (AGR):

.. code-block::

           sum_{i=Y_start}^Y_end  Num_Documents[i] - Num_Documents[i-1]
    AGR = --------------------------------------------------------------
                            Y_end - Y_start + 1


* Average documents per year (ADY):

.. code-block::

           sum_{i=Y_start}^Y_end  Num_Documents[i]
    ADY = -----------------------------------------
                    Y_end - Y_start + 1


* Percentage of documents in last year (PDLY):

.. code-block::

           sum_{i=Y_start}^Y_end  Num_Documents[i]      1
    PDLY = ---------------------------------------- * _____
                  Y_end - Y_start + 1                  TND


With:

.. code-block::

    Y_start = Y_end - time_window + 1



    
If ``Y_end = 2018`` and ``time_window = 2``, then ``Y_start = 2017``.




>>> root_dir = "data/regtech/"


>>> from techminer2  import techminer
>>> indicators = techminer.indicators.indicators_by_field(
...     field='author_keywords',
...     root_dir=root_dir,
... )
>>> print(indicators.head(10).to_markdown())
| author_keywords             |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:----------------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| ACCOUNTABILITY              |     2 |             2 |                   0 |                 14 |                 3 |                             7   |                            1.5 |                  -0.5 |                     0   |                         0   |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| ALGORITHMIC_DECISION_MAKING |     1 |             1 |                   0 |                  0 |                 0 |                             0   |                            0   |                   0   |                     0   |                         0   |                     2020 |     4 |                        0    |         0 |         0 |      0    |
| ALGORITHMIC_PROCESS         |     1 |             1 |                   0 |                  3 |                 2 |                             3   |                            2   |                   0   |                     0   |                         0   |                     2019 |     5 |                        0.6  |         1 |         1 |      0.2  |
| ALGORITHMIC_STANDARDS       |     1 |             1 |                   0 |                 21 |                 8 |                            21   |                            8   |                   0   |                     0   |                         0   |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
| ALGORITHMIC_TRANSPARENCY    |     1 |             0 |                   1 |                  3 |                 0 |                             3   |                            0   |                   0   |                     0.5 |                         0.5 |                     2022 |     2 |                        1.5  |         1 |         1 |      0.5  |
| ANALYTIC_HIERARCHY_PROCESS  |     1 |             1 |                   0 |                  2 |                 3 |                             2   |                            3   |                   0   |                     0   |                         0   |                     2020 |     4 |                        0.5  |         1 |         1 |      0.25 |
| ANNUAL_GENERAL_MEETINGS     |     1 |             0 |                   1 |                  0 |                 0 |                             0   |                            0   |                   0.5 |                     0.5 |                         0.5 |                     2023 |     1 |                        0    |         0 |         0 |      0    |
| ANOMALY_DETECTION           |     1 |             1 |                   0 |                  2 |                 0 |                             2   |                            0   |                  -0.5 |                     0   |                         0   |                     2021 |     3 |                        0.67 |         1 |         1 |      0.33 |
| ANTITRUST                   |     1 |             1 |                   0 |                  3 |                 3 |                             3   |                            3   |                  -0.5 |                     0   |                         0   |                     2021 |     3 |                        1    |         1 |         1 |      0.33 |
| ANTI_MONEY_LAUNDERING       |     5 |             5 |                   0 |                 34 |                 8 |                             6.8 |                            1.6 |                  -1.5 |                     0   |                         0   |                     2020 |     4 |                        8.5  |         3 |         2 |      0.75 |





# pylint: disable=line-too-long
"""

import numpy as np

from ...load_utils import load_stopwords
from ...record_utils import read_records
from .items_occ_by_year import items_occ_by_year


def indicators_by_field(
    field,
    time_window=2,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Bibliometric column indicators.

    Args:
        field (str): column name to be used as criterion.
        root_dir (str): root directory.
        database (str): database name.
        year_filter (tuple, optional): Year database filter. Defaults to None.
        cited_by_filter (tuple, optional): Cited by database filter. Defaults to None.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.

    Returns:
        pandas.DataFrame: a dataframe containing the indicators.

    """

    def extract_items_from_field(records):
        """Creates a dataframe with the items in the field column."""

        records = records.copy()

        unique_items = (
            records[field]
            .dropna()
            .str.split(";")
            .explode()
            .str.strip()
            .drop_duplicates()
            .to_frame()
        )

        unique_items.columns = [field]
        unique_items = unique_items.reset_index(drop=True)
        unique_items.index = unique_items[field]

        return unique_items

    def compute_column_sum_by_item(records, indicators, column):
        """Computes global citations from database and adds the column to indicators."""

        records = records.copy()

        column_sum = records[[field, column]].dropna()
        column_sum[field] = (
            column_sum[field]
            .str.split(";")
            .map(lambda x: [_.strip() for _ in x])
        )
        column_sum = column_sum.explode(field)
        column_sum = column_sum.groupby(field, as_index=True).sum().astype(int)
        indicators.loc[column_sum.index, column] = column_sum

        return indicators

    def compute_global_citations_per_document(indicators):
        indicators = indicators.copy()
        indicators = indicators.assign(
            global_citations_per_document=(
                indicators.global_citations / indicators.OCC
            ).round(2)
        )
        return indicators

    def compute_local_citations_per_document(indicators):
        indicators = indicators.copy()
        indicators = indicators.assign(
            local_citations_per_document=(
                indicators.local_citations / indicators.OCC
            ).round(2)
        )
        return indicators

    def compute_age(records, indicators):
        indicators = indicators.copy()
        indicators = indicators.assign(
            age=(
                records.year.max() - indicators.first_publication_year + 1
            ).astype(int)
        )
        return indicators

    def compute_global_citations_per_year(indicators):
        """Computes the global citations per year."""

        indicators = indicators.copy()
        indicators = indicators.assign(
            global_citations_per_year=(
                indicators.global_citations / indicators.age
            ).round(2)
        )

        return indicators

    def compute_first_publication_year(records, indicators):
        """Computes the first publication year for each item."""

        records = records.copy()

        records = records[[field, "year"]].dropna()
        records[field] = (
            records[field].str.split(";").map(lambda x: [_.strip() for _ in x])
        )
        records = records.explode(field)

        records["first_publication_year"] = records.groupby(field)[
            "year"
        ].transform("min")

        records = records.drop("year", axis=1)
        records = records.drop_duplicates()
        records = records.set_index(field)

        indicators.loc[
            records.first_publication_year.index, "first_publication_year"
        ] = records.first_publication_year

        return indicators

    def compute_growth_indicators(indicators):
        """Computes the average growth rate."""

        # computes item occurrences by year
        items_by_year = items_occ_by_year(
            field=field,
            cumulative=False,
            # Database params:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

        # computes the range of years in the time window
        year_end = items_by_year.columns.max()
        year_start = year_end - time_window + 1
        year_columns = list(range(year_start - 1, year_end + 1))

        # computes the number of documents per period by item
        between = f"Between {year_start}-{year_end}"
        before = f"Before {year_start}"
        between_occ = items_by_year.loc[:, year_columns[1:]].sum(axis=1)
        before_occ = items_by_year.sum(axis=1) - between_occ
        indicators.loc[between_occ.index, between] = between_occ
        indicators.loc[before_occ.index, before] = before_occ

        # sort the columns
        columns = ["OCC", before, between] + [
            col
            for col in indicators.columns
            if col not in ["OCC", before, between]
        ]
        indicators = indicators[columns]

        # selects the columns of interest
        items_by_year = items_by_year.loc[:, year_columns]

        # agr: average growth rate
        agr = items_by_year.diff(axis=1)
        agr = agr.loc[:, year_columns[1:]]
        agr = agr.sum(axis=1) / time_window
        indicators.loc[agr.index, "average_growth_rate"] = agr

        # ady: average documents per year
        ady = items_by_year.loc[:, year_columns[1:]].sum(axis=1) / time_window
        indicators.loc[ady.index, "average_docs_per_year"] = ady

        # pdly: percentage of documents in last year
        indicators["percentage_docs_last_year"] = (
            indicators.average_docs_per_year.copy() / indicators.OCC.copy()
        )

        return indicators

    def compute_impact_indicators(records, indicators):
        """Computes the impact indicators."""

        records = records.copy()
        records = records[[field, "global_citations"]].dropna()

        records[field] = records[field].str.split(";")
        records = records.explode(field)
        records[field] = records[field].str.strip()
        records = records.sort_values(
            [field, "global_citations"], ascending=[True, False]
        )
        records = records.reset_index(drop=True)

        records = records.assign(
            cumcount_=records.sort_values("global_citations", ascending=False)
            .groupby(field)
            .cumcount()
            + 1
        )

        records = records.assign(
            cumcount_2=records.cumcount_.map(lambda w: w * w)
        )

        h_indexes = records.query("global_citations >= cumcount_")
        h_indexes = h_indexes.groupby(field, as_index=True).agg(
            {"cumcount_": np.max}
        )
        h_indexes = h_indexes.rename(columns={"cumcount_": "h_index"})
        indicators.loc[h_indexes.index, "h_index"] = h_indexes.astype(int)
        indicators["h_index"] = indicators["h_index"].fillna(0)

        g_indexes = records.query("global_citations >= cumcount_2")
        g_indexes = g_indexes.groupby(field, as_index=True).agg(
            {"cumcount_": np.max}
        )
        g_indexes = g_indexes.rename(columns={"cumcount_": "g_index"})
        indicators.loc[g_indexes.index, "g_index"] = g_indexes.astype(int)
        indicators["g_index"] = indicators["g_index"].fillna(0)

        indicators = indicators.assign(
            m_index=indicators.h_index / indicators.age
        )
        indicators["m_index"] = indicators.m_index.round(decimals=2)

        return indicators

    #
    #
    # Main code:
    #
    #
    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    records["OCC"] = 1

    indicators = extract_items_from_field(records)
    indicators = compute_column_sum_by_item(records, indicators, "OCC")
    indicators = compute_column_sum_by_item(
        records, indicators, "global_citations"
    )
    indicators = compute_column_sum_by_item(
        records, indicators, "local_citations"
    )
    indicators = compute_global_citations_per_document(indicators)
    indicators = compute_local_citations_per_document(indicators)
    indicators = compute_growth_indicators(indicators)
    indicators = compute_first_publication_year(records, indicators)
    indicators = compute_age(records, indicators)
    indicators = compute_global_citations_per_year(indicators)
    indicators = compute_impact_indicators(records, indicators)

    stopwords = load_stopwords(root_dir=root_dir)
    indicators = indicators.drop(stopwords, axis=0)

    indicators = indicators.drop(field, axis=1)
    indicators = indicators.sort_index(axis=0, ascending=True)

    # indicators = indicators.sort_values("OCC", ascending=False)
    # average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |

    return indicators

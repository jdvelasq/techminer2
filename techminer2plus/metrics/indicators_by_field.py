# flake8: noqa
"""
Indicators by Field
===============================================================================


TechMiner2+ computes three growth indicators for each item in a field (usually
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


>>> import techminer2plus
>>> indicators = techminer2plus.metrics.indicators_by_field(
...     field='author_keywords',
...     root_dir=root_dir,
... )
>>> print(indicators.head(30).to_markdown())
| author_keywords           |   rank_occ |   rank_gc |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:--------------------------|-----------:|----------:|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| REGTECH                   |          1 |         1 |    28 |            20 |                   8 |                329 |                74 |                           11.75 |                           2.64 |                  -0.5 |                     4   |                   0.142857  |                     2017 |     7 |                       47    |         9 |         4 |      1.29 |
| FINTECH                   |          2 |         2 |    12 |            10 |                   2 |                249 |                49 |                           20.75 |                           4.08 |                  -0.5 |                     1   |                   0.0833333 |                     2018 |     6 |                       41.5  |         5 |         3 |      0.83 |
| REGULATORY_TECHNOLOGY     |          3 |         8 |     7 |             5 |                   2 |                 37 |                14 |                            5.29 |                           2    |                  -1.5 |                     1   |                   0.142857  |                     2020 |     4 |                        9.25 |         4 |         2 |      1    |
| COMPLIANCE                |          4 |        12 |     7 |             5 |                   2 |                 30 |                 9 |                            4.29 |                           1.29 |                   0   |                     1   |                   0.142857  |                     2019 |     5 |                        6    |         3 |         2 |      0.6  |
| REGULATION                |          5 |         4 |     5 |             4 |                   1 |                164 |                22 |                           32.8  |                           4.4  |                  -0.5 |                     0.5 |                   0.1       |                     2018 |     6 |                       27.33 |         2 |         2 |      0.33 |
| ANTI_MONEY_LAUNDERING     |          6 |        10 |     5 |             5 |                   0 |                 34 |                 8 |                            6.8  |                           1.6  |                  -1.5 |                     0   |                   0         |                     2020 |     4 |                        8.5  |         3 |         2 |      0.75 |
| FINANCIAL_SERVICES        |          7 |         3 |     4 |             3 |                   1 |                168 |                20 |                           42    |                           5    |                   0   |                     0.5 |                   0.125     |                     2017 |     7 |                       24    |         3 |         2 |      0.43 |
| FINANCIAL_REGULATION      |          8 |         9 |     4 |             2 |                   2 |                 35 |                 8 |                            8.75 |                           2    |                   0   |                     1   |                   0.25      |                     2017 |     7 |                        5    |         2 |         2 |      0.29 |
| ARTIFICIAL_INTELLIGENCE   |          9 |        19 |     4 |             3 |                   1 |                 23 |                 6 |                            5.75 |                           1.5  |                   0   |                     0.5 |                   0.125     |                     2019 |     5 |                        4.6  |         3 |         2 |      0.6  |
| RISK_MANAGEMENT           |         10 |        25 |     3 |             2 |                   1 |                 14 |                 8 |                            4.67 |                           2.67 |                   0   |                     0.5 |                   0.166667  |                     2018 |     6 |                        2.33 |         2 |         2 |      0.33 |
| INNOVATION                |         11 |        32 |     3 |             2 |                   1 |                 12 |                 4 |                            4    |                           1.33 |                  -0.5 |                     0.5 |                   0.166667  |                     2020 |     4 |                        3    |         1 |         1 |      0.25 |
| BLOCKCHAIN                |         12 |        59 |     3 |             3 |                   0 |                  5 |                 0 |                            1.67 |                           0    |                  -0.5 |                     0   |                   0         |                     2017 |     7 |                        0.71 |         1 |         1 |      0.14 |
| SUPTECH                   |         13 |        60 |     3 |             1 |                   2 |                  4 |                 2 |                            1.33 |                           0.67 |                   0   |                     1   |                   0.333333  |                     2019 |     5 |                        0.8  |         1 |         1 |      0.2  |
| SEMANTIC_TECHNOLOGIES     |         14 |         7 |     2 |             2 |                   0 |                 41 |                19 |                           20.5  |                           9.5  |                   0   |                     0   |                   0         |                     2018 |     6 |                        6.83 |         2 |         2 |      0.33 |
| DATA_PROTECTION           |         15 |        13 |     2 |             1 |                   1 |                 27 |                 5 |                           13.5  |                           2.5  |                   0   |                     0.5 |                   0.25      |                     2020 |     4 |                        6.75 |         2 |         1 |      0.5  |
| SMART_CONTRACTS           |         16 |        20 |     2 |             2 |                   0 |                 22 |                 8 |                           11    |                           4    |                   0   |                     0   |                   0         |                     2017 |     7 |                        3.14 |         1 |         1 |      0.14 |
| CHARITYTECH               |         17 |        23 |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                   0.25      |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| ENGLISH_LAW               |         18 |        24 |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                   0.25      |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| ACCOUNTABILITY            |         19 |        26 |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                   0         |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| DATA_PROTECTION_OFFICER   |         20 |        27 |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                   0         |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| GDPR                      |         21 |        28 |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                   0         |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| SANDBOXES                 |         22 |        33 |     2 |             2 |                   0 |                 12 |                 3 |                            6    |                           1.5  |                  -0.5 |                     0   |                   0         |                     2017 |     7 |                        1.71 |         1 |         1 |      0.14 |
| TECHNOLOGY                |         23 |        44 |     2 |             1 |                   1 |                 10 |                 3 |                            5    |                           1.5  |                   0   |                     0.5 |                   0.25      |                     2020 |     4 |                        2.5  |         1 |         1 |      0.25 |
| FINANCE                   |         24 |        96 |     2 |             1 |                   1 |                  1 |                 0 |                            0.5  |                           0    |                   0   |                     0.5 |                   0.25      |                     2020 |     4 |                        0.25 |         1 |         1 |      0.25 |
| REPORTING                 |         25 |        97 |     2 |             0 |                   2 |                  1 |                 0 |                            0.5  |                           0    |                   0   |                     1   |                   0.5       |                     2022 |     2 |                        0.5  |         1 |         1 |      0.5  |
| BUSINESS_MODELS           |         26 |         5 |     1 |             1 |                   0 |                153 |                17 |                          153    |                          17    |                   0   |                     0   |                   0         |                     2018 |     6 |                       25.5  |         1 |         1 |      0.17 |
| FUTURE_RESEARCH_DIRECTION |         27 |         6 |     1 |             1 |                   0 |                153 |                17 |                          153    |                          17    |                   0   |                     0   |                   0         |                     2018 |     6 |                       25.5  |         1 |         1 |      0.17 |
| STANDARDS                 |         28 |        11 |     1 |             1 |                   0 |                 33 |                14 |                           33    |                          14    |                   0   |                     0   |                   0         |                     2019 |     5 |                        6.6  |         1 |         1 |      0.2  |
| DIGITAL_IDENTITY          |         29 |        14 |     1 |             1 |                   0 |                 24 |                 5 |                           24    |                           5    |                   0   |                     0   |                   0         |                     2020 |     4 |                        6    |         1 |         1 |      0.25 |
| EUROPEAN_UNION            |         30 |        15 |     1 |             1 |                   0 |                 24 |                 5 |                           24    |                           5    |                   0   |                     0   |                   0         |                     2020 |     4 |                        6    |         1 |         1 |      0.25 |



# pylint: disable=line-too-long
"""

import numpy as np

from ..records import read_records
from ..sorting import sort_indicators_by_metric
from ..stopwords import load_stopwords
from .items_occ_by_year import items_occ_by_year


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
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
    # indicators = indicators.sort_index(axis=0, ascending=True)

    indicators = sort_indicators_by_metric(indicators, "global_citations")
    indicators.insert(0, "rank_gc", range(1, len(indicators) + 1))

    indicators = sort_indicators_by_metric(indicators, "OCC")
    indicators.insert(0, "rank_occ", range(1, len(indicators) + 1))

    return indicators

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Indicators by Field
===============================================================================

>>> from techminer2.indicators import global_indicators_by_field
>>> indicators = global_indicators_by_field(
...     #
...     # METRICS PARAMS:
...     field='author_keywords',
...     time_window=2,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(indicators.head().to_markdown())
| author_keywords      |   rank_occ |   rank_lcs |   rank_gcs |   OCC |   before_2018 |   between_2018_2019 |   growth_percentage |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:---------------------|-----------:|-----------:|-----------:|------:|--------------:|--------------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| FINTECH              |          1 |          1 |          1 |    31 |            13 |                  18 |               58.06 |               5168 |                27 |                          166.71 |                           0.87 |                  -1   |                     9   |                   0.290323  |                     2016 |     4 |                     1292    |        31 |        12 |      7.75 |
| INNOVATION           |          2 |          2 |          2 |     7 |             6 |                   1 |               14.29 |                911 |                 5 |                          130.14 |                           0.71 |                  -1.5 |                     0.5 |                   0.0714286 |                     2016 |     4 |                      227.75 |         7 |         7 |      1.75 |
| FINANCIAL_SERVICES   |          3 |         40 |          5 |     4 |             1 |                   3 |               75    |                667 |                 1 |                          166.75 |                           0.25 |                   0   |                     1.5 |                   0.375     |                     2016 |     4 |                      166.75 |         4 |         4 |      1    |
| FINANCIAL_TECHNOLOGY |          4 |         41 |         12 |     4 |             1 |                   3 |               75    |                551 |                 1 |                          137.75 |                           0.25 |                   0.5 |                     1.5 |                   0.375     |                     2017 |     3 |                      183.67 |         4 |         4 |      1.33 |
| BUSINESS             |          5 |         10 |          3 |     3 |             0 |                   3 |              100    |                896 |                 3 |                          298.67 |                           1    |                   0   |                     1.5 |                   0.5       |                     2018 |     2 |                      448    |         3 |         3 |      1.5  |



"""

#
# TechMiner2+ computes three growth indicators for each item in a field (usually
# keywords or noun phrases):
#
# * Average growth rate (AGR):
#
# .. code-block::
#
#            sum_{i=Y_start}^Y_end  Num_Documents[i] - Num_Documents[i-1]
#     AGR = --------------------------------------------------------------
#                             Y_end - Y_start + 1
#
#
# * Average documents per year (ADY):
#
# .. code-block::
#
#            sum_{i=Y_start}^Y_end  Num_Documents[i]
#     ADY = -----------------------------------------
#                     Y_end - Y_start + 1
#
#
# * Percentage of documents in last year (PDLY):
#
# .. code-block::
#
#            sum_{i=Y_start}^Y_end  Num_Documents[i]      1
#     PDLY = ---------------------------------------- * _____
#                   Y_end - Y_start + 1                  TND
#
# With:
#
# .. code-block::
#
#     Y_start = Y_end - time_window + 1
#
# If ``Y_end = 2018`` and ``time_window = 2``, then ``Y_start = 2017``.
#


from .._common._sorting_lib import sort_indicators_by_metric
from .._read_records import read_records
from .._stopwords import load_stopwords
from .items_occurrences_by_year import items_occurrences_by_year


def global_indicators_by_field(
    #
    # METRICS PARAMS:
    field,
    time_window=2,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Bibliometric column indicators."""

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
            column_sum[field].str.split(";").map(lambda x: [_.strip() for _ in x])
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
            age=(records.year.max() - indicators.first_publication_year + 1).astype(int)
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

        records["first_publication_year"] = records.groupby(field)["year"].transform(
            "min"
        )

        records = records.drop("year", axis=1)
        records = records.drop_duplicates()
        records = records.set_index(field)

        indicators.loc[
            records.first_publication_year.index, "first_publication_year"
        ] = records.first_publication_year

        return indicators

    def compute_growth_indicators(indicators):
        """Computes growth indicators."""

        #
        # Computes item occurrences by year
        items_by_year = items_occurrences_by_year(
            #
            # FUNCTION PARAMS:
            field=field,
            cumulative=False,
            #
            # DATABASE PARAMS:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

        #
        # Computes the range of years in the time window
        year_end = items_by_year.columns.max()
        year_start = year_end - time_window + 1
        year_columns = list(range(year_start, year_end + 1))

        #
        # TODO: CHECK
        if items_by_year.columns.max() - items_by_year.columns.min() <= time_window:
            return indicators
        #

        #
        # Computes the number of documents per period by item
        between = f"between_{year_start}_{year_end}"
        before = f"before_{year_start}"
        between_occ = items_by_year.loc[:, year_columns].sum(axis=1)
        before_occ = items_by_year.sum(axis=1) - between_occ
        indicators.loc[between_occ.index, between] = between_occ
        indicators.loc[before_occ.index, before] = before_occ

        indicators = indicators.assign(
            growth_percentage=(
                100 * indicators[between].copy() / indicators["OCC"].copy()
            ).round(2)
        )

        #
        # sort the columns
        columns = ["OCC", before, between, "growth_percentage"] + [
            col
            for col in indicators.columns
            if col not in ["OCC", before, between, "growth_percentage"]
        ]
        indicators = indicators[columns]

        #
        # selects the columns of interest
        items_by_year = items_by_year.loc[:, [year_columns[0] - 1] + year_columns]

        # agr: average growth rate
        agr = items_by_year.diff(axis=1)
        agr = agr.loc[:, year_columns]
        agr = agr.sum(axis=1) / time_window
        indicators.loc[agr.index, "average_growth_rate"] = agr

        # ady: average documents per year
        ady = items_by_year.loc[:, year_columns].sum(axis=1) / time_window
        indicators.loc[ady.index, "average_docs_per_year"] = ady

        # pdly: percentage of documents in last year
        indicators = indicators.assign(
            percentage_docs_last_year=(
                indicators.average_docs_per_year.copy() / indicators.OCC.copy()
            )
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

        records = records.assign(cumcount_2=records.cumcount_.map(lambda w: w * w))

        h_indexes = records.query("global_citations >= cumcount_")
        h_indexes = h_indexes.groupby(field, as_index=True).agg({"cumcount_": "max"})
        h_indexes = h_indexes.rename(columns={"cumcount_": "h_index"})
        indicators.loc[h_indexes.index, "h_index"] = h_indexes.astype(int)
        indicators["h_index"] = indicators["h_index"].fillna(0)

        g_indexes = records.query("global_citations >= cumcount_2")
        g_indexes = g_indexes.groupby(field, as_index=True).agg({"cumcount_": "max"})
        g_indexes = g_indexes.rename(columns={"cumcount_": "g_index"})
        indicators.loc[g_indexes.index, "g_index"] = g_indexes.astype(int)
        indicators["g_index"] = indicators["g_index"].fillna(0)

        indicators = indicators.assign(m_index=indicators.h_index / indicators.age)
        indicators["m_index"] = indicators.m_index.round(decimals=2)

        return indicators

    #
    #
    # MAIN CODE:
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
    indicators = compute_column_sum_by_item(records, indicators, "global_citations")
    indicators = compute_column_sum_by_item(records, indicators, "local_citations")
    indicators = compute_global_citations_per_document(indicators)
    indicators = compute_local_citations_per_document(indicators)
    indicators = compute_growth_indicators(indicators)
    indicators = compute_first_publication_year(records, indicators)
    indicators = compute_age(records, indicators)
    indicators = compute_global_citations_per_year(indicators)
    indicators = compute_impact_indicators(records, indicators)

    stopwords = load_stopwords(root_dir=root_dir)
    indicators = indicators.drop(stopwords, axis=0, errors="ignore")

    indicators = indicators.drop(field, axis=1)
    # indicators = indicators.sort_index(axis=0, ascending=True)

    indicators = sort_indicators_by_metric(indicators, "global_citations")
    indicators.insert(0, "rank_gcs", range(1, len(indicators) + 1))

    indicators = sort_indicators_by_metric(indicators, "local_citations")
    indicators.insert(0, "rank_lcs", range(1, len(indicators) + 1))

    indicators = sort_indicators_by_metric(indicators, "OCC")
    indicators.insert(0, "rank_occ", range(1, len(indicators) + 1))

    if "OCC" in indicators.columns:
        indicators["OCC"] = indicators["OCC"].astype(int)

    if "global_citations" in indicators.columns:
        indicators["global_citations"] = indicators["global_citations"].astype(int)

    if "local_citations" in indicators.columns:
        indicators["local_citations"] = indicators["local_citations"].astype(int)

    if "h_index" in indicators.columns:
        indicators["h_index"] = indicators["h_index"].astype(int)

    if "g_index" in indicators.columns:
        indicators["g_index"] = indicators["g_index"].astype(int)

    return indicators

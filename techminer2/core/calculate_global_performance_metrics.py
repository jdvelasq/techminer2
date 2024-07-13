# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
This function computes global performance (bibliometric) metrics for a given field.


"""
from .sort_records_by_metric import sort_records_by_metric
from .stopwords.load_user_stopwords import load_user_stopwords
from .read_filtered_database import read_filtered_database


def calculate_global_performance_metrics(
    #
    # FIELD PARAMS
    field: str,
    #
    # DATABASE PARAMS
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """:meta private:"""

    records = read_filtered_database(
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    records["OCC"] = 1

    # --------------------------------------------------------------------------------------------
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

    indicators = extract_items_from_field(records)

    # --------------------------------------------------------------------------------------------
    def compute_column_sum_by_item(records, indicators, column):
        """Computes global citations from database and adds the column to indicators."""

        records = records.copy()

        column_sum = records[[field, column]].dropna()
        column_sum[field] = column_sum[field].str.split(";").map(lambda x: [_.strip() for _ in x])
        column_sum = column_sum.explode(field)
        column_sum = column_sum.groupby(field, as_index=True).sum().astype(int)
        indicators.loc[column_sum.index, column] = column_sum

        return indicators

    indicators = compute_column_sum_by_item(records, indicators, "OCC")
    indicators = compute_column_sum_by_item(records, indicators, "global_citations")
    indicators = compute_column_sum_by_item(records, indicators, "local_citations")

    # --------------------------------------------------------------------------------------------
    def compute_global_citations_per_document(indicators):
        indicators = indicators.copy()
        indicators = indicators.assign(
            global_citations_per_document=(indicators.global_citations / indicators.OCC).round(2)
        )
        return indicators

    indicators = compute_global_citations_per_document(indicators)

    # --------------------------------------------------------------------------------------------
    def compute_local_citations_per_document(indicators):
        indicators = indicators.copy()
        indicators = indicators.assign(
            local_citations_per_document=(indicators.local_citations / indicators.OCC).round(2)
        )
        return indicators

    indicators = compute_local_citations_per_document(indicators)

    # --------------------------------------------------------------------------------------------
    def compute_first_publication_year(records, indicators):
        """Computes the first publication year for each item."""

        records = records.copy()

        records = records[[field, "year"]].dropna()
        records[field] = records[field].str.split(";").map(lambda x: [_.strip() for _ in x])
        records = records.explode(field)

        records["first_publication_year"] = records.groupby(field)["year"].transform("min")

        records = records.drop("year", axis=1)
        records = records.drop_duplicates()
        records = records.set_index(field)

        indicators.loc[records.first_publication_year.index, "first_publication_year"] = (
            records.first_publication_year
        )

        return indicators

    indicators = compute_first_publication_year(records, indicators)

    # --------------------------------------------------------------------------------------------
    def compute_age(records, indicators):
        indicators = indicators.copy()
        indicators = indicators.assign(
            age=(records.year.max() - indicators.first_publication_year + 1).astype(int)
        )
        return indicators

    indicators = compute_age(records, indicators)

    # --------------------------------------------------------------------------------------------
    def compute_global_citations_per_year(indicators):
        """Computes the global citations per year."""

        indicators = indicators.copy()
        indicators = indicators.assign(
            global_citations_per_year=(indicators.global_citations / indicators.age).round(2)
        )

        return indicators

    indicators = compute_global_citations_per_year(indicators)

    # --------------------------------------------------------------------------------------------
    def compute_impact_indicators(records, indicators):
        """Computes the impact indicators."""

        records = records.copy()
        records = records[[field, "global_citations"]].dropna()

        records[field] = records[field].str.split(";")
        records = records.explode(field)
        records[field] = records[field].str.strip()
        records = records.sort_values([field, "global_citations"], ascending=[True, False])
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

    indicators = compute_impact_indicators(records, indicators)

    # --------------------------------------------------------------------------------------------
    def remove_stopwords(indicators):
        stopwords = load_user_stopwords(root_dir=root_dir)
        indicators = indicators.drop(stopwords, axis=0, errors="ignore")
        indicators = indicators.drop(field, axis=1)
        return indicators

    indicators = remove_stopwords(indicators)

    # --------------------------------------------------------------------------------------------
    def compute_ranks(indicators):
        indicators = sort_records_by_metric(indicators, "global_citations")
        indicators.insert(0, "rank_gcs", range(1, len(indicators) + 1))

        indicators = sort_records_by_metric(indicators, "local_citations")
        indicators.insert(0, "rank_lcs", range(1, len(indicators) + 1))

        indicators = sort_records_by_metric(indicators, "OCC")
        indicators.insert(0, "rank_occ", range(1, len(indicators) + 1))
        return indicators

    indicators = compute_ranks(indicators)

    # --------------------------------------------------------------------------------------------
    def check_types(indicators):
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

    indicators = check_types(indicators)
    # --------------------------------------------------------------------------------------------

    return indicators

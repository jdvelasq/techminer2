"""Obtain articles per cluster.

"""
from ...records import read_records


def obtain_records_per_cluster(articles_per_cluster, coupling_matrix):
    """Obtain records"""

    records = read_records(
        root_dir=coupling_matrix.root_dir_,
        database=coupling_matrix.database_,
        year_filter=coupling_matrix.year_filter_,
        cited_by_filter=coupling_matrix.cited_by_filter_,
        **coupling_matrix.filters_,
    )

    records_per_cluster = {}

    for cluster, articles in articles_per_cluster.items():
        selected_records = records[records.article.isin(articles)]
        selected_records = selected_records.sort_values(
            ["global_citations", "local_citations", "year"],
            ascending=False,
        )
        records_per_cluster[cluster] = selected_records.copy()

    return records_per_cluster

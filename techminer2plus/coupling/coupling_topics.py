# flake8: noqa
"""
Coupling Topics
===============================================================================

>>> ROOT_DIR = "data/regtech/"

>>> import techminer2plus
>>> coupling_matrix = techminer2plus.analyze.coupling.coupling_matrix(
...     field="author_keywords",
...     top_n=20,
...     root_dir=ROOT_DIR,
... )
>>> graph = techminer2plus.analyze.coupling.coupling_network(
...    coupling_matrix,
...    algorithm_or_estimator="louvain",
... )
>>> print( coupling_topics(
...     graph,
...     coupling_matrix,
... ).to_markdown())
|    | CL_00                        | CL_02                     | CL_01                        |
|---:|:-----------------------------|:--------------------------|:-----------------------------|
|  0 | REGTECH 23:278               | FINANCIAL_REGULATION 4:35 | REGULATORY_TECHNOLOGY 7:37   |
|  1 | FINTECH 10:224               | REGTECH 2:35              | ANTI_MONEY_LAUNDERING 5:34   |
|  2 | COMPLIANCE 6:29              | FINANCIAL_SERVICES 2:11   | ARTIFICIAL_INTELLIGENCE 3:20 |
|  3 | REGULATION 4:163             | DATA_PROTECTION 1:24      | REGTECH 3:16                 |
|  4 | BLOCKCHAIN 3:5               | FINTECH 1:24              | RISK_MANAGEMENT 2:6          |
|  5 | FINANCIAL_SERVICES 2:157     | INNOVATION 1:0            | CHARITYTECH 1:14             |
|  6 | SEMANTIC_TECHNOLOGIES 2:41   |                           | ENGLISH_LAW 1:14             |
|  7 | SMART_CONTRACTS 2:22         |                           | INNOVATION 1:11              |
|  8 | ACCOUNTABILITY 2:14          |                           | COMPLIANCE 1:1               |
|  9 | DATA_PROTECTION_OFFICER 2:14 |                           | FINTECH 1:1                  |
| 10 | SUPTECH 2:3                  |                           | REGULATION 1:1               |
| 11 | RISK_MANAGEMENT 1:8          |                           | SUPTECH 1:1                  |
| 12 | ARTIFICIAL_INTELLIGENCE 1:3  |                           |                              |
| 13 | CHARITYTECH 1:3              |                           |                              |
| 14 | DATA_PROTECTION 1:3          |                           |                              |
| 15 | ENGLISH_LAW 1:3              |                           |                              |
| 16 | INNOVATION 1:1               |                           |                              |



# pylint: disable=line-too-long
"""
import pandas as pd

# from .extract_articles_per_cluster import extract_articles_per_cluster
# from .obtain_records_per_cluster import obtain_records_per_cluster


def coupling_topics(
    graph,
    coupling_matrix,
):
    """Coupling Abstracts Report."""

    def compute_topics_per_cluster(records):
        records = records.copy()
        field = coupling_matrix.field_
        records = records.dropna(subset=[field])
        records = records[["article", field, "global_citations"]]
        records[field] = records[field].str.split("; ")
        records = records.explode(field)
        records[field] = records[field].str.strip()

        records = records.loc[records[field].isin(coupling_matrix.topics_)]

        records["OCC"] = 1
        records = records.groupby([field]).sum().reset_index()
        records = records.sort_values(
            ["OCC", "global_citations"], ascending=False
        )
        topics = (
            records[field]
            + " "
            + records.OCC.astype(int).astype(str)
            + ":"
            + records.global_citations.astype(int).astype(str)
        )
        return topics.to_list()

    #
    # Main code:
    #
    articles_per_cluster = extract_articles_per_cluster(graph)
    records_per_cluster = obtain_records_per_cluster(
        articles_per_cluster, coupling_matrix
    )

    topics_per_cluster = {}
    for cluster, records in records_per_cluster.items():
        topics_per_cluster[cluster] = compute_topics_per_cluster(records)

    clusters_table = pd.DataFrame.from_dict(
        topics_per_cluster, orient="index"
    ).T
    clusters_table = clusters_table.fillna("")
    return clusters_table

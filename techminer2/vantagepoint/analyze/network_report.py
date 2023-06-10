# flake8: noqa
"""
Network Report
===============================================================================



Example:
-------------------------------------------------------------------------------


>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occurrence_matrix(
...    columns='author_keywords',
...    col_occ_range=(2, None),
...    root_dir=root_dir,
... )
>>> graph = vantagepoint.analyze.cluster_field(
...    co_occ_matrix,
...    community_clustering='louvain',
... )
>>> print(vantagepoint.analyze.cluster_members(graph).to_markdown())
|    | CL_00                          | CL_01                       | CL_02                        | CL_03                          |
|---:|:-------------------------------|:----------------------------|:-----------------------------|:-------------------------------|
|  0 | REGTECH 28:329                 | FINTECH 12:249              | REGULATORY_TECHNOLOGY 07:037 | ANTI_MONEY_LAUNDERING 05:034   |
|  1 | COMPLIANCE 07:030              | FINANCIAL_SERVICES 04:168   | REGULATION 05:164            | ARTIFICIAL_INTELLIGENCE 04:023 |
|  2 | BLOCKCHAIN 03:005              | FINANCIAL_REGULATION 04:035 | RISK_MANAGEMENT 03:014       | CHARITYTECH 02:017             |
|  3 | SMART_CONTRACTS 02:022         | INNOVATION 03:012           | SUPTECH 03:004               | ENGLISH_LAW 02:017             |
|  4 | ACCOUNTABILITY 02:014          | DATA_PROTECTION 02:027      | SEMANTIC_TECHNOLOGIES 02:041 |                                |
|  5 | DATA_PROTECTION_OFFICER 02:014 | SANDBOX 02:012              | REPORTING 02:001             |                                |
|  6 | GDPR 02:014                    | FINANCE 02:001              |                              |                                |
|  7 | TECHNOLOGY 02:010              |                             |                              |                                |



>>> vantagepoint.analyze.network_report(
...     graph,
...     field='author_keywords',
...     report_dir='network_report',
...     root_dir=root_dir,
... )
--INFO-- The file 'data/regtech/reports/network_report/CL_00_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report/CL_01_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report/CL_02_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report/CL_03_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report/CL_00_gpt_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report/CL_01_gpt_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report/CL_02_gpt_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report/CL_03_gpt_prompt.txt' was created.




# pylint: disable=line-too-long
"""
import os
import os.path
import pathlib
import textwrap
from collections import defaultdict

import pandas as pd

from ...network_utils import extract_communities_from_graph
from ...record_utils import create_records_report, read_records
from ...tlab.concordances import concordances


def network_report(
    graph,
    field,
    report_dir,
    # Concordances
    top_n=100,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Generes"""

    make_report_dir(root_dir, report_dir)

    communities = extract_communities_from_graph(
        graph, conserve_counters=False
    )

    assign_records_to_clusters(
        communities=communities,
        field=field,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    genereate_concordances_report(
        communities=communities,
        top_n=top_n,
        report_dir=report_dir,
        # Database params:
        root_dir=root_dir,
    )

    generate_abstracts_report(
        communities=communities,
        report_dir=report_dir,
        # Database params:
        root_dir=root_dir,
    )

    generate_chatgpt_prompt(
        communities=communities,
        report_dir=report_dir,
        # Database params:
        root_dir=root_dir,
    )


def generate_chatgpt_prompt(
    communities,
    report_dir,
    # Database params:
    root_dir,
    # database,
    # year_filter,
    # cited_by_filter,
    # **filters,
):
    """ChatGPT prompt."""

    for cluster in communities:
        cluster_file = f"_CLUSTER_{cluster[-2:]}_"

        records = read_records(
            root_dir=root_dir,
            database=cluster_file,
            # year_filter=year_filter,
            # cited_by_filter=cited_by_filter,
            # **filters,
        )

        file_name = f"{cluster}_gpt_prompt.txt"
        file_path = os.path.join(root_dir, "reports", report_dir, file_name)

        abstracts = records[["abstract", "global_citations"]].dropna()
        max_citations = abstracts["global_citations"].max()
        # abstracts["global_citations"] = (
        #     abstracts["global_citations"].astype(float) / max_citations
        # )
        # abstracts["global_citations"] = abstracts["global_citations"].round(3)
        weights = abstracts["global_citations"].to_list()
        abstracts = abstracts["abstract"]

        abstracts = abstracts.map(
            lambda x: textwrap.fill(x, width=70).replace("\n", " \\\n")
        )
        abstracts = abstracts.to_list()

        with open(file_path, "w", encoding="utf-8") as file:
            print(
                "Your task is to summarize in only one pargraph the following \\\n"
                "text weighted by the  number of citations. The more citations, \\\n"
                "the more important the text is. Your summary should capture \\\n"
                "the central idea of the  all text, in at most 200 words.\n\n"
                "Summarize the text below, delimited by triple backticks:\n\n",
                file=file,
            )

            for i_abstract, (abstract, weight) in enumerate(
                zip(abstracts, weights)
            ):
                print(
                    f"Paragraph {i_abstract + 1} (Citations: {weight})",
                    file=file,
                )
                print(f"```\n{abstract}\n```\n\n", file=file)

            print(f"--INFO-- The file '{file_path}' was created.")


def generate_abstracts_report(
    communities,
    report_dir,
    # Database params:
    root_dir,
    # database,
    # year_filter,
    # cited_by_filter,
    # **filters,
):
    """Generates records report."""

    for cluster in communities:
        cluster_file = f"_CLUSTER_{cluster[-2:]}_"

        records = read_records(
            root_dir=root_dir,
            database=cluster_file,
            # year_filter=year_filter,
            # cited_by_filter=cited_by_filter,
            # **filters,
        )

        file_name = f"{cluster}_abstracts_report.txt"
        create_records_report(
            root_dir=root_dir,
            target_dir=report_dir,
            records=records,
            report_filename=file_name,
        )


def genereate_concordances_report(
    communities,
    top_n,
    report_dir,
    # Database params:
    root_dir,
    # database,
    # year_filter,
    # cited_by_filter,
    # **filters,
):
    """Generates concordances report."""

    for cluster, members in communities.items():
        for i_member, member in enumerate(members):
            report_file = os.path.join(
                report_dir,
                f"{cluster}_{i_member:>02d}_{member}_concordances_report.txt",
            )
            prompt_file = os.path.join(
                report_dir,
                f"{cluster}_{i_member:>02d}_{member}_concordances_prompt.txt",
            )
            cluster_file = f"_CLUSTER_{cluster[-2:]}_"
            concordances(
                search_for=member,
                top_n=top_n,
                report_file=report_file,
                prompt_file=prompt_file,
                # Database params:
                root_dir=root_dir,
                database=cluster_file,
                # year_filter=year_filter,
                # cited_by_filter=cited_by_filter,
                # **filters,
            )


def make_report_dir(root_dir, report_dir):
    """Make report directory."""

    report_path = os.path.join(root_dir, "reports", report_dir)

    if os.path.exists(report_path):
        for root, dirs, files in os.walk(report_path, topdown=False):
            for filename in files:
                if filename.endswith(""):
                    os.remove(os.path.join(root, filename))
            for dirname in dirs:
                if dirname.endswith(""):
                    os.rmdir(os.path.join(root, dirname))
        os.rmdir(report_path)
    os.makedirs(report_path)

    for directory in ["databases", "reports"]:
        directory_path = os.path.join(root_dir, directory)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)


def assign_records_to_clusters(
    communities,
    field,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Assigns records to clusters."""

    #
    # clusters is a dict of lists with terms in each cluster
    #

    def convert_cluster_to_items_dict(communities):
        """Converts the cluster to items dict."""

        items2cluster = {}
        for cluster, items in communities.items():
            for item in items:
                items2cluster[item] = cluster

        return items2cluster

    def explode_field(records, field):
        """Explodes records."""

        records = records.copy()
        records = records[field]
        records = records.dropna()
        records = records.str.split("; ").explode().map(lambda w: w.strip())

        return records

    def select_valid_records(records, clusters):
        """Selects valid records."""

        community_terms = []
        for cluster in clusters.values():
            community_terms.extend(cluster)

        records = records.copy()
        records = records[records.isin(community_terms)]

        return records

    def assign_points_to_records(records, field, clusters):
        """Assigns points to records."""

        def compute_cluster(data):
            """Computes the cluster most frequent in a list."""

            counter = defaultdict(int)
            for cluster in data:
                counter[cluster] += 1
            return max(counter, key=counter.get)

        records = records.to_frame()
        records["clusters"] = records[field].map(clusters)
        # records["article"] = records.index.to_list()
        records = records.groupby("article").agg({"clusters": list})
        records["clusters"] = records["clusters"].apply(lambda x: sorted(x))
        records["cluster"] = records["clusters"].map(compute_cluster)

        return records

    #
    # Main code:
    #

    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    records.index = records.article

    items2cluster = convert_cluster_to_items_dict(communities)
    exploded_records = explode_field(records, field)
    selected_records = select_valid_records(exploded_records, communities)
    selected_records = assign_points_to_records(
        selected_records, field, items2cluster
    )

    # not include more parameters to avoid destroy the database.
    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    records.index = records.article

    records["_CLUSTER_"] = pd.NA
    records.loc[selected_records.index, "_CLUSTER_"] = selected_records[
        "cluster"
    ]

    database_dir = pathlib.Path(root_dir) / "databases"
    files = list(database_dir.glob("_CLUSTER_*_.csv"))
    for file in files:
        os.remove(file)

    n_clusters = len(communities)
    for i_cluster in range(n_clusters):
        clustered_records = records[
            records._CLUSTER_ == f"CL_{i_cluster:>02d}"
        ]
        clustered_records = clustered_records.sort_values(
            ["global_citations", "local_citations"],
            ascending=[False, False],
        )

        file_name = f"_CLUSTER_{i_cluster:>02d}_.csv"
        file_path = os.path.join(root_dir, "databases", file_name)
        clustered_records.to_csv(file_path, index=False, encoding="utf-8")

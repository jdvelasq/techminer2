# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Network Report
===============================================================================


* Preparation

>>> import techminer2 as tm2
>>> root_dir = "data/regtech/"

* Object oriented interface

>>> (
...     tm2p.records(root_dir=root_dir)
...     .co_occurrence_matrix(
...         columns='author_keywords',
...         col_top_n=20,
...     )
...     .network_create(
...         algorithm_or_estimator="louvain",
...     )
...     .network_report(
...         report_dir='network_report_0',
...     )
... )
--INFO-- The file 'data/regtech/reports/network_report_0/CL_00_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report_0/CL_01_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report_0/CL_02_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report_0/CL_03_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report_0/CL_00_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report_0/CL_01_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report_0/CL_02_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report_0/CL_03_prompt.txt' was created.


* Functional interface

>>> cooc_matrix = tm2p.co_occurrence_matrix(
...    columns='author_keywords',
...    col_top_n=20,
...    root_dir=root_dir,
... )
>>> network = tm2p.network_create(
...     cooc_matrix,
...     algorithm_or_estimator='louvain',
...     root_dir=root_dir,
... )
>>> network_report(
...     network, 
...     report_dir='network_report_1',
...     root_dir=root_dir,
... )
--INFO-- The file 'data/regtech/reports/network_report_1/CL_00_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report_1/CL_01_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report_1/CL_02_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report_1/CL_03_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report_1/CL_00_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report_1/CL_01_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report_1/CL_02_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report_1/CL_03_prompt.txt' was created.

"""
import os
import os.path
import textwrap
from collections import defaultdict

import pandas as pd

from ._read_records import read_records
from .format_prompt_for_records import format_prompt_for_records
from .format_report_for_records import format_report_for_records
from .make_report_dir import make_report_dir
from .nx_extract_communities_as_dict import nx_extract_communities_as_dict
from .search.concordances import concordances_from_records

TEXTWRAP_WIDTH = 73


def nx_create_co_occurrences_report(
    #
    # REPORT PARAMS:
    nx_graph,
    rows_and_columns,
    report_dir,
    top_n=100,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Generes"""

    make_report_dir(root_dir, report_dir)

    communities = nx_extract_communities_as_dict(nx_graph, conserve_counters=False)

    records_per_cluster = __extract_records_per_cluster(
        communities=communities,
        field=rows_and_columns,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    __genereate_concordances_report(
        communities=communities,
        records_per_cluster=records_per_cluster,
        top_n=top_n,
        report_dir=report_dir,
        root_dir=root_dir,
    )

    __generate_records_report(
        communities=communities,
        records_per_cluster=records_per_cluster,
        report_dir=report_dir,
        root_dir=root_dir,
    )

    __generate_records_prompt(
        communities=communities,
        records_per_cluster=records_per_cluster,
        report_dir=report_dir,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )


def __extract_records_per_cluster(
    communities,
    field,
    # Database params:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    """Return a dictionary of records per cluster."""

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

    def create_raw_cluster_field(records, field, clusters):
        """Adds a cluster field with non unique elements."""

        records = records.to_frame()
        records["clusters"] = records[field].map(clusters)
        # records["article"] = records.index.to_list()
        records = records.groupby("article").agg({"clusters": list})
        records["clusters"] = records["clusters"].apply(lambda x: sorted(x)).str.join("; ")

        return records

    def compute_cluster(list_of_clusters):
        """Computes the cluster most frequent in a list."""

        counter = defaultdict(int)
        for cluster in list_of_clusters:
            counter[cluster] += 1
        return max(counter, key=counter.get)

    #
    # Main code:
    #

    records_main = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    records_main.index = pd.Index(records_main.article)

    items2cluster = convert_cluster_to_items_dict(communities)
    exploded_records = explode_field(records_main, field)
    selected_records = select_valid_records(exploded_records, communities)
    selected_records = create_raw_cluster_field(selected_records, field, items2cluster)

    records_main = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    records_main.index = pd.Index(records_main.article)

    records_main["RAW_CLUSTERS"] = pd.NA
    records_main.loc[records_main.index, "RAW_CLUSTERS"] = selected_records["clusters"]
    records_main["_CLUSTERS_"] = records_main["RAW_CLUSTERS"]
    records_main = records_main.dropna(subset=["_CLUSTERS_"])
    records_main["_CLUSTERS_"] = (
        records_main["_CLUSTERS_"]
        .str.split("; ")
        .map(lambda x: [z.strip() for z in x])
        .map(set)
        .str.join("; ")
    )

    records_main["ASSIGNED_CLUSTER"] = (
        records_main["RAW_CLUSTERS"]
        .str.split("; ")
        .map(lambda x: [z.strip() for z in x])
        .map(compute_cluster)
    )

    clusters = records_main["ASSIGNED_CLUSTER"].dropna().drop_duplicates().to_list()

    records_per_cluster = {}

    for cluster in clusters:
        clustered_records = records_main[records_main.ASSIGNED_CLUSTER == cluster].copy()
        clustered_records = clustered_records.sort_values(
            ["global_citations", "local_citations", "year", "authors"],
            ascending=[False, False, False, True],
        )

        records_per_cluster[cluster] = clustered_records.copy()

    return records_per_cluster


def __genereate_concordances_report(
    communities,
    records_per_cluster,
    top_n,
    report_dir,
    root_dir,
):
    """Generates concordances report."""

    for cluster, members in communities.items():
        for i_member, member in enumerate(members):
            #
            #
            report_file = os.path.join(
                report_dir,
                f"{cluster}_{i_member:>02d}_{member}_concordances_report.txt",
            )

            prompt_file = os.path.join(
                report_dir,
                f"{cluster}_{i_member:>02d}_{member}_concordances_prompt.txt",
            )

            concordances_from_records(
                search_for=member,
                top_n=top_n,
                report_file=report_file,
                prompt_file=prompt_file,
                root_dir=root_dir,
                records=records_per_cluster[cluster],
            )


def __generate_records_prompt(
    communities,
    records_per_cluster,
    report_dir,
    root_dir,
):
    """ChatGPT prompt."""

    for cluster in sorted(communities.keys()):
        # -------------------------------------------------------------------------------------
        # Terms:
        terms = "; ".join(communities[cluster][:10])

        #
        # Main text:
        text = (
            "You are an automated scientific writer assistant. Use only the information provided "
            "in the following records to write one paragraph explaining and exemplifying the "
            "relationships among the following keywords: "
        )
        text = textwrap.fill(text, width=TEXTWRAP_WIDTH)
        text = text.replace("\n", " \\\n")
        main_text = text + "\n\n"

        text = textwrap.fill(terms, width=TEXTWRAP_WIDTH)
        text = text.replace("\n", " \\\n")
        main_text += text + "\n\n"

        text = (
            "Use the Record-No value between brackets to indicate the reference to the record. "
            "For example, [1] means that the information is in the Record-No 1. Use notes below "
            "of the generated text to justify the affirmation. Use only phrases appearing in the "
            "provided text. Here are the records: "
        )
        text = textwrap.fill(text, width=TEXTWRAP_WIDTH)
        text = text.replace("\n", " \\\n")
        main_text += text + "\n\n"

        #
        # Secondary text:
        text = (
            "Improve and make more clear the explanation of the relationships among the keywords:"
        )
        text = textwrap.fill(text, width=TEXTWRAP_WIDTH)
        text = text.replace("\n", " \\\n")
        secondary_text = text + "\n\n"

        text = textwrap.fill(terms, width=TEXTWRAP_WIDTH)
        text = text.replace("\n", " \\\n")
        secondary_text += text + "\n\n"

        text = (
            "in the next paragraphs delimited by '<<<' and '>>>', using only the information "
            "provided in the records presented below. Add cites to the added text using the "
            "corresponding Record-No value between brackets."
        )
        text = textwrap.fill(text, width=TEXTWRAP_WIDTH)
        text = text.replace("\n", " \\\n")
        secondary_text += text + "\n\n"

        text = "Here are text to improve and make more clear: "
        text = textwrap.fill(text, width=TEXTWRAP_WIDTH)
        text = text.replace("\n", " \\\n")
        secondary_text += text + "\n\n"

        secondary_text += "<<<\n\n>>>\n\n"

        text = "Here are the records: "
        text = textwrap.fill(text, width=TEXTWRAP_WIDTH)
        text = text.replace("\n", " \\\n")
        secondary_text += text + "\n\n"

        # -------------------------------------------------------------------------------------
        records = records_per_cluster[cluster]
        records = records.sort_values(
            ["global_citations", "local_citations", "year"], ascending=False
        )

        file_name = f"{cluster}_abstracts_prompt.txt"
        prompt = format_prompt_for_records(
            main_text, secondary_text, records, weight="global_citations"
        )

        file_name = f"{cluster}_prompt.txt"
        file_path = os.path.join(root_dir, "reports", report_dir, file_name)

        with open(file_path, "w", encoding="utf-8") as file:
            print(prompt, file=file)

        print(f"--INFO-- The file '{file_path}' was created.")


def __generate_records_report(
    communities,
    records_per_cluster,
    report_dir,
    root_dir,
):
    """Generates records report."""

    for cluster in sorted(communities.keys()):
        records = records_per_cluster[cluster]
        records = records.sort_values(
            ["global_citations", "local_citations", "year"], ascending=False
        )
        file_name = f"{cluster}_abstracts_report.txt"
        format_report_for_records(
            root_dir=root_dir,
            target_dir=report_dir,
            records=records,
            report_filename=file_name,
        )

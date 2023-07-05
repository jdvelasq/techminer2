# flake8: noqa
# pylint: disable=line-too-long
"""
Network Report
===============================================================================


* Preparation

>>> import techminer2plus as tm2p
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

from ._chatbot import format_prompt_for_records
from ._network_lib import extract_records_per_cluster, nx_extract_communities
from .concordances import concordances_from_records
from .create_records_report import create_records_report
from .make_report_dir import make_report_dir


# pylint: disable=too-many-arguments
def network_report(
    #
    # PARAMS:
    network,
    report_dir,
    #
    # CONCORDANCES
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

    field = network.cooc_matrix.columns
    nx_graph = network.nx_graph
    make_report_dir(root_dir, report_dir)

    communities = nx_extract_communities(nx_graph, conserve_counters=False)

    records_per_cluster = extract_records_per_cluster(
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
        records_per_cluster=records_per_cluster,
        top_n=top_n,
        report_dir=report_dir,
        root_dir=root_dir,
    )

    generate_records_report(
        communities=communities,
        records_per_cluster=records_per_cluster,
        report_dir=report_dir,
        root_dir=root_dir,
    )

    generate_records_prompt(
        communities=communities,
        records_per_cluster=records_per_cluster,
        report_dir=report_dir,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )


def generate_records_prompt(
    communities,
    records_per_cluster,
    report_dir,
    root_dir,
):
    """ChatGPT prompt."""

    main_text = (
        "Your task is to summarize in only one pargraph the following "
        "abstracts, delimited by triple backticks, and weighted by the "
        "number of citations. The more citations, "
        "the more important the abstract is. Your summary should capture "
        "the central idea of the  all text, in at most 200 words."
    )

    for cluster in communities:
        records = records_per_cluster[cluster]
        records = records.sort_values(
            ["global_citations", "local_citations", "year"], ascending=False
        )

        file_name = f"{cluster}_abstracts_prompt.txt"
        prompt = format_prompt_for_records(
            main_text, records, weight="global_citations"
        )

        file_name = f"{cluster}_prompt.txt"
        file_path = os.path.join(root_dir, "reports", report_dir, file_name)

        with open(file_path, "w", encoding="utf-8") as file:
            print(prompt, file=file)

        print(f"--INFO-- The file '{file_path}' was created.")


def generate_records_report(
    communities,
    records_per_cluster,
    report_dir,
    root_dir,
):
    """Generates records report."""

    for cluster in communities:
        records = records_per_cluster[cluster]
        records = records.sort_values(
            ["global_citations", "local_citations", "year"], ascending=False
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
    records_per_cluster,
    top_n,
    report_dir,
    root_dir,
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

            concordances_from_records(
                records=records_per_cluster[cluster],
                search_for=member,
                top_n=top_n,
                report_file=report_file,
                prompt_file=prompt_file,
                root_dir=root_dir,
            )

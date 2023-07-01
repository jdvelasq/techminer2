# flake8: noqa
"""
Network Report
===============================================================================





>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> cooc_matrix = techminer2plus.co_occurrence_matrix(
...    columns='author_keywords',
...    col_top_n=20,
...    root_dir=root_dir,
... )
>>> graph = techminer2plus.network_clustering(
...    cooc_matrix,
...    algorithm_or_estimator='louvain',
... )
>>> print(techminer2plus.network_communities(graph).to_markdown())
|    | CL_00                          | CL_01                       | CL_02                        | CL_03                          |
|---:|:-------------------------------|:----------------------------|:-----------------------------|:-------------------------------|
|  0 | REGTECH 28:329                 | FINTECH 12:249              | REGULATORY_TECHNOLOGY 07:037 | ANTI_MONEY_LAUNDERING 05:034   |
|  1 | COMPLIANCE 07:030              | FINANCIAL_SERVICES 04:168   | REGULATION 05:164            | ARTIFICIAL_INTELLIGENCE 04:023 |
|  2 | BLOCKCHAIN 03:005              | FINANCIAL_REGULATION 04:035 | RISK_MANAGEMENT 03:014       | CHARITYTECH 02:017             |
|  3 | SMART_CONTRACTS 02:022         | INNOVATION 03:012           | SUPTECH 03:004               | ENGLISH_LAW 02:017             |
|  4 | ACCOUNTABILITY 02:014          | DATA_PROTECTION 02:027      | SEMANTIC_TECHNOLOGIES 02:041 |                                |
|  5 | DATA_PROTECTION_OFFICER 02:014 |                             |                              |                                |



>>> techminer2plus.network_report(
...     graph,
...     field='author_keywords',
...     report_dir='network_report',
...     root_dir=root_dir,
... )
--INFO-- The file 'data/regtech/reports/network_report/CL_00_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report/CL_01_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report/CL_02_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report/CL_03_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report/CL_00_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report/CL_01_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report/CL_02_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/network_report/CL_03_prompt.txt' was created.



# pylint: disable=line-too-long
"""
import os
import os.path
import textwrap

from .api.chatbot_prompts import format_prompt_for_records
from .api.records.concordances import concordances
from .create_records_report import create_records_report
from .make_report_dir import make_report_dir
from .network_lib import extract_records_per_cluster, nx_extract_communities


# pylint: disable=too-many-arguments
def network_report(
    graph,
    field,
    report_dir,
    #
    # Concordances
    top_n=100,
    #
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Generes"""

    make_report_dir(root_dir, report_dir)

    communities = nx_extract_communities(graph, conserve_counters=False)

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
        # Database params:
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

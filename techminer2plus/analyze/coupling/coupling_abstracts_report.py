# flake8: noqa
"""
Coupling Abstracts Report
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
>>> coupling_abstracts_report(
...     graph,
...     coupling_matrix,
...     report_dir="coupling",
... )
--INFO-- The file 'data/regtech/reports/coupling/CL_00_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/coupling/CL_02_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/coupling/CL_01_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/coupling/CL_00_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/coupling/CL_02_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/coupling/CL_01_prompt.txt' was created.

# pylint: disable=line-too-long
"""
import os.path

from ...make_report_dir import make_report_dir
from ...prompts import format_prompt_for_records
from ...records import create_records_report, read_records
from .extract_articles_per_cluster import extract_articles_per_cluster
from .obtain_records_per_cluster import obtain_records_per_cluster


def coupling_abstracts_report(
    graph,
    coupling_matrix,
    report_dir,
):
    """Coupling Abstracts Report."""

    def create_abstracts_report(records_per_cluster, root_dir, report_dir):
        """Creates the report."""

        for cluster in records_per_cluster:
            records = records_per_cluster[cluster]
            report_filename = f"{cluster}_abstracts_report.txt"
            create_records_report(
                root_dir=root_dir,
                target_dir=report_dir,
                records=records,
                report_filename=report_filename,
            )

    def create_abstracts_prompt(records_per_cluster, root_dir, report_dir):
        """Creates the prompt."""

        main_text = (
            "Your task is to summarize in only one pargraph the following "
            "abstracts, delimited by triple backticks, and weighted by the "
            "number of citations. The more citations, "
            "the more important the abstract is. Your summary should capture "
            "the central idea of the  all text, in at most 200 words."
        )

        for cluster in records_per_cluster:
            records = records_per_cluster[cluster]
            records = records.sort_values(
                ["global_citations", "local_citations", "year"],
                ascending=False,
            )
            prompt = format_prompt_for_records(
                main_text, records, weight="global_citations"
            )
            file_name = f"{cluster}_prompt.txt"
            file_path = os.path.join(
                root_dir, "reports", report_dir, file_name
            )
            with open(file_path, "w", encoding="utf-8") as file:
                print(prompt, file=file)
            print(f"--INFO-- The file '{file_path}' was created.")

    #
    # Main code:
    #
    articles_per_cluster = extract_articles_per_cluster(graph)
    records_per_cluster = obtain_records_per_cluster(
        articles_per_cluster, coupling_matrix
    )

    make_report_dir(coupling_matrix.root_dir_, report_dir)

    create_abstracts_report(
        records_per_cluster,
        coupling_matrix.root_dir_,
        report_dir,
    )

    create_abstracts_prompt(
        records_per_cluster,
        coupling_matrix.root_dir_,
        report_dir,
    )

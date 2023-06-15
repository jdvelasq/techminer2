# flake8: noqa
"""Most cited cited documents.

"""
import os
import textwrap

from ..classes import ItemsList, MostCitedDocuments
from ..record_utils import create_records_report, read_records
from ..techminer.indicators.indicators_by_document import (
    indicators_by_document,
)
from ..vantagepoint.report import ranking_chart


# pylint: disable=too-many-locals
# pylint: disable=too-many-arguments
def most_cited_documents(
    metric,
    top_n,
    # Figure params:
    title=None,
    field_label=None,
    metric_label=None,
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Most cited documents."""

    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    if metric == "local_citations":
        columns = ["local_citations", "global_citations", "year", "article"]
        ascending = [False, False, False, True]
        report_filename = "most_local_cited_documents__abstracts.txt"
        prompt_filename = "most_local_cited_documents__gpt_prompt.txt"
    else:
        columns = ["global_citations", "local_citations", "year", "article"]
        ascending = [False, False, False, True]
        report_filename = "most_global_cited_documents__abstracts.txt"
        prompt_filename = "most_global_cited_documents__gpt_prompt.txt"

    records = records.sort_values(columns, ascending=ascending)
    records = records.head(top_n)

    create_records_report(
        root_dir=root_dir,
        target_dir="",
        records=records,
        report_filename=report_filename,
    )

    generate_chatgpt_prompt(
        records=records,
        prompt_filename=prompt_filename,
        root_dir=root_dir,
    )

    indicators = indicators_by_document(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    indicators = indicators.sort_values(columns, ascending=ascending)
    indicators = indicators.head(top_n)
    indicators = indicators.reset_index()
    indicators = indicators.set_index("article")

    item_list = ItemsList()
    item_list.table_ = indicators
    item_list.metric_ = metric
    item_list.field_ = "Document"
    item_list.prompt_ = None

    cited_documents = MostCitedDocuments()
    cited_documents.table_ = indicators
    cited_documents.plot_ = ranking_chart(
        item_list,
        title=title,
        field_label=field_label,
        metric_label=metric_label,
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_color=line_color,
        line_width=line_width,
        yshift=yshift,
    ).plot_

    return cited_documents


def generate_chatgpt_prompt(
    records,
    prompt_filename,
    root_dir,
):
    """ChatGPT prompt."""

    abstracts = records["abstract"].dropna()
    abstracts = abstracts.map(
        lambda x: textwrap.fill(x, width=70).replace("\n", " \\\n")
    )
    abstracts = abstracts.to_list()

    file_path = os.path.join(root_dir, "reports", prompt_filename)
    with open(file_path, "w", encoding="utf-8") as file:
        print(
            # pylint: disable=line-too-long
            "Your task is to summarize in each abstract of the following text. Your summary \\\n"
            "should capture the central idea of the each abstract, in at most 40 words.\n\n"
            "Summarize the text below, delimited by triple backticks:\n\n",
            file=file,
        )

        for i_abstract, abstract in enumerate(abstracts):
            print(
                f"Abstract {i_abstract + 1}: ",
                file=file,
            )
            print(f"```\n{abstract}\n```\n\n", file=file)

        print(f"--INFO-- The file '{file_path}' was created.")

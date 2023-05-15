import os
import sys
import textwrap
from dataclasses import dataclass

import plotly.express as px

from .._read_records import read_records
from ..techminer.indicators.indicators_by_document import indicators_by_document


@dataclass(init=False)
class _Results:
    plot_ = None
    table_ = None
    prompts_ = None


def bibiometrix_cited_documents(
    metric,
    directory="./",
    database="documents",
    top_n=20,
    title=None,
    file_name=None,
    start_year=None,
    end_year=None,
    **filters,
):
    """Most cited documents."""

    results = _Results()

    results.table_ = indicators_by_document(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    ).sort_values(by=metric, ascending=False)

    top_n_documents = _get_top_n_documents(
        metric,
        directory=directory,
        top_n=top_n,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    _write_report(top_n_documents, directory, file_name)

    results.prompts_ = _get_prompts(top_n_documents)

    indicators = _prepare_indicators(metric, top_n, results.table_)
    results.plot_ = _create_figure(metric, title, indicators)

    return results


###########


def _get_prompts(top_n_documents):
    prompts = []
    for _, row in top_n_documents.iterrows():
        text = f"Summarize the following text in 30 words or less: \n\n{row.abstract}"
        prompts.append(text)
    return prompts


def _prepare_indicators(metric, top_n, indicators):
    indicators = indicators.copy()
    indicators = indicators.sort_values(by=metric, ascending=False)
    indicators = indicators.head(top_n)
    indicators = indicators.rename(
        columns={col: col.replace("_", " ").title() for col in indicators.columns}
    )
    indicators = indicators.reset_index()
    indicators = indicators.rename(columns={"article": "Document"})
    return indicators


def _get_top_n_documents(
    metric,
    directory="./",
    top_n=20,
    start_year=None,
    end_year=None,
    **filters,
):
    indicators = indicators_by_document(
        directory=directory,
        database="documents",
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    indicators = indicators.sort_values(by=metric, ascending=False)
    indicators = indicators.head(top_n)

    records = read_records(
        directory=directory,
        database="documents",
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    records.index = records.article
    records = records.loc[indicators.index, :]

    return records


##########


def _write_report(documents, directory, file_name):
    column_list = []

    reported_columns = [
        "article",
        "title",
        "authors",
        "global_citations",
        "source_title",
        "year",
        "abstract",
        "author_keywords",
        "index_keywords",
    ]

    for criterion in reported_columns:
        if criterion in documents.columns:
            column_list.append(criterion)
    documents = documents[column_list]

    if "global_citations" in documents.columns:
        documents = documents.sort_values(by="global_citations", ascending=False)

    file_path = os.path.join(directory, "reports", file_name)

    counter = 0
    with open(file_path, "w", encoding="utf-8") as file:
        for _, row in documents.iterrows():
            print("---{:03d}".format(counter) + "-" * 86, file=file)
            counter += 1

            for criterion in reported_columns:
                if criterion not in row.index:
                    continue

                if row[criterion] is None:
                    continue

                if criterion == "article":
                    print("AR ", end="", file=file)
                if criterion == "title":
                    print("TI ", end="", file=file)
                if criterion == "authors":
                    print("AU ", end="", file=file)
                if criterion == "global_citations":
                    print("TC ", end="", file=file)
                if criterion == "source_title":
                    print("SO ", end="", file=file)
                if criterion == "year":
                    print("PY ", end="", file=file)
                if criterion == "abstract":
                    print("AB ", end="", file=file)
                if criterion == "raw_author_keywords":
                    print("DE ", end="", file=file)
                if criterion == "author_keywords":
                    print("DE ", end="", file=file)
                if criterion == "raw_index_keywords":
                    print("ID ", end="", file=file)
                if criterion == "index_keywords":
                    print("ID ", end="", file=file)

                text = textwrap.fill(
                    str(row[criterion]),
                    width=87,
                    initial_indent=" " * 3,
                    subsequent_indent=" " * 3,
                    fix_sentence_endings=True,
                )[3:]

                # if criterion == "abstract":
                #     text = text.split("\n")
                #     text = [x.strip() for x in text]
                #     text = " \\\n".join(text)
                #     text = '\n"""\n' + text + '\n"""'

                print(text, file=file)

    sys.stdout.write(f"--INFO-- The file '{file_path}' was created\n")


def _create_figure(metric, title, indicators):
    fig = px.scatter(
        indicators,
        x=metric.replace("_", " ").title(),
        y="Document",
        hover_data=["Global Citations", "Local Citations"],
        title=title,
    )
    fig.update_traces(marker=dict(size=10, color="black"))
    fig.update_traces(textposition="middle right")
    fig.update_traces(line=dict(color="black"))
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        autorange="reversed",
        griddash="dot",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
    )

    return fig

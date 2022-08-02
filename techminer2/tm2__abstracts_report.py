"""
Abstracts Report
===============================================================================


>>> directory = "data/regtech/"

>>> # file generated in data/regtech/reports/abstracts_report.txt
>>> from techminer2 import tm2__abstracts_report
>>> tm2__abstracts_report(
...     criterion="author_keywords",
...     custom_topics=["blockchain" ,"regtech"],
...     n_abstracts=10,    
...     directory=directory,
... )


"""
import os.path
import textwrap

import pandas as pd

from ._read_records import read_records


def tm2__abstracts_report(
    criterion=None,
    custom_topics=None,
    file_name="abstracts_report.txt",
    n_abstracts=10,
    use_textwrap=True,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Extracts abstracts of documents meeting the given criteria."""

    records = read_records(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    if criterion is not None:
        ##
        selected_records = records[["article", criterion]]
        selected_records[criterion] = selected_records[criterion].str.split(";")
        selected_records = selected_records.explode(criterion)
        selected_records[criterion] = selected_records[criterion].str.strip()
        selected_records = selected_records[
            selected_records[criterion].isin(custom_topics)
        ]
        records = records[records["article"].isin(selected_records["article"])]

        ##
        records["TOPICS"] = records[criterion].copy()
        records["TOPICS"] = records["TOPICS"].str.split(";")
        records["TOPICS"] = records["TOPICS"].map(lambda x: [y.strip() for y in x])

        records["POINTS"] = ""
        for topic in custom_topics:
            records["POINTS"] += records["TOPICS"].map(
                lambda x: "1" if topic in x else "0"
            )

        records = records.sort_values(
            by=["POINTS", "global_citations", "local_citations"],
            ascending=[False, False, False],
        )

    else:

        records = records.sort_values(
            by=["global_citations", "local_citations"],
            ascending=[False, False],
        )

    records = records.head(n_abstracts)

    # if "TOPICS" not in records.columns:
    #     records["TOPICS"] = records[criterion].copy()

    # records = records.sort_values(
    #     by=["TOPICS", "global_citations", "local_citations"],
    #     ascending=[True, False, False],
    # )

    with open(
        os.path.join(directory, "reports", file_name), "w", encoding="utf-8"
    ) as out_file:

        for _, row in records.iterrows():

            if use_textwrap:
                if not pd.isna(row["article"]):
                    text_article = textwrap.fill(row["article"], width=90)
                if not pd.isna(row["title"]):
                    text_title = textwrap.fill(row["title"], width=90)
                if not pd.isna(row[criterion]):
                    text_criterion = textwrap.fill(row[criterion], width=90)
                if not pd.isna(row["abstract"]):
                    text_abstract = textwrap.fill(row["abstract"], width=90)

            else:
                text_article = row["article"]
                text_title = row["title"]
                text_criterion = row[criterion]
                if not pd.isna(row["abstract"]):
                    text_abstract = row["abstract"]

            text_citation = "Citations: " + str(row["global_citations"])

            print("-" * 90, file=out_file)
            print(text_article, file=out_file)
            print(text_title, file=out_file)
            print(text_criterion, file=out_file)
            print(text_citation, file=out_file)
            print("\n", file=out_file)
            print(text_abstract, file=out_file)
            print("\n\n", file=out_file)

    # sys.stdout.write("--INFO-- Abstrats Report generated.\n")

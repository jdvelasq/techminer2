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

        records["RNK"] = records.groupby("POINTS")["global_citations"].rank(
            ascending=False, method="dense"
        )

        records = records[records["RNK"] < 10]

        records["TERMS"] = records[criterion].str.split(";")
        records["TERMS"] = records["TERMS"].map(lambda x: [y.strip() for y in x])
        records["TERMS_1"] = records["TERMS"].map(
            lambda x: [
                "(*) " + custom_topic
                for custom_topic in custom_topics
                if custom_topic in x
            ],
            na_action="ignore",
        )
        records["TERMS_2"] = records["TERMS"].map(
            lambda x: [y for y in x if y not in custom_topics], na_action="ignore"
        )
        records["TERMS"] = records["TERMS_1"] + records["TERMS_2"]
        records[criterion] = records["TERMS"].str.join("; ")

    else:

        records = records.sort_values(
            by=["global_citations", "local_citations"],
            ascending=[False, False],
        )

    records = records.head(n_abstracts)

    with open(
        os.path.join(directory, "reports", file_name), "w", encoding="utf-8"
    ) as out_file:

        for _, row in records.iterrows():

            if use_textwrap:
                if not pd.isna(row["article"]):
                    text_article = textwrap.fill(
                        row["article"],
                        width=87,
                        initial_indent=" " * 0,
                        subsequent_indent=" " * 3,
                        fix_sentence_endings=True,
                    )
                if not pd.isna(row["title"]):
                    text_title = textwrap.fill(
                        row["title"],
                        width=87,
                        initial_indent=" " * 0,
                        subsequent_indent=" " * 3,
                        fix_sentence_endings=True,
                    )
                if not pd.isna(row[criterion]):
                    text_criterion = textwrap.fill(
                        row[criterion],
                        width=87,
                        initial_indent=" " * 0,
                        subsequent_indent=" " * 3,
                        fix_sentence_endings=True,
                    )
                if not pd.isna(row["abstract"]):
                    text_abstract = textwrap.fill(
                        row["abstract"],
                        width=87,
                        initial_indent=" " * 0,
                        subsequent_indent=" " * 3,
                        fix_sentence_endings=True,
                    )

            else:
                text_article = row["article"]
                text_title = row["title"]
                text_criterion = row[criterion]
                if not pd.isna(row["abstract"]):
                    text_abstract = row["abstract"]

            text_citation = str(row["global_citations"])

            print("-" * 90, file=out_file)
            print("AR ", end="", file=out_file)
            print(text_article, file=out_file)

            print("TI ", end="", file=out_file)
            print(text_title, file=out_file)

            print("KW ", end="", file=out_file)
            print(text_criterion, file=out_file)

            print("TC ", end="", file=out_file)
            print(text_citation, file=out_file)

            print("AB ", end="", file=out_file)
            print(text_abstract, file=out_file)

            print("\n", file=out_file)

    # sys.stdout.write("--INFO-- Abstrats Report generated.\n")

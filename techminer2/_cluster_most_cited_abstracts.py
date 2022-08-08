"""Clusters summarization"""
import os
import textwrap

from ._create_directory import create_directory
from ._read_records import read_records


def cluster_most_cited_abstracts(
    criterion,
    communities,
    directory_for_abstracts,
    n_keywords=10,
    n_abstracts=30,
    directory="./",
    start_year=None,
    end_year=None,
    **filters,
):
    """Clusters summarization."""

    create_directory(
        base_directory=directory,
        target_directory=directory_for_abstracts,
    )

    communities = communities.head(n_keywords)
    for community_name in communities:

        community = communities[community_name].tolist()
        community = [x for x in community if x != ""]
        community = [" ".join(x.split()[:-1]) for x in community]

        records = read_records(
            directory=directory,
            database="documents",
            start_year=start_year,
            end_year=end_year,
            **filters,
        )

        records = records.sort_values(
            by="global_citations",
            ascending=False,
        ).head(n_abstracts)

        ####

        records["TERMS"] = records[criterion].str.split(";")
        records["TERMS"] = records["TERMS"].map(
            lambda x: [y.strip() for y in x], na_action="ignore"
        )
        records["TERMS_1"] = records["TERMS"].map(
            lambda x: [
                "(*) " + custom_topic for custom_topic in community if custom_topic in x
            ],
            na_action="ignore",
        )
        records["TERMS_2"] = records["TERMS"].map(
            lambda x: [y for y in x if y not in community], na_action="ignore"
        )
        records["TERMS"] = records["TERMS_1"] + records["TERMS_2"]
        records[criterion] = records["TERMS"].str.join("; ")
        ####

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
            if criterion in records.columns:
                column_list.append(criterion)
        records = records[column_list]

        if "global_citations" in records.columns:
            records = records.sort_values(by="global_citations", ascending=False)

        file_name = os.path.join(
            directory, "reports", directory_for_abstracts, community_name + ".txt"
        )

        counter = 0
        with (open(file_name, "w", encoding="utf-8")) as file:

            for _, row in records.iterrows():

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

                    print(
                        textwrap.fill(
                            str(row[criterion]),
                            width=87,
                            initial_indent=" " * 3,
                            subsequent_indent=" " * 3,
                            fix_sentence_endings=True,
                        )[3:],
                        file=file,
                    )

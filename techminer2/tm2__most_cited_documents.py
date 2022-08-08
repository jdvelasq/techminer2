"""
Most Global Cited Documents
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import tm2__most_cited_documents
>>> tm2__most_cited_documents(
...     directory=directory,
... )


"""
import os.path
import textwrap

from ._read_records import read_records


def tm2__most_cited_documents(
    directory="./",
    file_name="most_cited_documents.txt",
    start_year=None,
    end_year=None,
    **filters,
):
    """Prints ."""

    records = read_records(
        directory=directory,
        database="documents",
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

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

    file_path = os.path.join(directory, "reports", file_name)

    counter = 0
    with (open(file_path, "w", encoding="utf-8")) as file:

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

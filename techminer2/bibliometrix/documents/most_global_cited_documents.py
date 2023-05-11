"""
Most Global Cited Documents
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_global_cited_documents.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.documents.most_global_cited_documents(
...     top_n=5,
...     directory=directory,
... )
--INFO-- The file 'data/regtech/reports/most_global_cited_documents.txt' was created

>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_global_cited_documents.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head(5)
                                                    global_citations  ...                                 doi
article                                                               ...                                    
Anagnostopoulos I, 2018, J ECON BUS, V100, P7                    153  ...      10.1016/J.JECONBUS.2018.07.003
Arner DW, 2017, HANDB OF BLOCKCHAIN, DIGIT FINA...                11  ...  10.1016/B978-0-12-810441-5.00016-6
Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, ...               150  ...                                 NaN
Battanta L, 2020, PROC EUR CONF INNOV ENTREPREN...                 1  ...                 10.34190/EIE.20.143
Baxter LG, 2016, DUKE LAW J, V66, P567                            30  ...                                 NaN
<BLANKLINE>
[5 rows x 5 columns]

"""
import os.path
import sys
import textwrap

from ..._read_records import read_records
from ...techminer.indicators.indicators_by_document import indicators_by_document
from ..cited_documents import bibiometrix_cited_documents


def most_global_cited_documents(
    directory="./",
    top_n=20,
    title="Most Global Cited Documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Plots the most global cited documents in the main collection."""

    ## TODO: Review and extract

    indicators = indicators_by_document(
        directory=directory,
        database="documents",
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    indicators = indicators.sort_values(by="global_citations", ascending=False)
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

    _save_report(records, directory)

    return bibiometrix_cited_documents(
        metric="global_citations",
        directory=directory,
        database="documents",
        top_n=top_n,
        title=title,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )


def _save_report(records, directory):
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

    file_path = os.path.join(directory, "reports/most_global_cited_documents.txt")

    counter = 0
    with open(file_path, "w", encoding="utf-8") as file:
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

                text = textwrap.fill(
                    str(row[criterion]),
                    width=87,
                    initial_indent=" " * 3,
                    subsequent_indent=" " * 3,
                    fix_sentence_endings=True,
                )[3:]

                if criterion == "abstract":
                    text = text.split("\n")
                    text = [x.strip() for x in text]
                    text = " \\\n".join(text)
                    text = '\n"""\n' + text + '\n"""'

                print(text, file=file)

    sys.stdout.write(f"--INFO-- The file '{file_path}' was created\n")

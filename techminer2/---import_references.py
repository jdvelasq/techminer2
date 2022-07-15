"""
Import References File
===============================================================================

Import a 'cited by' scopus file with references.

* The references file is called 'raw-references.csv' and it is obtained from
  references option in Scopus.

* This function must be called after the import of the documents.

>>> from techminer2 import *
>>> directory = "data/regtech/"

## >>> import_references(directory=directory, disable_progress_bar=True)
- INFO - 5123 raw records found in data/raw/references.
- INFO - Creating references file
- INFO - References table saved to data/processed/cited_references_table.csv
- INFO - References table saved to data/processed/references.csv






"""
from os.path import join

import numpy as np
from tqdm import tqdm

from . import logging

# from ._read_raw_csv_files import read_raw_csv_files
from ._read_records import read_all_records

# from .import_scopus_files import (  # _delete_and_rename_columns,; _disambiguate_authors,; _search_for_new_iso_source_name,; _process__iso_source_name__column,; _repair__iso_source_name__column,; _complete__source_abbr__colum,
#     _create__document_id__column,
#     _create__record_no__column,
#     _process__authors_id__column,
#     _process__doi__column,
#     _process__raw_authors__column,
#     _process__source_name__column,
# )


def _create_references_file(
    documents, references, directory, disable_progress_bar=False
):

    logging.info("Creating references file")
    references = references.copy()
    references = references.assign(authors=references.authors.str.lower())

    # builds a table with:
    #   record_no  raw_reference
    #   ------------------------------------------------
    cited_references = documents[["record_no", "global_references"]].copy()

    cited_references = cited_references.rename(
        columns={"global_references": "raw_reference"}
    )
    cited_references = cited_references.dropna()
    cited_references = cited_references.assign(
        raw_reference=cited_references.raw_reference.str.split(";")
    )
    cited_references = cited_references.explode("raw_reference")
    cited_references = cited_references.assign(
        raw_reference=cited_references.raw_reference.str.strip()
    )
    cited_references = cited_references.assign(
        raw_reference=cited_references.raw_reference.str.lower()
    )

    cited_references = cited_references.sort_values("raw_reference")

    # -------------------------------------------------------------------------
    # optimized for speed
    # raw references and list of citting documents:
    cited_references = cited_references.groupby(["raw_reference"], as_index=False).agg(
        list
    )
    cited_references = cited_references.assign(cited_id=np.nan)
    #
    references = references.assign(document_title=references.document_title.str.lower())
    references = references[~references.authors.isna()]

    with tqdm(total=len(references), disable=disable_progress_bar) as pbar:
        for _, row in references.iterrows():
            cited_references.loc[
                cited_references.raw_reference.str.contains(
                    row["document_title"], regex=False
                )
                & cited_references.raw_reference.str.contains(str(row["pub_year"]))
                & cited_references.raw_reference.str.contains(
                    row["authors"].split(" ")[0].strip()
                ),
                "cited_id",
            ] = row["record_no"]
            pbar.update(1)

    cited_references = cited_references.dropna()
    # -------------------------------------------------------------------------
    # with open(
    #     join(directory, "debug_references.txt"), "wt", encoding="utf-8"
    # ) as out_file:
    #     for index, row in references.iterrows():

    #         _cited_references = cited_references.loc[
    #             cited_references.raw_reference.str.contains(
    #                 row["document_title"], regex=False
    #             )
    #             & cited_references.raw_reference.str.contains(str(row["pub_year"]))
    #             & cited_references.raw_reference.str.contains(
    #                 row["authors"].split(" ")[0].strip()
    #             ),
    #             "raw_reference",
    #         ]

    #         if len(_cited_references) > 0:
    #             print(row["pub_year"], row["document_title"], file=out_file)
    #             for m in _cited_references:
    #                 print("    ", m[:200], file=out_file)

    #         else:
    #             print("**** ", row["pub_year"], row["document_title"], file=out_file)

    # -------------------------------------------------------------------------
    cited_references = cited_references.explode("record_no")
    cited_references = cited_references[["record_no", "cited_id"]].copy()
    cited_references = cited_references.rename(columns={"record_no": "citing_id"})
    cited_references = cited_references.reset_index(drop=True)
    cited_references = cited_references.dropna()
    cited_references = cited_references.sort_values(["citing_id", "cited_id"])
    references_file = join(directory, "processed", "cited_references_table.csv")
    cited_references.to_csv(references_file, index=False)
    logging.info(f"References table saved to {references_file}")

    return cited_references


# def _create_cited_references_csv(documents, directory):

#     if "global_references" in documents.columns:

#         # split references
#         cited_references = documents[["fdocument_id", "global_references"]].copy()
#         cited_references = cited_references.rename(
#             columns={"global_references": "raw_reference"}
#         )
#         cited_references = cited_references.dropna()
#         cited_references = cited_references.assign(
#             raw_reference=cited_references.raw_reference.str.split(";")
#         )
#         cited_references = cited_references.explode("raw_reference")
#         cited_references = cited_references.assign(
#             raw_reference=cited_references.raw_reference.str.strip()
#         )
#         cited_references = cited_references.assign(
#             ref_no=cited_references.groupby(["record_no"]).cumcount()
#         )

#         cited_references = cited_references[["record_no", "ref_no", "raw_reference"]]

#         # save to disk
#         file_name = join(directory, "cited_references.csv")
#         cited_references.to_csv(file_name, index=False)

#         logging.info(f"Cited references saved to {file_name}")


def import_references(directory="./", disable_progress_bar=False):
    """
    Import references file.

    Args:
        directory (str): Directory where the file is located.
        scopus_file (str): Name of the file.

    Returns:
        None

    """

    documents = read_all_records(directory)
    #
    # references = read_raw_csv_files(join(directory, "raw", "references"))
    # references = _delete_and_rename_columns(references)
    # references = _process__authors_id__column(references)
    # references = _process__raw_authors_names__column(references)
    # references = _disambiguate_authors(references)
    # references = _process__doi__column(references)
    # references = _process__source_name__column(references)
    # references = _process__iso_source_name__column(references)
    # references = _search_for_new_iso_source_name(references)
    # references = _complete__iso_source_name__colum(references)
    # references = _repair__iso_source_name__column(references)
    # references = _create__record_no__column(references)
    # references = _create__document_id__column(references)
    #
    cited_references_table = _create_references_file(
        documents=documents,
        references=references,
        directory=directory,
        disable_progress_bar=disable_progress_bar,
    )
    #
    cited_references_frequency = cited_references_table.groupby(
        "cited_id", as_index=True
    ).count()

    references = references.assign(local_citations=0)
    references.index = references.record_no
    references.loc[
        cited_references_frequency.index, "local_citations"
    ] = cited_references_frequency.citing_id
    references = references.reset_index(drop=True)
    references["local_citations"].fillna(1, inplace=True)
    references["local_citations"] = references["local_citations"].astype(int)

    file_name = join(directory, "processed", "references.csv")
    references.to_csv(file_name, index=False)
    logging.info(f"References table saved to {file_name}")

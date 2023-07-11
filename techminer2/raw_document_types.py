# flake8: noqa
# pylint: disable=line-too-long
"""
Document Types in Raw Documents 
===============================================================================

Return the number of records by document type in the databases.



>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> techminer2plus.ingest.raw_document_types(root_dir)
--INFO-- Concatenating raw files in data/regtech/raw-data/cited_by/
--INFO-- Document types in: cited_by
No document types found
<BLANKLINE>
--INFO-- Concatenating raw files in data/regtech/raw-data/references/
--INFO-- Document types in: references
No document types found
<BLANKLINE>
--INFO-- Concatenating raw files in data/regtech/raw-data/main/
--INFO-- Document types in: main
No document types found
<BLANKLINE>


"""
import os

from .ingest.ingest_raw_data import concat_raw_csv_files, get_subdirectories


def raw_document_types(root_dir):
    """Document types in raw documents.

    Args:
        root_dir (str): root directory.

    Returns:
        None.

    """
    raw_dir = os.path.join(root_dir, "raw-data")

    folders = get_subdirectories(raw_dir)
    for folder in folders:
        data = concat_raw_csv_files(os.path.join(raw_dir, folder))
        if "docuemnt_type" in data.columns:
            print(f"--INFO-- Document types in: {folder}")
            print(data.document_type.value_counts())
            print("")
        else:
            print(f"--INFO-- Document types in: {folder}")
            print("No document types found")
            print("")

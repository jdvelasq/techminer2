"""
Column documents
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> column_documents(
...     'authors',
...     directory=directory,
... ).head()
      authors  ...                                        document_id
0   Razak MIA  ...  Razak MIA et al, 2021, PERTANIKA J SOC SCI HUM...
1    Dali NAM  ...  Razak MIA et al, 2021, PERTANIKA J SOC SCI HUM...
2   Dhillon G  ...  Razak MIA et al, 2021, PERTANIKA J SOC SCI HUM...
3   Manaf AWA  ...  Razak MIA et al, 2021, PERTANIKA J SOC SCI HUM...
4  Omodero CO  ...  Omodero CO et al, 2021, STUD UNIV VASILE GOLDI...
<BLANKLINE>
[5 rows x 6 columns]

"""

from ._read_records import read_all_records, read_filtered_records


def column_documents(
    column,
    directory="./",
    file_name="documents.csv",
    sep=";",
):
    """Column documents"""

    if file_name == "documents.csv":
        records = read_filtered_records(directory=directory)
    elif file_name == "references.csv":
        records = read_all_records(directory=directory, file_name=file_name)
    else:
        raise ValueError("file_name must be 'documents.csv' or 'references.csv'")

    if sep is not None:
        records[column] = records[column].str.split(sep)
        records = records.explode(column)
        records[column] = records[column].str.strip()

    records = records[
        [
            column,
            "document_title",
            "source_name",
            "global_citations",
            "local_citations",
            "document_id",
        ]
    ]
    records = records.reset_index(drop=True)

    return records

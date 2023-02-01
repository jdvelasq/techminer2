"""
Document types in raw documents
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import tm2__raw_document_types
>>> tm2__raw_document_types(directory)
--INFO__ Document types in: cited_by
Article             314
Conference Paper     76
Review               34
Book Chapter         34
Book                 11
Editorial             5
Name: Document Type, dtype: int64
<BLANKLINE>
<BLANKLINE>
--INFO__ Document types in: references
Article             828
Conference Paper    196
Review               88
Book Chapter         46
Book                 25
Editorial            15
Note                 11
Short Survey          3
Data Paper            1
Letter                1
Name: Document Type, dtype: int64
<BLANKLINE>
<BLANKLINE>
--INFO__ Document types in: documents
Article             51
Conference Paper    22
Book Chapter        14
Review               4
Editorial            2
Book                 1
Name: Document Type, dtype: int64
<BLANKLINE>
<BLANKLINE>

"""
import os
import sys

from techminer2.techminer.tools.import_scopus_files import _concat_raw_csv_files


def tm2__raw_document_types(directory):
    """Document types in raw documents."""
    folders = os.listdir(os.path.join(directory, "raw"))
    folders = [f for f in folders if os.path.isdir(os.path.join(directory, "raw", f))]
    for folder in folders:
        data = _concat_raw_csv_files(os.path.join(directory, "raw", folder), quiet=True)
        document_types = data["Document Type"].dropna()
        document_types = document_types.value_counts()
        sys.stdout.write(f"--INFO-- Document types in: {folder}\n")
        print(document_types)
        print("")
        print("")

"""
Document types in raw documents
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import techminer
>>> techminer.reports.raw_document_types(directory)
--INFO-- Document types in: cited_by
Article             248
Book Chapter         49
Conference Paper     41
Review               30
Book                 14
Editorial             6
Name: Document Type, dtype: int64
<BLANKLINE>
<BLANKLINE>
--INFO-- Document types in: references
Article             690
Conference Paper     88
Review               74
Book Chapter         26
Book                 16
Editorial             8
Note                  6
Short Survey          2
Name: Document Type, dtype: int64
<BLANKLINE>
<BLANKLINE>
--INFO-- Document types in: documents
Article             31
Conference Paper    11
Book Chapter         9
Book                 1
Name: Document Type, dtype: int64
<BLANKLINE>
<BLANKLINE>

"""
import os
import sys

from techminer2.techminer.tools.import_scopus_files import _concat_raw_csv_files


def raw_document_types(directory):
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

"""
Document Types in Raw Documents 
===============================================================================

Return the number of records by document type in the databases.

Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"

>>> from techminer2 import techminer
>>> techminer.reports.raw_document_types(root_dir)
--INFO-- Document types in: cited_by
document_type
article             248
book_chapter         48
conference_paper     41
review               30
book                 14
editorial             6
Name: OCC, dtype: int64
<BLANKLINE>
--INFO-- Document types in: references
document_type
article             689
conference_paper     88
review               74
book_chapter         26
book                 16
editorial             8
note                  6
short_survey          2
Name: OCC, dtype: int64
<BLANKLINE>
--INFO-- Document types in: documents
document_type
article             31
conference_paper    11
book_chapter         9
book                 1
Name: OCC, dtype: int64
<BLANKLINE>


"""
import os
import sys

from ..indicators import indicators_by_topic


def raw_document_types(root_dir):
    """Document types in raw documents.

    Args:
        root_dir (str): root directory.

    Returns:
        None.

    """

    folders = os.listdir(os.path.join(root_dir, "raw"))

    folders = [
        f for f in folders if os.path.isdir(os.path.join(root_dir, "raw", f))
    ]

    for folder in folders:
        indicators = indicators_by_topic(
            criterion="document_type",
            root_dir=root_dir,
            database=folder,
            start_year=None,
            end_year=None,
        )

        sys.stdout.write(f"--INFO-- Document types in: {folder}\n")

        print(indicators["OCC"])
        print("")

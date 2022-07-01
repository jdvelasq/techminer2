"""
Documents by author
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"

>>> documents_by_author(
...     directory=directory,
... ).head()
        authors  ...                                 document_id
0   von Solms J  ...       von Solms J et al, 2021, J BANK REGUL
1   Dashottar S  ...       Dashottar S et al, 2021, J BANK REGUL
2  Srivastava V  ...       Dashottar S et al, 2021, J BANK REGUL
3       Turki M  ...  Turki M et al, 2021, ADV INTELL SYS COMPUT
4      Hamdan A  ...  Turki M et al, 2021, ADV INTELL SYS COMPUT
<BLANKLINE>
[5 rows x 6 columns]

"""
from .column_documents import column_documents


def documents_by_author(
    directory="./",
):
    """Returns a dataframe with the documents by each author."""
    return column_documents(
        column="authors",
        directory=directory,
    )

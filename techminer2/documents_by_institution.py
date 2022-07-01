"""
Documents by institution
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"

>>> documents_by_institution(
...     directory=directory,
... ).head()
                                 institutions  ...                                 document_id
0              University of Johannesburg ZAF  ...       von Solms J et al, 2021, J BANK REGUL
1  Indian Institute of Management Lucknow IND  ...       Dashottar S et al, 2021, J BANK REGUL
2                        Ahlia University BHR  ...  Turki M et al, 2021, ADV INTELL SYS COMPUT
3             Conventional Wholesale Bank BHR  ...  Turki M et al, 2021, ADV INTELL SYS COMPUT
4         Technical University of Ostrava CZE  ...       Guo H et al, 2021, STUD COMPUT INTELL
<BLANKLINE>
[5 rows x 6 columns]

"""
from .column_documents import column_documents


def documents_by_institution(
    directory="./",
):
    """Returns a dataframe with the documents by each institution."""
    return column_documents(
        column="institutions",
        directory=directory,
    )

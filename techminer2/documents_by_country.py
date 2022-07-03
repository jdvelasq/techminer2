"""
Documents by country (NEW)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"

>>> documents_by_country(
...     directory=directory,
... ).head()
           countries  ...                                 document_id
0       South Africa  ...       von Solms J et al, 2021, J BANK REGUL
1              India  ...       Dashottar S et al, 2021, J BANK REGUL
2            Bahrain  ...  Turki M et al, 2021, ADV INTELL SYS COMPUT
3            Bahrain  ...  Turki M et al, 2021, ADV INTELL SYS COMPUT
4  Brunei Darussalam  ...       Guo H et al, 2021, STUD COMPUT INTELL
<BLANKLINE>
[5 rows x 6 columns]

"""

from .column_documents import column_documents


def documents_by_country(
    directory="./",
):
    """Returns a dataframe with the documents by each country."""
    return column_documents(
        column="countries",
        directory=directory,
    )

"""
Documents per author
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"

>>> documents_by_author(
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

from .column_documents import column_documents


def documents_by_author(
    directory="./",
):
    return column_documents(
        column="authors",
        directory=directory,
    )

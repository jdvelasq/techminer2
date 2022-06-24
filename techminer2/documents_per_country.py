"""
Documents per country
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"

>>> documents_per_country(
...     directory=directory,
... ).head()
  countries  ...                                        document_id
0  malaysia  ...  Razak MIA et al, 2021, PERTANIKA J SOC SCI HUM...
1   nigeria  ...  Omodero CO et al, 2021, STUD UNIV VASILE GOLDI...
2     china  ...                  Li B et al, 2021, FINANCIAL INNOV
3   hungary  ...         Daragmeh A et al, 2021, J BEHAV EXP FINANC
4     china  ...         Xiang D et al, 2021, IEEE TRANS ENG MANAGE
<BLANKLINE>
[5 rows x 6 columns]

"""

from .column_documents import column_documents


def documents_per_country(
    directory="./",
):
    return column_documents(
        column="countries",
        directory=directory,
    )

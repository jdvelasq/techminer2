"""
Documents per institution
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"

>>> documents_by_institution(
...     directory=directory,
... ).head()
                                        institutions  ...                                        document_id
0                          Multimedia University MYS  ...  Razak MIA et al, 2021, PERTANIKA J SOC SCI HUM...
1                        Covenant University Ota NGA  ...  Omodero CO et al, 2021, STUD UNIV VASILE GOLDI...
2                  Zhejiang Gongshang University CHN  ...                  Li B et al, 2021, FINANCIAL INNOV
3                             Sichuan University CHN  ...                  Li B et al, 2021, FINANCIAL INNOV
4  Hungarian University of Agriculture and Life S...  ...         Daragmeh A et al, 2021, J BEHAV EXP FINANC
<BLANKLINE>
[5 rows x 6 columns]

"""
from .column_documents import column_documents


def documents_by_institution(
    directory="./",
):
    return column_documents(
        column="institutions",
        directory=directory,
    )

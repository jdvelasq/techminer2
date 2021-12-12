"""
Most Local Cited Documents
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/most_local_cited_documents.png"
>>> most_local_cited_documents(directory=directory).savefig(file_name)

.. image:: images/most_local_cited_documents.png
    :width: 700px
    :align: center


>>> most_local_cited_documents(directory=directory, plot=False).head()
                                                    global_citations  ...                          doi
document_id                                                           ...                             
Abdullah EME et al, 2018, INT J ENG TECHNOL                        8  ...  10.14419/IJET.V7I2.29.13140
Abu Daqar MAM et al, 2020, BANKS BANK SYST                         2  ...   10.21511/BBS.15(3).2020.03
Acar O et al, 2019, PROCEDIA COMPUT SCI                           10  ...  10.1016/J.PROCS.2019.09.138
Ahern D et al, 2021, EUR BUS ORG LAW REV                           0  ...   10.1007/S40804-021-00217-Z
Al Nawayseh MK et al, 2020, J OPEN INNOV: TECHN...                10  ...        10.3390/JOITMC6040153
<BLANKLINE>
[5 rows x 5 columns]


"""

from .cleveland_dot_chart import cleveland_dot_chart
from .document_indicators import document_indicators


def most_local_cited_documents(
    top_n=20,
    color="k",
    figsize=(8, 6),
    directory="./",
    plot=True,
):
    indicators = document_indicators(directory=directory)

    if plot is False:
        return indicators

    indicators = indicators.sort_values(by="local_citations", ascending=False)
    indicators = indicators.head(top_n)
    indicators = indicators.local_citations

    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        title="Most Local Cited Documents",
        xlabel="Local Citations",
        ylabel="Document",
    )

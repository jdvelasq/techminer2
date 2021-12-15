"""
Most Global Cited Documents
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/most_global_cited_documents.png"
>>> most_global_cited_documents(directory=directory).savefig(file_name)

.. image:: images/most_global_cited_documents.png
    :width: 700px
    :align: center

>>> most_global_cited_documents(directory=directory, plot=False).head()
                                                                     doi  ...  global_citations_per_year
document_id                                                               ...                           
Gomber P et al, 2018, J MANAGE INF SYST    10.1080/07421222.2018.1440766  ...                  55.000000
Gabor D et al, 2017, NEW POLIT ECON        10.1080/13563467.2017.1259298  ...                  29.200000
Schueffel P et al, 2016, J INNOV MANAG   10.24840/2183-0606_004.004_0004  ...                  17.666667
Leong C et al, 2017, INT J INF MANAGE    10.1016/J.IJINFOMGT.2016.11.006  ...                  20.200000
Haddad C et al, 2019, SMALL BUS ECON           10.1007/S11187-018-9991-X  ...                  32.333333
<BLANKLINE>
[5 rows x 3 columns]


"""


from .cleveland_dot_chart import cleveland_dot_chart
from .document_indicators import document_indicators
from .utils import load_filtered_documents


def most_global_cited_documents(
    top_n=20,
    color="k",
    figsize=(8, 6),
    directory="./",
    plot=True,
):

    indicators = document_indicators(
        global_citations=True,
        normalized_citations=False,
        top_n=None,
        directory=directory,
    )
    indicators = indicators.set_index("document_id")

    if plot is False:
        indicators.pop("authors")
        indicators.pop("document_title")
        indicators.pop("source_name")
        indicators.pop("iso_source_name")
        indicators.pop("record_no")

        documents = load_filtered_documents(directory=directory)
        max_year = documents.pub_year.max()
        indicators = indicators.assign(
            global_citations_per_year=indicators.global_citations
            / (max_year - indicators.pub_year + 1)
        )
        indicators.pop("pub_year")

        return indicators

    indicators = indicators.global_citations
    indicators = indicators.head(top_n)

    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        title="Most Global Cited Documents",
        xlabel="Total Citations",
        ylabel="Document",
    )

"""
Most Global Cited Countries (!)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/most_global_cited_countries.png"
>>> most_global_cited_countries(
...     top_n=20,
...     directory=directory,
... ).write_image(file_name)

.. image:: images/most_global_cited_countries.png
    :width: 700px
    :align: center


>>> column_indicators("countries",directory=directory).head()
                num_documents  ...  avg_document_global_citations
countries                      ...                               
china                      43  ...                              7
united kingdom             41  ...                             12
indonesia                  22  ...                              2
united states              22  ...                             22
australia                  18  ...                             17
<BLANKLINE>
[5 rows x 4 columns]

"""
from ._bibliometrix_scatter_plot import bibliometrix_scatter_plot
from .column_indicators import column_indicators


def most_global_cited_countries(directory="./", top_n=20):

    indicators = column_indicators(column="countries", directory=directory)
    indicators = indicators.sort_values(
        by=["global_citations", "num_documents", "local_citations"], ascending=False
    )
    indicators = indicators.head(top_n)

    return bibliometrix_scatter_plot(
        x=indicators.global_citations,
        y=indicators.index,
        title="Most global cited countries",
        text=indicators.global_citations,
        xlabel="Global citations",
        ylabel="Country",
    )

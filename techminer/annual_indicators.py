"""
Annual indicators
===============================================================================

>>> from . import annual_indicators
>>> directory = "/workspaces/techminer-api/data/"
>>> annual_indicators(directory)
          num_documents  ...  cum_local_citations
pub_year                 ...                     
2015                  6  ...                   39
2016                 20  ...                  190
2017                 55  ...                  920
2018                124  ...                 1549
2019                122  ...                 1866
2020                223  ...                 2123
2021                269  ...                 2233
2022                  7  ...                 2234
<BLANKLINE>
[8 rows x 8 columns]


>>> from . import line_chart
>>> line_chart(annual_indicators(directory).num_documents, title="Annual Scientific Production")
<Figure size 600x600 with 1 Axes>

.. image:: images/annual_scientific_production.png
    :width: 600px
    :align: center

"""


from .utils import load_filtered_documents


def annual_indicators(directory="./"):

    indicators = load_filtered_documents(directory)
    indicators = indicators.assign(num_documents=1)
    indicators = indicators[
        [
            "pub_year",
            "num_documents",
            "local_citations",
            "global_citations",
        ]
    ].copy()
    indicators = indicators.groupby("pub_year", as_index=True).sum()
    indicators = indicators.sort_index(ascending=True, axis="index")
    indicators = indicators.assign(
        mean_global_citations=indicators.global_citations / indicators.num_documents
    )
    indicators = indicators.assign(
        mean_local_citations=indicators.local_citations / indicators.num_documents
    )
    indicators = indicators.assign(cum_num_documents=indicators.num_documents.cumsum())
    indicators = indicators.assign(
        cum_global_citations=indicators.global_citations.cumsum()
    )
    indicators = indicators.assign(
        cum_local_citations=indicators.local_citations.cumsum()
    )

    return indicators

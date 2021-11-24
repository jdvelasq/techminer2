"""
Annual indicators
===============================================================================

>>> from . import annual_indicators
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> annual_indicators(directory)
          num_documents  ...  cum_local_citations
pub_year                 ...                     
1986                  1  ...                    0
1998                  1  ...                    0
2002                  1  ...                    0
2003                  1  ...                    0
2008                  1  ...                   12
2010                  2  ...                   12
2011                  2  ...                   12
2013                  2  ...                   12
2014                  1  ...                   12
2015                 10  ...                   75
2016                 33  ...                  367
2017                 89  ...                 1618
2018                227  ...                 2830
2019                272  ...                 3426
2020                473  ...                 3922
2021                519  ...                 4104
2022                 14  ...                 4105
<BLANKLINE>
[17 rows x 8 columns]

>>> from . import line_chart
>>> line_chart(annual_indicators()['num_documents'], title="Annual Scientific Production")
<Figure size 600x600 with 1 Axes>

.. image:: images/annual_scientific_production.png
    :width: 600px
    :align: center

"""


from .utils import load_filtered_documents


def annual_indicators(directory=None):
    if directory is None:
        directory = "/workspaces/techminer-api/tests/data/"

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


if __name__ == "__main__":
    import doctest

    doctest.testmod()

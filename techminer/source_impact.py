"""
Source impact
===============================================================================



>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/source_impact.png"
>>> source_impact(20, directory=directory).savefig(file_name)

.. image:: images/source_impact.png
    :width: 650px
    :align: center


>>> impact_indicators("iso_source_name", directory=directory).sort_values('h_index', ascending=False).head(20)
                               num_documents  ...  avg_global_citations
FINANCIAL INNOV                           11  ...                 12.00
SUSTAINABILITY                            15  ...                  6.47
ENVIRON PLANN A                            4  ...                  7.50
FRONTIER ARTIF INTELL                      5  ...                  4.60
J ASIAN FINANC ECON BUS                    3  ...                  5.33
J MANAGE INF SYST                          4  ...                 72.75
SMALL BUS ECON                             4  ...                 27.50
PROCEDIA COMPUT SCI                        4  ...                  6.00
J OPEN INNOV: TECHNOL MARK CO              8  ...                  4.38
INVESTM MANANGE FINANC INNOV               4  ...                  7.00
EUR BUS ORG LAW REV                        3  ...                 11.00
NEW POLIT ECON                             3  ...                 54.00
J THEOR APPL ELECTRON COMMER               3  ...                  1.67
EUR RES STUD                               2  ...                 20.00
EUR J FINANC                               4  ...                  6.00
J FINANC REGUL                             2  ...                 11.00
J ECON BUS                                 2  ...                 62.50
ELECTRON MARK                              2  ...                 64.50
INT J ENG TECHNOL                          2  ...                 13.50
REV FINANC STUD                            3  ...                 45.33
<BLANKLINE>
[20 rows x 9 columns]

"""


from .cleveland_dot_chart import cleveland_dot_chart
from .impact_indicators import impact_indicators


def source_impact(
    top_n=20,
    metric="h_index",
    color="k",
    figsize=(8, 6),
    directory="./",
):
    indicators = impact_indicators(directory=directory, column="iso_source_name")[
        metric
    ]
    indicators = indicators.sort_values(ascending=False).head(top_n)

    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        title="Source local impact",
        xlabel=metric.replace("_", " ").title(),
        ylabel="Source",
    )

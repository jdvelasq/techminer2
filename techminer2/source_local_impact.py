"""
Source Local Impact
===============================================================================



>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/source_local_impact.png"
>>> source_local_impact(impact_measure='h_index', top_n=20, directory=directory).savefig(file_name)

.. image:: images/source_local_impact.png
    :width: 700px
    :align: center


>>> source_local_impact(impact_measure='h_index', top_n=20, directory=directory, plot=False).head()
                         num_documents  ...  avg_global_citations
iso_source_name                         ...                      
FINANCIAL INNOV                     11  ...                 12.00
SUSTAINABILITY                      15  ...                  6.47
ENVIRON PLANN A                      4  ...                  7.50
FRONTIER ARTIF INTELL                5  ...                  4.60
J ASIAN FINANC ECON BUS              3  ...                  5.33
<BLANKLINE>
[5 rows x 9 columns]

"""


from ._cleveland_chart import _cleveland_chart
from .impact_indicators import impact_indicators


def source_local_impact(
    impact_measure="h_index",
    top_n=20,
    color="k",
    figsize=(8, 6),
    directory="./",
    plot=True,
):
    if impact_measure not in ["h_index", "g_index", "m_index", "global_citations"]:
        raise ValueError(
            "Impact measure must be one of: h_index, g_index, m_index, global_citations"
        )

    indicators = impact_indicators(directory=directory, column="iso_source_name")
    indicators = indicators.sort_values(by=impact_measure, ascending=False)

    if plot is False:
        return indicators

    indicators = indicators[impact_measure].head(top_n)

    return _cleveland_chart(
        indicators,
        figsize=figsize,
        color=color,
        title="Source Local Impact by " + impact_measure.capitalize(),
        xlabel=impact_measure.capitalize(),
        ylabel="Sources",
    )

"""
Source Local Impact (!)
===============================================================================



>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/source_local_impact.png"
>>> source_local_impact(
...     impact_measure='h_index', 
...     top_n=20, 
...     directory=directory,
... ).write_image(file_name)

.. image:: images/source_local_impact.png
    :width: 700px
    :align: center


>>> impact_indicators("iso_source_name", directory=directory)[
...     [
...         'h_index',
...         'g_index',
...         'm_index',
...         'global_citations',
...         'num_documents', 
...         'first_pb_year',
...     ]   
... ].head()
                 h_index  g_index  ...  num_documents  first_pb_year
iso_source_name                    ...                              
ACCOUNT FINANC         1        1  ...              1           2018
AM BEHAV SCI           0        0  ...              1           2020
ANN OPER RES           0        0  ...              1           2021
APPL SCI               0        0  ...              1           2021
BANKS BANK SYST        2        1  ...              3           2019
<BLANKLINE>
[5 rows x 6 columns]

"""
from ._bibliometrix_scatter_plot import bibliometrix_scatter_plot
from .impact_indicators import impact_indicators


def source_local_impact(
    impact_measure="h_index",
    top_n=20,
    directory="./",
):
    if impact_measure not in [
        "h_index",
        "g_index",
        "m_index",
        "global_citations",
    ]:
        raise ValueError(
            "Impact measure must be one of: h_index, g_index, m_index, global_citations"
        )

    indicators = impact_indicators(directory=directory, column="iso_source_name")
    indicators = indicators.sort_values(by=impact_measure, ascending=False)
    indicators = indicators[impact_measure].head(top_n)

    return bibliometrix_scatter_plot(
        x=indicators,
        y=indicators.index,
        title="Source Local Impact by " + impact_measure.capitalize(),
        text=indicators,
        xlabel=impact_measure.replace("_", " ").title(),
        ylabel="Source Title",
    )

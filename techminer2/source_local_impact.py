"""
Source Local Impact (*)
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


>>> from pprint import pprint
>>> columns = impact_indicators("iso_source_name", directory=directory).columns.to_list()
>>> columns = sorted(columns)
>>> pprint(columns)
['age',
 'avg_global_citations',
 'first_pb_year',
 'g_index',
 'global_citations',
 'global_citations_per_year',
 'h_index',
 'm_index',
 'num_documents']


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

"""
Author Local Impact
===============================================================================



>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/author_local_impact.png"
>>> author_local_impact(
...     impact_measure='h_index', 
...     top_n=20, 
...     directory=directory,
... ).savefig(file_name)

.. image:: images/author_local_impact.png
    :width: 700px
    :align: center


>>> author_local_impact(
...     impact_measure='h_index', 
...     top_n=20, 
...     directory=directory, 
...     plot=False,
... ).head()
          num_documents  ...  avg_global_citations
Wojcik D              5  ...                  3.80
Hornuf L              3  ...                 36.67
Arqawi S              2  ...                  2.50
Zhang MX              2  ...                  6.00
Khan S                2  ...                 18.50
<BLANKLINE>
[5 rows x 9 columns]

"""


from .indicators_api.impact_indicators import impact_indicators
from .visualization_api.cleveland_dot_chart import cleveland_dot_chart


def author_local_impact(
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

    indicators = impact_indicators(directory=directory, column="authors")
    indicators = indicators.sort_values(by=impact_measure, ascending=False)

    if plot is False:
        return indicators

    indicators = indicators[impact_measure].head(top_n)

    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        title="Authors Local Impact by " + impact_measure.capitalize(),
        xlabel=impact_measure.capitalize(),
        ylabel="Authors",
    )

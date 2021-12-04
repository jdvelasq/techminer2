"""
Author local impact plot
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/author_local_impact.png"
>>> author_local_impact(n_authors=20, directory=directory).savefig(file_name)

.. image:: images/author_local_impact_plot.png
    :width: 650px
    :align: center

>>> author_local_impact(n_authors=20, directory=directory, plot=False).head()
               num_documents  ...  avg_global_citations
Aas TH                     1  ...                   0.0
Abakah EJA                 1  ...                  17.0
Abbas F                    1  ...                   5.0
Abdullah EME               1  ...                   8.0
Abu Daqar MAM              1  ...                   2.0
<BLANKLINE>
[5 rows x 9 columns]

"""


from .cleveland_dot_chart import cleveland_dot_chart
from .impact_indicators import impact_indicators


def author_local_impact(
    metric="h_index",
    n_authors=30,
    figsize=(6, 6),
    directory="./",
    plot=True,
):
    indicators = impact_indicators("authors", directory=directory)
    if plot is False:
        return indicators
    indicators = indicators[metric]
    indicators = indicators.sort_values(ascending=False).head(n_authors)
    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        title="Author Local Impact",
        xlabel=metric.replace("_", " ").title(),
        ylabel="Authors",
    )

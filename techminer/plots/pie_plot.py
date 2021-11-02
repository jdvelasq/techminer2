import textwrap

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

TEXTLEN = 40


def pie_plot(
    x,
    darkness=None,
    colormap="Greys",
    figsize=(6, 6),
    fontsize=11,
    wedgeprops={
        "width": 0.6,
        "edgecolor": "k",
        "linewidth": 0.5,
        "linestyle": "-",
        "antialiased": True,
    },
):
    """Plot a pie chart.

    Examples
    ----------------------------------------------------------------------------------------------

    >>> import pandas as pd
    >>> df = pd.DataFrame(
    ...     {
    ...         "Num_Documents": [3, 2, 2, 1],
    ...         "Global_Citations": [1, 2, 3, 4],
    ...     },
    ...     index="author 3,author 1,author 0,author 2".split(","),
    ... )
    >>> df
              Num_Documents  Global_Citations
    author 3              3            1
    author 1              2            2
    author 0              2            3
    author 2              1            4
    >>> fig = pie(x=df['num_records'], darkness=df['global_citations'], cmap="Blues")
    >>> fig.savefig('/workspaces/techminer/sphinx/images/pieplot.png')

    .. image:: images/pieplot.png
        :width: 400px
        :align: center


    """
    darkness = x if darkness is None else darkness

    cmap = plt.cm.get_cmap(colormap)
    colors = [
        cmap(0.1 + 0.90 * (d - min(darkness)) / (max(darkness) - min(darkness)))
        for d in darkness
    ]

    matplotlib.rc("font", size=fontsize)
    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    ax.pie(
        x=x,
        labels=x.index,
        colors=colors,
        wedgeprops=wedgeprops,
    )

    fig.set_tight_layout(True)

    return fig

"""
Column Cleveland Dot Chart
===============================================================================

Plots the number of documents per item in the selected column


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/column_cleveland_dot_chart.jpg"
>>> column_cleveland_dot_chart(
...    column="authors", 
...    directory=directory,
... ).savefig(file_name)

.. image:: images/column_cleveland_dot_chart.jpg
    :width: 700px
    :align: center


>>> column_cleveland_dot_chart(
...     column='authors',
...     directory=directory, 
...     plot=False,
... )
                num_documents  global_citations  local_citations
authors                                                         
Wojcik D                    5                19                4
Hornuf L                    3               110               24
Rabbani MR                  3                39                3
Gomber P                    2               228               34
Kauffman RJ                 2               228               34
Parker C                    2               228               34
Weber BW                    2               228               34
Gozman D                    2                63                8
Dolata M                    2                54               10
Schwabe G                   2                54               10
Zavolokina L                2                54               10
Khan S                      2                37                2
Bernards N                  2                35               12
Thalassinos EI              2                21                2
Iman N                      2                19                7
Mention A-L                 2                18               10
Giudici P                   2                18                1
Kou G                       2                17                1
Dincer H                    2                15                0
Yuksel S                    2                15                0


>>> column_cleveland_dot_chart(
...     column='authors',
...     directory=directory, 
...     plot=False,
...     sort_index=dict(ascending=True),
... )
                num_documents  global_citations  local_citations
authors                                                         
Bernards N                  2                35               12
Dincer H                    2                15                0
Dolata M                    2                54               10
Giudici P                   2                18                1
Gomber P                    2               228               34
Gozman D                    2                63                8
Hornuf L                    3               110               24
Iman N                      2                19                7
Kauffman RJ                 2               228               34
Khan S                      2                37                2
Kou G                       2                17                1
Mention A-L                 2                18               10
Parker C                    2               228               34
Rabbani MR                  3                39                3
Schwabe G                   2                54               10
Thalassinos EI              2                21                2
Weber BW                    2               228               34
Wojcik D                    5                19                4
Yuksel S                    2                15                0
Zavolokina L                2                54               10


>>> column_cleveland_dot_chart(
...     column='authors',
...     directory=directory, 
...     plot=False,
...     sort_values=dict(by='local_citations', ascending=False),
... )
                num_documents  global_citations  local_citations
authors                                                         
Gomber P                    2               228               34
Kauffman RJ                 2               228               34
Parker C                    2               228               34
Weber BW                    2               228               34
Hornuf L                    3               110               24
Bernards N                  2                35               12
Dolata M                    2                54               10
Schwabe G                   2                54               10
Zavolokina L                2                54               10
Mention A-L                 2                18               10
Gozman D                    2                63                8
Iman N                      2                19                7
Wojcik D                    5                19                4
Rabbani MR                  3                39                3
Khan S                      2                37                2
Thalassinos EI              2                21                2
Giudici P                   2                18                1
Kou G                       2                17                1
Dincer H                    2                15                0
Yuksel S                    2                15                0

"""


from .cleveland_dot_chart import cleveland_dot_chart
from .column_indicators import column_indicators
from .column_indicators_subset import column_indicators_subset


def column_cleveland_dot_chart(
    column,
    top_n=20,
    color="k",
    figsize=(9, 6),
    directory="./",
    metric="num_documents",
    sort_values=None,
    sort_index=None,
    plot=True,
):

    indicators = column_indicators(column, directory=directory)
    indicators = column_indicators_subset(
        column=column,
        indicators=indicators,
        metric=metric,
        top_n=top_n,
        sort_values=sort_values,
        sort_index=sort_index,
    )

    indicators = indicators.head(top_n)

    if plot is False:
        return indicators

    indicators = indicators[metric]

    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        xlabel=metric.replace("_", " ").title(),
        ylabel=column.replace("_", " ").title(),
    )

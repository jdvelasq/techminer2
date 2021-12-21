"""
Thematic Analysis / Map
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/thematic_analysis_map.png"
>>> thematic_analysis_map(
...     column="author_keywords",
...     min_occ=4,
...     norm="l2",
...     use_idf=True,
...     smooth_idf=True,
...     sublinear_tf=False,
...     n_clusters=6,
...     linkage="ward",
...     affinity="euclidean",
...     directory=directory,
...     random_state=0, 
... ).savefig(file_name)


.. image:: images/thematic_analysis_map.png
    :width: 700px
    :align: center


"""

from .thematic_analysis import ThematicAnalysis


def thematic_analysis_map(
    column,
    min_occ=None,
    norm="l2",
    use_idf=True,
    smooth_idf=True,
    sublinear_tf=False,
    n_clusters=6,
    linkage="ward",
    affinity="euclidean",
    directory="./",
    random_state=0,
    dim_x=0,
    dim_y=1,
    color_scheme="clusters",
    figsize=(9, 9),
):
    analysis = ThematicAnalysis(
        column=column,
        min_occ=min_occ,
        norm=norm,
        use_idf=use_idf,
        smooth_idf=smooth_idf,
        sublinear_tf=sublinear_tf,
        n_clusters=n_clusters,
        linkage=linkage,
        affinity=affinity,
        directory=directory,
        random_state=random_state,
    )

    return analysis.map(
        dim_x=dim_x,
        dim_y=dim_y,
        color_scheme=color_scheme,
        figsize=figsize,
    )

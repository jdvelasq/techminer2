"""
Thematic Analysis / Partitions
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> thematic_analysis_partitions(
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
... )
CLUSTER
0    120
1      7
2     12
3     32
4      6
5      6
Name: num_documents, dtype: int64


"""

from .thematic_analysis import ThematicAnalysis


def thematic_analysis_partitions(
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

    return analysis.partitions

"""
Thematic Analysis / Themes
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> thematic_analysis_themes(
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
... ).head()
                     CL_0                    CL_1  ...     CL_4      CL_5
0                 fintech  financial technologies  ...  fintech  covid-19
1  financial technologies    peer-to-peer lending  ...            fintech
2                    bank                 fintech  ...            bitcoin
3              innovation              regulation  ...                   
4       financial service                          ...                   
<BLANKLINE>
[5 rows x 6 columns]


"""

from .tf_idf_matrix import tf_idf_matrix

# from .thematic_analysis import ThematicAnalysis


def thematic_analysis_themes(
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

    return analysis.themes

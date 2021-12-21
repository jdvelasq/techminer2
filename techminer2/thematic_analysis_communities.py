"""
Thematic Analysis / Communities
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> thematic_analysis_communities(
...     tfidf_matrix, 
...     clustering_method=KMeans(n_clusters=6, random_state=0), 
...     manifold_method=MDS(random_state=0)
... ).themes_by_words_
author_keywords    fintech  ... open innovation
#d                     139  ...             3  
#c                    1285  ...            12  
THEME_0           3.531425  ...        0.000000
THEME_1           4.109095  ...        0.000000
THEME_2          15.040339  ...        1.521395
THEME_3          21.000000  ...        0.000000
THEME_4           2.715340  ...        0.000000
THEME_5           2.014328  ...        0.628626
<BLANKLINE>
[6 rows x 59 columns]


"""

from .tf_idf_matrix import tf_idf_matrix
from .thematic_analysis import ThematicAnalysis


def thematic_analysis_communities(
    column,
    min_occ=None,
    max_occ=None,
    scheme=None,
    norm="l2",
    use_idf=True,
    smooth_idf=True,
    sublinear_tf=False,
    max_items=3000,
    directory="./",
    manifold_method=None,
    clustering_method=None,
):
    tfidf_matrix = tf_idf_matrix(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        scheme=scheme,
        norm=norm,
        use_idf=use_idf,
        smooth_idf=smooth_idf,
        sublinear_tf=sublinear_tf,
        max_items=max_items,
        directory=directory,
    )

    thematic_analysis = ThematicAnalysis(
        tf_idf_matrix=tfidf_matrix,
        manifold_method=manifold_method,
        clustering_method=clustering_method,
    )

    return thematic_analysis.themes_by_words_

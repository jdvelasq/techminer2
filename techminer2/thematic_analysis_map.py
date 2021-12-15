"""
Thematic analysis --- map
===============================================================================


>>> from techminer2 import *
>>> from sklearn.cluster import KMeans
>>> from sklearn.manifold import MDS
>>> directory = "/workspaces/techminer-api/data/"
>>> tfidf_matrix = tf_idf_matrix('author_keywords', min_occ=3, directory=directory)
>>> thematic_analysis(
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

>>> file_name = "/workspaces/techminer-api/sphinx/images/thematic_analysis_map.png"
>>> thematic_analysis(
...     tfidf_matrix, 
...     clustering_method=KMeans(n_clusters=6), 
...     manifold_method=MDS()
... ).map().savefig(file_name)

.. image:: images/thematic_analysis_map.png
    :width: 700px
    :align: center

"""

from .tf_idf_matrix import tf_idf_matrix
from .thematic_analysis import ThematicAnalysis


def thematic_analysis_map(
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
    dim_x=0,
    dim_y=1,
    color_scheme="clusters",
    figsize=(7, 7),
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

    return thematic_analysis.map(
        dim_x=dim_x,
        dim_y=dim_y,
        color_scheme=color_scheme,
        figsize=figsize,
    )

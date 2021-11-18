"""
Thematic analysis
===============================================================================

This analysis is used to obtain and explore a representation of the documents
throught thematic clusters.

The implemented methodology is based on the Thematic Analysis of Elementary
Contexts implemented in T-LAB.

**Algorithm**

    1. Obtain the TF-IDF normalized matrix with rows scaled to unit length 
       using the Euclidean norm. Rows represent documents and columns represent
       keywords.

    2. Clustering the rows (cosine similarity).

    3. Build a table of keywords by clusters.

    4. Analyze the keywords by clusters.


Visualization with n-1 clusters    


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> tfidf_matrix = TfIdfMatrix(directory, 'author_keywords', min_occ=13)
>>> thematic_analysis(tfidf_matrix, clustering_method=KMeans(n_clusters=6), manifold_method=MDS()).themes_by_words_
author_keywords     fintech blockchain financial inclusion  \\
#d                      882        131                 72    
#c                     5181       1031                742    
THEME_0           68.084530   2.034130            0.000000   
THEME_1          334.000000   0.000000            0.000000   
THEME_2            8.019709   2.418918            4.570119   
THEME_3           23.158876  70.478395            0.000000   
THEME_4           11.314807   1.552039           41.276159   
THEME_5            8.505424   4.494321            1.506909   
...
author_keywords financial institutions smart contracts financial literacy  
#d                                  13              13                 13   
#c                                 274              19                 24    
THEME_0                       7.968039        2.653674           7.329968  
THEME_1                       0.000000        0.000000           0.000000  
THEME_2                       1.339041        0.000000           0.823928  
THEME_3                       0.000000        7.683336           0.000000  
THEME_4                       0.550843        0.000000           3.092813  
THEME_5                       0.000000        0.000000           0.000000  

>>> thematic_analysis(tfidf_matrix, clustering_method=KMeans(n_clusters=6), manifold_method=MDS()).map()

.. image:: images/thematic_analysis_map.png
    :width: 700px
    :align: center

"""
import numpy as np
import pandas as pd

from .co_occurrence_matrix import co_occurrence_matrix
from .co_occurrence_network_analysis import co_occurrence_network_analysis
from .plots import bubble_map


class ThematicAnalysis:
    def __init__(self, tf_idf_matrix, manifold_method, clustering_method):
        self.tf_idf_matrix = tf_idf_matrix.copy()
        self.clustering_method = clustering_method
        self.manifold_method = manifold_method
        self.themes_by_words_ = None
        self.run()

    def run(self):

        self.clustering_method.fit(self.tf_idf_matrix)
        clustered_tf_idf_matrix = self.tf_idf_matrix.copy()
        clustered_tf_idf_matrix["CLUSTER"] = self.clustering_method.labels_
        themes_by_words = clustered_tf_idf_matrix.groupby("CLUSTER").sum()
        themes_by_words.index = [
            "THEME_{:d}".format(i) for i in range(len(themes_by_words))
        ]
        self.themes_by_words_ = themes_by_words.copy()

        new_n_components = self.clustering_method.get_params()["n_clusters"] - 1
        self.manifold_method.set_params(n_components=new_n_components)
        decomposed_themes_by_words_ = self.manifold_method.fit_transform(
            themes_by_words
        )

        self.decomposed_themes_by_words_ = pd.DataFrame(
            decomposed_themes_by_words_,
            columns=[f"DIM-{i}" for i in range(new_n_components)],
            index=["THEME_{:d}".format(i) for i in range(len(themes_by_words))],
        )

        self.num_documents_by_theme_ = clustered_tf_idf_matrix.groupby("CLUSTER").size()

        self.cluster_centers_ = self.clustering_method.cluster_centers_

    def map(self, dim_x=0, dim_y=1, color_scheme="clusters", figsize=(7, 7)):

        return bubble_map(
            node_x=self.decomposed_themes_by_words_["DIM-{:d}".format(dim_x)],
            node_y=self.decomposed_themes_by_words_["DIM-{:d}".format(dim_y)],
            node_clusters=range(len(self.decomposed_themes_by_words_)),
            node_texts=self.decomposed_themes_by_words_.index.tolist(),
            node_sizes=self.num_documents_by_theme_,
            x_axis_at=0,
            y_axis_at=0,
            color_scheme=color_scheme,
            xlabel=f"X-Axis (Dim-{dim_x})",
            ylabel=f"Y-Axis (Dim-{dim_y})",
            figsize=figsize,
            fontsize=7,
        )

    # def table(self):
    #     return self.co_occurrence_network.table()

    # def network(self):
    #     return self.co_occurrence_network.plot()

    # def clusters(self):
    #     return self.clusters_


def thematic_analysis(
    tf_idf_matrix,
    manifold_method,
    clustering_method,
):

    return ThematicAnalysis(
        tf_idf_matrix=tf_idf_matrix,
        manifold_method=manifold_method,
        clustering_method=clustering_method,
    )

"""
Co-Word Analysis
===============================================================================


>>> directory = "data/regtech/"


>>> from sklearn.cluster import AgglomerativeClustering


>>> from techminer2 import tlab__co_occurrence_analysis__co_word_analysis
>>> cwa = tlab__co_occurrence_analysis__co_word_analysis(
...     criterion='words',
...     topics_length=10,
...     clustering_method=AgglomerativeClustering(n_clusters=5),
...     directory=directory,
... )

>>> file_name = "sphinx/_static/tlab__co_occ__co_word_analysis_mds_map.html"
>>> cwa.mds_map_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/tlab__co_occ__co_word_analysis_mds_map.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> file_name = "sphinx/_static/tlab__co_occ__co_word_analysis_tsne_map.html"
>>> cwa.tsne_map_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/tlab__co_occ__co_word_analysis_tsne_map.html" height="600px" width="100%" frameBorder="0"></iframe>



>>> cwa.communities_
                            CL_00  ...                        CL_04
0  artificial intelligence 19:071  ...  financial regulation 17:367
1               blockchain 18:109  ...                             
2                                  ...                             
3                                  ...                             
<BLANKLINE>
[4 rows x 5 columns]





"""
from dataclasses import dataclass

import pandas as pd
import plotly.express as px
from sklearn.manifold import MDS, TSNE
from sklearn.metrics.pairwise import (
    cosine_distances,
    euclidean_distances,
    haversine_distances,
)

from ._association_index import association_index
from ._bubble_map import bubble_map
from .vantagepoint.analyze.matrix.co_occ_matrix import co_occ_matrix


@dataclass(init=False)
class _Results:
    communities_: None
    mds_map_: None
    tsne_map_: None


def tlab__co_occurrence_analysis__co_word_analysis(
    criterion,
    topics_length=None,
    topic_min_occ=None,
    topic_min_citations=None,
    normalization="association",
    #
    distance_metric="euclidean_distances",
    clustering_method=None,
    #
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Word Association"""

    if criterion not in [
        "raw_author_keywords",
        "raw_index_keywords",
        "raw_title_words",
        "raw_abstract_words",
        "raw_words",
        "author_keywords",
        "index_keywords",
        "title_words",
        "abstract_words",
        "words",
    ]:
        raise ValueError(
            "criterion must be one of: "
            "{'author_keywords', 'index_keywords', 'title_words', 'abstract_words', 'words', "
            "{'raw_author_keywords', 'raw_index_keywords', 'raw_title_words', 'raw_abstract_words', "
            "'raw_words'}"
        )

    #
    # Algorithm:
    #

    matrix = co_occ_matrix(
        criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix = association_index(matrix, association=normalization)

    if distance_metric == "euclidean_distances":
        distance_metric_fn = euclidean_distances
    elif distance_metric == "cosine_distances":
        distance_metric_fn = cosine_distances
    elif distance_metric == "haversine_distance":
        distance_metric_fn = haversine_distances
    else:
        raise ValueError(
            "distance_metric must be one of: "
            "{'euclidean_distances', 'cosine_distances', 'haversine_distance'}"
        )

    dissimilarity_matrix = pd.DataFrame(
        distance_metric_fn(matrix),
        columns=matrix.columns,
        index=matrix.columns,
    )

    clustering_method.fit(dissimilarity_matrix)

    results = _Results()
    results.communities_ = _get_matrix_communities(
        clustering_method, dissimilarity_matrix
    )
    results.mds_map_ = _get_manifold_map(
        matrix=dissimilarity_matrix,
        clustering_method=clustering_method,
        manifold_method=MDS(n_components=2),
    )

    results.tsne_map_ = _get_manifold_map(
        matrix=dissimilarity_matrix,
        clustering_method=clustering_method,
        manifold_method=TSNE(n_components=2),
    )

    return results


def _get_manifold_map(matrix, clustering_method, manifold_method):

    transformed_matrix = manifold_method.fit_transform(matrix)

    nodes = matrix.index.to_list()
    node_occ = [int(name.split()[-1].split(":")[0]) for name in nodes]
    node_global_citations = [int(name.split()[-1].split(":")[-1]) for name in nodes]

    manifold_data = pd.DataFrame(
        {
            "node": nodes,
            "OCC": node_occ,
            "global_citations": node_global_citations,
        }
    )

    manifold_data["Dim-0"] = transformed_matrix[:, 0]
    manifold_data["Dim-1"] = transformed_matrix[:, 1]

    manifold_data["cluster"] = clustering_method.labels_

    manifold_data["color"] = manifold_data["cluster"].map(
        lambda x: px.colors.qualitative.Dark24[x]
        if x < 24
        else px.colors.qualitative.Light24[x]
    )

    fig = bubble_map(
        node_x=manifold_data["Dim-0"],
        node_y=manifold_data["Dim-1"],
        node_text=manifold_data["node"],
        node_color=manifold_data["color"],
        node_size=manifold_data["OCC"],
    )

    return fig


def _get_matrix_communities(clustering_method, dissimilarity_matrix):
    """Extracts communities from a dissimilarity matrix"""

    communities = {}
    for cluster_id, cluster in enumerate(clustering_method.labels_):
        text = f"CL_{cluster :02d}"
        if text not in communities:
            communities[text] = []
        communities[text].append(dissimilarity_matrix.columns[cluster_id])

    for key, items in communities.items():
        communities[key] = sorted(items)

    pdf = pd.DataFrame.from_dict(communities, orient="index").T
    pdf = pdf.fillna("")
    pdf = pdf.sort_index(axis=1)

    return pdf

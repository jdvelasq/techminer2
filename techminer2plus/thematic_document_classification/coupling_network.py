# flake8: noqa
"""
Documents Network
===============================================================================

1. Compute the TF matrix.
2. Apply TF-IDF transformation
3. Clustering using cosine distance
4. Obtain the table of units by clusters


>>> ROOT_DIR = "data/regtech/"
>>> import techminer2plus
>>> import techminer2plus
>>> root_dir = "data/regtech/"
>>> # 1. Define the clustering method and number of clusters
>>> from sklearn.cluster import AgglomerativeClustering
>>> estimator = AgglomerativeClustering(
...     n_clusters=5,
... ) 
>>> # 2. Compute the TF-IDF matrix
>>> tf_matrix = techminer2plus.analyze.tfidf.tf_matrix(
...     field='author_keywords',
...     top_n=50,
...     root_dir=root_dir,
... )
>>> tf_idf_matrix = techminer2plus.analyze.tfidf.tf_idf_matrix(tf_matrix)


------------

>>> coupling_matrix = techminer2plus.analyze.coupling.coupling_matrix(
...     field="author_keywords",
...     top_n=20,
...     root_dir=ROOT_DIR,
... )

>>> graph = techminer2plus.analyze.coupling.coupling_network(
...    coupling_matrix,
...    algorithm_or_estimator="louvain",
... )



>>> print(techminer2plus.analyze.network.network_communities(graph).to_markdown())




# pylint: disable=line-too-long
"""
# from ..coupling import coupling_matrix


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def coupling_network(
    tf_idf_matrix,
    estimator,
):
    """Documents Network."""

    # Document-term matrix
    dt_matrix = tf_idf_matrix.table_.copy()

    # Clustering
    estimator.fit(dt_matrix)
    dt_matrix["CLUSTER"] = [f"CL_{label:>02d}" for label in estimator.labels_]

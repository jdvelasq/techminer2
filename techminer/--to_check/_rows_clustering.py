#
#

import pandas as pd
from sklearn.cluster import KMeans


def rows_clustering(
    matrix,
    cluster_estimator=None,
):

    if cluster_estimator is None:
        cluster_estimator = KMeans(n_clusters=3, random_state=0)

    cluster_estimator.fit(matrix)
    clusters = cluster_estimator.predict(matrix)

    cluster_members = pd.Series(
        data=clusters,
        index=matrix.index,
        name="cluster",
    )

    cluster_centers = pd.DataFrame(
        data=cluster_estimator.cluster_centers_,
        index=[f"CLUST_{i}" for i in range(cluster_estimator.n_clusters)],
        columns=matrix.columns,
    )

    return cluster_members, cluster_centers

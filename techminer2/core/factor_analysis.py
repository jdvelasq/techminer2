# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from typing import Literal

import graphviz
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.decomposition import PCA, KernelPCA, TruncatedSVD
from sklearn.manifold import MDS, TSNE
from sklearn.metrics.pairwise import cosine_similarity

from ..metrics.tfidf import tfidf as _tfidf
from ..co_occurrence.compute_co_occurrence_matrix import compute_co_occurrence_matrix
from ..co_occurrence.normalize_co_occurrence_matrix import (
    normalize_co_occurrence_matrix,
)
from .manifold_2d_map import manifold_2d_map

CLUSTER_COLORS = (
    px.colors.qualitative.Dark24
    + px.colors.qualitative.Light24
    + px.colors.qualitative.Pastel1
    + px.colors.qualitative.Pastel2
    + px.colors.qualitative.Set1
    + px.colors.qualitative.Set2
    + px.colors.qualitative.Set3
)


class ConceptGridClustering:
    def __init__(self, threshold):
        self.threshold = threshold
        self.labels_ = None
        self.n_clusters_ = None

    def fit(self, matrix):
        #
        #
        labels = {index: None for index in matrix.index}
        i_cluster = 0
        matrix = matrix.copy()

        for i_col, col in enumerate(matrix.columns):
            #
            # Upper part:
            selected_matrix = matrix.loc[matrix.iloc[:, i_col] > self.threshold, :]
            max_col = selected_matrix.idxmax(axis=1)
            selected_matrix = selected_matrix.loc[max_col == col, :]
            if selected_matrix.shape[0] > 0:
                found = False
                for index in selected_matrix.index:
                    if labels[index] is None:
                        labels[index] = i_cluster
                        found = True
                if found is True:
                    i_cluster += 1

            #
            # Lower part
            selected_matrix = matrix.loc[matrix.iloc[:, i_col] < -self.threshold, :]
            min_col = selected_matrix.idxmin(axis=1)
            selected_matrix = selected_matrix.loc[min_col == col, :]
            if selected_matrix.shape[0] > 0:
                found = False
                for index in selected_matrix.index:
                    if labels[index] is None:
                        labels[index] = i_cluster
                        found = True
                if found is True:
                    i_cluster += 1

        self.labels_ = [labels[index] for index in matrix.index]
        self.n_clusters_ = len(set(self.labels_))


class FactorAnalyzer:
    def __init__(self, field):
        #
        #
        self.field = field
        self.embedding_estimator = None
        self.matrix_values = None
        self.embedding_ = None
        self.n_components = None
        self.clustering_estimator = None
        self.n_clusters = None
        self.cluster_centers_ = None
        self.communities_ = None
        self.communtiies_dict_ = None
        self.labels_ = None
        self.threshold = None
        self.communities_dict_ = None

    # --------------------------------------------------------------------------------------------
    # STEP 1: Embedding
    #
    def cooc_matrix(
        self,
        #
        # COOC PARAMS:
        association_index=None,
        #
        # ITEM PARAMS:
        top_n=None,
        occ_range=(None, None),
        gc_range=(None, None),
        custom_items=None,
        #
        # DATABASE PARAMS:
        root_dir="./",
        database="main",
        year_filter=(None, None),
        cited_by_filter=(None, None),
        **filters,
    ):
        matrix = compute_co_occurrence_matrix(
            #
            # FUNCTION PARAMS:
            columns=self.field,
            #
            # COLUMN PARAMS:
            col_top_n=top_n,
            col_occ_range=occ_range,
            col_gc_range=gc_range,
            col_custom_items=custom_items,
            #
            # DATABASE PARAMS:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )
        matrix = normalize_co_occurrence_matrix(matrix, association_index)
        self.matrix_values = matrix.df_

    def tfidf(
        self,
        #
        # TF PARAMS:
        is_binary: bool = True,
        cooc_within: int = 1,
        #
        # TF-IDF parameters:
        norm: Literal["l1", "l2", None] = None,
        use_idf=False,
        smooth_idf=False,
        sublinear_tf=False,
        #
        # ITEM PARAMS:
        top_n=None,
        occ_range=(None, None),
        gc_range=(None, None),
        custom_items=None,
        #
        # DATABASE PARAMS:
        root_dir="./",
        database="main",
        year_filter=(None, None),
        cited_by_filter=(None, None),
        **filters,
    ):
        matrix = _tfidf(
            #
            # TF PARAMS:
            field=self.field,
            is_binary=is_binary,
            cooc_within=cooc_within,
            #
            # ITEM FILTERS:
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
            custom_items=custom_items,
            #
            # TF-IDF parameters:
            norm=norm,
            use_idf=use_idf,
            smooth_idf=smooth_idf,
            sublinear_tf=sublinear_tf,
            #
            # DATABASE PARAMS:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

        self.matrix_values = matrix.T

    # --------------------------------------------------------------------------------------------
    # STEP 2: Embedding
    #
    def kernel_pca(
        self,
        #
        # KERNEL PCA PARAMS:
        n_components=None,
        kernel="linear",
        gamma=None,
        degree=3,
        coef0=1,
        kernel_params=None,
        alpha=1.0,
        fit_inverse_transform=False,
        eigen_solver="auto",
        tol=0,
        max_iter=None,
        iterated_power="auto",
        remove_zero_eig=False,
        random_state=0,
    ):
        if n_components is None:
            n_components = min(min(self.matrix_values.shape) - 1, 100)

        self.n_components = n_components

        self.embedding_estimator = KernelPCA(
            n_components=n_components,
            kernel=kernel,
            gamma=gamma,
            degree=degree,
            coef0=coef0,
            kernel_params=kernel_params,
            alpha=alpha,
            fit_inverse_transform=fit_inverse_transform,
            eigen_solver=eigen_solver,
            tol=tol,
            max_iter=max_iter,
            iterated_power=iterated_power,
            remove_zero_eig=remove_zero_eig,
            random_state=random_state,
        )

    def pca(
        self,
        #
        # PCA PARAMS:
        n_components=None,
        whiten=False,
        svd_solver="auto",
        tol=0.0,
        iterated_power="auto",
        n_oversamples=10,
        power_iteration_normalizer="auto",
        random_state=0,
    ):
        if n_components is None:
            n_components = min(min(self.matrix_values.shape) - 1, 100)

        self.n_components = n_components

        self.embedding_estimator = PCA(
            n_components=n_components,
            whiten=whiten,
            svd_solver=svd_solver,
            tol=tol,
            iterated_power=iterated_power,
            n_oversamples=n_oversamples,
            power_iteration_normalizer=power_iteration_normalizer,
            random_state=random_state,
        )

    def svd(
        self,
        #
        # SVD PARAMS:
        n_components=None,
        algorithm="randomized",
        n_iter=5,
        n_oversamples=10,
        power_iteration_normalizer="auto",
        random_state=0,
        tol=0.0,
    ):
        if n_components is None:
            n_components = min(min(self.matrix_values.shape) - 1, 100)

        self.n_components = n_components

        self.embedding_estimator = TruncatedSVD(
            n_components=n_components,
            algorithm=algorithm,
            n_iter=n_iter,
            n_oversamples=n_oversamples,
            power_iteration_normalizer=power_iteration_normalizer,
            random_state=random_state,
            tol=tol,
        )

    # --------------------------------------------------------------------------------------------
    #
    def compute_embedding(self):
        #
        #
        self.embedding_estimator.fit(self.matrix_values)
        trans_matrix_values = self.embedding_estimator.transform(self.matrix_values)

        n_zeros = int(np.log10(self.n_components - 1)) + 1
        fmt = "DIM_{:0" + str(n_zeros) + "d}"
        columns = [fmt.format(i_component) for i_component in range(self.n_components)]

        embedding = pd.DataFrame(
            trans_matrix_values,
            index=self.matrix_values.index,
            columns=columns,
        )
        embedding.index.name = self.matrix_values.index.name
        self.embedding_ = embedding

    # --------------------------------------------------------------------------------------------
    # Embedding Results
    #
    def embedding(self):
        return self.embedding_.copy()

    def embedding_2d_chart(
        self,
        #
        # MAP PARAMS:
        dim_x,
        dim_y,
        node_color="#465c6b",
        node_size=10,
        textfont_size=8,
        textfont_color="#465c6b",
        xaxes_range=None,
        yaxes_range=None,
    ):
        return manifold_2d_map(
            node_x=self.embedding_[dim_x],
            node_y=self.embedding_[dim_y],
            node_text=self.embedding_.index.to_list(),
            node_color=node_color,
            node_size=node_size,
            title_x=dim_x,
            title_y=dim_y,
            textfont_size=textfont_size,
            textfont_color=textfont_color,
            xaxes_range=xaxes_range,
            yaxes_range=yaxes_range,
        )

    def cosine_similarities(
        self,
    ):
        similarity = cosine_similarity(self.embedding_)

        term_similarities = []
        for i in range(similarity.shape[0]):
            values_to_sort = []
            for j in range(similarity.shape[1]):
                if i != j and similarity[i, j] > 0:
                    values_to_sort.append(
                        (
                            self.embedding_.index[j],
                            similarity[i, j],
                        )
                    )
            sorted_values = sorted(values_to_sort, key=lambda x: x[1], reverse=True)
            sorted_values = [f"{x[0]} ({x[1]:>0.3f})" for x in sorted_values]
            sorted_values = "; ".join(sorted_values)
            term_similarities.append(sorted_values)

        term_similarities = pd.DataFrame(
            {"cosine_similariries": term_similarities},
            index=self.embedding_.index,
        )

        return term_similarities

    def tsne(
        self,
        #
        # TSNE PARAMS:
        perplexity=10.0,
        early_exaggeration=12.0,
        learning_rate="auto",
        n_iter=1000,
        n_iter_without_progress=300,
        min_grad_norm=1e-07,
        metric="euclidean",
        metric_params=None,
        init="pca",
        random_state=0,
        method="barnes_hut",
        angle=0.5,
        n_jobs=None,
        #
        # MAP:
        node_color="#465c6b",
        node_size=10,
        textfont_size=8,
        textfont_color="#465c6b",
        xaxes_range=None,
        yaxes_range=None,
    ):
        decomposed_matrix = TSNE(
            n_components=2,
            perplexity=perplexity,
            early_exaggeration=early_exaggeration,
            learning_rate=learning_rate,
            n_iter=n_iter,
            n_iter_without_progress=n_iter_without_progress,
            min_grad_norm=min_grad_norm,
            metric=metric,
            metric_params=metric_params,
            init=init,
            random_state=random_state,
            method=method,
            angle=angle,
            n_jobs=n_jobs,
        ).fit_transform(self.embedding_)

        return manifold_2d_map(
            node_x=decomposed_matrix[:, 0],
            node_y=decomposed_matrix[:, 1],
            node_text=self.embedding_.index.to_list(),
            node_color=node_color,
            node_size=node_size,
            textfont_size=textfont_size,
            textfont_color=textfont_color,
            xaxes_range=xaxes_range,
            yaxes_range=yaxes_range,
        )

    def mds(
        self,
        #
        # MDS PARAMS:
        metric=True,
        n_init=4,
        max_iter=300,
        eps=0.001,
        n_jobs=None,
        random_state=0,
        dissimilarity="euclidean",
        #
        # MAP:
        node_color="#465c6b",
        node_size=10,
        textfont_size=8,
        textfont_color="#465c6b",
        xaxes_range=None,
        yaxes_range=None,
    ):
        decomposed_matrix = MDS(
            n_components=2,
            metric=metric,
            n_init=n_init,
            max_iter=max_iter,
            eps=eps,
            n_jobs=n_jobs,
            random_state=random_state,
            dissimilarity=dissimilarity,
        ).fit_transform(self.embedding_)

        return manifold_2d_map(
            node_x=decomposed_matrix[:, 0],
            node_y=decomposed_matrix[:, 1],
            node_text=self.embedding_.index.to_list(),
            node_color=node_color,
            node_size=node_size,
            textfont_size=textfont_size,
            textfont_color=textfont_color,
            xaxes_range=xaxes_range,
            yaxes_range=yaxes_range,
        )

    # --------------------------------------------------------------------------------------------
    # Clustering
    #
    def kmeans(
        self,
        #
        # KMEANS PARAMS:
        n_clusters=8,
        init="k-means++",
        n_init=10,
        max_iter=300,
        tol=0.0001,
        random_state=0,
        algorithm: Literal["lloyd", "elkan", "auto", "full"] = "auto",
    ):
        self.n_clusters = n_clusters
        self.clustering_estimator = KMeans(
            n_clusters=n_clusters,
            init=init,
            n_init=n_init,
            max_iter=max_iter,
            tol=tol,
            random_state=random_state,
            algorithm=algorithm,
        )

    def hierarchical(
        self,
        #
        # HIERARCHICAL PARAMS:
        n_clusters,
        metric=None,
        memory=None,
        connectivity=None,
        compute_full_tree="auto",
        linkage="ward",
        distance_threshold=None,
    ):
        self.n_clusters = n_clusters
        self.clustering_estimator = AgglomerativeClustering(
            n_clusters=n_clusters,
            metric=metric,
            memory=memory,
            connectivity=connectivity,
            compute_full_tree=compute_full_tree,
            linkage=linkage,
            distance_threshold=distance_threshold,
        )

    def pcd(
        self,
        #
        # VANTAGEPOINT CONCEPT GRID PARAMS:
        threshold=0.5,
    ):
        self.clustering_estimator = ConceptGridClustering(threshold=threshold)

    # --------------------------------------------------------------------------------------------
    #
    def run_clustering(self, brute_force_labels):
        #
        # Selects first n_cluster components for clustering
        matrix = self.embedding_.iloc[:, : self.n_clusters]

        if brute_force_labels is None:
            #
            # Train the clustering estimator
            self.clustering_estimator.fit(matrix)

            #
            # Set n_clusters
            if self.n_clusters is None:
                self.n_clusters = self.clustering_estimator.n_clusters_

            #
            # Obtain the communities
            communities = {i_cluster: [] for i_cluster in range(self.n_clusters)}
            for item, label in zip(matrix.index, self.clustering_estimator.labels_):
                communities[label].append(item)

            #
            # Sorts the communities by the number of members
            lengths = [(key, len(communities[key])) for key in communities.keys()]
            lengths = sorted(lengths, key=lambda x: x[1], reverse=True)
            sorted_labels = [index for index, _ in lengths]
            old_2_new = {old: new for new, old in enumerate(sorted_labels)}
            labels = [old_2_new[label] for label in self.clustering_estimator.labels_]
            self.labels_ = labels

        else:
            self.labels_ = [brute_force_labels[index] for index in matrix.index]
            self.n_clusters = len(set(self.labels_))

        #
        # Recompute the communities with the new labels
        communities = {i_cluster: [] for i_cluster in range(self.n_clusters)}
        for item, label in zip(matrix.index, self.labels_):
            communities[label].append(item)

        #
        # Computes the centers
        centers = matrix.copy()
        centers["LABELS"] = self.labels_
        centers = centers.groupby("LABELS").mean()
        centers = centers.sort_index(axis=0)

        #
        # Formats cluster name with prefix CL_ and zeros
        n_zeros = int(np.log10(self.n_clusters - 1)) + 1
        fmt = "CL_{:0" + str(n_zeros) + "d}"
        cluster_names = {i_cluster: fmt.format(i_cluster) for i_cluster in range(self.n_clusters)}

        centers.index = centers.index.map(cluster_names)
        centers = centers.sort_index(axis=0)
        self.cluster_centers_ = centers.copy()

        #
        # Creates a dataframe with the communities
        communities = {fmt.format(key): communities[key] for key in communities.keys()}
        self.communities_dict_ = communities.copy()

        communities = pd.DataFrame.from_dict(communities, orient="index").T
        communities = communities.fillna("")
        communities = communities.sort_index(axis=1)
        self.communities_ = communities.copy()

    # --------------------------------------------------------------------------------------------
    # Clustering Results
    #
    def communities(self):
        return self.communities_

    def cluster_centers(self):
        return self.cluster_centers_.copy()

    def treemap(
        self,
        #
        # TREEMAP PARAMS:
        title,
    ):
        node_occ = []
        node_color = []
        node_text = []
        parents = []

        name2color = {}
        for name, label in zip(self.embedding_.index, self.labels_):
            name2color[name] = CLUSTER_COLORS[label]

        clusters = self.communities_dict_.copy()
        cluster_occ = {key: 0 for key in clusters}
        for key, names in clusters.items():
            for name in names:
                #
                # Extracs occurrences from node names. Example: 'regtech 10:100' -> 10
                occ = name.split(" ")[-1]
                occ = occ.split(":")[0]
                occ = float(occ)
                node_occ.append(occ)

                cluster_occ[key] += occ

                #
                # Uses the same color of clusters
                node_color.append(name2color[name])

                #
                # Sets text to node names without metrics
                node_name = name
                node_name = node_name.split(" ")[:-1]
                node_name = " ".join(node_name)

                node_text.append(node_name)
                parents.append(key)

        node_occ = [cluster_occ[key] * 0 for key in clusters] + node_occ
        node_color = ["lightgrey"] * len(clusters) + node_color
        node_text = list(clusters.keys()) + node_text
        parents = [""] * len(clusters) + parents

        fig = go.Figure()
        fig.add_trace(
            go.Treemap(
                labels=node_text,
                parents=parents,
                values=node_occ,
                textinfo="label+value+percent entry",
                opacity=0.9,
            )
        )
        fig.update_traces(marker={"cornerradius": 5})
        fig.update_layout(
            showlegend=False,
            margin={"t": 30, "l": 0, "r": 0, "b": 0},
            title=title if title is not None else "",
        )

        #
        # Change the colors of the treemap white
        fig.update_traces(
            #    marker={"line": {"color": "darkslategray", "width": 1}},
            marker_colors=node_color,
        )

        #
        # Change the font size of the labels
        fig.update_traces(textfont_size=12)

        return fig

    # --------------------------------------------------------------------------------------------
    # Concept Grid
    #
    def concept_grid(
        self,
        conserve_counters,
        n_head,
        fontsize,
    ):
        data_frame = self.communities()

        if n_head is not None:
            data_frame = data_frame.head(n_head)

        graph = graphviz.Digraph(
            "graph",
            node_attr={"shape": "record"},
        )

        for _, col in enumerate(data_frame.columns):
            text = data_frame[col].to_list()
            if conserve_counters is False:
                text = [" ".join(str(t).split(" ")[:-1]) for t in text]
            text = [t if t != "" else "." for t in text]
            text = "\\r".join(text) + "\\r"
            cluster_name = col
            graph.node(
                col,
                label=r"{" + cluster_name + "|" + text + r"}",
                fontsize=fontsize,
            )

        return graph

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from dataclasses import dataclass

import pandas as pd
from sklearn.manifold import MDS, TSNE

from ....manifold_2d_map import manifold_2d_map


@dataclass
class Results:
    df_: pd.DataFrame
    cosine_similarities_: pd.DataFrame

    # -----------------------------------------------------------------------------------
    # This plot is equivalent to the presented in TLAB / Co-occurrence Analysis /
    # Word Associations where the Co-occurrence matrix is decomposed using SVD,
    # and then, the a scatter plot for different dimmnensions is presented.
    #
    def fig_(
        self,
        dim_x,
        dim_y,
        #
        # MAP:
        node_color="#465c6b",
        node_size=10,
        textfont_size=8,
        textfont_color="#465c6b",
        xaxes_range=None,
        yaxes_range=None,
    ):
        return manifold_2d_map(
            node_x=self.df_[dim_x],
            node_y=self.df_[dim_y],
            node_text=self.df_.index.to_list(),
            node_color=node_color,
            node_size=node_size,
            title_x=dim_x,
            title_y=dim_y,
            textfont_size=textfont_size,
            textfont_color=textfont_color,
            xaxes_range=xaxes_range,
            yaxes_range=yaxes_range,
        )

    # -----------------------------------------------------------------------------------
    # TSNE map of the SVD decomposition
    #
    def TSNE_(
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
        ).fit_transform(self.df_)

        return manifold_2d_map(
            node_x=decomposed_matrix[:, 0],
            node_y=decomposed_matrix[:, 1],
            node_text=self.df_.index.to_list(),
            node_color=node_color,
            node_size=node_size,
            textfont_size=textfont_size,
            textfont_color=textfont_color,
            xaxes_range=xaxes_range,
            yaxes_range=yaxes_range,
        )

    # -----------------------------------------------------------------------------------
    # TSNE map of the SVD decomposition
    #
    def MDS_(
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
        ).fit_transform(self.df_)

        return manifold_2d_map(
            node_x=decomposed_matrix[:, 0],
            node_y=decomposed_matrix[:, 1],
            node_text=self.df_.index.to_list(),
            node_color=node_color,
            node_size=node_size,
            textfont_size=textfont_size,
            textfont_color=textfont_color,
            xaxes_range=xaxes_range,
            yaxes_range=yaxes_range,
        )

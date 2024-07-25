# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Cluster Records
===============================================================================

>>> from techminer2.tools import cluster_records 
>>> cluster_records(
...     field='author_keywords',
...     #
...     # ITEM FILTERS:
...     top_n=50,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_terms=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).write_html("sphinx/_static/tools/cluster_records.html")

.. raw:: html

    <iframe src="../_static/tools/cluster_records.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""

import numpy as np
import pandas as pd  # type: ignore
import plotly.express as px  # type: ignore
import plotly.graph_objects as go
from sklearn.manifold import MDS
from sklearn.neighbors import KernelDensity

from ..metrics.tfidf import tfidf


def cluster_records(
    field,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Cluster records based on the most frequent terms in a each record.

    :meta private:
    """
    tfidf_matrix = tfidf(
        field=field,
        is_binary=False,
        cooc_within=1,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # TF-IDF parameters:
        norm=None,
        use_idf=False,
        smooth_idf=False,
        sublinear_tf=False,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    mds = MDS(n_components=2, random_state=1)
    mds_matrix = pd.DataFrame(
        mds.fit_transform(tfidf_matrix),
        index=tfidf_matrix.index,
        columns=["x", "y"],
    )

    tfidf_matrix = tfidf_matrix.assign(ITEM_=None)

    # for each row in the dataframe, determines the first column with
    # a value greater than zero
    for idx in tfidf_matrix.index:
        tfidf_matrix.loc[idx, "ITEM_"] = tfidf_matrix.loc[idx, tfidf_matrix.loc[idx, :] > 0].index[0]

    mds_matrix = mds_matrix.assign(group=tfidf_matrix.ITEM_)

    # compute density
    kde = KernelDensity(bandwidth="silverman", kernel="gaussian").fit(mds_matrix[["x", "y"]])

    # matrix
    x_range = mds_matrix["x"].max() - mds_matrix["x"].min()
    x_max = mds_matrix["x"].max() + 0.05 * x_range
    x_min = mds_matrix["x"].min() - 0.05 * x_range

    y_range = mds_matrix["y"].max() - mds_matrix["y"].min()
    y_max = mds_matrix["y"].max() + 0.05 * y_range
    y_min = mds_matrix["y"].min() - 0.05 * y_range

    x_plot = np.linspace(x_min, x_max, 100)
    y_plot = np.linspace(y_min, y_max, 100)
    x_mtx_plot, y_mtx_plot = np.meshgrid(x_plot, y_plot)
    xy_plot = np.vstack([x_mtx_plot.ravel(), y_mtx_plot.ravel()]).T
    z_mtx = np.exp(kde.score_samples(xy_plot))
    z_mtx = z_mtx.reshape(x_mtx_plot.shape)

    fig = go.Figure(
        data=go.Contour(
            z=z_mtx,
            x=x_plot,
            y=y_plot,
            opacity=0.3,
            showscale=False,
            colorscale="Aggrnyl",
        )
    )

    group_names = mds_matrix.group.drop_duplicates().tolist()

    for i_name, name in enumerate(group_names):
        data = mds_matrix[mds_matrix.group == name]

        fig.add_trace(
            go.Scatter(
                x=data["x"],
                y=data["y"],
                mode="markers",
                marker=dict(
                    size=7,
                    color=px.colors.qualitative.Dark24[i_name],
                    colorscale="Viridis",
                    showscale=False,
                ),
                name=name,
                text=mds_matrix.index,
                hovertemplate="<b>%{text}</b><br><br>" + "<extra></extra>",
            )
        )

    # puts legend on the top right side
    fig.update_layout(
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
        )
    )

    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin=dict(l=1, r=1, t=1, b=1),
    )
    fig.update_layout(
        xaxis={
            "showgrid": False,
            "zeroline": False,
            "showticklabels": False,
        },
        yaxis={
            "showgrid": False,
            "zeroline": False,
            "showticklabels": False,
        },
    )

    fig.update_xaxes(range=[x_min, x_max])
    fig.update_yaxes(range=[y_min, y_max])

    return fig

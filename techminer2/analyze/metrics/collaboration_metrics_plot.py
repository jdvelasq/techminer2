# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Collaboration Metrics Plot
===============================================================================

>>> from techminer2.metrics import collaboration_metrics_plot
>>> plot = collaboration_metrics_plot(
...     #
...     # PARAMS:
...     field="countries",
...     #
...     # ITEM FILTERS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_terms=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> # plot.write_html("sphinx/_static/metrics/collaboration_metrics.html")

.. raw:: html

    <iframe src="../_static/metrics/collaboration_metrics.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
"""
import plotly.express as px  # type: ignore

from .collaboration_metrics_frame import collaboration_metrics_frame


def collaboration_metrics_plot(
    #
    # PARAMS:
    field,
    #
    # ITEM FILTERS:
    top_n,
    occ_range,
    gc_range,
    custom_terms,
    #
    # DATABASE PARAMS:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    """:meta private:"""

    #
    # Figure
    #
    def create_fig(field, metrics):
        #
        metrics = metrics.copy()
        metrics = metrics.reset_index()

        metrics = metrics.melt(
            id_vars=field,
            value_vars=["single_publication", "multiple_publication"],
        )
        metrics = metrics.rename(
            columns={"variable": "publication", "value": "Num Documents"}
        )
        metrics.publication = metrics.publication.map(
            lambda x: x.replace("_", " ").title()
        )
        metrics[field] = metrics[field].map(lambda x: x.title())

        fig = px.bar(
            metrics,
            x="Num Documents",
            y=field,
            color="publication",
            title="Corresponding Author's " + field.title(),
            hover_data=["Num Documents"],
            orientation="h",
            color_discrete_map={
                "Single Publication": "#7793a5",
                "Multiple Publication": "#465c6b",
            },
        )
        fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
        fig.update_yaxes(
            linecolor="gray",
            linewidth=2,
            autorange="reversed",
        )
        fig.update_xaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="gray",
            griddash="dot",
        )

        return fig

    #
    # MAIN CODE:
    #
    metrics = collaboration_metrics_frame(
        #
        # PARAMS:
        field=field,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    fig = create_fig(field, metrics)

    return fig

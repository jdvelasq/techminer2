# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""
Chart
===============================================================================


# >>> from techminer2.visualize.specialized_plots.trending_words import chart
# >>> plot = chart(
# ...     #
# ...     # ITEMS PARAMS:
# ...     field='author_keywords',
# ...     #
# ...     # TREND ANALYSIS:
# ...     time_window=2,
# ...     #
# ...     # CHART PARAMS:
# ...     metric_label=None,
# ...     field_label=None,
# ...     #
# ...     # ITEM FILTERS:
# ...     top_n=20,
# ...     occ_range=(None, None),
# ...     gc_range=(None, None),
# ...     custom_terms=None,
# ...     #
# ...     # DATABASE PARAMS:
# ...     root_dir="example/",
# ...     database="main",
# ...     year_filter=(None, None),
# ...     cited_by_filter=(None, None),
# ... )
# >>> plot.write_html("docs_src/_generated/px.visualize/specialized_charts/trending_words/chart.html")

.. raw:: html

    <iframe src="../../../_generated/visualize/specialized_charts/trending_words/chart.html"
    height="600px" width="100%" frameBorder="0"></iframe>



"""
import plotly.express as px  # type: ignore

from .dataframe import dataframe


def chart(
    #
    # ITEM PARAMS:
    field,
    #
    # TREND ANALYSIS:
    time_window=2,
    #
    # CHART PARAMS:
    metric_label=None,
    field_label=None,
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
    """:meta private:"""

    #
    # Extracs only the performance metrics data frame
    data_frame = dataframe(
        #
        # ITEMS PARAMS:
        field=field,
        #
        # TREND ANALYSIS:
        time_window=time_window,
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

    metric_label = "OCC" if metric_label is None else metric_label
    field_label = (
        field.replace("_", " ").upper() if field_label is None else field_label
    )

    # extracts the name of column starting with 'between'
    between = [_ for _ in data_frame.columns if _.startswith("between")][0]
    before = [_ for _ in data_frame.columns if _.startswith("before")][0]

    fig_data = data_frame[["OCC", before, between]].copy()
    fig_data[field] = fig_data.index
    fig_data = fig_data.reset_index(drop=True)

    fig_data = fig_data.melt(
        id_vars=field,
        value_vars=[before, between],
    )

    fig_data = fig_data.rename(
        columns={
            field: field.replace("_", " ").title(),
            "variable": "Period",
            "value": "Num Documents",
        }
    )

    fig = px.bar(
        fig_data,
        x="Num Documents",
        y=field.replace("_", " ").title(),
        color="Period",
        orientation="h",
        color_discrete_map={
            before: "#7793a5",
            between: "#465c6b",
        },
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
        title=field_label,
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="gray",
        griddash="dot",
    )

    return fig

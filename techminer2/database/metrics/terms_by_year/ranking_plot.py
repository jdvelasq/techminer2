# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Terms by Year Plot
===============================================================================

## >>> from techminer2.analyze.metrics import terms_by_year_plot
## >>> plot = terms_by_year_plot(
## 
## ...     #
## ...     # FILTER PARAMS:
## ...     metric='OCC',
## ...     .set_item_params(
## ...         field="author_keywords",
## ...         top_n=20,
## ...         occ_range=(None, None),
## ...         gc_range=(None, None),
## ...         custom_terms=None,
## ...     #
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     #
## ...     ).build()
## ... )
## >>> # plot.write_html("sphinx/_static/metrics/terms_by_plot.html")

.. raw:: html

    <iframe src="../_static/metrics/terms_by_year_plot.html" 
    height="800px" width="100%" frameBorder="0"></iframe>



"""
import plotly.express as px  # type: ignore

from .data_frame import PerformanceMetricsDataFrame

COLOR = "#465c6b"
TEXTLEN = 40


def terms_by_year_plot(
    #
    # FUNCTION PARAMS:
    field,
    #
    # FILTER PARAMS:
    metric="OCC",
    top_n=20,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """:meta private:"""

    def create_gantt_diagram(data_frame):
        #
        data_frame = data_frame.copy()
        data_frame["RANKING"] = range(1, len(data_frame) + 1)
        data_frame = data_frame.melt(
            value_name="OCC",
            var_name="column",
            ignore_index=False,
            id_vars=["RANKING"],
        )

        data_frame = data_frame[data_frame.OCC > 0]
        data_frame = data_frame.sort_values(by=["RANKING"], ascending=True)
        data_frame = data_frame.drop(columns=["RANKING"])

        data_frame = data_frame.rename(columns={"column": "Year"})
        data_frame = data_frame.reset_index()

        fig = px.scatter(
            data_frame,
            x="Year",
            y=field,
            size="OCC",
            hover_data=data_frame.columns.to_list(),
            color=field,
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            showlegend=False,
            xaxis_title=None,
            yaxis_title=field.replace("_", " ").upper(),
        )
        fig.update_traces(
            marker={
                "line": {"color": "white", "width": 0.5},
                "opacity": 1.0,
            },
            marker_color=COLOR,
            mode="lines+markers",
            line={"width": 2, "color": COLOR},
        )
        fig.update_xaxes(
            linecolor="white",
            linewidth=1,
            gridcolor="gray",
            griddash="dot",
            tickangle=270,
            dtick=1.0,
        )
        fig.update_yaxes(
            linecolor="white",
            linewidth=1,
            gridcolor="gray",
            griddash="dot",
        )

        return fig

    # --------------------------------------------------------------------------------------------
    data_frame = terms_by_year_frame(
        field=field,
        cumulative=False,
        #
        # FILTER PARAMS:
        metric=metric,
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

    fig = create_gantt_diagram(data_frame)

    return fig

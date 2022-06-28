"""Primitive to plot production over time."""

from .column_indicators import column_indicators
from .column_indicators_by_year import column_indicators_by_year
from .scatter_px import scatter_px


def production_over_time(
    column,
    top_n=10,
    directory="./",
    title=None,
):
    """Primitive to plot production over time."""

    indicators_by_year = _compute_production_over_time(
        column=column,
        top_n=top_n,
        directory=directory,
    )

    fig = scatter_px(
        dataframe=indicators_by_year,
        x_label="Year",
        y_label=column.replace("_", " ").title(),
        size="Num Documents",
        title=title,
    )
    fig.update_traces(
        marker=dict(
            line=dict(
                color="black",
                width=2,
            ),
        ),
        marker_color="darkslategray",
    )
    fig.update_yaxes(
        linecolor="white",
        linewidth=1,
        autorange="reversed",
        gridcolor="gray",
        griddash="dot",
    )
    fig.update_xaxes(
        linecolor="white",
        linewidth=1,
        gridcolor="gray",
        griddash="dot",
        tickangle=270,
    )
    fig.update_layout(
        xaxis_type="category",
    )
    return fig


def _compute_production_over_time(
    column,
    top_n=10,
    directory="./",
):

    indicators_by_year = column_indicators_by_year(column=column, directory=directory)
    indicators_by_year = indicators_by_year.reset_index()
    selected_terms = column_indicators(column=column, directory=directory).head(top_n)
    terms = selected_terms.index.to_list()

    indicators_by_year = indicators_by_year[
        indicators_by_year[column].map(lambda x: x in terms)
    ]

    indicators_by_year = indicators_by_year.rename(
        columns={
            col: col.replace("_", " ").title() for col in indicators_by_year.columns
        }
    )
    indicators_by_year = indicators_by_year.rename(columns={"Pub Year": "Year"})

    return indicators_by_year

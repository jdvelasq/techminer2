# This function is used to create a horizontal bar plot with the data provided.
# The output is a horizontal bar plot.
# The input parameters are the dataframe, the x axis label, the y axis label and the title.


import plotly.express as px


def bar_px(
    dataframe,
    x_label,
    y_label,
    title,
):
    """Create a horizontal bar plot using Plotly Express.

    Args:
        dataframe (pd.DataFrame): The data to plot.
        x_label (str): The label for the x-axis.
        y_label (str): The label for the y-axis.
        title (str): The title of the plot.

    Returns:
        plotly.graph_objs._figure.Figure: The plotly figure object.

    """

    figure = px.bar(
        dataframe,
        x=x_label,
        y=y_label,
        hover_data=dataframe.columns.to_list(),
        title=title,
        orientation="h",
    )
    figure.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
    )
    figure.update_traces(
        marker_color="rgb(171,171,171)",
        marker_line={"color": "darkslategray"},
    )
    figure.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
    )
    figure.update_yaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
        gridcolor="lightgray",
        griddash="dot",
    )
    return figure

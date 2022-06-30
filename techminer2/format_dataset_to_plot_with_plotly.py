"""Formats a dataframe for plotting."""
import textwrap

TEXTLEN = 40


def format_dataset_to_plot_with_plotly(
    dataframe,
    metric,
):
    """Formats a dataframe for plotting."""

    metric = metric.replace("_", " ").title()
    column = dataframe.index.name.replace("_", " ").title()
    dataframe = dataframe.reset_index()
    dataframe.rename(
        columns={col: col.replace("_", " ").title() for col in dataframe.columns},
        inplace=True,
    )
    if dataframe[column].dtype != "int64":
        dataframe[column] = dataframe[column].apply(_shorten)

    return metric, column, dataframe


def _shorten(text):
    return textwrap.shorten(
        text=text,
        width=TEXTLEN,
        placeholder="...",
        break_long_words=False,
    )

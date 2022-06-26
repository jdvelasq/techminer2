"""Formats a dataframe for plotting."""
import textwrap

TEXTLEN = 40


def format_dataset_to_plot(
    dataframe,
    metric,
):
    """Formats a dataframe for plotting."""

    metric = metric.replace("_", " ").title()
    column = dataframe.index.name.replace("_", " ").title()

    dataframe = dataframe.reset_index()
    names_dict = {col: col.replace("_", " ").title() for col in dataframe.columns}
    dataframe.rename(columns=names_dict, inplace=True)
    dataframe[column] = dataframe[column].str.title()

    if dataframe.index.dtype != "int64":
        dataframe.index = [
            textwrap.shorten(
                text=text,
                width=TEXTLEN,
                placeholder="...",
                break_long_words=False,
            )
            for text in dataframe.index.to_list()
        ]

    return metric, column, dataframe

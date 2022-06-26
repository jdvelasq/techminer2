"""Formats a dataframe for plotting."""
import textwrap

TEXTLEN = 40


def prepare_plot(
    dataframe,
    column,
):
    """Formats a dataframe for plotting."""

    x_label = column.replace("_", " ").title()
    y_label = dataframe.index.name.replace("_", " ").title()

    dataframe = dataframe.reset_index()
    names_dict = {col: col.replace("_", " ").title() for col in dataframe.columns}
    dataframe.rename(columns=names_dict, inplace=True)
    dataframe[y_label] = dataframe[y_label].str.title()

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

    return x_label, y_label, dataframe

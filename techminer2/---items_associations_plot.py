"""
Items Assocations Plot
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/items_associations_plot.html"

>>> items_associations_plot(
...     'regtech', 
...     'author_keywords',
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/items_associations_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from .tlab__word_associations_for_a_item import tlab__word_associations_for_a_item
from .bar_px import bar_px
from .cleveland_px import cleveland_px
from .column_px import column_px
from .line_px import line_px
from .pie_px import pie_px


def items_associations_plot(
    item,
    column,
    top_n=10,
    directory="./",
    database="documents",
    plot="cleveland",
):
    """Items association plot."""

    word_associations = tlab__word_associations_for_a_item(
        item=item,
        column=column,
        directory=directory,
        database=database,
    ).to_frame()

    word_associations = word_associations.head(top_n)

    word_associations = word_associations.reset_index()
    word_associations = word_associations.rename(
        columns={column: column.replace("_", " ").title()}
    )

    # word_associations = word_associations.set_index(column.replace("_", " ").title())

    plot_function = {
        "bar": bar_px,
        "column": column_px,
        "line": line_px,
        "pie": pie_px,
        "cleveland": cleveland_px,
    }[plot]

    return plot_function(
        dataframe=word_associations,
        x_label="OCC",
        y_label=column.replace("_", " ").title(),
        title=f"Word associations of '{item}'",
    )

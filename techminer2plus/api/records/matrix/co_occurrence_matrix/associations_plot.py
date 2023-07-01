# flake8: noqa
"""
Associations Plot
===============================================================================

Plots the co-occurrences of a given descriptor with the remaining descriptors.




>>> root_dir = "data/regtech/"
>>> import techminer2plus
>>> cooc_matrix = techminer2plus.co_occurrence_matrix(
...    columns='author_keywords',
...    col_top_n=20,
...    root_dir=root_dir,
... )
>>> associations = techminer2plus.item_associations("REGTECH", cooc_matrix)
>>> file_name = "sphinx/_static/associations_plot.html"
>>> chart = techminer2plus.associations_plot(associations)
>>> chart.fig_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/associations_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>
 
    


# pylint: disable=line-too-long
"""


from ...list_items.ranking_chart import ranking_chart


def associations_plot(
    item_associations,
    title=None,
    field_label=None,
    metric_label=None,
):
    """association plot"""

    if title is None:
        title = f"Co-occurrence with of '{item_associations.item_}' with '{item_associations.field_}'"

    item_associations.df_.columns = ["OCC"]

    return ranking_chart(
        item_associations,
        title=title,
        field_label=field_label,
        metric_label=metric_label,
    )

# flake8: noqa
# pylint: disable=line-too-long
"""
.. _associations_plot:

Associations Plot
===============================================================================

Plots the co-occurrences of a given descriptor with the remaining descriptors.

* Preparation

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

* Object oriented interface

>>> fig = (
...     tm2p.records(root_dir=root_dir)
...     .co_occurrence_matrix(
...         columns='author_keywords',
...         col_top_n=20,
...     )
...     .item_associations(item="REGTECH") 
...     .associations_plot()
... )

>>> cooc_matrix = tm2p.co_occurrence_matrix(
...    columns='author_keywords',
...    col_top_n=20,
...    root_dir=root_dir,
... )
>>> associations = tm2p.item_associations(
...     item="REGTECH", 
...     cooc_matrix=cooc_matrix,
... )
>>> fig = tm2p.associations_plot(associations)

* Results:

>>> fig.write_html("sphinx/_static/associations_plot.html")

.. raw:: html

    <iframe src="../../_static/associations_plot.html" height="600px" width="100%" frameBorder="0"></iframe>
 
    
"""


from .ranking_chart import ranking_chart


def associations_plot(
    item_associations,
    title=None,
    field_label=None,
    metric_label=None,
):
    """association plot"""

    if title is None:
        item_name = item_associations.df_.iloc[:, 0].name
        series_name = item_associations.df_.iloc[:, 0].index.name
        title = f"Co-occurrence with of '{item_name}' with '{series_name}'"

    item_associations.df_.columns = ["OCC"]

    return ranking_chart(
        item_associations,
        title=title,
        field_label=field_label,
        metric_label=metric_label,
    )

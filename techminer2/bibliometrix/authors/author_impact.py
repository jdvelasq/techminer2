"""
Author Impact
===============================================================================



Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__author_impact.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.authors.author_impact(
...     impact_measure='h_index',
...     top_n=20,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__author_impact.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> print(r.table_.head().to_markdown())



>>> print(r.prompt_)




# pylint: disable=line-too-long
"""
# from ..utils import bbx_impact_by_item


# pylint: disable=too-many-arguments
def author_impact(
    impact_measure="h_index",
    root_dir="./",
    database="documents",
    # Plot options:
    plot="cleveland_dot_chart",
    title=None,
    impact_measure_label=None,
    field_label=None,
    # Item filters:
    top_n=20,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database filters:
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Plots the selected impact measure by author."""

    if title is None:
        "Author Local Impact by " + impact_measure.replace("_", " ").title()

    obj = bbx_impact_by_item(
        field="authors",
        metric=impact_measure,
        root_dir=root_dir,
        database=database,
        # Plot options:
        plot=plot,
        title=title,
        metric_label=impact_measure_label,
        field_label=field_label,
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database filters:
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    obj.prompt_ = _create_prompt(obj.table_, impact_measure)

    return obj


def _create_prompt(table, impact_measure):
    return f"""\
The table below provides data on top {table.shape[0]} authors with the \
highest {impact_measure.replace("_", "-").title()}. 'OCC' represents the \
number of documents published by the author in the dataset. Use the \
information in the table to draw conclusions about the impact and \
productivity of the author. In your analysis, be sure to describe in a clear \
and concise way, any findings or any patterns you observe, and identify any \
outliers or anomalies in the data. Limit your description to one paragraph \
with no more than 250 words.

{table.to_markdown()}


"""

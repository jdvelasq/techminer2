# flake8: noqa
"""
Most Global Cited Organizations
===============================================================================


Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_global_cited_organizations.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.organizations.most_global_cited_organizations(
...     root_dir=root_dir,
...     top_n=20,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_global_cited_organizations.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> r.table_.head()
authors
Arner DW             185
Buckley RP           185
Barberis JN          161
Anagnostopoulos I    153
Butler T/1            41
Name: global_citations, dtype: int64



>>> print(r.prompt_)
Analyze the table below, which provides bibliometric indicators for the field 'authors' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| authors           |   OCC |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |
|:------------------|------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|
| Arner DW          |     3 |                185 |                 8 |                           61.67 |                           2.67 |
| Buckley RP        |     3 |                185 |                 8 |                           61.67 |                           2.67 |
| Barberis JN       |     2 |                161 |                 3 |                           80.5  |                           1.5  |
| Anagnostopoulos I |     1 |                153 |                17 |                          153    |                          17    |
| Butler T/1        |     2 |                 41 |                19 |                           20.5  |                           9.5  |
| OBrien L          |     1 |                 33 |                14 |                           33    |                          14    |
| Baxter LG         |     1 |                 30 |                 0 |                           30    |                           0    |
| Weber RH          |     1 |                 24 |                 5 |                           24    |                           5    |
| Zetzsche DA       |     1 |                 24 |                 5 |                           24    |                           5    |
| Breymann W        |     1 |                 21 |                 8 |                           21    |                           8    |
| Gross FJ          |     1 |                 21 |                 8 |                           21    |                           8    |
| Kavassalis P      |     1 |                 21 |                 8 |                           21    |                           8    |
| Saxton K          |     1 |                 21 |                 8 |                           21    |                           8    |
| Stieber H         |     1 |                 21 |                 8 |                           21    |                           8    |
| Hamdan A          |     2 |                 18 |                 5 |                            9    |                           2.5  |
| Turki M           |     2 |                 18 |                 5 |                            9    |                           2.5  |
| Lin W             |     2 |                 17 |                 4 |                            8.5  |                           2    |
| Singh C           |     2 |                 17 |                 4 |                            8.5  |                           2    |
| Brennan R         |     2 |                 14 |                 3 |                            7    |                           1.5  |
| Crane M           |     2 |                 14 |                 3 |                            7    |                           1.5  |
<BLANKLINE>
<BLANKLINE>




# pylint: disable=line-too-long
"""
from ...vantagepoint.analyze import list_view
from ..utils import bbx_generic_indicators_by_item


# pylint: disable=too-many-arguments
def most_global_cited_organizations(
    root_dir="./",
    database="documents",
    # Plot options:
    plot="cleveland_dot_chart",
    metric_label=None,
    field_label=None,
    title=None,
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
    """Most global cited organizations.

    Args:
        root_dir (str): path to the database directory.
        database (str): name of the database.
        plot (str): plot type. Options: 'bar_chart', 'cleveland_dot_chart', 'column_chart', 'line_chart'.
        metric_label (str): metric label.
        field_label (str): field label.
        title (str): plot title.
        top_n (int): number of items to be plotted.
        occ_range (tuple): range of occurrences.
        gc_range (tuple): range of global citations.
        custom_items (list): list of items to be plotted.
        year_filter (tuple): range of years.
        cited_by_filter (tuple): range of citations.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.

    Returns:
        BasicChart: A basic chart object.

    # pylint: disable=line-too-long
    """

    if title is None:
        title = "Most Global Cited Organizations"

    return bbx_generic_indicators_by_item(
        fnc_view=list_view,
        field="authors",
        root_dir=root_dir,
        database=database,
        metric="global_citations",
        # Plot options:
        plot=plot,
        metric_label=metric_label,
        field_label=field_label,
        title=title,
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

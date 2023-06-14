# flake8: noqa
"""
Most Local Cited Authors
===============================================================================


Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_local_cited_authors.html"


>>> from techminer2 import bibliometrix
>>> r = bibliometrix.authors.most_local_cited_authors(
...     top_n=20,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_local_cited_authors.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()    
authors
Butler T/1           19
Anagnostopoulos I    17
OBrien L             14
Arner DW              8
Buckley RP            8
Name: local_citations, dtype: int64



>>> print(r.prompt_)
Analyze the table below, which provides bibliometric indicators for the field 'authors' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| authors           |   OCC |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |
|:------------------|------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|
| Butler T/1        |     2 |                 41 |                19 |                           20.5  |                           9.5  |
| Anagnostopoulos I |     1 |                153 |                17 |                          153    |                          17    |
| OBrien L          |     1 |                 33 |                14 |                           33    |                          14    |
| Arner DW          |     3 |                185 |                 8 |                           61.67 |                           2.67 |
| Buckley RP        |     3 |                185 |                 8 |                           61.67 |                           2.67 |
| Breymann W        |     1 |                 21 |                 8 |                           21    |                           8    |
| Gross FJ          |     1 |                 21 |                 8 |                           21    |                           8    |
| Kavassalis P      |     1 |                 21 |                 8 |                           21    |                           8    |
| Saxton K          |     1 |                 21 |                 8 |                           21    |                           8    |
| Stieber H         |     1 |                 21 |                 8 |                           21    |                           8    |
| Weber RH          |     1 |                 24 |                 5 |                           24    |                           5    |
| Zetzsche DA       |     1 |                 24 |                 5 |                           24    |                           5    |
| Hamdan A          |     2 |                 18 |                 5 |                            9    |                           2.5  |
| Turki M           |     2 |                 18 |                 5 |                            9    |                           2.5  |
| Brooks R          |     1 |                  8 |                 5 |                            8    |                           5    |
| Lin W             |     2 |                 17 |                 4 |                            8.5  |                           2    |
| Singh C           |     2 |                 17 |                 4 |                            8.5  |                           2    |
| Sarea A           |     2 |                 12 |                 4 |                            6    |                           2    |
| Anasweh M         |     1 |                 11 |                 4 |                           11    |                           4    |
| Cummings RT       |     1 |                 11 |                 4 |                           11    |                           4    |
<BLANKLINE>
<BLANKLINE>

# pylint: disable=line-too-long
"""
from ...vantagepoint.analyze import list_items
from ..utils import bbx_generic_indicators_by_item


# pylint: disable=too-many-arguments
def most_local_cited_authors(
    root_dir="./",
    database="main",
    # Plot options:
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
    metric_label=None,
    field_label=None,
    title=None,
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database filters:
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Most local cited authors.

    Args:
        root_dir (str): path to the database directory.
        database (str): name of the database.
        textfont_size (int, optional): Font size. Defaults to 10.
        marker_size (int, optional): Marker size. Defaults to 6.
        line_color (str, optional): Line color. Defaults to "black".
        line_width (int, optional): Line width. Defaults to 1.
        yshift (int, optional): Y shift. Defaults to 4.
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
        title = "Most Local Cited Authors"

    return bbx_generic_indicators_by_item(
        fnc_view=list_items,
        field="authors",
        root_dir=root_dir,
        database=database,
        metric="local_citations",
        # Plot options:
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_color=line_color,
        line_width=line_width,
        yshift=yshift,
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

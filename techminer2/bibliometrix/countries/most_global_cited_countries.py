# flake8: noqa
"""
Most Global Cited Countries
===============================================================================



Example
-------------------------------------------------------------------------------

>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_global_cited_countries.html"


>>> from techminer2 import bibliometrix
>>> r = bibliometrix.countries.most_global_cited_countries(
...     directory=directory,
...     topics_length=20,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_global_cited_countries.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> r.table_.head()
countries
United Kingdom    199
Australia         199
Hong Kong         185
United States      59
Ireland            55
Name: global_citations, dtype: int64

>>> print(r.prompt_)
Analyze the table below, which provides bibliographic indicators for a collection of research articles. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| countries            |   global_citations |
|:---------------------|-------------------:|
| United Kingdom       |                199 |
| Australia            |                199 |
| Hong Kong            |                185 |
| United States        |                 59 |
| Ireland              |                 55 |
| Germany              |                 51 |
| Switzerland          |                 45 |
| Luxembourg           |                 34 |
| China                |                 27 |
| Greece               |                 21 |
| Bahrain              |                 19 |
| United Arab Emirates |                 13 |
| Japan                |                 13 |
| Jordan               |                 11 |
| South Africa         |                 11 |
| Italy                |                  5 |
| Spain                |                  4 |
| Ukraine              |                  4 |
| Malaysia             |                  3 |
| Palestine            |                  1 |
<BLANKLINE>
<BLANKLINE>

# pylint: disable=line-too-long
"""
from ...vantagepoint.analyze import list_view
from ..utils import bbx_generic_indicators_by_item


# pylint: disable=too-many-arguments
def most_global_cited_countries(
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
    """Most global cited countries.

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
        title = "Most Global Cited Countries"

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

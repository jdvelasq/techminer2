# flake8: noqa
"""
Most Local Cited Countries 
===============================================================================


Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_local_cited_countries.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.countries.most_local_cited_countries(
...     top_n=20,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_local_cited_countries.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
countries
United Kingdom    34
Ireland           22
Germany           17
Australia         15
Switzerland       13
Name: local_citations, dtype: int64



>>> print(r.prompt_)
Analyze the table below, which provides bibliometric indicators for the field 'countries' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| countries            |   OCC |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |
|:---------------------|------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|
| United Kingdom       |     7 |                199 |                34 |                           28.43 |                           4.86 |
| Ireland              |     5 |                 55 |                22 |                           11    |                           4.4  |
| Germany              |     4 |                 51 |                17 |                           12.75 |                           4.25 |
| Australia            |     7 |                199 |                15 |                           28.43 |                           2.14 |
| Switzerland          |     4 |                 45 |                13 |                           11.25 |                           3.25 |
| United States        |     6 |                 59 |                11 |                            9.83 |                           1.83 |
| Hong Kong            |     3 |                185 |                 8 |                           61.67 |                           2.67 |
| Luxembourg           |     2 |                 34 |                 8 |                           17    |                           4    |
| Greece               |     1 |                 21 |                 8 |                           21    |                           8    |
| United Arab Emirates |     2 |                 13 |                 7 |                            6.5  |                           3.5  |
| China                |     5 |                 27 |                 5 |                            5.4  |                           1    |
| Bahrain              |     4 |                 19 |                 5 |                            4.75 |                           1.25 |
| Jordan               |     1 |                 11 |                 4 |                           11    |                           4    |
| South Africa         |     1 |                 11 |                 4 |                           11    |                           4    |
| Italy                |     5 |                  5 |                 2 |                            1    |                           0.4  |
| Japan                |     1 |                 13 |                 1 |                           13    |                           1    |
| India                |     1 |                  1 |                 1 |                            1    |                           1    |
| Palestine            |     1 |                  1 |                 1 |                            1    |                           1    |
| Spain                |     2 |                  4 |                 0 |                            2    |                           0    |
| Ukraine              |     1 |                  4 |                 0 |                            4    |                           0    |
<BLANKLINE>
<BLANKLINE>



"""
from ..utils import bbx_indicators_by_item


# pylint: disable=too-many-arguments
def most_local_cited_countries(
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
    """Most local cited countries.

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
        title = "Most Local Cited Countries"

    return bbx_indicators_by_item(
        field="countries",
        root_dir=root_dir,
        database=database,
        metric="local_citations",
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

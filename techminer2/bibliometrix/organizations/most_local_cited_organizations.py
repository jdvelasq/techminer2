# flake8: noqa
"""
Most Local Cited Institutions
===============================================================================


Example


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_local_cited_organizations.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.organizations.most_local_cited_organizations(
...     top_n=20,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_local_cited_organizations.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
organizations
University College Cork        19
---Kingston Business School    17
University of Hong Kong         8
---KS Strategic                 8
---Panepistemio Aigaiou         8
Name: local_citations, dtype: int64

>>> print(r.prompt_)
Analyze the table below, which provides bibliometric indicators for the field 'organizations' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| organizations                                                   |   OCC |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |
|:----------------------------------------------------------------|------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|
| University College Cork                                         |     3 |                 41 |                19 |                           13.67 |                           6.33 |
| ---Kingston Business School                                     |     1 |                153 |                17 |                          153    |                          17    |
| University of Hong Kong                                         |     3 |                185 |                 8 |                           61.67 |                           2.67 |
| ---KS Strategic                                                 |     1 |                 21 |                 8 |                           21    |                           8    |
| ---Panepistemio Aigaiou                                         |     1 |                 21 |                 8 |                           21    |                           8    |
| ---School of Engineering                                        |     1 |                 21 |                 8 |                           21    |                           8    |
| European Central Bank                                           |     1 |                 21 |                 8 |                           21    |                           8    |
| Harvard University Weatherhead Center for International Affairs |     1 |                 21 |                 8 |                           21    |                           8    |
| ---UNSW Sydney                                                  |     1 |                 24 |                 5 |                           24    |                           5    |
| Heinrich Heine University                                       |     1 |                 24 |                 5 |                           24    |                           5    |
| University of Luxembourg                                        |     1 |                 24 |                 5 |                           24    |                           5    |
| University of Zurich                                            |     1 |                 24 |                 5 |                           24    |                           5    |
| Ahlia University                                                |     3 |                 19 |                 5 |                            6.33 |                           1.67 |
| ---Deloitte LLP                                                 |     1 |                  8 |                 5 |                            8    |                           5    |
| Coventry University                                             |     2 |                 17 |                 4 |                            8.5  |                           2    |
| University of Westminster                                       |     2 |                 17 |                 4 |                            8.5  |                           2    |
| Department of Finance and Banking                               |     1 |                 11 |                 4 |                           11    |                           4    |
| Finance and Banking                                             |     1 |                 11 |                 4 |                           11    |                           4    |
| University of Johannesburg                                      |     1 |                 11 |                 4 |                           11    |                           4    |
| Zayed University                                                |     1 |                 11 |                 4 |                           11    |                           4    |
<BLANKLINE>
<BLANKLINE>

# pylint: disable=line-too-long
"""
from ..utils import bbx_indicators_by_item


def most_local_cited_organizations(
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
    """Most local cited organizations.

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

    return bbx_indicators_by_item(
        field="organizations",
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

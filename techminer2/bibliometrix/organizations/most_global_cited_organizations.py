# flake8: noqa
"""
Most Global Cited Organizations
===============================================================================


Example
-------------------------------------------------------------------------------

>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_global_cited_organizations.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.organizations.most_global_cited_organizations(
...     directory=directory,
...     topics_length=20,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_global_cited_organizations.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> r.table_.head()
organizations
University of Hong Kong        185
---FinTech HK                  161
---Kingston Business School    153
---Centre for Law              150
University College Cork         41
Name: global_citations, dtype: int64

>>> print(r.prompt_)
Analyze the table below, which provides bibliographic indicators for a collection of research articles. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| organizations                                                   |   global_citations |
|:----------------------------------------------------------------|-------------------:|
| University of Hong Kong                                         |                185 |
| ---FinTech HK                                                   |                161 |
| ---Kingston Business School                                     |                153 |
| ---Centre for Law                                               |                150 |
| University College Cork                                         |                 41 |
| Duke University School of Law                                   |                 30 |
| Heinrich Heine University                                       |                 24 |
| University of Zurich                                            |                 24 |
| University of Luxembourg                                        |                 24 |
| ---UNSW Sydney                                                  |                 24 |
| Harvard University Weatherhead Center for International Affairs |                 21 |
| ---School of Engineering                                        |                 21 |
| ---Panepistemio Aigaiou                                         |                 21 |
| ---KS Strategic                                                 |                 21 |
| European Central Bank                                           |                 21 |
| Ahlia University                                                |                 19 |
| University of Westminster                                       |                 17 |
| Coventry University                                             |                 17 |
| Dublin City University                                          |                 14 |
| Shanghai University                                             |                 13 |
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

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
organizations
Univ of Hong Kong (HKG)                                               185
Kingston Bus Sch (GBR)                                                153
FinTech HK, Hong Kong (HKG)                                           150
ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS)    150
Univ Coll Cork (IRL)                                                   41
Name: global_citations, dtype: int64


>>> print(r.prompt_)
Analyze the table below, which provides bibliometric indicators for the field 'organizations' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| organizations                                                      |   OCC |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |
|:-------------------------------------------------------------------|------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|
| Univ of Hong Kong (HKG)                                            |     3 |                185 |                 8 |                           61.67 |                           2.67 |
| Kingston Bus Sch (GBR)                                             |     1 |                153 |                17 |                          153    |                          17    |
| FinTech HK, Hong Kong (HKG)                                        |     1 |                150 |                 0 |                          150    |                           0    |
| ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) |     1 |                150 |                 0 |                          150    |                           0    |
| Univ Coll Cork (IRL)                                               |     3 |                 41 |                19 |                           13.67 |                           6.33 |
| Duke Univ Sch of Law (USA)                                         |     1 |                 30 |                 0 |                           30    |                           0    |
| Heinrich-Heine-Univ (DEU)                                          |     1 |                 24 |                 5 |                           24    |                           5    |
| UNSW Sydney, Kensington, Australia (AUS)                           |     1 |                 24 |                 5 |                           24    |                           5    |
| Univ of Luxembourg (LUX)                                           |     1 |                 24 |                 5 |                           24    |                           5    |
| Univ of Zurich (CHE)                                               |     1 |                 24 |                 5 |                           24    |                           5    |
| European Central B (DEU)                                           |     1 |                 21 |                 8 |                           21    |                           8    |
| Harvard Univ Weatherhead ctr for International Affairs (USA)       |     1 |                 21 |                 8 |                           21    |                           8    |
| KS Strategic, London, United Kingdom (GBR)                         |     1 |                 21 |                 8 |                           21    |                           8    |
| Panepistemio Aigaiou, Chios, Greece (GRC)                          |     1 |                 21 |                 8 |                           21    |                           8    |
| Sch of Eng (CHE)                                                   |     1 |                 21 |                 8 |                           21    |                           8    |
| Ahlia Univ (BHR)                                                   |     3 |                 19 |                 5 |                            6.33 |                           1.67 |
| Coventry Univ (GBR)                                                |     2 |                 17 |                 4 |                            8.5  |                           2    |
| Univ of Westminster (GBR)                                          |     2 |                 17 |                 4 |                            8.5  |                           2    |
| Dublin City Univ (IRL)                                             |     2 |                 14 |                 3 |                            7    |                           1.5  |
| Hebei Univ of Technol (CHN)                                        |     1 |                 13 |                 1 |                           13    |                           1    |
<BLANKLINE>
<BLANKLINE>


# pylint: disable=line-too-long
"""
from ...vantagepoint.analyze import list_view
from ..utils import bbx_generic_indicators_by_item


# pylint: disable=too-many-arguments
def most_global_cited_organizations(
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
    """Most global cited organizations.

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
        title = "Most Global Cited Organizations"

    return bbx_generic_indicators_by_item(
        fnc_view=list_view,
        field="organizations",
        root_dir=root_dir,
        database=database,
        metric="global_citations",
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

# flake8: noqa
"""
Most Frequent Words
===============================================================================


Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_frequent_words.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.words.most_frequent_words(
...     field="author_keywords",
...     root_dir=root_dir,
...     top_n=20,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_frequent_words.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()
author_keywords
REGTECH               28
FINTECH               12
COMPLIANCE             7
REGULATION             5
FINANCIAL_SERVICES     4
Name: OCC, dtype: int64


>>> print(r.prompt_)
Analyze the table below, which provides bibliometric indicators for the field 'author_keywords' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| author_keywords                 |   OCC |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |
|:--------------------------------|------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|
| REGTECH                         |    28 |                329 |                74 |                           11.75 |                           2.64 |
| FINTECH                         |    12 |                249 |                49 |                           20.75 |                           4.08 |
| COMPLIANCE                      |     7 |                 30 |                 9 |                            4.29 |                           1.29 |
| REGULATION                      |     5 |                164 |                22 |                           32.8  |                           4.4  |
| FINANCIAL_SERVICES              |     4 |                168 |                20 |                           42    |                           5    |
| FINANCIAL_REGULATION            |     4 |                 35 |                 8 |                            8.75 |                           2    |
| REGULATORY_TECHNOLOGY (REGTECH) |     4 |                 30 |                10 |                            7.5  |                           2.5  |
| ARTIFICIAL_INTELLIGENCE         |     4 |                 23 |                 6 |                            5.75 |                           1.5  |
| ANTI_MONEY_LAUNDERING           |     4 |                 23 |                 4 |                            5.75 |                           1    |
| RISK_MANAGEMENT                 |     3 |                 14 |                 8 |                            4.67 |                           2.67 |
| INNOVATION                      |     3 |                 12 |                 4 |                            4    |                           1.33 |
| REGULATORY_TECHNOLOGY           |     3 |                  7 |                 4 |                            2.33 |                           1.33 |
| BLOCKCHAIN                      |     3 |                  5 |                 0 |                            1.67 |                           0    |
| SUPTECH                         |     3 |                  4 |                 2 |                            1.33 |                           0.67 |
| DATA_PROTECTION                 |     2 |                 27 |                 5 |                           13.5  |                           2.5  |
| SMART_CONTRACT                  |     2 |                 22 |                 8 |                           11    |                           4    |
| CHARITYTECH                     |     2 |                 17 |                 4 |                            8.5  |                           2    |
| ENGLISH_LAW                     |     2 |                 17 |                 4 |                            8.5  |                           2    |
| ACCOUNTABILITY                  |     2 |                 14 |                 3 |                            7    |                           1.5  |
| DATA_PROTECTION_OFFICER         |     2 |                 14 |                 3 |                            7    |                           1.5  |
<BLANKLINE>
<BLANKLINE>


# pylint: disable=line-too-long
"""
from ...vantagepoint.analyze import list_items
from ..utils import bbx_generic_indicators_by_item


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def most_frequent_words(
    field="author_keywords",
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
    top_n=20,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database filters:
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Plots the number of documents by country using the specified plot.

    Args:
        field (str): field name. Options {'author_keywords', 'index_keywords', 'abstract_words', 'title_words'}
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

    return bbx_generic_indicators_by_item(
        fnc_view=list_items,
        # Function options:
        field=field,
        root_dir=root_dir,
        database=database,
        metric="OCC",
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

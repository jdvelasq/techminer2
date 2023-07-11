# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _countries_metrics_table:

Countries Metrics Table
===============================================================================

>>> root_dir = "data/regtech/"
>>> import techminer2 as tm2
>>> tm2.countries_metrics_table(
...     root_dir=root_dir,
...     top_n=10,
... ).head()
                rank_occ  rank_gc  OCC  ...  h_index  g_index  m_index
countries                               ...                           
United Kingdom         1        1    7  ...      4.0      3.0     0.67
Australia              2        2    7  ...      4.0      3.0     0.57
United States          3        4    6  ...      3.0      2.0     0.38
Ireland                4        5    5  ...      3.0      2.0     0.50
China                  5        9    5  ...      3.0      2.0     0.43
<BLANKLINE>
[5 rows x 18 columns]

"""
from ....vantagepoint.discover.list_items_table import list_items_table

FIELD = "countries"


def countries_metrics_table(
    #
    # ITEM FILTERS:
    top_n=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Returns the most frequent sources."""

    return list_items_table(
        #
        # ITEMS PARAMS:
        field=FIELD,
        metric="OCC",
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=(None, None),
        gc_range=(None, None),
        custom_items=None,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

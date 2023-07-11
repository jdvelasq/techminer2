# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _organizations_metrics_table:

Organizations Metrics Table
===============================================================================

>>> root_dir = "data/regtech/"
>>> import techminer2 as tm2
>>> tm2.organizations_metrics_table(
...     root_dir=root_dir,
...     top_n=10,
... ).head()
                           rank_occ  rank_gc  OCC  ...  h_index  g_index  m_index
organizations                                      ...                           
Univ of Hong Kong (HKG)           1        1    3  ...      3.0      3.0     0.43
Univ Coll Cork (IRL)              2        5    3  ...      2.0      2.0     0.33
Ahlia Univ (BHR)                  3       16    3  ...      2.0      2.0     0.50
Coventry Univ (GBR)               4       17    2  ...      2.0      1.0     0.50
Univ of Westminster (GBR)         5       18    2  ...      2.0      1.0     0.50
<BLANKLINE>
[5 rows x 18 columns]

"""
from ....vantagepoint.analyze.discover.list_items_table import list_items_table

FIELD = "organizations"


def organizations_metrics_table(
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

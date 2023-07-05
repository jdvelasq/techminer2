# flake8: noqa
# pylint: disable=line-too-long
"""
.. _statistics:

Statistics
===============================================================================


* Preparation

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"


* Object oriented interface

>>> (
...     tm2p.records(root_dir=root_dir)
...     .statistics()
...     .head()
... )
                  count         mean         std  ...     50%     75%     max
year               52.0  2020.230769    1.675842  ...  2020.0  2022.0  2023.0
page_start         41.0   295.146341  255.835451  ...   300.0   431.0   912.0
page_end           41.0   318.365854  253.043352  ...   311.0   446.0   929.0
global_citations   52.0    10.826923   29.401028  ...     2.5     8.5   153.0
num_authors        52.0     2.288462    1.348006  ...     2.0     3.0     6.0
<BLANKLINE>
[5 rows x 8 columns]


* Functional interface

>>> tm2p.statistics(
...     root_dir=root_dir,
... ).head()
                  count         mean         std  ...     50%     75%     max
year               52.0  2020.230769    1.675842  ...  2020.0  2022.0  2023.0
page_start         41.0   295.146341  255.835451  ...   300.0   431.0   912.0
page_end           41.0   318.365854  253.043352  ...   311.0   446.0   929.0
global_citations   52.0    10.826923   29.401028  ...     2.5     8.5   153.0
num_authors        52.0     2.288462    1.348006  ...     2.0     3.0     6.0
<BLANKLINE>
[5 rows x 8 columns]


"""
from ._read_records import read_records


# =============================================================================
#
#
#  COMPUTATIONAL API:
#
#
# =============================================================================
def statistics(
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Returns the statistics of the records."""

    documents = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return documents.describe().T

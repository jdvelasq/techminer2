# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Production over Time
===============================================================================


>>> from techminer2 import bibliometrix
>>> root_dir = "data/regtech/"
>>> production_over_time = bibliometrix.authors.production_over_time(
...    top_n=10,
...    root_dir=root_dir,
... )
>>> production_over_time.fig_.write_html("sphinx/_static/authors_production_over_time.html")

.. raw:: html

    <iframe src="../../../../_static/authors_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> print(production_over_time.df_.to_markdown())



>>> print(production_over_time.prompt_)

>>> print(production_over_time.metrics_.head().to_markdown())


>>> print(production_over_time.documents_.head().to_markdown())




"""
from ...vantagepoint.discover import terms_by_year

FIELD = "authors"


def production_over_time(
    #
    # PARAMS:
    cumulative=False,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Sources production over time."""

    return terms_by_year(
        #
        # PARAMS:
        field=FIELD,
        cumulative=cumulative,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

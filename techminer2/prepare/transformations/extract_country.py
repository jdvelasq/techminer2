# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Extract Country
===============================================================================

>>> from techminer2.fields.further_processing import extract_country
>>> extract_country( # doctest: +SKIP 
...     source="affiliations",
...     dest="countries_from_affiliations",
...     root_dir="example/",
... )

>>> # TEST:  
>>> from techminer2.analyze.metrics import performance_metrics_frame
>>> performance_metrics( # doctest: +SKIP 
...     field='countries_from_affiliations',
...     metric='OCC',
...     top_n=10,
...     root_dir="example/", 
... )


>>> from techminer2.fields import delete_field
>>> delete_field( # doctest: +SKIP 
...     field="countries_from_affiliations",
...     root_dir="example",
... )


"""

from ..operations.protected_database_fields import PROTECTED_FIELDS


def extract_country(
    source,
    dest,
    root_dir,
):
    """:meta private:"""

    if dest in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dest}` is protected")

    transformations__extract_country(
        source=source,
        dest=dest,
        root_dir=root_dir,
    )

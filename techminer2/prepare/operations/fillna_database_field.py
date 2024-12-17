# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Fill NA
===============================================================================

>>> from techminer2.fields import fillna_field
>>> fillna_field(  # doctest: +SKIP 
...     fill_field="author_keywords",
...     with_field="index_keywords",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

"""
from ...internals.fields.fields__fillna import fields__fillna
from .protected_database_fields import PROTECTED_FIELDS


def fillna_database_field(
    fill_field,
    with_field,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """
    if fill_field in PROTECTED_FIELDS:
        raise ValueError(f"Field `{fill_field}` is protected")

    fields__fillna(
        fill_field=fill_field,
        with_field=with_field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )

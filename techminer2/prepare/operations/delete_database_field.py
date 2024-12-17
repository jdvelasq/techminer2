# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Delete a Field
===============================================================================

>>> from techminer2.fields import delete_field
>>> delete_field(  # doctest: +SKIP 
...     field="author_keywords_copy",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

"""

from ...internals.fields.fields__delete import fields__delete
from .protected_database_fields import PROTECTED_FIELDS


def delete_database_field(
    field,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    if field in PROTECTED_FIELDS:
        raise ValueError(f"Field `{field}` is protected")

    fields__delete(
        field=field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )

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

## >>> from techminer2.fields import delete_field
## >>> delete_field(  # doctest: +SKIP 
## ...     field="author_keywords_copy",
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example",
## ... )

"""

from ..internals.field_operations.internal__delete_field import internal__delete_field
from .operations__protected_fields import PROTECTED_FIELDS


def operations__delete_field(
    field,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    if field in PROTECTED_FIELDS:
        raise ValueError(f"Field `{field}` is protected")

    internal__delete_field(
        field=field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )

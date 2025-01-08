# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Copy a Field
===============================================================================

## >>> from techminer2.fields import copy_field
## >>> copy_field(  # doctest: +SKIP 
## ...     source="author_keywords",
## ...     dest="author_keywords_copy",
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example",
## ... )

"""
from ..internals.field_operations.internal__copy_field import internal__copy_field
from .operations__protected_fields import PROTECTED_FIELDS


def operations__copy_field(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    if dest in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dest}` is protected")

    internal__copy_field(
        source=source,
        dest=dest,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )

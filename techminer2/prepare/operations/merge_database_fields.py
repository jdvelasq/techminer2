# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Merge Fields
===============================================================================

## >>> from techminer2.fields import merge_fields
## >>> merge_fields(  # doctest: +SKIP
## ...     fields_to_merge=["author_keywords", "index_keywords"],
## ...     dest="merged_keywords",
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example",
## ... )

"""
from ...internals.fields.fields__merge import fields__merge
from .protected_database_fields import PROTECTED_FIELDS


def merge_database_fields(
    sources,
    dest,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    if dest in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dest}` is protected")

    fields__merge(
        sources=sources,
        dest=dest,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )

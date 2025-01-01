# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Rename a Field
===============================================================================

## >>> from techminer2.fields import rename_field
## >>> rename_field(  # doctest: +SKIP
## ...     source="author_keywords",
## ...     dest="author_keywords_new",
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example",
## ... )

"""
from ...internals.fields.fields__rename import fields__rename
from .protected_database_fields import PROTECTED_FIELDS


def rename_database_field(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """
    if dest in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dest}` is protected")

    fields__rename(
        source=source,
        dest=dest,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )

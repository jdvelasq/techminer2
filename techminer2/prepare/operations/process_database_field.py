# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Process a Field
===============================================================================

>>> from techminer2.fields import process_field
>>> process_field(  # doctest: +SKIP
...     source="author_keywords",
...     dest="author_keywords_copy",
...     func=lambda x: x.str.lower(),
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

"""
from ...internals.fields.fields__process import fields__process
from .protected_database_fields import PROTECTED_FIELDS


def process_database_field(
    source,
    dest,
    func,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    if dest in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dest}` is protected")

    fields__process(
        source=source,
        dest=dest,
        func=func,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Stemming Field with AND
===============================================================================

## >>> from techminer2.fields.further_processing import stemming_field_with_and
## >>> stemming_field_with_and(  # doctest: +SKIP
## ...     items="ARTIFICIAL_INTELLIGENCE",
## ...     source="author_keywords",
## ...     dest="stemming",
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example",
## ... )

"""

import pandas as pd  # type: ignore
from textblob import TextBlob  # type: ignore

from ..._dtypes import DTYPES
from ..operations.protected_database_fields import PROTECTED_FIELDS


def stemming_field_with_and(
    items,
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    if dest in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dest}` is protected")

    transformations__stemming_with_and(
        items=items,
        source=source,
        dest=dest,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )

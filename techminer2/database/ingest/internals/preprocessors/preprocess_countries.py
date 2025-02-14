# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Create countries thesaurus from affiliations.

# >>> from techminer2.ingest._list_cleanup_countries import list_cleanup_countries
# >>> list_cleanup_countries(  # doctest: +SKIP
# ...     #
# ...     # DATABASE PARAMS:
# ...     root_dir="example/",
# ... )
# --INFO-- The example/thesauri/countries.the.txt thesaurus file was created

"""
import pathlib
import sys

from .....thesaurus.countries import ApplyThesaurus, ResetThesaurusToInitial


# -------------------------------------------------------------------------
def internal__preprocess_countries(params):
    """:meta private:"""

    ResetThesaurusToInitial().update(**params).build()
    ApplyThesaurus().update(**params).build()


# =============================================================================

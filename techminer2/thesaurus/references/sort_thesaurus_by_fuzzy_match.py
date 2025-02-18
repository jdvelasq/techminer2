# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Thesaurus by Fuzzy Match
===============================================================================

## >>> from techminer2.thesaurus.references import SortThesaurusByFuzzyMatch
## >>> (
## ...     SortThesaurusByFuzzyMatch()
## ...     # 
## ...     # THESAURUS:
## ...     .having_keys_like("alphabetical")
## ...     .having_match_threshold(70)
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     #
## ...     .build()
## ... ) 
--INFO-- The thesaurus file 'example/thesaurus/references.the.txt' has been rerodered.

"""
from ...internals.mixins import ParamsMixin
from ..user.sort_thesaurus_by_fuzzy_match import (
    SortThesaurusByFuzzyMatch as SortUserThesaurusByFuzzyMatch,
)


class SortThesaurusByFuzzyMatch(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            SortUserThesaurusByFuzzyMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("references.the.txt")
            .build()
        )

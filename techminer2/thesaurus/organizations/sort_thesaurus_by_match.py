# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Thesaurus by Match
===============================================================================

Finds a string in the terms of a thesaurus.


## >>> from techminer2.thesaurus.organizations import SortThesaurusByMatch
## >>> (
## ...     SortThesaurusByMatch()
## ...     # 
## ...     # THESAURUS:
## ...     .having_keys_like("univ")
## ...     .having_keys_starting_with(None)
## ...     .having_keys_ending_with(None)
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     #
## ...     .build()
## ... ) 
--INFO-- The thesaurus file 'example/thesaurus/organizations.the.txt' has been rerodered.



"""
from ...internals.mixins import ParamsMixin
from ..user.sort_thesaurus_by_match import (
    SortThesaurusByMatch as SortUserThesaurusByMatch,
)


class SortThesaurusByMatch(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            SortUserThesaurusByMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("organizations.the.txt")
            .build()
        )

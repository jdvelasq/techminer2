# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Thesaurus by Key Match
===============================================================================

Finds a string in the terms of a thesaurus.


>>> from techminer2.thesaurus.descriptors import SortThesaurusByKeyMatch
>>> (
...     SortThesaurusByKeyMatch()
...     # 
...     # THESAURUS:
...     .having_keys_like("ARTIFICIAL_INTELLIGENCE")
...     .having_keys_starting_with(None)
...     .having_keys_ending_with(None)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... ) 
<BLANKLINE>
Thesaurus sorting by key match completed successfully: ...s/descriptors.the.txt


>>> (
...     SortThesaurusByKeyMatch()
...     # 
...     # THESAURUS:
...     .having_keys_like(None)
...     .having_keys_starting_with("ARTIFICIAL_INTELLIGENCE")
...     .having_keys_ending_with(None)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... ) 
<BLANKLINE>
Thesaurus sorting by key match completed successfully: ...s/descriptors.the.txt


>>> (
...     SortThesaurusByKeyMatch()
...     # 
...     # THESAURUS:
...     .having_keys_like(None)
...     .having_keys_starting_with(None)
...     .having_keys_ending_with("ARTIFICIAL_INTELLIGENCE")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... ) 
<BLANKLINE>
Thesaurus sorting by key match completed successfully: ...s/descriptors.the.txt

"""
from ..._internals.mixins import ParamsMixin
from ..user.sort_thesaurus_by_key_match import (
    SortThesaurusByKeyMatch as SortUserThesaurusByKeyMatch,
)


class SortThesaurusByKeyMatch(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            SortUserThesaurusByKeyMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .build()
        )

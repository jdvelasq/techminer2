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

>>> from techminer2.thesaurus.references import SortThesaurusByFuzzyKeyMatch
>>> (
...     SortThesaurusByFuzzyKeyMatch()
...     # 
...     # THESAURUS:
...     .having_keys_like("FUTURO")
...     .having_match_threshold(70)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .build()
... ) 
<BLANKLINE>
Thesaurus sorting by fuzzy key match completed successfully: ...erences.the.txt


"""
from ..._internals.mixins import ParamsMixin
from ..user import SortByFuzzyKeyMatch as UserSortByFuzzyKeyMatch


class SortThesaurusByFuzzyKeyMatch(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            UserSortByFuzzyKeyMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("global_references.the.txt")
            .build()
        )

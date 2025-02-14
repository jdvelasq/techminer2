# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Thesaurus by Key
===============================================================================


>>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
>>> from techminer2.thesaurus.references import SortThesaurusByKey
>>> (
...     SortThesaurusByKey()
...     # 
...     # THESAURUS:
...     .having_keys_ordered_by("alphabetical")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )
--INFO-- The thesaurus file 'examples/thesaurus/references.the.txt' has been ordered alphabetically.

"""
from ...internals.mixins import ParamsMixin
from ..user.sort_thesaurus_by_key import SortThesaurusByKey as SortUserThesaurusByKey


class SortThesaurusByKey(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            SortUserThesaurusByKey()
            .update(**self.params.__dict__)
            .with_thesaurus_file("references.the.txt")
            .build()
        )

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Thesaurus by Key Order
===============================================================================


>>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
>>> from techminer2.thesaurus.organizations import SortThesaurusByKeyOrder
>>> (
...     SortThesaurusByKeyOrder()
...     # 
...     # THESAURUS:
...     .having_keys_ordered_by("alphabetical")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .build()
... )
<BLANKLINE>
Thesaurus sorting completed successfully for file: ...rus/organizations.the.txt


"""
from ..._internals.mixins import ParamsMixin
from ..user import SortByKeyOrder as UserSortByKeyOrder


class SortThesaurusByKeyOrder(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            UserSortByKeyOrder()
            .update(**self.params.__dict__)
            .with_thesaurus_file("organizations.the.txt")
            .build()
        )

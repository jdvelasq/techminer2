# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Check Thesaurus Integrity
===============================================================================

>>> from techminer2.thesaurus.countries import CheckThesaurusIntegrity
>>> (
...     CheckThesaurusIntegrity()
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .build()
... )
<BLANKLINE>
Thesaurus integrity check completed successfully for file: ...countries.the.txt


"""

from ..._internals.mixins import ParamsMixin
from ..user import IntegrityCheck as CheckUserThesaurusIntegrity


#
#
class CheckThesaurusIntegrity(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        (
            CheckUserThesaurusIntegrity()
            .with_thesaurus_file("countries.the.txt")
            .with_field("affiliations")
            .where_root_directory_is(self.params.root_directory)
            .build()
        )

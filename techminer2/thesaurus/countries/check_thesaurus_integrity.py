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

## >>> from techminer2.thesaurus.countries import CheckThesaurusIntegrity
## >>> (
## ...     CheckThesaurusIntegrity()
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     #
## ...     .build()
## ... )



"""

from ..._internals.mixins import ParamsMixin
from ..user.check_thesaurus_integrity import (
    CheckThesaurusIntegrity as CheckUserThesaurusIntegrity,
)


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
            .where_directory_is(self.params.root_dir)
            .with_prompt_flag(self.params.prompt_flag)
            .build()
        )

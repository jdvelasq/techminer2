# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Cleanup Thesaurus
===============================================================================


## >>> from techminer2.thesaurus.countries import CleanupThesaurus
## >>> (
## ...     CleanupThesaurus()
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     #
## ...     .build()
## ... )


"""
from ..._internals.log_message import internal__log_message
from ..._internals.mixins import ParamsMixin
from ..user.cleanup_thesaurus import CleanupThesaurus as CleanupUserThesaurus
from .apply_thesaurus import ApplyThesaurus


class CleanupThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        (
            CleanupUserThesaurus()
            .update(**self.params.__dict__)
            .with_thesaurus_file("countries.the.txt")
            .with_prompt_flag(self.params.prompt_flag)
            .build()
        )

        ApplyThesaurus().update(**self.params.__dict__).with_prompt_flag(-1).build()

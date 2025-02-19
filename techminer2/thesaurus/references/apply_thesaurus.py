# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Apply Thesaurus 
===============================================================================

## >>> from techminer2.thesaurus.references import ApplyThesaurus
## >>> (
## ...     ApplyThesaurus()
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     #
## ...     .build()
## ... )
--INFO-- The example/global_references.txt thesaurus file was applied to global_references in 'main' database

"""

from ..._internals.mixins import ParamsMixin
from ..user.apply_thesaurus import ApplyThesaurus as ApplyUserThesaurus


#
#
class ApplyThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        # Affiliations to countries mmapping
        (
            ApplyUserThesaurus()
            .with_thesaurus_file("references.the.txt")
            .with_field("raw_global_references")
            .with_other_field("global_references")
            .where_directory_is(self.params.root_dir)
            .build()
        )

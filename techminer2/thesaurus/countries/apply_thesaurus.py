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


## >>> from techminer2.thesaurus.coutries import ApplyThesaurus
## >>> (
## ...     ApplyThesaurus()
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     #
## ...     .build()
## ... )


"""
import sys

from ..._internals.mixins import ParamsMixin
from ...database.ingest._internals.operators.transform_field import (
    internal__transform_field,
)
from ..system import ApplyThesaurus as ApplySystemThesaurus
from ..user.apply_thesaurus import ApplyThesaurus as ApplyUserThesaurus


class ApplyThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        # Affiliations to countries mmapping
        (
            ApplyUserThesaurus()
            .with_thesaurus_file("countries.the.txt")
            .with_field("affiliations")
            .with_other_field("countries")
            .where_directory_is(self.params.root_dir)
            .with_prompt_flag(self.params.prompt_flag)
            .build()
        )

        # Country of first author
        internal__transform_field(
            #
            # FIELD:
            field="countries",
            other_field="country_1st_author",
            function=lambda x: x.str.split("; ").str[0],
            root_dir=self.params.root_dir,
        )

        # Country to region mapping
        (
            ApplySystemThesaurus()
            .with_thesaurus_file("geography/country_to_region.the.txt")
            .with_field("countries")
            .with_other_field("regions")
            .where_directory_is(self.params.root_dir)
            .with_prompt_flag(-1)
            .build()
        )

        # Country to subregion mapping
        (
            ApplySystemThesaurus()
            .with_thesaurus_file("geography/country_to_subregion.the.txt")
            .with_field("countries")
            .with_other_field("subregions")
            .where_directory_is(self.params.root_dir)
            .with_prompt_flag(-1)
            .build()
        )

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

>>> from techminer2.thesaurus.organizations import ApplyThesaurus
>>> (
...     ApplyThesaurus()
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )
--INFO-- The example/thesauri/organizations.the.txt thesaurus file was applied to affiliations in all databases

"""
import sys

from ...database.ingest.internals.operators.transform_field import (
    internal__transform_field,
)
from ...internals.mixins import ParamsMixin
from ..system import ApplyThesaurus as ApplySystemThesaurus
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
            .with_thesaurus_file("organizations.the.txt")
            .with_field("affiliations")
            .with_other_field("organizations")
            .where_directory_is(self.params.root_dir)
            .build()
        )

        # Country of first author
        internal__transform_field(
            #
            # FIELD:
            field="organizations",
            other_field="organization_1st_author",
            function=lambda x: x.str.split("; ").str[0],
            root_dir=self.params.root_dir,
        )

        print(f"--INFO-- The thesaurus file 'organizations.the.txt' was applied.")

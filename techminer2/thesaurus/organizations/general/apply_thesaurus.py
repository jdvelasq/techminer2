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

Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.organizations import ApplyThesaurus, CreateThesaurus

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()


    >>> (
    ...     ApplyThesaurus()
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ...     #
    ...     .run()
    ... )


    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Applying user thesaurus to database
              File : example/data/thesaurus/organizations.the.txt
      Source field : affiliations
      Target field : organizations
      Application process completed successfully
    <BLANKLINE>
    <BLANKLINE>


"""
from ...._internals.mixins import ParamsMixin
from ....database.ingest._internals.operators.transform_field import (
    internal__transform_field,
)
from ...user import ApplyThesaurus as ApplyUserThesaurus


#
#
class ApplyThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        # Affiliations to countries mmapping
        (
            ApplyUserThesaurus(quiet=self.params.quiet)
            .with_thesaurus_file("organizations.the.txt")
            .with_field("affiliations")
            .with_other_field("organizations")
            .where_root_directory_is(self.params.root_directory)
            .run()
        )

        # Country of first author
        internal__transform_field(
            #
            # FIELD:
            field="organizations",
            other_field="organization_1st_author",
            function=lambda x: x.str.split("; ").str[0],
            root_dir=self.params.root_directory,
        )

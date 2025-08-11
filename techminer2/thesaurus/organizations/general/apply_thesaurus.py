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
    >>> from techminer2.thesaurus.organizations import ApplyThesaurus, InitializeThesaurus

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()


    >>> (
    ...     ApplyThesaurus(use_colorama=False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     #
    ...     .run()
    ... )


    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Applying user thesaurus to database...
              File : examples/fintech/data/thesaurus/organizations.the.txt
      Source field : affiliations
      Target field : organizations
      Application process completed successfully
    <BLANKLINE>
    <BLANKLINE>


"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.database._internals.operators.transform import internal__transform
from techminer2.thesaurus.user import ApplyThesaurus as ApplyUserThesaurus


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
            .update(**self.params.__dict__)
            .with_thesaurus_file("organizations.the.txt")
            .with_field("affiliations")
            .with_other_field("organizations")
            .where_root_directory_is(self.params.root_directory)
            .run()
        )

        # Country of first author
        internal__transform(
            #
            # FIELD:
            field="organizations",
            other_field="organization_1st_author",
            function=lambda x: x.str.split("; ").str[0],
            root_dir=self.params.root_directory,
        )

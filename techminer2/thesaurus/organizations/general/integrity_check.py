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

Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.organizations import CreateThesaurus, IntegrityCheck

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> checker = (
    ...     IntegrityCheck()
    ...     .where_root_directory_is("example/")
    ... )
    >>> checker.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Checking thesaurus integrity
      File : example/data/thesaurus/organizations.the.txt
      106 terms checked
      Integrity check completed successfully
    <BLANKLINE>
    <BLANKLINE>


"""

from ...._internals.mixins import ParamsMixin
from ...user import IntegrityCheck as UserIntegrityCheck


#
#
class IntegrityCheck(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        (
            UserIntegrityCheck()
            .with_thesaurus_file("organizations.the.txt")
            .with_field("affiliations")
            .where_root_directory_is(self.params.root_directory)
            .run()
        )

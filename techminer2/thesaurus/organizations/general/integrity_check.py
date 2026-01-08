# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Integrity Check
===============================================================================

Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.organizations import InitializeThesaurus, IntegrityCheck

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> checker = (
    ...     IntegrityCheck()
    ...     .where_root_directory("examples/fintech/")
    ... )
    >>> checker.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Checking thesaurus integrity...
      File : examples/fintech/data/thesaurus/organizations.the.txt
      106 terms checked
      Integrity check completed successfully
    <BLANKLINE>
    <BLANKLINE>


"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.thesaurus.user import IntegrityCheck as UserIntegrityCheck


#
#
class IntegrityCheck(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        (
            UserIntegrityCheck()
            .update(**self.params.__dict__)
            .with_thesaurus_file("organizations.the.txt")
            .with_field("affiliations")
            .where_root_directory(self.params.root_directory)
            .run()
        )

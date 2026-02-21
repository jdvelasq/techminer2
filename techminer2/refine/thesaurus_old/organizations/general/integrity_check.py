"""
Integrity Check
===============================================================================

Smoke tests:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.refine.thesaurus_old.organizations import InitializeThesaurus, IntegrityCheck

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> checker = (
    ...     IntegrityCheck()
    ...     .where_root_directory("examples/tests/")
    ... )
    >>> checker.run()




"""

from techminer2._internals import ParamsMixin
from techminer2.refine.thesaurus_old.user import IntegrityCheck as UserIntegrityCheck


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

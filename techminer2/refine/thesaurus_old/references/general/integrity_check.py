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

Smoke tests:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.refine.thesaurus_old.references import IntegrityCheck

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Configure and run the integrity check
    >>> checker = (
    ...     IntegrityCheck()
    ...     .where_root_directory("examples/tests/")
    ... )
    >>> checker.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output) # doctest: +SKIP


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
            .with_thesaurus_file("references.the.txt")
            .with_field("global_references")
            .where_root_directory(self.params.root_directory)
            .run()
        )

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
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.refine.thesaurus_old.descriptors import InitializeThesaurus, IntegrityCheck

    >>> # Redirect stderr to capture output
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True, ).run()

    >>> # Run the integrity check
    >>> checker = (
    ...     IntegrityCheck()
    ...     .where_root_directory("examples/small/")
    ... )
    >>> checker.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Checking thesaurus integrity...
      File : examples/fintech/data/thesaurus/descriptors.the.txt
      1788 terms checked
      Integrity check completed successfully
    <BLANKLINE>
    <BLANKLINE>


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
            .with_thesaurus_file("descriptors.the.txt")
            .with_field("raw_descriptors")
            .where_root_directory(self.params.root_directory)
            .run()
        )

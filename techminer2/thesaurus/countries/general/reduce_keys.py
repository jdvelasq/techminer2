# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Reduce Keys
===============================================================================

Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.countries import CreateThesaurus, ReduceKeys

    >>> # Redirect stderr to capture output
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> # Reduce thesaurus keys
    >>> ReduceKeys().where_root_directory_is("example/").run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Reducing thesaurus keys
      File : example/thesaurus/countries.the.txt
      Keys reduced from 24 to 24
      Keys reduction completed successfully
    <BLANKLINE>
    <BLANKLINE>

"""
from ...._internals.mixins import ParamsMixin
from ...user import ReduceKeys as UserReduceKeys


class ReduceKeys(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        (
            UserReduceKeys(
                thesaurus_file="countries.the.txt",
                root_directory=self.params.root_directory,
            ).run()
        )


# =============================================================================

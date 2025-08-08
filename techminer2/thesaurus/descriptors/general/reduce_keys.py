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
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus, ReduceKeys

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Reduce thesaurus keys
    >>> reducer = (
    ...     ReduceKeys(use_colorama=False)
    ...     .where_root_directory_is("examples/fintech/")
    ... )
    >>> reducer.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Reducing thesaurus keys...
      File : examples/fintech/data/thesaurus/descriptors.the.txt
      Keys reduced from 1724 to 1724
      Reduction process completed successfully
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
            UserReduceKeys()
            .update(**self.params.__dict__)
            .update(
                thesaurus_file="descriptors.the.txt",
                root_directory=self.params.root_directory,
            )
            .run()
        )


# =============================================================================

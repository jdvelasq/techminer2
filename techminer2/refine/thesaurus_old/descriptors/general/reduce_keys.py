"""
Reduce Keys
===============================================================================


Smoke tests:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.refine.thesaurus_old.descriptors import InitializeThesaurus, ReduceKeys

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Reduce thesaurus keys
    >>> reducer = (
    ...     ReduceKeys()
    ...     .where_root_directory("examples/tests/")
    ... )
    >>> reducer.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)  # doctest: +SKIP
    Reducing thesaurus keys...
      File : examples/fintech/data/thesaurus/descriptors.the.txt
      Keys reduced from 1724 to 1724
      Reduction process completed successfully
    <BLANKLINE>
    <BLANKLINE>


"""

from techminer2._internals import ParamsMixin
from techminer2.refine.thesaurus_old.user import ReduceKeys as UserReduceKeys


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

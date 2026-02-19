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


Smoke tests:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.refine.thesaurus_old.organizations import InitializeThesaurus, ReduceKeys

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Creates and run the reducer
    >>> reducer = (
    ...     ReduceKeys()
    ...     .where_root_directory("examples/tests/")
    ... )
    >>> reducer.run()

>>> from techminer2.refine.thesaurus_old.organizations import PrintHeader
    >>> (
    ...     PrintHeader()
    ...     .using_colored_output(False)
    ...     .where_root_directory("examples/tests/")
    ... ).run()

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
                thesaurus_file="organizations.the.txt",
                root_directory=self.params.root_directory,
            )
            .run()
        )


# =============================================================================

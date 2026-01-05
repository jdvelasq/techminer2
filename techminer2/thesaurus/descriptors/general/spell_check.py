# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Spell Check
===============================================================================


Example:
    >>> # Redirecting stderr to avoid messages
    >>> import sys
    >>> from io import StringIO
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Reduce thesaurus keys
    >>> from techminer2.thesaurus.descriptors import SpellCheck
    >>> (
    ...     SpellCheck(use_colorama=False)
    ...     .where_root_directory("examples/fintech/")
    ...     .run()
    ... )


    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)


"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.thesaurus.user import SpellCheck as UserSpellCheck


class SpellCheck(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        (
            UserSpellCheck()
            .update(**self.params.__dict__)
            .update(thesaurus_file="descriptors.the.txt")
            .run()
        )


# =============================================================================

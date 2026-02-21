"""
Spell Check
===============================================================================


Smoke tests:
    >>> # Redirecting stderr to avoid messages
    >>> import sys
    >>> from io import StringIO
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> from techminer2.refine.thesaurus_old.descriptors import InitializeThesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Reduce thesaurus keys
    >>> from techminer2.refine.thesaurus_old.descriptors import SpellCheck
    >>> (
    ...     SpellCheck()
    ...     .where_root_directory("examples/tests/")
    ...     .run()
    ... )


    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)


"""

from techminer2._internals import ParamsMixin
from techminer2.refine.thesaurus_old.user import SpellCheck as UserSpellCheck


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

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Replace Last Word
===============================================================================

Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus, ReplaceLastWord

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Configure and run the replacer
    >>> replacer = (
    ...     ReplaceLastWord()
    ...     .having_word("FINTECH")
    ...     .having_replacement("fintech")
    ...     .where_root_directory("examples/fintech/")
    ... )
    >>> replacer.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)  # doctest: +SKIP
    Replacing last word in keys...
             File : ...h/data/thesaurus/descriptors.the.txt
             Word : FINTECH
      Replacement : fintech
      9 replacements made successfully
      Replacement process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        ADOPTION_OF_fintech
          ADOPTION_OF_FINTECH
        AI_IN_fintech
          AI_IN_FINTECH
        CHARACTERIZE_fintech
          CHARACTERIZE_FINTECH
        EXPLORE_fintech
          EXPLORE_FINTECH
        fintech
          FINTECH; FINTECHS
        FRAME_fintech
          FRAME_FINTECH
        INTENTION_TO_ADOPT_fintech
          INTENTION_TO_ADOPT_FINTECH
        PROMPTPAY_fintech
          PROMPTPAY_FINTECH
    <BLANKLINE>
    <BLANKLINE>



"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.thesaurus.user import ReplaceLastWord as UserReplaceEndsWithWord


class ReplaceLastWord(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserReplaceEndsWithWord()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )


# ===============================================================================

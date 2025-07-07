# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Replace Ends With Word
===============================================================================

Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import CreateThesaurus, ReplaceEndsWithWord

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> # Configure and run the replacer
    >>> replacer = (
    ...     ReplaceEndsWithWord()
    ...     .having_word("FINTECH")
    ...     .having_replacement("fintech")
    ...     .where_root_directory_is("example/")
    ... )
    >>> replacer.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Replacing ending word in keys
             File : ...e/data/thesaurus/descriptors.the.txt
             Word : FINTECH
      Replacement : fintech
      12 replacements made successfully
      Word replacing completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/descriptors.the.txt
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
        REGULATING_fintech
          REGULATING_FINTECH
    <BLANKLINE>
    <BLANKLINE>



"""
from ...._internals.mixins import ParamsMixin
from ...user import ReplaceEndsWithWord as UserReplaceEndsWithWord


class ReplaceEndsWithWord(
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

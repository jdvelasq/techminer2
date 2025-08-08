# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Replace Initial Word
===============================================================================

Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus, ReplaceInitialWord

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Configure and run the replacer
    >>> replacer = (
    ...     ReplaceInitialWord(use_colorama=False)
    ...     .having_word("FINTECH")
    ...     .having_replacement("fintech")
    ...     .where_root_directory_is("examples/fintech/")
    ... )
    >>> replacer.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Replacing initial word in keys...
             File : ...e/data/thesaurus/descriptors.the.txt
             Word : FINTECH
      Replacement : fintech
      39 replacements made successfully
      Replacement process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        fintech
          FINTECH; FINTECHS
        fintech_AND_FINANCIAL_INNOVATIONS_THE_BANKS
          FINTECH_AND_FINANCIAL_INNOVATIONS_THE_BANKS
        fintech_AND_REGTECH_:_IMPACT
          FINTECH_AND_REGTECH_:_IMPACT
        fintech_AND_SUSTAINABLE_DEVELOPMENT_:_EVIDENCE
          FINTECH_AND_SUSTAINABLE_DEVELOPMENT_:_EVIDENCE
        fintech_BANKING_INDUSTRY
          FINTECH_BANKING_INDUSTRY
        fintech_BASED_INNOVATION_DEVELOPMENT
          FINTECH_BASED_INNOVATION_DEVELOPMENT
        fintech_BASED_INNOVATIONS
          FINTECH_BASED_INNOVATIONS; FINTECH_INNOVATION
        fintech_CLUSTERS
          FINTECH_CLUSTERS
    <BLANKLINE>
    <BLANKLINE>



"""
from ...._internals.mixins import ParamsMixin
from ...user import ReplaceInitialWord as UserReplaceStartsWithWord


class ReplaceInitialWord(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserReplaceStartsWithWord()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )


# ===============================================================================

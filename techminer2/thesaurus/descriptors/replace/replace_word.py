# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Replace Word
===============================================================================

Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import CreateThesaurus, ReplaceWord

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> # Configure and run the replacer
    >>> replacer = (
    ...     ReplaceWord()
    ...     .having_word("FINTECH")
    ...     .having_replacement("fintech")
    ...     .where_root_directory_is("example/")
    ... )
    >>> replacer.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Replacing word in keys
             File : example/thesaurus/descriptors.the.txt
             Word : FINTECH
      Replacement : fintech
      96 replacements made successfully
      Word replacing completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/descriptors.the.txt
    <BLANKLINE>
        A_EUROPEAN_OR_NATIONAL_fintech_MARKET
          A_EUROPEAN_OR_NATIONAL_FINTECH_MARKET
        A_fintech_COMPANY
          A_FINTECH_COMPANY
        A_fintech_ECOSYSTEM
          A_FINTECH_ECOSYSTEM
        A_NEW_fintech_INNOVATION_MAPPING_APPROACH
          A_NEW_FINTECH_INNOVATION_MAPPING_APPROACH
        A_THEORETICAL_DATA_DRIVEN_fintech_FRAMEWORK
          A_THEORETICAL_DATA_DRIVEN_FINTECH_FRAMEWORK
        ACTIVE_fintech_SOLUTIONS
          ACTIVE_FINTECH_SOLUTIONS
        BANK_fintech_PARTNERSHIP
          BANK_FINTECH_PARTNERSHIP
        BANKS_OFFERING_fintech_SERVICES_NEED
          BANKS_OFFERING_FINTECH_SERVICES_NEED
    <BLANKLINE>
    <BLANKLINE>


"""
from ...._internals.mixins import ParamsMixin
from ...user import ReplaceWord as UserReplaceWord


class ReplaceWord(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserReplaceWord()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )


# -----------------------------------------------------------------------------
# SHORTCUTS
# -----------------------------------------------------------------------------
def replace(replace, by):

    from techminer2.thesaurus.descriptors import ReduceKeys  # type: ignore
    from techminer2.thesaurus.descriptors import ReplaceWord  # type: ignore

    (
        ReplaceWord()
        .having_word(replace)
        .having_replacement(by)
        .where_root_directory_is("../")
    ).run()

    ReduceKeys(root_directory="../").run()  #  type: ignore


# ===============================================================================

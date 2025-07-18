# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort By Match
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus, SortByMatch

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="example/", quiet=True).run()

    >>> # Configure and run the sorter
    >>> sorter = (
    ...     SortByMatch(use_colorama=False)
    ...     .having_pattern("BLOCK")
    ...     .having_case_sensitive(False)
    ...     .having_regex_flags(0)
    ...     .having_regex_search(False)
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Sorting thesaurus by match...
                File : example/data/thesaurus/descriptors.the.txt
             Pattern : BLOCK
      Case sensitive : False
         Regex Flags : 0
        Regex Search : False
      6 matching keys found
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        A_BLOCKCHAIN_IMPLEMENTATION_STUDY
          A_BLOCKCHAIN_IMPLEMENTATION_STUDY
        BLOCKCHAIN
          BLOCKCHAIN; BLOCKCHAINS
        BLOCKCHAIN_AND_FINTECH_INNOVATIONS
          BLOCKCHAIN_AND_FINTECH_INNOVATIONS
        BLOCKCHAIN_ENABLES_BLOCKCHAIN
          BLOCKCHAIN_ENABLES_BLOCKCHAIN
        BLOCKCHAIN_IMPLEMENTATION
          BLOCKCHAIN_IMPLEMENTATION
        BLOCKCHAIN_USE_CASES
          BLOCKCHAIN_USE_CASES
        A_A_THEORY
          A_A_THEORY
        A_BASIC_RANDOM_SAMPLING_STRATEGY
          A_BASIC_RANDOM_SAMPLING_STRATEGY
    <BLANKLINE>
    <BLANKLINE>


"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByMatch as UserSortByMatch


class SortByMatch(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserSortByMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )


# ===============================================================================

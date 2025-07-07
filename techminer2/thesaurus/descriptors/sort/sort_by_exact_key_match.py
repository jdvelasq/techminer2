# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort By Exact Key Match
===============================================================================


Example:
    >>> # Command line interface
    >>> # python3 -m techminer2.thesaurus.descriptors.sort.sort_by_exact_key_match BLOCKCHAIN BLOCK_CHAIN


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import CreateThesaurus, SortByExactKeyMatch

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> # Configure and run the sorter
    >>> sorter = (
    ...     SortByExactKeyMatch()
    ...     .having_pattern("BLOCKCHAIN")
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
    Reducing thesaurus keys
      File : example/data/thesaurus/descriptors.the.txt
      Keys reduced from 1729 to 1729
      Keys reduction completed successfully
    <BLANKLINE>
    Sorting thesaurus file by exact key match
         File : example/data/thesaurus/descriptors.the.txt
      Pattern : BLOCKCHAIN
      1 matching keys found
      Thesaurus sorting by exact key match completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        BLOCKCHAIN
          BLOCKCHAIN; BLOCKCHAINS
        A_A_THEORY
          A_A_THEORY
        A_BASIC_RANDOM_SAMPLING_STRATEGY
          A_BASIC_RANDOM_SAMPLING_STRATEGY
        A_BEHAVIOURAL_PERSPECTIVE
          A_BEHAVIOURAL_PERSPECTIVE
        A_BETTER_UNDERSTANDING
          A_BETTER_UNDERSTANDING
        A_BLOCKCHAIN_IMPLEMENTATION_STUDY
          A_BLOCKCHAIN_IMPLEMENTATION_STUDY
        A_CASE_STUDY
          A_CASE_STUDY
        A_CHALLENGE
          A_CHALLENGE
    <BLANKLINE>
    <BLANKLINE>



"""
import argparse

from ...._internals.mixins import ParamsMixin
from ...user import SortByExactKeyMatch as UserSortByExactKeyMatch


class SortByExactKeyMatch(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserSortByExactKeyMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )


# -----------------------------------------------------------------------------
# SHORTCUTS
# -----------------------------------------------------------------------------
def exactmatch(pattern):
    """:meta private:"""

    SortByExactKeyMatch(pattern=pattern, root_directory="../").run()


#
#
# COMMAND LINE INTERFACE:
#
#
def create_argparser():
    """:meta private:"""

    parser = argparse.ArgumentParser(
        description="Sort thesaurus file by exact key match."
    )
    parser.add_argument(
        "--root-directory",
        type=str,
        default=".",
        help="The root directory of the project.",
    )
    parser.add_argument(
        "pattern",
        type=str,
        help="The pattern to match exactly in the thesaurus keys.",
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":

    args = create_argparser()

    SortByExactKeyMatch(
        pattern=args.pattern.split(" "),
        root_directory=args.root_directory,
        quiet=False,
    ).run()


# ===============================================================================

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
    >>> from techminer2.thesaurus.system.descriptors import SortByMatch

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Configure and run the sorter
    >>> (
    ...     SortByMatch(use_colorama=False)
    ...     .having_pattern("BLOCK")
    ...     .having_case_sensitive(False)
    ...     .having_regex_flags(0)
    ...     .having_regex_search(False)
    ...     .run()
    ... )

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Sorting thesaurus by match...
                File : ...techminer2/package_data/thesaurus/system/descriptors.the.txt
             Pattern : BLOCK
      Case sensitive : False
         Regex Flags : 0
        Regex Search : False
      1 matching keys found
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : /Volumes/GitHub/techminer2/techminer2/package_data/thesaurus/system/descriptors.the.txt
    <BLANKLINE>
        BLOCK_CHAIN
          BLOCK_CHAINS; BLOCK_CHAIN_SYSTEM; BLOCK_CHAIN_SYSTEMS; BLOCK_CHAIN_TECHNO...
        *ARTICLE*
          ACADEMIC_ARTICLE; ACADEMIC_ARTICLES; ARTICLE; ARTICLES
        *AUTHOR*
          AUTHOR; AUTHORS
        *BIBLIOMETRICS*
          BIBLIOMETRIC; BIBLIOMETRICS
        *BOOK*
          BOOK; BOOKS
        *CHAPTER*
          CHAPTER; CHAPTERS
        *EDITORIAL*
          EDITORIAL
        *ERROR_METRICS*
          ABSOLUTE_AVERAGE_DEVIATION; ABSOLUTE_AVERAGE_DEVIATIONS; ABSOLUTE_ERROR; ...
    <BLANKLINE>
    <BLANKLINE>


"""
from techminer2.thesaurus.user import SortByMatch as UserSortByMatch


class SortByMatch(
    UserSortByMatch,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):

        self.with_thesaurus_file("system/descriptors.the.txt")
        self.internal__build_system_thesaurus_path()
        self.internal__run()


# ===============================================================================

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort By Exact Match
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.system.descriptors import SortByExactMatch

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Configure and run the sorter
    >>> (
    ...     SortByExactMatch(use_colorama=False)
    ...     .having_pattern("BLOCKCHAIN")
    ...     .run()
    ... )


    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Sorting thesaurus by exact match...
         File : ...techminer2/package_data/thesaurus/system/descriptors.the.txt
      Pattern : BLOCKCHAIN
      0 matching keys found
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : /Volumes/GitHub/techminer2/techminer2/package_data/thesaurus/system/descriptors.the.txt
    <BLANKLINE>
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
        *GEOGRAPHIC_REGIONS*
          AEGEAN_ISLANDS; AFGHANISTAN; AFRICA; ALBANIA; ALGERIA; AMERICAN_SAMOA; AM...
    <BLANKLINE>
    <BLANKLINE>



"""
from techminer2.thesaurus.user import SortByExactMatch as UserSortByExactMatch


class SortByExactMatch(
    UserSortByExactMatch,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.with_thesaurus_file("system/descriptors.the.txt")
        self.internal__build_system_thesaurus_path()
        self.internal__run()


# ===============================================================================

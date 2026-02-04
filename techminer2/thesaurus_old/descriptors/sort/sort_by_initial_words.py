# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Initial Words
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus_old.descriptors import InitializeThesaurus, SortByInitialWords

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Configure and run the sorter
    >>> sorter = (
    ...     SortByInitialWords()
    ...     .where_root_directory("examples/small/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)  # doctest: +SKIP
    Sorting thesaurus by common initial words...
      File : examples/fintech/data/thesaurus/descriptors.the.txt
      214 matching keys found
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        ACCELERATE_ACCESS
          ACCELERATE_ACCESS
        ACTIVE_CUSTOMERS
          ACTIVE_CUSTOMERS
        ACTIVE_FINTECH_SOLUTIONS
          ACTIVE_FINTECH_SOLUTIONS
        ACTIVE_POLICIES
          ACTIVE_POLICIES
        ADDITIONAL_DATA
          ADDITIONAL_DATA
        ADDITIONAL_USE
          ADDITIONAL_USE
        ADDRESSES_RISK
          ADDRESSES_RISK
        ADVANCED_ECONOMIES
          ADVANCED_ECONOMIES
    <BLANKLINE>
    <BLANKLINE>



"""
from techminer2._internals import ParamsMixin
from techminer2.thesaurus_old.user import SortByInitialWords as UserSortByInitialWords


class SortByInitialWords(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserSortByInitialWords()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )


# =============================================================================

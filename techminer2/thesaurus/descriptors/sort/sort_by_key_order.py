# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Key Order
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import CreateThesaurus, SortByKeyOrder

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> # Configure and run the sorter
    >>> sorter = (
    ...     SortByKeyOrder()
    ...     .having_keys_ordered_by("alphabetical")
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = StringIO()
    >>> print(output)
    Reducing thesaurus keys
      File : example/thesaurus/descriptors.the.txt
      Keys reduced from 1729 to 1729
      Keys reduction completed successfully
    <BLANKLINE>
    Sorting thesaurus alphabetically
      File : example/thesaurus/descriptors.the.txt
      Thesaurus sorting completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/descriptors.the.txt
    <BLANKLINE>
        ACADEMIA
          ACADEMIA
        ACADEMICS
          ACADEMICS
        ACADEMIC_OBSERVERS
          ACADEMIC_OBSERVERS
        ACADEMIC_RESEARCH
          ACADEMIC_RESEARCH
        ACCELERATE_ACCESS
          ACCELERATE_ACCESS
        ACCEPTANCE_MODELS
          ACCEPTANCE_MODELS
        ACCESS
          ACCESS
        ACCESS_LOANS
          ACCESS_LOANS
    <BLANKLINE>
    <BLANKLINE>

    >>> # Configure and run the sorter
    >>> sorter = (
    ...     SortByKeyOrder()
    ...     .having_keys_ordered_by("key_length")
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = StringIO()
    >>> print(output)
    Reducing thesaurus keys
      File : example/thesaurus/descriptors.the.txt
      Keys reduced from 1729 to 1729
      Keys reduction completed successfully
    <BLANKLINE>
    Sorting thesaurus by key length
      File : example/thesaurus/descriptors.the.txt
      Thesaurus sorting completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/descriptors.the.txt
    <BLANKLINE>
        CONTINUOUS_INTENTION_TO_USE_MOBILE_FINTECH_PAYMENT_SERVICES
          CONTINUOUS_INTENTION_TO_USE_MOBILE_FINTECH_PAYMENT_SERVICES
        UNIFIED_THEORY_OF_ACCEPTANCE_AND_USE_OF_TECHNOLOGY_MODEL
          UNIFIED_THEORY_OF_ACCEPTANCE_AND_USE_OF_TECHNOLOGY_MODEL
        A_NOVEL_HYBRID_MULTIPLE_CRITERIA_DECISION_MAKING_METHOD
          A_NOVEL_HYBRID_MULTIPLE_CRITERIA_DECISION_MAKING_METHOD
        THE_MOST_IMPORTANT_AND_FASTEST_GROWING_FINTECH_SERVICES
          THE_MOST_IMPORTANT_AND_FASTEST_GROWING_FINTECH_SERVICES
        INSTITUTIONS_OVERLOOKS_THE_CONCEPTUALLY_DISTINCT_RISKS
          INSTITUTIONS_OVERLOOKS_THE_CONCEPTUALLY_DISTINCT_RISKS
        THE_HEFEI_SCIENCE_AND_TECHNOLOGY_RURAL_COMMERCIAL_BANK
          THE_HEFEI_SCIENCE_AND_TECHNOLOGY_RURAL_COMMERCIAL_BANK
        FUTURE_AND_PRESENT_MOBILE_FINTECH_PAYMENT_SERVICES
          FUTURE_AND_PRESENT_MOBILE_FINTECH_PAYMENT_SERVICES
        UNIFIED_THEORY_OF_ACCEPTANCE_AND_USE_OF_TECHNOLOGY
          UNIFIED_THEORY_OF_ACCEPTANCE_AND_USE_OF_TECHNOLOGY
    <BLANKLINE>
    <BLANKLINE>

    >>> # Configure and run the sorter
    >>> sorter = (
    ...     SortByKeyOrder()
    ...     .having_keys_ordered_by("word_length")
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Reducing thesaurus keys
      File : example/thesaurus/descriptors.the.txt
      Keys reduced from 1729 to 1729
      Keys reduction completed successfully
    <BLANKLINE>
    Sorting thesaurus by word length
      File : example/thesaurus/descriptors.the.txt
      Thesaurus sorting completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/descriptors.the.txt
    <BLANKLINE>
        RESEARCH_LIMITATIONS/IMPLICATIONS
          RESEARCH_LIMITATIONS/IMPLICATIONS
        COMPETITION (ECONOMICS)
          COMPETITION (ECONOMICS)
        FINANCIAL_TECHNOLOGY (FINTECH)
          FINANCIAL_TECHNOLOGY (FINTECH)
        A_WIDE_RANGING_RECONCEPTUALIZATION
          A_WIDE_RANGING_RECONCEPTUALIZATION
        NETWORKS (CIRCUITS)
          NETWORKS (CIRCUITS)
        THE_RECONCEPTUALIZATION
          THE_RECONCEPTUALIZATION
        CLASSIFICATION (OF_INFORMATION)
          CLASSIFICATION (OF_INFORMATION)
        EXPLORE_INTERRELATIONSHIPS
          EXPLORE_INTERRELATIONSHIPS
    <BLANKLINE>
    <BLANKLINE>


"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByKeyOrder as UserSortByKeyOrder


class SortByKeyOrder(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            UserSortByKeyOrder()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )

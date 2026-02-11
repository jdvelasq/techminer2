# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Key Length
===============================================================================


Smoke tests:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.refine.thesaurus_old.descriptors import InitializeThesaurus, SortByKeyLength

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Configure and run the sorter
    >>> sorter = (
    ...     SortByKeyLength()
    ...     .where_root_directory("examples/small/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = StringIO()
    >>> print(output) # doctest: +SKIP
    Sorting thesaurus by key length...
      File : examples/fintech/data/thesaurus/descriptors.the.txt
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        CONTINUOUS_INTENTION_TO_USE_MOBILE_FINTECH_PAYMENT_SERVICES
          CONTINUOUS_INTENTION_TO_USE_MOBILE_FINTECH_PAYMENT_SERVICES
        UNIFIED_THEORY_OF_ACCEPTANCE_AND_USE_OF_TECHNOLOGY_MODEL
          UNIFIED_THEORY_OF_ACCEPTANCE_AND_USE_OF_TECHNOLOGY_MODEL
        A_NOVEL_HYBRID_MULTIPLE_CRITERIA_DECISION_MAKING_METHOD
          A_NOVEL_HYBRID_MULTIPLE_CRITERIA_DECISION_MAKING_METHOD
        THAT_FUTURE_AND_PRESENT_MOBILE_FINTECH_PAYMENT_SERVICES
          THAT_FUTURE_AND_PRESENT_MOBILE_FINTECH_PAYMENT_SERVICES
        THE_MOST_IMPORTANT_AND_FASTEST_GROWING_FINTECH_SERVICES
          THE_MOST_IMPORTANT_AND_FASTEST_GROWING_FINTECH_SERVICES
        THE_HEFEI_SCIENCE_AND_TECHNOLOGY_RURAL_COMMERCIAL_BANK
          THE_HEFEI_SCIENCE_AND_TECHNOLOGY_RURAL_COMMERCIAL_BANK
        THE_MODIFIED_VISEKRITERIJUMSKO_KOMPROMISNO_RANGIRANJE
          THE_MODIFIED_VISEKRITERIJUMSKO_KOMPROMISNO_RANGIRANJE
        PURCHASE_RELATED_GLOBAL_MOBILE_PAYMENT_MARKET_SIZE
          PURCHASE_RELATED_GLOBAL_MOBILE_PAYMENT_MARKET_SIZE
    <BLANKLINE>
    <BLANKLINE>




"""
from techminer2._internals import ParamsMixin
from techminer2.refine.thesaurus_old.user import SortByKeyLength as UserSortByKeyLength


class SortByKeyLength(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            UserSortByKeyLength()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )


# =============================================================================

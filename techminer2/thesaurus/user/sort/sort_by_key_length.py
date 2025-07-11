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


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.user import CreateThesaurus, SortByKeyLength

    >>> # Redirecting stderr to avoid messages during doctests
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Reset the thesaurus to initial state
    >>> CreateThesaurus(thesaurus_file="demo.the.txt", field="raw_descriptors",
    ...     root_directory="example/", quiet=True).run()

    >>> # Creates, configures, an run the sorter
    >>> sorter = (
    ...     SortByKeyLength()
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = StringIO()
    >>> print(output)
    Reducing thesaurus keys
      File : example/data/thesaurus/demo.the.txt
      Keys reduced from 1726 to 1726
      Reduction process completed successfully
    <BLANKLINE>
    Sorting thesaurus by key length
      File : example/data/thesaurus/demo.the.txt
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/demo.the.txt
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



"""
import sys

from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header
from ..general.reduce_keys import ReduceKeys


class SortByKeyLength(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = self.thesaurus_path

        sys.stderr.write("Sorting thesaurus by key length\n")
        sys.stderr.write(f"  File : {file_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Sorting process completed successfully\n\n")
        sys.stderr.flush()

        internal__print_thesaurus_header(self.thesaurus_path)

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__reduce_keys(self):
        ReduceKeys().update(**self.params.__dict__).run()

    # -------------------------------------------------------------------------
    def internal__sort_keys(self):

        self.data_frame["length"] = self.data_frame["key"].str.len()
        self.data_frame = self.data_frame.sort_values(
            ["length", "key"], ascending=[False, True]
        )

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__reduce_keys()
        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__sort_keys()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()


# =============================================================================

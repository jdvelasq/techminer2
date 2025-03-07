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
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.user import CreateThesaurus, SortByKeyOrder

    >>> # Redirecting stderr to avoid messages during doctests
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Reset the thesaurus to initial state
    >>> CreateThesaurus(thesaurus_file="demo.the.txt", field="raw_descriptors",
    ...     root_directory="example/", quiet=True).run()

    >>> # Creates, configures, an run the sorter
    >>> sorter = (
    ...     SortByKeyOrder()
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .having_keys_ordered_by("alphabetical")
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = StringIO()
    >>> print(output)
    Sorting thesaurus alphabetically
      File : example/thesaurus/demo.the.txt
      Thesaurus sorting completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/demo.the.txt
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
        ACCEPTANCE
          ACCEPTANCE
        ACCEPTANCE_MODELS
          ACCEPTANCE_MODELS
        ACCESS
          ACCESS
    <BLANKLINE>
    <BLANKLINE>


    >>> sorter = (
    ...     SortByKeyOrder()
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .having_keys_ordered_by("key_length")
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = StringIO()
    >>> print(output)
    Sorting thesaurus by key length
      File : example/thesaurus/demo.the.txt
      Thesaurus sorting completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/demo.the.txt
    <BLANKLINE>
        A_NOVEL_HYBRID_MULTIPLE_CRITERIA_DECISION_MAKING_METHOD
          A_NOVEL_HYBRID_MULTIPLE_CRITERIA_DECISION_MAKING_METHOD
        THE_MOST_IMPORTANT_AND_FASTEST_GROWING_FINTECH_SERVICES
          THE_MOST_IMPORTANT_AND_FASTEST_GROWING_FINTECH_SERVICES
        THE_HEFEI_SCIENCE_AND_TECHNOLOGY_RURAL_COMMERCIAL_BANK
          THE_HEFEI_SCIENCE_AND_TECHNOLOGY_RURAL_COMMERCIAL_BANK
        FUTURE_AND_PRESENT_MOBILE_FINTECH_PAYMENT_SERVICES
          FUTURE_AND_PRESENT_MOBILE_FINTECH_PAYMENT_SERVICES
        UNIFIED_THEORY_OF_ACCEPTANCE_AND_USE_OF_TECHNOLOGY
          UNIFIED_THEORY_OF_ACCEPTANCE_AND_USE_OF_TECHNOLOGY
        THE_FINANCIAL_AND_DIGITAL_INNOVATION_LITERATURE
          THE_FINANCIAL_AND_DIGITAL_INNOVATION_LITERATURE
        ECONOMIC_SUSTAINABILITY_AND_COST_EFFECTIVENESS
          ECONOMIC_SUSTAINABILITY_AND_COST_EFFECTIVENESS
        FINTECH_AND_SUSTAINABLE_DEVELOPMENT_:_EVIDENCE
          FINTECH_AND_SUSTAINABLE_DEVELOPMENT_:_EVIDENCE
    <BLANKLINE>
    <BLANKLINE>

    >>> # Creates, configures, an run the sorter
    >>> sorter = (
    ...     SortByKeyOrder()
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .having_keys_ordered_by("word_length")
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Sorting thesaurus by word length
      File : example/thesaurus/demo.the.txt
      Thesaurus sorting completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/demo.the.txt
    <BLANKLINE>
        THE_FINTECHPHILANTHROPYDEVELOPMENT_COMPLEX
          THE_FINTECHPHILANTHROPYDEVELOPMENT_COMPLEX
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
import sys

from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header


class SortByKeyOrder(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = self.thesaurus_path

        self.order_by = {
            "alphabetical": "alphabetically",
            "key_length": "by key length",
            "word_length": "by word length",
        }[self.params.keys_order_by]
        order_by = self.order_by

        sys.stderr.write(f"Sorting thesaurus {order_by}\n")
        sys.stderr.write(f"  File : {file_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Thesaurus sorting completed successfully\n\n")
        sys.stderr.flush()

        internal__print_thesaurus_header(self.thesaurus_path)

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__sort_keys(self):

        if self.params.keys_order_by == "alphabetical":
            self.data_frame = self.data_frame.sort_values("key")

        if self.params.keys_order_by == "key_length":
            self.data_frame["length"] = self.data_frame["key"].str.len()
            self.data_frame = self.data_frame.sort_values(
                ["length", "key"], ascending=[False, True]
            )

        if self.params.keys_order_by == "word_length":

            n_spaces = len(self.data_frame[self.data_frame["key"].str.contains(" ")])
            n_underscores = len(
                self.data_frame[self.data_frame["key"].str.contains("_")]
            )

            if n_spaces > n_underscores:
                self.data_frame["length"] = self.data_frame["key"].str.split(" ")
            else:
                self.data_frame["length"] = self.data_frame["key"].str.split("_")
            self.data_frame["length"] = self.data_frame["length"].apply(
                lambda x: max(len(i) for i in x)
            )
            self.data_frame = self.data_frame.sort_values(
                ["length", "key"], ascending=[False, True]
            )

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__sort_keys()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()


# =============================================================================

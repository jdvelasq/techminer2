# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# mypy: ignore-errors
"""
Cleanup Thesaurus
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import CleanupThesaurus, CreateThesaurus

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> cleaner = (
    ...     CleanupThesaurus()
    ...     .where_root_directory_is("example/")
    ... )
    >>> cleaner.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output) # doctest: +NORMALIZE_WHITESPACE
    Cleanup Thesaurus
      File : example/data/thesaurus/descriptors.the.txt
      21 replacements made successfully
    Cleanup process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        *GEOGRAPHIC_REGIONS*
          AUSTRALIA_AND_NEW_ZEALAND; BRAZIL; CHINA; EUROPE; GERMANY; INDONESIA; KEN...
        *LITERATURE_REVIEW*
          LITERATURE_REVIEW
        *PUBLISHERS*
          RESEARCH_INDIA_PUBLICATIONS
        *STUDY*
          CASE_STUDIES; CASE_STUDY
        APPROACH
          APPROACHES
        CONSTRUCT
          CONSTRUCTS
        ORGANIZATION
          BUSINESS; BUSINESSES; COMPANIES; FIRMS; INTERNATIONAL_ORGANIZATION; ORGAN...
        RESEARCH
          ACADEMIC_RESEARCH; RESEARCH
    <BLANKLINE>
    <BLANKLINE>


"""
import glob
import re
import sys

import pkg_resources  # type: ignore
from tqdm import tqdm  # type: ignore

from ...._internals.mixins import ParamsMixin
from ..._internals import (
    ThesaurusMixin,
    internal__load_reversed_thesaurus_as_mapping,
    internal__print_thesaurus_header,
)

tqdm.pandas()


class CleanupThesaurus(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        truncated_path = str(self.thesaurus_path)
        if len(truncated_path) > 72:
            truncated_path = "..." + truncated_path[-68:]
        sys.stderr.write("Cleanup Thesaurus \n")
        sys.stderr.write(f"  File : {truncated_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write(". Cleanup process completed successfully\n\n")
        sys.stderr.flush()

        internal__print_thesaurus_header(self.thesaurus_path)

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__transform_keys(self):

        self.data_frame["__row_selected__"] = False
        self.data_frame["org_key"] = self.data_frame["key"].copy()

        file_paths = pkg_resources.resource_filename(
            "techminer2",
            "package_data/thesaurus/cleanup/*.the.txt",
        )

        for file_path in glob.glob(file_paths):
            mapping = internal__load_reversed_thesaurus_as_mapping(file_path)
            self.data_frame["key"] = self.data_frame["key"].map(
                lambda x: mapping.get(x, x)
            )

        self.data_frame.loc[
            self.data_frame.key != self.data_frame.org_key,
            "__row_selected__",
        ] = True

        n_matches = self.data_frame.__row_selected__.sum()

        sys.stderr.write(f"  {n_matches} replacements made successfully\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.with_thesaurus_file("descriptors.the.txt")
        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__transform_keys()
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()

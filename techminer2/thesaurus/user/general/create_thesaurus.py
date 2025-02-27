# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Create Thesaurus
===============================================================================


>>> from techminer2.thesaurus.user import CreateThesaurus
>>> (
...     CreateThesaurus()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("demo.the.txt")
...     #
...     # FIELD:
...     .with_field("descriptors")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... )
Creating thesaurus from 'descriptors' field
  File : example/thesaurus/demo.the.txt
  1796 keys found
  Thesaurus creation completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/demo.the.txt
<BLANKLINE>
    A_A_)_THEORY
      A_A_)_THEORY
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

"""
import sys

import pandas as pd  # type: ignore
from textblob import Word  # type: ignore
from tqdm import tqdm  # type: ignore

from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header

tqdm.pandas()


class CreateThesaurus(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        if not self.params.quiet:

            field = self.params.field
            truncated_path = str(self.thesaurus_path)
            if len(truncated_path) > 72:
                truncated_path = "..." + truncated_path[-68:]
            sys.stdout.write(f"Creating thesaurus from '{field}' field\n")
            sys.stdout.write(f"  File : {truncated_path}\n")
            sys.stdout.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        if not self.params.quiet:

            sys.stdout.write(f"  {len(self.data_frame)} keys found\n")
            sys.stdout.write("  Thesaurus creation completed successfully\n\n")
            sys.stdout.flush()

            internal__print_thesaurus_header(self.thesaurus_path)

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_filtered_records()
        self.internal__create_thesaurus_data_frame_from_field()
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Reduce Keys
===============================================================================


>>> from techminer2.thesaurus.user import CreateThesaurus
>>> CreateThesaurus(thesaurus_file="demo.the.txt", field="descriptors", 
...     root_directory="example/", quiet=True).run()


>>> from techminer2.thesaurus.user import ReduceKeys
>>> (
...     ReduceKeys()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("demo.the.txt")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... )
Reducing thesaurus keys
  File : example/thesaurus/demo.the.txt
  Keys reduced from 1796 to 1796
  Keys reduction completed successfully
<BLANKLINE>



"""
import sys

from tqdm import tqdm  # type: ignore

from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header

tqdm.pandas()


class ReduceKeys(
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
        sys.stdout.write(f"Reducing thesaurus keys\n")
        sys.stdout.write(f"  File : {truncated_path}\n")
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stdout.write(
            f"  Keys reduced from {self.n_initial_keys} to {self.n_final_keys}\n"
        )
        sys.stdout.write(f"  Keys reduction completed successfully\n\n")
        sys.stdout.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Key Reducer
===============================================================================


>>> from techminer2.thesaurus.user import KeyReducer
>>> (
...     KeyReducer()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("demo.the.txt")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .build()
... )
<BLANKLINE>
Keys reduction completed successfully for file: ...ample/thesaurus/demo.the.txt



"""
import sys

from tqdm import tqdm  # type: ignore

from ..._internals.mixins import ParamsMixin
from .._internals import ThesaurusMixin, internal__print_thesaurus_header

tqdm.pandas()


class KeyReducer(
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
        sys.stderr.write(f"\nReducing thesaurus keys")
        sys.stderr.write(f"\n  File : {truncated_path}")
        sys.stderr.write("\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        truncated_path = str(self.thesaurus_path)
        if len(truncated_path) > 32:
            truncated_path = "..." + truncated_path[-28:]
        sys.stdout.write(
            f"\nKeys reduction completed successfully for file: {truncated_path}"
        )
        sys.stdout.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        self.internal__build_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_thesaurus_mapping_to_data_frame()
        self.internal__reduce_keys()
        self.internal__group_values_by_key()
        self.internal__sort_data_frame_by_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()

        internal__print_thesaurus_header(self.thesaurus_path)

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Starting Stopwords Remover
===============================================================================


>>> from techminer2.thesaurus.user import StartingStopwordsRemover
>>> (
...     StartingStopwordsRemover()
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
Removing stopwords completed successfully for file: ...e/thesaurus/demo.the.txt



"""
import re
import sys

from textblob import Word  # type: ignore
from tqdm import tqdm  # type: ignore

from ...._internals.mixins import ParamsMixin
from ....package_data.text_processing import internal__load_text_processing_terms
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header

tqdm.pandas()


class StartingStopwordsRemover(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def notify__process_start(self):

        file_path = self.thesaurus_path

        sys.stdout.write("\nRemoving starting stopwords from thesaurus keys")
        sys.stdout.write(f"\n  File : {file_path}")
        sys.stdout.write("\n")
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def notify__process_end(self):
        truncated_file_path = str(self.thesaurus_path)
        if len(truncated_file_path) > 31:
            truncated_file_path = "..." + truncated_file_path[-27:]
        sys.stdout.write(
            f"\nRemoving stopwords completed successfully for file: {truncated_file_path}"
        )
        sys.stdout.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__remove_starting_stopwords_from_keys(self):

        words = internal__load_text_processing_terms("technical_stopwords.txt")

        words = [w for w in words if len(w) > 1]
        words = [w for w in words if "'" not in w]

        # create regular expressions
        patterns = []
        patterns += [re.compile(r"^" + d.lower() + r" ") for d in words]
        patterns += [re.compile(r"^" + d.upper() + r" ") for d in words]
        patterns += [re.compile(r"^" + d.upper() + r"_") for d in words]
        patterns += [re.compile(r"^" + d.title() + r" ") for d in words]

        def replace_patterns(text):
            for pattern in patterns:
                text = pattern.sub("", text)
            return text

        tqdm.pandas(desc="  Progress")
        self.data_frame["key"] = self.data_frame.key.progress_apply(replace_patterns)
        tqdm.pandas(desc=None)

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        self.internal__build_user_thesaurus_path()
        self.notify__process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__remove_starting_stopwords_from_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.notify__process_end()

        internal__print_thesaurus_header(self.thesaurus_path)

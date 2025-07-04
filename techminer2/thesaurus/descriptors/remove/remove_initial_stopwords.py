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


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import CreateThesaurus, RemoveInitialStopwords

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> # Remove initial stopwords
    >>> RemoveInitialStopwords(root_directory="example/", tqdm_disable=True).run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Removing starting stopwords from thesaurus keys
      File : example/thesaurus/descriptors.the.txt
      548 initial stopwords removed successfully
      Starting stopwords removal completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/descriptors.the.txt
    <BLANKLINE>
        ACADEMIC_FINANCE_COMMUNITY
          THE_ACADEMIC_FINANCE_COMMUNITY
        ACADEMICS
          ACADEMICS; BOTH_ACADEMICS; OTHER_ACADEMICS
        ACCEPTANCE
          THE_ACCEPTANCE
        ACTION
          OUR_ACTION
        ACTIVE_PARTICIPANT
          AN_ACTIVE_PARTICIPANT
        ACTORS
          ACTORS; ALL_ACTORS
        ADDITIONAL_COMPONENTS
          FIVE_ADDITIONAL_COMPONENTS
        ADOPTION
          ADOPTION; THE_ADOPTION
    <BLANKLINE>
    <BLANKLINE>

"""
import re
import sys

from textblob import Word  # type: ignore
from tqdm import tqdm  # type: ignore

from ...._internals.mixins import ParamsMixin
from ....package_data.text_processing import internal__load_text_processing_terms
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header

tqdm.pandas()


class RemoveInitialStopwords(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = self.thesaurus_path

        sys.stderr.write("Removing starting stopwords from thesaurus keys\n")
        sys.stderr.write(f"  File : {file_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Starting stopwords removal completed successfully\n\n")
        sys.stderr.flush()

        internal__print_thesaurus_header(self.thesaurus_path)

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__remove_starting_stopwords_from_keys(self):

        self.data_frame["__row_selected__"] = False
        self.data_frame["org_key"] = self.data_frame["key"].copy()

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

        tqdm.pandas(desc="  Progress ", disable=self.params.tqdm_disable, ncols=80)
        self.data_frame["key"] = self.data_frame.key.progress_apply(replace_patterns)
        tqdm.pandas(desc=None)

        self.data_frame.loc[
            self.data_frame.key != self.data_frame.org_key,
            "__row_selected__",
        ] = True

        n_matches = self.data_frame.__row_selected__.sum()

        sys.stderr.write(f"  {n_matches} initial stopwords removed successfully\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.with_thesaurus_file("descriptors.the.txt")

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__remove_starting_stopwords_from_keys()
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()

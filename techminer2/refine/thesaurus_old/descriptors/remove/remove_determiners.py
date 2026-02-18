# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Determiners
===============================================================================


Smoke tests:
    >>> import sys
    >>> from io import StringIO

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> from techminer2.refine.thesaurus_old.descriptors import InitializeThesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> from techminer2.refine.thesaurus_old.descriptors import RemoveDeterminers
    >>> RemoveDeterminers(root_directory="examples/fintech/", tqdm_disable=True, ).run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Removing initial determiners from thesaurus keys...
      File : examples/fintech/data/thesaurus/descriptors.the.txt
      601 initial determiners removed successfully
      Removal process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        A_THEORY
          A_A_THEORY
        ACADEMIC_FINANCE_COMMUNITY
          THE_ACADEMIC_FINANCE_COMMUNITY
        ACADEMICS
          ACADEMICS; BOTH_ACADEMICS
        ACCEPTANCE
          THE_ACCEPTANCE
        ACTIVE_PARTICIPANT
          AN_ACTIVE_PARTICIPANT
        ACTORS
          ACTORS; ALL_ACTORS
        ADOPTION
          ADOPTION; THE_ADOPTION
        ADVANCEMENT
          THE_ADVANCEMENT
    <BLANKLINE>
    <BLANKLINE>


"""
import re
import sys

from colorama import Fore, init
from tqdm import tqdm  # type: ignore

from techminer2._internals import ParamsMixin
from techminer2._internals.package_data.word_lists import load_builtin_word_list
from techminer2.refine.thesaurus_old._internals import ThesaurusMixin

tqdm.pandas()


class RemoveDeterminers(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = str(self.thesaurus_path)

        if self.params.colored_stderr:
            filename = str(file_path).rsplit("/", maxsplit=1)[1]
            file_path = file_path.replace(filename, f"{Fore.RESET}{filename}")
            file_path = Fore.LIGHTBLACK_EX + file_path

        sys.stderr.write("Removing initial determiners from thesaurus keys...\n")
        sys.stderr.write(f"  File : {file_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Removal process completed successfully\n\n")
        sys.stderr.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__remove_starting_determiners_from_keys(self):

        self.data_frame["__row_selected__"] = False
        self.data_frame["org_key"] = self.data_frame["key"].copy()

        words = load_builtin_word_list("determiners.txt")
        known_phrases = load_builtin_word_list("noun_phrases.txt")

        # create regular expressions
        patterns = []
        patterns += [re.compile(r"^" + d.lower() + r" ") for d in words]
        patterns += [re.compile(r"^" + d.upper() + r" ") for d in words]
        patterns += [re.compile(r"^" + d.upper() + r"_") for d in words]
        patterns += [re.compile(r"^" + d.title() + r" ") for d in words]

        def replace_patterns(text):
            if text not in known_phrases:
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

        sys.stderr.write(f"  {n_matches} initial determiners removed successfully\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.with_thesaurus_file("descriptors.the.txt")

        self._build_user_thesaurus_path()
        self.internal__notify_process_start()
        self._load_thesaurus_as_mapping()
        self._transform_mapping_to_data_frame()
        self.internal__remove_starting_determiners_from_keys()
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self._sort_data_frame_by_rows_and_key()
        self._write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()
        self.internal__print_thesaurus_header_to_stream(n=8, stream=sys.stderr)

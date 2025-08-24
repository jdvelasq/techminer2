# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Translate American to British Spelling
===============================================================================


Example:
    >>> # Redirecting stderr to avoid messages during doctests
    >>> import sys
    >>> from io import StringIO
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Reset the thesaurus to initial state
    >>> from techminer2.thesaurus.user import InitializeThesaurus
    >>> InitializeThesaurus(thesaurus_file="demo.the.txt", field="raw_descriptors",
    ...     root_directory="examples/fintech/", quiet=True).run()

    >>> # Creates, configures, an run the translator
    >>> from techminer2.thesaurus.user import AmericanToBritishSpelling
    >>> (
    ...     AmericanToBritishSpelling(tqdm_disable=True, use_colorama=False)
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .where_root_directory_is("examples/fintech/")
    ...     .run()
    ... )


    >>> # Capture and print stderr output to test the code using doctest
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output) # doctest: +ELLIPSIS +SKIP
    Converting American to British English...
      File : examples/fintech/data/thesaurus/demo.the.txt
      21 replacements made successfully
      Translation process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/demo.the.txt
    <BLANKLINE>
        A_COMPLETE_GENERALISATION
          A_COMPLETE_GENERALIZATION
        AN_ORGANISATION
          AN_ORGANIZATION
        BEHAVIOURAL_BIASES
          BEHAVIORAL_BIASES
        CATEGORISES_RESEARCH
          CATEGORIZES_RESEARCH
        CHARACTERISE_FINTECH
          CHARACTERIZE_FINTECH
        DECENTRALISED_FINTECH_MARKETS
          DECENTRALIZED_FINTECH_MARKETS
        DIGITISED_AGRICULTURE
          DIGITIZED_AGRICULTURE
        EXCESSIVELY_RISKY_BEHAVIOUR
          EXCESSIVELY_RISKY_BEHAVIOR
    <BLANKLINE>
    <BLANKLINE>



"""
import re
import sys

from colorama import Fore, init
from tqdm import tqdm  # type: ignore

from techminer2._internals.mixins import ParamsMixin
from techminer2.thesaurus._internals import (
    ThesaurusMixin,
    internal__generate_system_thesaurus_file_path,
    internal__load_thesaurus_as_mapping,
    internal__print_thesaurus_header,
)

tqdm.pandas()


class AmericanToBritishSpelling(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        file_path = str(self.thesaurus_path)
        if len(file_path) > 72:
            file_path = "..." + file_path[-68:]

        if self.params.use_colorama:
            filename = str(file_path).rsplit("/", maxsplit=1)[1]
            file_path = file_path.replace(filename, f"{Fore.RESET}{filename}")
            file_path = Fore.LIGHTBLACK_EX + file_path

        sys.stderr.write("Converting American to British English...\n")
        sys.stderr.write(f"  File : {file_path}\n")
        sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stderr.write("  Translation process completed successfully\n\n")
        sys.stderr.flush()

        internal__print_thesaurus_header(
            thesaurus_path=self.thesaurus_path, use_colorama=self.params.use_colorama
        )

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__translate_words_on_keys(self):

        self.data_frame["__row_selected__"] = False
        self.data_frame["org_key"] = self.data_frame["key"].copy()

        file_path = internal__generate_system_thesaurus_file_path(
            "language/american2british.the.txt"
        )
        mapping = internal__load_thesaurus_as_mapping(file_path)
        mapping = {k: v[0] for k, v in mapping.items()}

        patterns = []

        for key, value in mapping.items():
            pat = [
                (re.compile(r"^" + key.lower() + " "), value.lower() + " "),
                (re.compile(r" " + key.lower() + r"$"), " " + value.lower()),
                (re.compile(r"^" + key.lower() + r"$"), value.lower()),
                (re.compile(r"^" + key.upper() + " "), value.upper() + " "),
                (re.compile(r" " + key.upper() + r"$"), " " + value.upper()),
                (re.compile(r"^" + key.upper() + r"$"), value.upper()),
                (re.compile(r"^" + key.upper() + "_"), value.upper() + "_"),
                (re.compile(r"_" + key.upper() + r"$"), "_" + value.upper()),
            ]
            patterns.extend(pat)

        # replace the words
        def f(x):
            for pattern, replacement in patterns:
                x = pattern.sub(replacement, x)
            return x

        sys.stderr.flush()
        tqdm.pandas(desc="  Progress ", disable=self.params.tqdm_disable, ncols=80)
        self.data_frame["key"] = self.data_frame["key"].progress_apply(f)
        tqdm.pandas(desc=None)
        sys.stderr.flush()

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

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__translate_words_on_keys()
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()

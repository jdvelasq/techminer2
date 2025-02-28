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

>>> from techminer2.thesaurus.user import CreateThesaurus
>>> CreateThesaurus(thesaurus_file="demo.the.txt", field="descriptors", 
...     root_directory="example/", quiet=True).run()


>>> from techminer2.thesaurus.user import AmericanToBritishSpelling
>>> (
...     AmericanToBritishSpelling()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("demo.the.txt")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... )
Converting American to British English
  File : example/thesaurus/demo.the.txt
  23 replacements made successfully
Translation completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/demo.the.txt
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




"""
import re
import sys

from tqdm import tqdm  # type: ignore

from ...._internals.mixins import ParamsMixin
from ..._internals import (
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

        truncated_path = str(self.thesaurus_path)
        if len(truncated_path) > 72:
            truncated_path = "..." + truncated_path[-68:]
        sys.stdout.write("Converting American to British English\n")
        sys.stdout.write(f"  File : {truncated_path}\n")
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        sys.stdout.write("Translation completed successfully\n\n")
        sys.stdout.flush()

        internal__print_thesaurus_header(self.thesaurus_path)

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

        sys.stderr.write("\n")
        sys.stderr.flush()
        tqdm.pandas(desc="  Progress")
        self.data_frame["key"] = self.data_frame["key"].progress_apply(f)
        tqdm.pandas(desc=None)
        sys.stderr.write("\n")
        sys.stderr.flush()

        self.data_frame.loc[
            self.data_frame.key != self.data_frame.org_key,
            "__row_selected__",
        ] = True

        n_matches = self.data_frame.__row_selected__.sum()

        sys.stdout.write(f"  {n_matches} replacements made successfully\n")
        sys.stdout.flush()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__build_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__translate_words_on_keys()
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()

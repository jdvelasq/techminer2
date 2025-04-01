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


Example:

    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.abbreviations import CreateThesaurus

    >>> # Redirect stderr to capture output
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> CreateThesaurus(root_directory="example/").run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Creating thesaurus
      20 abbreviations found
      Thesaurus creation completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/abbreviations.the.txt
    <BLANKLINE>
        A_A_
          using AFFORDANCE_ACTUALIZATION ( A_A_)_THEORY as THE_THEORETICAL_LENS , w...
        AI
          ARTIFICIAL_INTELLIGENCE; purpose : considering THE_INCREASING_IMPACT of A...
        ANT
          ACTOR_NETWORK_THEORY; THIS_STUDY applies THE_LENS of ACTOR_NETWORK_THEORY...
        DEMATEL
          A_SIX_DIMENSIONAL_MODEL comprising 20 SUB_CRITERIA is constructed and BOT...
        E_FINANCE
          ELECTRONIC_FINANCE
        E_PAYMENT
          ELECTRONIC_PAYMENT
        EPAM
          we propose A_RESEARCH_MODEL using AN_EXTENDED_POST_ACCEPTANCE_MODEL ( EPA...
        EU
          EUROPEAN_UNION; yet , empirically , FINTECH remains very small , especial...
    <BLANKLINE>


"""
import sys

import pandas as pd  # type: ignore
from nltk.corpus import words
from textblob import TextBlob  # type: ignore

from ...._internals.log_message import internal__log_message
from ...._internals.mixins import ParamsMixin
from ....thesaurus._internals import (
    internal__generate_system_thesaurus_file_path,
    internal__load_thesaurus_as_mapping,
)
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header
from ..._internals.load_thesaurus_as_mapping import internal__load_thesaurus_as_mapping


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

            sys.stderr.write(f"Creating thesaurus\n")
            sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        if not self.params.quiet:

            sys.stderr.write(f"  {len(self.data_frame)} abbreviations found\n")
            sys.stderr.write("  Thesaurus creation completed successfully\n\n")
            sys.stderr.flush()

            internal__print_thesaurus_header(self.thesaurus_path)

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__create_valid_words(self):

        data_frame = self.data_frame.copy()
        data_frame = data_frame[["value"]]

        data_frame["value"] = data_frame["value"].str.split("_")
        data_frame = data_frame.explode("value")
        data_frame["value"] = data_frame["value"].str.strip()

        data_frame["value"] = data_frame["value"].str.split(" ")
        data_frame = data_frame.explode("value")
        data_frame["value"] = data_frame["value"].str.strip()

        data_frame["value"] = data_frame["value"].map(
            lambda x: x[1:-1] if x.startswith("(") and x.endswith(")") else x
        )
        data_frame["value"] = data_frame["value"].str.strip()

        data_frame = data_frame[data_frame["value"].str.len() > 1]

        self.words = data_frame["value"].drop_duplicates().tolist()

    # -------------------------------------------------------------------------
    def internal__extracts_abbreviations_from_definitions(self):

        data_frame = self.data_frame.copy()

        data_frame = data_frame.loc[data_frame.value.str.contains("(", regex=False), :]
        data_frame = data_frame.loc[data_frame.value.str.endswith(")"), :]
        data_frame = data_frame[["value"]].drop_duplicates()
        data_frame["value"] = data_frame["value"].str[:-1]
        data_frame["value"] = data_frame["value"].str.split(" (", regex=False)

        data_frame = data_frame[data_frame.value.map(len) == 2]
        data_frame["key"] = data_frame.value.map(lambda x: x[1])
        data_frame["value"] = data_frame.value.map(lambda x: x[0])
        data_frame = data_frame[data_frame.key.str.len() < data_frame.value.str.len()]

        self.data_frame = data_frame

    # -------------------------------------------------------------------------
    def internal__add_abbreviations_from_abstracts_to_data_frame(self):

        records = self.filtered_records[["abstract"]].dropna()

        # extract phrases
        records["abstract"] = records.abstract.map(
            lambda x: [str(s) for s in TextBlob(x).sentences]
        )
        # records["abstract"] = records.abstract.map(
        #     lambda x: [t for s in x for t in s.split(",")]
        # )
        records = records.explode("abstract")
        records["abstract"] = records.abstract.str.strip()

        # select abstracts with parentheses
        records = records[records.abstract.str.contains("(", regex=False)]
        records = records[records.abstract.str.contains(")", regex=False)]

        # extract abbreviations
        records["key"] = records.abstract.str.extract(r"\(([^)]+)\)")
        records["key"] = records.key.str.upper().str.strip()
        records["value"] = records.abstract.str.replace(r"\([^)]+\)", "")
        records = records[["key", "value"]].drop_duplicates()
        records = records.dropna(subset=["key"])

        # remove text from the right of the abbreviation
        records = records.reset_index(drop=True)
        for index, row in records.iterrows():
            records.loc[index, "value"] = row.value.split("( " + row.key + " )")[0]
            records.loc[index, "value"] = row.value.split(
                "( " + row.key.lower() + " )"
            )[0]
            records.loc[index, "value"] += "( " + row.key.upper() + " )"

        # remove enumerations
        records = records[
            records.key.map(
                lambda x: x not in ["I", "II", "III", "IV", "V"], na_action="ignore"
            )
        ]
        records = records[
            records.key.map(
                lambda x: x not in ["1", "2", "3", "4", "5"], na_action="ignore"
            )
        ]
        records = records[records.key.map(lambda x: "," not in x, na_action="ignore")]
        records = records[records.key.map(lambda x: " " not in x, na_action="ignore")]
        records = records[records.key.map(lambda x: x != "_S_", na_action="ignore")]

        records = records[
            records.key.map(
                lambda x: not (
                    x.startswith("_") and x[1:5].isdigit() and x.endswith("_")
                ),
                na_action="ignore",
            )
        ]

        # remove abbreviations of length 1
        records = records[records.key.str.len() > 1]

        # remove enumerations already listed in the keywords
        existent_abbr = self.data_frame.key.drop_duplicates().tolist()
        records = records[records.key.map(lambda x: x not in existent_abbr)]

        # remove abbreviations that are only digits
        records = records[
            records.key.map(lambda x: not x.isdigit(), na_action="ignore")
        ]

        # validate abbreviations
        records = records[
            records.key.map(lambda x: x in self.words, na_action="ignore")
        ]

        # concat data frames
        self.data_frame = pd.concat([self.data_frame, records], ignore_index=True)

    # -------------------------------------------------------------------------
    def internal__remove_bad_abbreviations(self):

        bad_abbreviations = [
            "CLASSIFICATION",
            "COMPUTER",
            "ECONOMICS",
            "ELECTRONICS",
            "ELECTRONIC",
            "IRRATIONAL",
            "ONLINE",
            "PERSONNEL",
        ]

        for abbr in bad_abbreviations:
            self.data_frame = self.data_frame[self.data_frame.key != abbr]

    # -------------------------------------------------------------------------
    def internal__add_knowns_abbreviations(self):

        # Load known abbreviations
        file_path = internal__generate_system_thesaurus_file_path(
            "abbreviations/common_abbr.the.txt"
        )
        common_abbrvs = internal__load_thesaurus_as_mapping(file_path)

        # Load raw descriptors from records
        raw_descriptors = self.filtered_records[self.params.field].dropna()
        raw_descriptors = raw_descriptors.str.split("; ")
        raw_descriptors = raw_descriptors.explode()
        raw_descriptors = raw_descriptors.str.strip()
        raw_descriptors = raw_descriptors.drop_duplicates().tolist()

        # Adds definitions from raw descriptors
        for abbr, meaning in common_abbrvs.items():

            process = False

            if abbr in self.data_frame.key.tolist():
                process = True

            if abbr in raw_descriptors:
                process = True

            if any([x.startswith(abbr + "_") for x in raw_descriptors]):
                process = True

            if any([x.endswith("_" + abbr) for x in raw_descriptors]):
                process = True

            if any([("_" + abbr + "_") in x for x in raw_descriptors]):
                process = True

            if process:
                new_frame = pd.DataFrame({"value": [meaning[0]], "key": [abbr]})
                self.data_frame = pd.concat(
                    [self.data_frame, new_frame], ignore_index=True
                )

    # -------------------------------------------------------------------------
    def internal__prepare_fingerprints(self):
        self.data_frame["key"] = self.data_frame["key"].str.strip()
        self.data_frame = self.data_frame[self.data_frame.key != ""]
        self.data_frame["fingerprint"] = self.data_frame.key.copy()

    # -------------------------------------------------------------------------
    def internal__sort_mapping_values(self):
        self.data_frame["value"] = self.data_frame["value"].str.split("; ")
        self.data_frame["value"] = self.data_frame["value"].map(
            lambda x: sorted(x, key=len)
        )
        self.data_frame["value"] = self.data_frame["value"].str.join("; ")

    # -------------------------------------------------------------------------
    def interval__validate_keys(self):
        english_words = set(words.words())
        self.data_frame = self.data_frame[
            self.data_frame.key.map(
                lambda x: x.lower() not in english_words, na_action="ignore"
            )
        ]

    # -------------------------------------------------------------------------
    def run(self):

        self.params.field = "raw_descriptors"
        self.params.thesaurus_file = "abbreviations.the.txt"

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_filtered_records()
        self.internal__create_thesaurus_data_frame_from_field()

        self.internal__create_valid_words()

        self.internal__extracts_abbreviations_from_definitions()
        self.internal__add_abbreviations_from_abstracts_to_data_frame()
        self.internal__remove_bad_abbreviations()
        self.internal__add_knowns_abbreviations()
        self.internal__prepare_fingerprints()
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__sort_mapping_values()
        self.interval__validate_keys()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()

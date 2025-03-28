# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Create thesaurus
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.organizations import CreateThesaurus

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create and run the thesaurus creator
    >>> creator = (
    ...     CreateThesaurus()
    ...     .where_root_directory_is("example/")
    ... )
    >>> creator.run()



    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Creating thesaurus from 'affiliations' field
      File : example/thesaurus/organizations.the.txt
      90 keys found
      Thesaurus creation completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/organizations.the.txt
    <BLANKLINE>
        Anhui Univ of Finan and Econ (CHN)
          School of Finance, Anhui University of Finance and Economics, Bengbu, 233...
        Baekseok Univ (KOR)
          Division of Tourism, Baekseok University, South Korea
        Baewha Women’s Univ (KOR)
          Department of Information Security, Baewha Women’s University, Seoul, Sou...
        Baylor Univ (USA)
          Baylor University, United States; Hankamer School of Business, Baylor Uni...
        Beihang Univ (CHN)
          School of Economics and Management, Beihang University, China
        Brussels, Belgium (BEL)
          Brussels, Belgium
        Cent for Law, Markets & Regulation, UNSW Australia, Australia (AUS)
          Centre for Law, Markets & Regulation, UNSW Australia, Australia
        CESifo, Poschingerstr. 5, Munich, 81679, Germany (DEU)
          CESifo, Poschingerstr. 5, Munich, 81679, Germany
    <BLANKLINE>
    <BLANKLINE>


"""
import re
import sys

import pandas as pd  # type: ignore

from ...._internals.mixins import Params, ParamsMixin
from ....package_data.text_processing import internal__load_text_processing_terms
from ..._internals import (
    ThesaurusMixin,
    internal__generate_system_thesaurus_file_path,
    internal__generate_user_thesaurus_file_path,
    internal__load_reversed_thesaurus_as_mapping,
    internal__load_thesaurus_as_mapping,
    internal__print_thesaurus_header,
)

# names sorted by proirity
ABBR = [
    "Min",  # ministry, ministerio
    #
    "Univ.",
    "Universidad",
    "Universidade",
    "Universita",
    "Universitas",
    "Universitat",
    "Universite",
    "Universiteit",
    "Universiti",
    "Universitity",
    "University",
    #
    "Bank",
    "Banco",
    #
    "Academia",
    "Academy",
    #
    "AG",  # agency, agencia
    "Counc",  # council, concilio, consejo
    "Conc",  # concilio, consejo
    "Com",  # comission, comision
    "Consortium",
    "Academia",
    #
    "Centre",
    "Center",
    "Centro",
    #
    "Politecnico",
    "Polytechnic",
    "Politech",
    #
    "Hosp",  # hospital
    #
    "Assn",
    "Association",
    "Associacao",
    "Asociacion",
    "Asoc",  # asociacion
    "Autoridad",
    "Authority",
    "Autorite",
    "Fundacion",
    #
    "Soc",
    "Consor",
    "Co",
    "Org",
    "Inc",
    "Ltd",
    "Off",
    "Corp",
    "Gob",
    "Gov",
    "Found",
    "Fund",
    #
    "Inst",
    "Institute",
    "Instituto",
    "Institut",
    #
    "Hospital",
    "Hosp",
    #
    "Coll",
    "College",
    "Colegio",
    #
    "Sch",
    "School",
    "Ecole",
    "Escuela",
    "Escola",
    #
]


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
            sys.stderr.write(f"Creating thesaurus from '{field}' field\n")
            sys.stderr.write(f"  File : {truncated_path}\n")
            sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        if not self.params.quiet:

            sys.stderr.write(f"  {len(self.data_frame)} keys found\n")
            sys.stderr.write("  Thesaurus creation completed successfully\n\n")
            sys.stderr.flush()

            internal__print_thesaurus_header(self.thesaurus_path)

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__create_cleaned_value_column(self):
        self.data_frame["key"] = pd.NA
        self.data_frame["cleaned_value"] = self.data_frame["value"].copy()
        self.data_frame["cleaned_value"] = self.data_frame.cleaned_value.str.lower()
        self.data_frame["cleaned_value"] = self.data_frame.cleaned_value.str.normalize(
            "NFKD"
        )
        self.data_frame["cleaned_value"] = self.data_frame.cleaned_value.str.encode(
            "ascii", errors="ignore"
        )
        self.data_frame["cleaned_value"] = self.data_frame.cleaned_value.str.decode(
            "utf-8"
        )

    # -------------------------------------------------------------------------
    def internal__assign_names_for_known_organizations(self):

        known_names = internal__load_text_processing_terms("known_organizations.txt")
        for name in known_names:
            # escaped_name = re.escape(name)
            escaped_name = name
            self.data_frame.loc[
                self.data_frame.cleaned_value.str.contains(
                    escaped_name.lower(),
                    case=False,
                    regex=False,
                ),
                "key",
            ] = name

    # -------------------------------------------------------------------------
    def internal__assign_names_by_priority(self):

        def select_name(cleaned_value, raw_value):

            cleaned_parts = cleaned_value.split(",")
            raw_parts = raw_value.split(",")

            for abbr in ABBR:
                regex = r"\b" + abbr + r"\b"
                for cleaned_part, raw_part in zip(cleaned_parts, raw_parts):
                    if re.search(regex, cleaned_part, re.IGNORECASE):
                        return raw_part.strip()

            return pd.NA

        #
        # Main code:
        #
        for index, row in self.data_frame.iterrows():
            if not pd.isna(row.key):
                continue
            self.data_frame.loc[index, "key"] = select_name(
                row.cleaned_value,
                row.value,
            )

    # -------------------------------------------------------------------------
    def internal__assign_names_by_discard(self):
        for index, row in self.data_frame.iterrows():
            if not pd.isna(row.key):
                continue
            self.data_frame.loc[index, "key"] = (
                "[UKN] " + self.data_frame.loc[index, "value"]
            )

    # -------------------------------------------------------------------------
    # def internal__assign_new_keys_from_candiate_keys(self):
    #     self.data_frame["key"] = self.data_frame["candidate_key"]

    # -------------------------------------------------------------------------
    def internal__create_country_column(self):

        # loads the country thesaurus as a mapping
        params = Params().update(
            thesaurus_file="countries.the.txt",
            root_directory=self.params.root_directory,
        )
        file_path = internal__generate_user_thesaurus_file_path(params)
        mapping = internal__load_reversed_thesaurus_as_mapping(file_path)

        # adds a column with the country
        self.data_frame["country"] = self.data_frame["value"].apply(
            lambda x: mapping.get(x, "[UNKNOWN]")
        )

    # -------------------------------------------------------------------------
    def internal__transforms_country_to_alpha3_code(self):

        # loads the country to alpha3 code mapping
        file_path = internal__generate_system_thesaurus_file_path(
            "geography/country_to_alpha3.the.txt"
        )
        mapping = internal__load_thesaurus_as_mapping(file_path)

        # transforms the country to alpha3 code
        self.data_frame["country"] = self.data_frame["country"].apply(
            lambda x: mapping.get(x, ["UKN"])[0]
        )

    # -------------------------------------------------------------------------
    # def internal__repair_unknown_keys(self):

    #     self.data_frame.loc[self.data_frame.key.isna(), "key"] = self.data_frame.loc[
    #         self.data_frame.key.isna(), "value"
    #     ]

    # -------------------------------------------------------------------------
    def internal__adds_alpha3_to_key(self):
        self.data_frame["key"] = (
            self.data_frame["key"] + " (" + self.data_frame["country"] + ")"
        )

    # -------------------------------------------------------------------------
    def internal__replace_abbr_names_in_organizations(self):

        # loads the abbreviation thesaurus
        # loads the country thesaurus as a mapping
        file_path = internal__generate_system_thesaurus_file_path(
            "abbreviations/organizations_abbr.the.txt"
        )
        mapping = internal__load_thesaurus_as_mapping(file_path)

        # replaces the abbreviations
        for word, abbr in mapping.items():
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                r"\b" + word + r"\b", abbr[0].replace(".", ""), regex=True
            )

        # remove leading and trailing spaces
        self.data_frame["key"] = self.data_frame["key"].str.strip()

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.with_thesaurus_file("organizations.the.txt")
        self.with_field("affiliations")

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_filtered_records()
        self.internal__create_thesaurus_data_frame_from_field()
        #
        self.internal__create_cleaned_value_column()
        self.internal__assign_names_for_known_organizations()
        self.internal__assign_names_by_priority()
        self.internal__assign_names_by_discard()
        # self.internal__repair_unknown_keys()
        #
        self.internal__create_country_column()
        self.internal__transforms_country_to_alpha3_code()
        self.internal__adds_alpha3_to_key()
        #
        self.internal__replace_abbr_names_in_organizations()
        #
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()


# =============================================================================

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Initialize Thesaurus
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.countries import InitializeThesaurus

    >>> # Redirect stderr to capture output
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="example/", use_colorama=False).run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Initializing thesaurus from 'affiliations' field...
      File : example/data/thesaurus/countries.the.txt
      24 keys found
      Initialization process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/countries.the.txt
    <BLANKLINE>
        Australia
          Centre for Law, Markets & Regulation, UNSW Australia, Australia; Charles ...
        Belgium
          Brussels, Belgium
        Brunei Darussalam
          Universiti Brunei Darussalam, School of Business and Economics, Jln Tungk...
        China
          Cheung Kong Graduate School of Business, and Institute of Internet Financ...
        Denmark
          Copenhagen Business School, Department of IT Management, Howitzvej 60, Fr...
        France
          SKEMA Business School, Lille, France; University of Lille Nord de France,...
        Germany
          CESifo, Poschingerstr. 5, Munich, 81679, Germany; Chair of e-Finance, Goe...
        Ghana
          University of the Free State and University of Ghana Business School, Uni...
    <BLANKLINE>


"""
import sys

import pkg_resources  # type: ignore
from colorama import Fore, init

from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin, internal__print_thesaurus_header
from ..._internals.load_thesaurus_as_mapping import internal__load_thesaurus_as_mapping


class InitializeThesaurus(
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

            file_path = str(self.thesaurus_path)
            if len(file_path) > 72:
                file_path = "..." + file_path[-68:]

            if self.params.use_colorama:
                filename = str(file_path).split("/")[-1]
                file_path = file_path.replace(filename, f"{Fore.RESET}{filename}")
                file_path = Fore.LIGHTBLACK_EX + file_path

            sys.stderr.write(f"Initializing thesaurus from '{field}' field...\n")
            sys.stderr.write(f"  File : {file_path}\n")
            sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        if not self.params.quiet:

            sys.stderr.write(f"  {len(self.data_frame)} keys found\n")
            sys.stderr.write("  Initialization process completed successfully\n\n")
            sys.stderr.flush()

            internal__print_thesaurus_header(
                thesaurus_path=self.thesaurus_path,
                use_colorama=self.params.use_colorama,
            )

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__extract_country_from_affiliation(self):

        replacements = [
            ("Bosnia and Herz.", "Bosnia and Herzegovina"),
            ("Brasil", "Brazil"),
            ("Czech Republic", "Czechia"),
            ("Espana", "Spain"),
            ("Macao", "China"),
            ("Macau", "China"),
            ("N. Cyprus", "Cyprus"),
            ("Peoples R China", "China"),
            ("Rusia", "Russia"),
            ("Russian Federation", "Russia"),
            ("Syrian Arab Republic", "Syria"),
            ("United States of America", "United States"),
            ("USA", "United States"),
            ("Türkiye", "Turkey"),
            ("Viet-Nam", "Vietnam"),
            ("Viet Nam", "Vietnam"),
            ("Perú", "Peru"),
        ]

        # extracts the country as the last position of the string
        self.data_frame["key"] = (
            self.data_frame["key"].str.split(",").str[-1].str.strip()
        )

        # normalizes country names
        for pat, repl in replacements:
            self.data_frame["key"] = self.data_frame["key"].str.replace(
                pat, repl, regex=False
            )

        # loads country valid names
        file_path = pkg_resources.resource_filename(
            "techminer2",
            "package_data/thesaurus/geography/country_to_alpha3.the.txt",
        )
        mapping = internal__load_thesaurus_as_mapping(file_path)
        valid_names = list(mapping.keys())

        # checks the data frame
        self.data_frame["key"] = self.data_frame["key"].apply(
            lambda x: x if x in valid_names else "[UNKNWON]"
        )

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        #
        # SPECIFIC DATA:
        self.with_thesaurus_file("countries.the.txt")
        self.with_field("affiliations")

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_filtered_records()
        self.internal__create_thesaurus_data_frame_from_field()
        self.internal__extract_country_from_affiliation()
        self.internal__reduce_keys()
        self.internal__explode_and_group_values_by_key()
        self.internal__sort_data_frame_by_rows_and_key()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()


# =============================================================================

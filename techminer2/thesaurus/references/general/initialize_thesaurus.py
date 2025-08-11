# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Initialize thesaurus
===============================================================================

Example:
    >>> import sys
    >>> from io import StringIO
    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> from techminer2.thesaurus.references import InitializeThesaurus
    >>> InitializeThesaurus(root_directory = "examples/fintech/", tqdm_disable=True, use_colorama=False).run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Initializing thesaurus from 'global_references' field
      File : examples/fintech/data/thesaurus/references.the.txt
      Creating main_documents data frame
      Creating references data frame
      62 keys found
      Initialization process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/references.the.txt
    <BLANKLINE>
        Alt R., 2018, ELECTRON MARK, V28, P235
          Alt R., Beck R., Smits M.T., Fintech and the Transformation of the Financ...
        Anagnostopoulos I., 2018, J ECON BUS, V100, P7
          Anagnostopoulos, Ioannis, FinTech and RegTech: Impact on regulators and b...
        Arner D.W., 2017, NORTHWEST J INTL LAW BUS, V37, P373
          Arner D.W., Barberis J., Buckley R.P., Fintech, regtech, and the reconcep...
        Buchak G., 2018, J FINANC ECON, V130, P453
          Buchak G., Matvos G., Piskorski T., Seru A., Fintech, regulatory arbitrag...
        Cai C.W., 2018, ACCOUNT FINANC, V58, P965
          Cai C.W., Disruption of financial intermediation by FinTech: A review on ...
        Chen L., 2016, CHINA ECON J, V9, P225
          Chen L., From Fintech to Finlife: The case of Fintech development in Chin...
        Dorfleitner G., 2017, FINTECH IN GER, P1
          Dorfleitner G., Hornuf L., Schmitt M., Weber M., FinTech in Germany, (2017)
        Gabor D., 2017, NEW POLIT ECON, V22, P423
          Gabor D., Brooks S., The Digital Revolution in Financial Inclusion: Inter...
    <BLANKLINE>
    <BLANKLINE>





"""
import re
import sys

import pandas as pd  # type: ignore
from techminer2._internals.mixins import ParamsMixin
from techminer2.database._internals.io import (
    internal__load_all_records_from_database,  # type: ignore
)
from techminer2.database._internals.io import (
    internal__load_filtered_records_from_database,
)
from techminer2.thesaurus._internals import internal__print_thesaurus_header
from techminer2.thesaurus._internals import ThesaurusMixin
from textblob import Word  # type: ignore
from tqdm import tqdm

tqdm.pandas()


def clean_text(text):
    """:meta private:"""
    text = (
        text.str.lower()
        .str.replace(".", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.replace(":", "", regex=False)
        .str.replace("-", " ", regex=False)
        .str.replace("_", " ", regex=False)
        .str.replace("'", "", regex=False)
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
        .str.replace("  ", " ", regex=False)
    )
    return text


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
            truncated_path = str(self.thesaurus_path)
            if len(truncated_path) > 72:
                truncated_path = "..." + truncated_path[-68:]
            sys.stderr.write(f"Initializing thesaurus from '{field}' field\n")
            sys.stderr.write(f"  File : {truncated_path}\n")
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
    def internal__create_main_documents_data_frame(self):

        if not self.params.quiet:
            sys.stderr.write(f"  Creating main_documents data frame\n")
            sys.stderr.flush()

        # loads the dataframe
        main_documents = internal__load_filtered_records_from_database(self.params)
        main_documents = main_documents[main_documents.global_citations > 0]
        main_documents = main_documents[
            ["record_id", "document_title", "authors", "year"]
        ]
        main_documents = main_documents.dropna()

        # extracts the first author surname
        main_documents["first_author"] = (
            main_documents["authors"]
            .astype(str)
            .str.split(" ")
            .map(lambda x: x[0].lower())
        )

        # formats the document title field
        main_documents["document_title"] = (
            main_documents["document_title"].astype(str).str.lower()
        )
        main_documents["document_title"] = clean_text(main_documents["document_title"])

        # formats the authors field
        main_documents["authors"] = clean_text(main_documents["authors"])

        # formats the year field
        main_documents["year"] = main_documents["year"].astype(str)

        # sorts the dataframe
        main_documents = main_documents.sort_values(by=["record_id"])

        self.main_documents = main_documents

    # -------------------------------------------------------------------------
    def internal__create_references_data_frame(self):

        if not self.params.quiet:
            sys.stderr.write(f"  Creating references data frame\n")
            sys.stderr.flush()

        # loads the dataframe
        references = internal__load_all_records_from_database(self.params)
        references = references[["raw_global_references"]].dropna()
        references = references.rename({"raw_global_references": "text"}, axis=1)

        references["text"] = references["text"].str.split(";")
        references = references.explode("text")
        references["text"] = references["text"].str.strip()
        references = references.drop_duplicates()
        references = references.reset_index(drop=True)

        references["key"] = clean_text(references["text"])

        self.references = references

    # -------------------------------------------------------------------------
    def internal__create_thesaurus(self):

        thesaurus = {}
        for _, row in tqdm(
            self.main_documents.iterrows(),
            total=self.main_documents.shape[0],
            desc="  Homogenizing global references ",
            disable=self.params.tqdm_disable,
            ncols=80,
        ):

            refs = self.references.copy()

            # filters by first author
            refs = refs.loc[
                refs.key.str.lower().str.contains(row.first_author.lower()), :
            ]

            # filters by year
            refs = refs.loc[refs.key.str.lower().str.contains(row.year), :]

            # filters by document title
            refs = refs.loc[
                refs.key.str.lower().str.contains(
                    re.escape(row.document_title[:50].lower())
                ),
                :,
            ]

            if len(refs) > 0:
                thesaurus[row.record_id] = sorted(refs.text.tolist())
                self.references = self.references.drop(refs.index)

        self.data_frame = pd.DataFrame(
            {
                "key": list(thesaurus.keys()),
                "value": list(thesaurus.values()),
            }
        )

        self.data_frame = self.data_frame.explode("value")

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.params.update(
            thesaurus_file="references.the.txt",
            field="global_references",
        )

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__create_main_documents_data_frame()
        self.internal__create_references_data_frame()
        self.internal__create_thesaurus()
        self.internal__write_thesaurus_data_frame_to_disk()
        self.internal__notify_process_end()


# =============================================================================

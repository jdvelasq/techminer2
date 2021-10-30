"""
Scopus CSV importer.


"""
import pandas as pd
from techminer.utils import logging

from . import BaseImporter


class ScopusImporter(BaseImporter):
    """
    Importer for Scopus CSV files.

    """

    def __init__(self, source, filetype, directory):
        super().__init__(source, filetype, directory)
        self.tagsfile = "scopus2tags.csv"

    def extract_data(self):
        """
        Imports data from a Scopus CSV file.

        """
        logging.info(f"Reading file '{self.source}' ...")
        self.raw_data = pd.read_csv(
            self.source, encoding="utf-8", error_bad_lines=False
        )
        # on_bad_lines="skip")

    def format_authors(self):
        """
        Formats Authors into a common format.
        """

        if "authors" in self.raw_data.columns:
            logging.info("Formating authors ...")
            self.raw_data.authors = self.raw_data.authors.map(
                lambda x: pd.NA if x == "[No author name available]" else x
            )

            self.raw_data.authors = self.raw_data.authors.str.replace(
                ", ", "; ", regex=False
            )
            self.raw_data.authors = self.raw_data.authors.str.replace(
                ".", "", regex=False
            )

        if "authors_id" in self.raw_data.columns:
            logging.info("Formating authors_id ...")
            self.raw_data["authors_id"] = self.raw_data.authors_id.map(
                lambda w: pd.NA if w == "[No author id available]" else w
            )
            self.raw_data["authors_id"] = self.raw_data.authors_id.map(
                lambda x: x[:-1] if isinstance(x, str) and x[-1] == ";" else x
            )

            authors_ids = self.raw_data[["authors", "authors_id"]].dropna()
            authors_ids = {
                b: a for a, b in zip(authors_ids.authors, authors_ids.authors_id)
            }

            authors_ids = {
                k: list(zip(k.split(";"), v.split("; ")))
                for k, v in authors_ids.items()
            }
            authors_ids = {
                k: ["/".join([b, a]) for a, b in v] for k, v in authors_ids.items()
            }
            authors_ids = {k: "; ".join(v) for k, v in authors_ids.items()}

            self.raw_data["authors_id"] = self.raw_data.authors_id.map(
                lambda x: authors_ids[x] if x in authors_ids.keys() else x
            )

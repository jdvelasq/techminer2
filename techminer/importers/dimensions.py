"""
Dimensions.ai CSV Importer

"""
import pandas as pd
from techminer.utils import logging

from . import BaseImporter


class DimensionsImporter(BaseImporter):
    """
    Imports raw CSV from dimensions.ai


    """

    def __init__(self, source, filetype, directory):
        super().__init__(source, filetype, directory)
        self.tagsfile = "dimensions2tags.csv"

    def extract_data(self):
        """
        Imports data from a Dimensions CSV file.

        """
        self.raw_data = pd.read_csv(self.source, skiprows=1)

    def format_authors(self):
        """
        Formats Authors into a common format.

        """

        def format_authorslits(authorslist):

            authorslist = authorslist.split(";")
            authorslist = [author.strip() for author in authorslist]

            surnames = [
                author.split(",")[0] if "," in author else author.split(" ")[0]
                for author in authorslist
            ]
            names = [
                author.split(",")[1] if "," in author else author.split(" ")[0]
                for author in authorslist
            ]

            names = [name.strip() for name in names]
            names = [name.split() for name in names]
            names = [
                [name_part[0] for name_part in name] for name in names if len(name) > 0
            ]
            names = ["".join(part_name) for name in names for part_name in name]

            authorslist = [
                surname + " " + name for surname, name in zip(surnames, names)
            ]
            authorslist = "; ".join(authorslist)
            return authorslist

        if "authors" in self.raw_data.columns:
            self.raw_data.authors = self.raw_data.authors.apply(
                lambda x: format_authorslits(x) if not pd.isnull(x) else None,
            )

            logging.info("Removing [Anonymous]")
            self.raw_data.authors = self.raw_data.authors.map(
                lambda x: pd.NA if not pd.isna(x) and x == "[Anonymous]" else x
            )

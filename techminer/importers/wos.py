"""
Web of Science / Clarivate TXT importer.


"""
import pandas as pd

from . import BaseImporter

# from techminer.utils import logging


class WoSImporter(BaseImporter):
    """
    Web of Science importer.

    """

    def __init__(self, source, filetype, directory):
        super().__init__(source, filetype, directory)
        self.tagsfile = "wos2tags.csv"

    def extract_data(self):
        """
        Imports data from a WoS text file.

        """

        def load_wosrecords():
            records = []
            record = {}
            key = None
            value = []
            with open(self.source, "rt", encoding="utf-8") as file:
                for line in file:
                    line = line.replace("\n", "")
                    if line.strip() == "ER":
                        if len(record) > 0:
                            records.append(record)
                        record = {}
                        key = None
                        value = []
                    elif len(line) >= 2 and line[:2] == "  ":
                        line = line[2:]
                        line = line.strip()
                        value.append(line)

                    elif (
                        len(line) >= 2
                        and line[:2] != "  "
                        and line[:2] not in ["FN", "VR"]
                    ):
                        if key is not None:
                            record[key] = "; ".join(value)
                        key = line[:2].strip()
                        value = [line[2:].strip()]

            return records

        def wosrecords2df(wosrecords):
            pdf = pd.DataFrame()
            for record in wosrecords:
                record = {key: [value] for key, value in record.items()}
                row = pd.DataFrame(record)
                pdf = pd.concat(
                    [pdf, row],
                    ignore_index=True,
                )
            return pdf

        super().extract_data()
        self.raw_data = wosrecords2df(wosrecords=load_wosrecords())

    def format_authors(self):
        """

        Formats Authors into a common format.

        """
        if "authors" in self.raw_data.columns:
            self.raw_data.authors = self.raw_data.authors.str.replace(
                ",", "", regex=True
            )

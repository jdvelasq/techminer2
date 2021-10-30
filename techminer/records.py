"""
Record management

"""

from os.path import isfile

import pandas as pd

from .analysis import core_sources
from .features import (
    apply_institutions_thesaurus,
    apply_keywords_thesaurus,
    process_records,
)
from .importers import DimensionsImporter, ScopusImporter, WoSImporter
from .utils import describe_records, load_records, logging


def create_import_object(source, filetype, directory):
    """
    Creates an import object based on the filetype.

    """
    if filetype == "scopus":
        return ScopusImporter(source, filetype, directory)
    if filetype == "wos":
        return WoSImporter(source, filetype, directory)
    if filetype == "dimensions":
        return DimensionsImporter(source, filetype, directory)
    raise NotImplementedError


class Records:
    """
    Manage records directory.

    """

    def __init__(self, directory) -> None:
        """
        Manage records directory.

        :param directory:
        """
        if directory[-1] != "/":
            directory += "/"
        self.directory = directory

    def import_records(self, source, filetype):
        """
        Read Scopus records.

        :param filetype:
        :param source:
        :return:
        """
        if isfile(source):
            create_import_object(source, filetype, self.directory).run()
            logging.info(
                f"The file '{source}' was successfully imported. Process finished!"
            )
        else:
            raise FileNotFoundError

    def process_records(self):
        """
        Consolidate records for analysis.


        """
        process_records(self.directory)
        logging.info("Applying thesaurus ...")
        apply_institutions_thesaurus(self.directory)
        apply_keywords_thesaurus(self.directory)
        logging.info("Processing records finished!")

    def coverage(self):
        """
        Coverage report.

        :return:
        """
        records = load_records(self.directory)
        columns = sorted(records.columns)
        n_records = len(records)
        coverage_ = pd.DataFrame(
            {
                "column": columns,
                "number of items": [
                    n_records - records[col].isnull().sum() for col in columns
                ],
                "coverage (%)": [
                    "{:5.2%}".format(
                        (n_records - records[col].isnull().sum()) / n_records
                    )
                    for col in columns
                ],
            }
        )

        return coverage_

    def describe(self):
        """
        Describe records.

        :return:
        """
        return describe_records(self.directory)

    def clean_institutions(self):
        """
        Clean institutions.

        :return:
        """
        apply_keywords_thesaurus(directory=self.directory)

    def clean_keywords(self):
        """
        Clean leywords.

        :return:
        """
        apply_institutions_thesaurus(directory=self.directory)

    def core_sources(self):
        """
        Core sources analysis.

        :return:
        """
        return core_sources(directory=self.directory)

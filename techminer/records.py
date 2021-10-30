"""
Record management

"""

from os.path import isfile

from .importers import DimensionsImporter, ScopusImporter, WoSImporter
from .utils import logging


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
    def __init__(self, directory) -> None:
        """
        Manage records directory.

        :param directory:
        """
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
            logging.info(f"The file '{source}' was successfully imported.")
        else:
            raise FileNotFoundError

import logging
from os.path import isfile

import pandas as pd


class DatastoreTransformations:
    """
    This class is used to transform the data from the datastore
    """

    def __init__(self, datastorepath="./"):
        """
        This method is used to initialize the class
        :param datastorepath:
        :return:
        """
        self.datastore = None
        self.datastorepath = datastorepath
        if self.datastorepath[-1] != "/":
            self.datastorepath += "/"

    def load_datastore(self):
        """
        Loads datastore.

        """
        filename = self.datastorepath + "datastore.csv"
        logging.info("Loading datastore from %s", filename)
        if isfile(filename):
            self.datastore = pd.read_csv(filename, sep=",", encoding="utf-8")
        else:
            self.datastore = pd.DataFrame()

    def save_datastore(self):
        """
        Saves datastore.

        """
        filename = self.datastorepath + "datastore.csv"
        logging.info("Saving datastore to %s", filename)
        self.datastore.to_csv(filename, sep=",", encoding="utf-8")


def process_datastore(datastorepath="./"):
    """
    This method is used to process the datastore

    :param datastorepath:
    :return:
    """
    datastore = DatastoreTransformations(datastorepath)
    datastore.load_datastore()

    datastore.save_datastore()

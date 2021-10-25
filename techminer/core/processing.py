import logging
import unicodedata
from os.path import isfile

import pandas as pd


def strip_accents(text):
    try:
        text = unicode(text, "utf-8")
    except NameError:  # unicode is a default on python 3
        pass

    if isinstance(text, str):
        text = (
            unicodedata.normalize("NFD", text).encode("ascii", "ignore").decode("utf-8")
        )
        return str(text)

    return text


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

    def strip_accents(self):
        """
        Strips accents from the dataframe.

        """
        logging.info("Replacing accents")
        self.datastore.applymap(strip_accents, na_action="ignore")

    def replace_invalid_author_name(self):
        """
        Replaces no author name with "Unknown"

        """
        logging.info("Removing invalid author names")
        self.datastore.replace(
            to_replace="[No author name available]", value=None, inplace=True
        )
        self.datastore.replace(to_replace="[Anonymous]", value=None, inplace=True)

    def count_num_authors_per_document(self):
        """
        Counts the number of authors per document

        """
        logging.info("Counting number of authors")
        self.datastore["num_authors"] = self.datastore.authors.apply(
            lambda x: len(x.split(";")) if not pd.isna(x) else 0
        )

    def remove_copyright(self):
        """
        Removes copyright text from abstracts.

        """
        if "abstract" in self.datastore.columns:
            logging.info("Removing copyright")
            self.datastore.abstract = self.datastore.abstract.map(
                lambda x: x[0 : x.find("\u00a9")] if not pd.isna(x) else x
            )

    def format_keywords(self):
        """
        Formats keywords.

        """
        logging.info("Formatting keywords")
        for keywords in ["author_keywords", "index_keywords"]:
            self.datastore[keywords] = self.datastore[keywords].map(
                lambda x: x.replace("; ", "; ") if not pd.isna(x) else x
            )
            self.datastore[keywords] = self.datastore[keywords].str.lower()

    def clean_document_title(self):
        """
        Cleans document title.

        """
        logging.info("Cleaning document title")
        self.datastore.document_title = self.datastore.document_title.map(
            lambda x: x[0 : x.find("[")] if pd.isna(x) is False and x[-1] == "]" else x
        )

    def fill_na_with_zero_in_global_citations(self):
        """
        Fills na with zero in global citations.

        """
        if "global_citations" in self.datastore.columns:
            logging.info("Filling na with zero in global citations")
            self.datastore.global_citations = self.datastore.global_citations.fillna(0)
            self.datastore.global_citations = self.datastore.global_citations.astype(
                int
            )


def process_datastore(datastorepath="./"):
    """
    This method is used to process the datastore

    :param datastorepath:
    :return:
    """
    datastore = DatastoreTransformations(datastorepath)
    datastore.load_datastore()
    datastore.strip_accents()
    datastore.replace_invalid_author_name()
    datastore.count_num_authors_per_document()
    datastore.remove_copyright()
    datastore.format_keywords()
    datastore.clean_document_title()
    datastore.fill_na_with_zero_in_global_citations()
    datastore.save_datastore()

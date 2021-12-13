"""
User Filters
===============================================================================

Allow users to select docuemnts to be mined.

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> user_filters(directory)
---< Document >-------------------------------------------------
               First year : 2022
                Last year : 2015
         Global citations : 201
---< User Filters >---------------------------------------------
               First year : 2015
                Last year : 2022
            Min citations : 0
            Max citations : 201
           Bradford zones : 3
  Selected document types : article
                          : book
                          : book_chapter
                          : conference_paper
                          : editorial
                          : erratum
                          : letter
                          : note
                          : review
                          : short_survey
>>> user_filters(directory, erratum=False,  letter=False, first_year=2016, last_year=2020)
---< Document >-------------------------------------------------
               First year : 2022
                Last year : 2015
         Global citations : 201
---< User Filters >---------------------------------------------
               First year : 2016
                Last year : 2020
            Min citations : 0
            Max citations : 201
           Bradford zones : 3
  Selected document types : article
                          : book
                          : book_chapter
                          : conference_paper
                          : editorial
                          : note
                          : review
                          : short_survey
 Discarded document types : erratum
                          : letter

"""
import os

import pandas as pd
import yaml

from .utils import load_filtered_documents, logging


def _load_filter(directory):
    yaml_filename = directory + "filter.yaml"
    with open(yaml_filename, "r", encoding="utf-8") as yaml_file:
        filter = yaml.load(yaml_file, Loader=yaml.FullLoader)
    return filter


class _UserFilters:
    def __init__(self, directory=None, kwargs=None):
        if directory is None:
            directory = "/workspaces/techminer-api/tests/data/"
            logging.info(" **** USING SAMPLE DATA ****")
        self.directory = directory
        if kwargs is None:
            kwargs = {}
        self.kwargs = kwargs
        self.filter = _load_filter(directory)
        self.load_raw_documents()

    def load_raw_documents(self):
        filename = self.directory + "documents.csv"
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"The file '{filename}' does not exist.")
        self.documents = pd.read_csv(filename, sep=",", encoding="utf-8")

    def document_report(self):

        # years
        first_year = self.documents["pub_year"].max()
        last_year = self.documents["pub_year"].min()

        # global citations
        citations = self.documents["global_citations"].max()

        # report
        print("---< Document >-------------------------------------------------")
        print("               First year : " + str(first_year))
        print("                Last year : " + str(last_year))
        print("         Global citations : " + str(citations))

    def user_report(self):
        first_year, last_year = self.filter["first_year"], self.filter["last_year"]
        min_citations, max_citations = (
            self.filter["min_citations"],
            self.filter["max_citations"],
        )
        bradford = self.filter["bradford"]
        selected_document_types = [
            key
            for key, value in self.filter.items()
            if isinstance(value, bool) and value is True
        ]
        discarded_document_types = [
            key
            for key, value in self.filter.items()
            if isinstance(value, bool) and value is False
        ]

        print("---< User Filters >---------------------------------------------")
        print("               First year : " + str(first_year))
        print("                Last year : " + str(last_year))
        print("            Min citations : " + str(min_citations))
        print("            Max citations : " + str(max_citations))
        print("           Bradford zones : " + str(bradford))
        if len(selected_document_types) > 0:
            print("  Selected document types : " + selected_document_types[0])
            for document_type in selected_document_types[1:]:
                print("                          : " + document_type)
        if len(discarded_document_types) > 0:
            print(" Discarded document types : " + discarded_document_types[0])
            for document_type in discarded_document_types[1:]:
                print("                          : " + document_type)

    def save_filter(self):
        yaml_filename = os.path.join(self.directory, "filter.yaml")
        with open(yaml_filename, "wt", encoding="utf-8") as yaml_file:
            yaml.dump(self.filter, yaml_file, sort_keys=True)

    def run(self):
        if len(self.kwargs) > 0:
            for key, value in self.kwargs.items():
                if key in self.filter:
                    self.filter[key] = value
                else:
                    raise ValueError(f"The filter '{key}' does not exist.")
        self.document_report()
        self.user_report()
        self.save_filter()


def user_filters(directory=None, **kwargs):
    user_filters_ = _UserFilters(directory, kwargs)
    user_filters_.run()

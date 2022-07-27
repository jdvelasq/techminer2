"""
User Filters
===============================================================================

Allow users to select docuemnts to be mined.

>>> directory = "data/regtech/"

>>> from techminer2 import tm2__user_filters
>>> tm2__user_filters(directory, book=True,  erratum=True, first_year=2016, last_year=2021)
---< Document >-------------------------------------------------
               First year : 2016
                Last year : 2021
         Global citations : 220
---< User Filters >---------------------------------------------
               First year : 2016
                Last year : 2021
            Min citations : 0
            Max citations : 220
           Bradford zones : 3
  Selected document types : article
                          : book
                          : book_chapter
                          : conference_paper
                          : editorial
                          : erratum
                          : note
                          : review
                          : short_survey

>>> user_filters(directory)
---< Document >-------------------------------------------------
               First year : 2016
                Last year : 2021
         Global citations : 220
---< User Filters >---------------------------------------------
               First year : 2016
                Last year : 2021
            Min citations : 0
            Max citations : 220
           Bradford zones : 3
  Selected document types : article
                          : book
                          : book_chapter
                          : conference_paper
                          : editorial
                          : erratum
                          : note
                          : review
                          : short_survey

>>> user_filters(directory, book=False,  erratum=False, first_year=2017, last_year=2020)
---< Document >-------------------------------------------------
               First year : 2016
                Last year : 2021
         Global citations : 220
---< User Filters >---------------------------------------------
               First year : 2017
                Last year : 2020
            Min citations : 0
            Max citations : 220
           Bradford zones : 3
  Selected document types : article
                          : book_chapter
                          : conference_paper
                          : editorial
                          : note
                          : review
                          : short_survey
 Discarded document types : book
                          : erratum



>>> user_filters(directory, book=True,  erratum=True, first_year=2016, last_year=2021)
---< Document >-------------------------------------------------
               First year : 2016
                Last year : 2021
         Global citations : 220
---< User Filters >---------------------------------------------
               First year : 2016
                Last year : 2021
            Min citations : 0
            Max citations : 220
           Bradford zones : 3
  Selected document types : article
                          : book
                          : book_chapter
                          : conference_paper
                          : editorial
                          : erratum
                          : note
                          : review
                          : short_survey



"""
import os
import os.path

import yaml


def _load_filter(directory):

    yaml_filename = os.path.join(directory, "processed", "filter.yaml")
    with open(yaml_filename, "r", encoding="utf-8") as yaml_file:
        filter = yaml.load(yaml_file, Loader=yaml.FullLoader)
    return filter


class _UserFilters:
    def __init__(self, directory=None, quiet=True, kwargs=None):
        # if directory is None:
        #     directory = "/workspaces/techminer-api/tests/data/"
        #     logging.info(" **** USING SAMPLE DATA ****")
        self.directory = directory
        if kwargs is None:
            kwargs = {}
        self.quiet = quiet
        self.kwargs = kwargs
        self.filter = _load_filter(directory)
        self.load_raw_documents()

    def load_raw_documents(self):
        self.documents = read_all_records(self.directory)

    def document_report(self):

        # years
        first_year = self.documents["pub_year"].min()
        last_year = self.documents["pub_year"].max()

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
        yaml_filename = os.path.join(self.directory, "processed", "filter.yaml")
        with open(yaml_filename, "wt", encoding="utf-8") as yaml_file:
            yaml.dump(self.filter, yaml_file, sort_keys=True)

    def run(self):
        if len(self.kwargs) > 0:
            for key, value in self.kwargs.items():
                if key in self.filter:
                    self.filter[key] = value
                else:
                    raise ValueError(f"The filter '{key}' does not exist.")
        if self.quiet is False:
            self.document_report()
            self.user_report()
        self.save_filter()


def tm2__user_filters(
    directory="./",
    quiet=False,
    **kwargs,
):
    """Data filtering."""

    user_filters_ = _UserFilters(directory=directory, quiet=quiet, kwargs=kwargs)
    user_filters_.run()

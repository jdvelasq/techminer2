"""
Main information
===============================================================================

>>> from techminer2.bibliometrix import *
>>> directory = "data/"
>>> main_information(directory)
                                                            Value
Category       Item                                              
GENERAL        Timespan                                 2016:2021
               Documents                                      248
               Annual growth rate %                         91.68
               Document average age                          2.23
               References                                   12836
               Average citations per document                9.36
               Average citations per document per year       1.56
               Average references per document              53.93
               Sources                                        145
               Average documents per source                  1.71
DOCUMENT TYPES article                                        178
               book                                             1
               book_chapter                                     4
               conference_paper                                31
               editorial                                       10
               erratum                                          3
               note                                             1
               review                                          19
               short_survey                                     1
AUTHORS        Authors                                      639.0
               Authors of single-authored documents          48.0
               Single-authored documents                     54.0
               Multi-authored documents                     192.0
               Authors per document                          2.75
               Co-authors per document                       3.28
               International co-authorship %                33.61
               Author appearances                           682.0
               Documents per author                          0.36
               Collaboration index                            1.0
               Institutions                                 382.0
               Institutions (1st author)                    200.0
               Countries                                     70.0
               Countries (1st author)                        53.0
KEYWORDS       Raw author keywords                            709
               Cleaned author keywords                        659
               Raw index keywords                             607
               Cleaned index keywords                         583


"""
import datetime

import numpy as np
import pandas as pd

from ._read_records import read_filtered_records


class _MainInformation:
    def __init__(self, directory):
        self.directory = directory
        self.records = read_filtered_records(directory)
        self.n_records = len(self.records)
        self.compute_general_information_stats()
        self.compute_document_types_stats()
        self.compute_authors_stats()
        self.compute_keywords_stats()
        self.make_report()

    def make_report(self):
        pdf = pd.concat(
            [
                self.general_information_stats,
                self.document_types_stats,
                self.authors_stats,
                self.keywords_stats,
            ]
        )
        index = pd.MultiIndex.from_arrays(
            [pdf.Category, pdf.Item], names=["Category", "Item"]
        )
        self.report_ = pd.DataFrame(pdf.Value.tolist(), columns=["Value"], index=index)

    #####################################################################################
    def compute_general_information_stats(self):
        self.general_information_stats = pd.DataFrame(
            columns=["Category", "Item", "Value"]
        )
        self.general_information_stats.loc[0] = [
            "GENERAL",
            "Timespan",
            self.compute_timespam(),
        ]
        self.general_information_stats.loc[1] = [
            "GENERAL",
            "Documents",
            self.documents(),
        ]
        self.general_information_stats.loc[2] = [
            "GENERAL",
            "Annual growth rate %",
            self.annual_growth_rate(),
        ]
        self.general_information_stats.loc[3] = [
            "GENERAL",
            "Document average age",
            self.document_average_age(),
        ]
        self.general_information_stats.loc[4] = [
            "GENERAL",
            "References",
            self.cited_references(),
        ]
        self.general_information_stats.loc[5] = [
            "GENERAL",
            "Average citations per document",
            self.average_citations_per_document(),
        ]
        self.general_information_stats.loc[6] = [
            "GENERAL",
            "Average citations per document per year",
            self.average_citations_per_document_per_year(),
        ]
        self.general_information_stats.loc[7] = [
            "GENERAL",
            "Average references per document",
            self.average_references_per_document(),
        ]
        self.general_information_stats.loc[8] = [
            "GENERAL",
            "Sources",
            self.sources(),
        ]
        self.general_information_stats.loc[9] = [
            "GENERAL",
            "Average documents per source",
            self.average_documents_per_source(),
        ]

    # -----------------------------------------------------------------------------------

    def compute_timespam(self):
        return str(min(self.records.year)) + ":" + str(max(self.records.year))

    def documents(self):
        return len(self.records)

    def annual_growth_rate(self):
        n_years = max(self.records.year) - min(self.records.year) + 1
        Po = len(self.records.year[self.records.year == min(self.records.year)])
        return round(100 * (np.power(self.n_records / Po, 1 / n_years) - 1), 2)

    def document_average_age(self):
        mean_years = self.records.year.copy()
        mean_years = mean_years.dropna()
        mean_years = mean_years.mean()
        current_year = datetime.datetime.now().year
        return round(int(current_year) - mean_years, 2)

    def cited_references(self):
        if "global_references" in self.records.columns:
            records = self.records.global_references.copy()
            records = records.dropna()
            records = records.str.split(";")
            records = records.explode()
            records = records.str.strip()
            return len(records)
        else:
            return pd.NA

    def average_citations_per_document(self):
        if "global_citations" in self.records.columns:
            return round(self.records.global_citations.mean(), 2)
        else:
            return pd.NA

    def average_citations_per_document_per_year(self):
        if "global_citations" in self.records.columns:
            return round(
                self.records.global_citations.mean()
                / (self.records.year.max() - self.records.year.min() + 1),
                2,
            )
        else:
            return pd.NA

    def average_references_per_document(self):
        if "global_references" in self.records.columns:
            num_references = self.records.global_references.copy()
            num_references = num_references.dropna()
            num_references = num_references.str.split(";")
            num_references = num_references.map(len)
            return round(num_references.mean(), 2)
        else:
            return pd.NA

    def sources(self):
        if "source_name" in self.records.columns:
            records = self.records.source_name.copy()
            records = records.dropna()
            records = records.drop_duplicates()
            return len(records)
        else:
            return pd.NA

    def average_documents_per_source(self):
        if "source_name" in self.records.columns:
            sources = self.records.source_name.copy()
            sources = sources.dropna()
            n_records = len(sources)
            sources = sources.drop_duplicates()
            n_sources = len(sources)
            return round(n_records / n_sources, 2)
        else:
            return pd.NA

    #####################################################################################
    def compute_document_types_stats(self):
        self.document_types_stats = pd.DataFrame(columns=["Category", "Item", "Value"])
        records = self.records[["document_type"]].dropna()
        document_types_count = (
            records[["document_type"]].groupby("document_type").size()
        )
        for index, (document_type, count) in enumerate(
            zip(document_types_count.index, document_types_count)
        ):
            self.document_types_stats.loc[index] = [
                "DOCUMENT TYPES",
                document_type,
                count,
            ]

    #####################################################################################
    def compute_authors_stats(self):
        self.authors_stats = pd.DataFrame(columns=["Category", "Item", "Value"])
        self.authors_stats.loc[0] = [
            "AUTHORS",
            "Authors",
            self.authors(),
        ]
        self.authors_stats.loc[1] = [
            "AUTHORS",
            "Authors of single-authored documents",
            self.authors_of_single_authored_documents(),
        ]
        self.authors_stats.loc[2] = [
            "AUTHORS",
            "Single-authored documents",
            self.count_single_authored_documents(),
        ]
        self.authors_stats.loc[3] = [
            "AUTHORS",
            "Multi-authored documents",
            self.count_multi_authored_documents(),
        ]
        self.authors_stats.loc[4] = [
            "AUTHORS",
            "Authors per document",
            self.average_authors_per_document(),
        ]
        self.authors_stats.loc[5] = [
            "AUTHORS",
            "Co-authors per document",
            self.co_authors_per_document(),
        ]
        self.authors_stats.loc[6] = [
            "AUTHORS",
            "International co-authorship %",
            self.international_co_authorship(),
        ]
        self.authors_stats.loc[7] = [
            "AUTHORS",
            "Author appearances",
            self.author_appearances(),
        ]
        self.authors_stats.loc[8] = [
            "AUTHORS",
            "Documents per author",
            self.average_documents_per_author(),
        ]

        self.authors_stats.loc[9] = [
            "AUTHORS",
            "Collaboration index",
            self.collaboration_index(),
        ]
        self.authors_stats.loc[10] = [
            "AUTHORS",
            "Institutions",
            self.institutions(),
        ]
        self.authors_stats.loc[11] = [
            "AUTHORS",
            "Institutions (1st author)",
            self.institutions_1st_author(),
        ]
        self.authors_stats.loc[12] = [
            "AUTHORS",
            "Countries",
            self.countries(),
        ]
        self.authors_stats.loc[13] = [
            "AUTHORS",
            "Countries (1st author)",
            self.countries_1st_author(),
        ]

    # -----------------------------------------------------------------------------------

    def authors(self):
        records = self.records.authors.copy()
        records = records.dropna()
        records = records.str.split(";")
        records = records.explode()
        records = records.str.strip()
        records = records.drop_duplicates()
        return len(records)

    def authors_of_single_authored_documents(self):
        records = self.records[self.records["num_authors"] == 1]
        authors = records.authors.dropna()
        authors = authors.drop_duplicates()
        return len(authors)

    def count_single_authored_documents(self):
        return len(self.records[self.records["num_authors"] == 1])

    def count_multi_authored_documents(self):
        return len(self.records[self.records["num_authors"] > 1])

    def average_authors_per_document(self):
        num_authors = self.records["num_authors"].dropna()
        return round(num_authors.mean(), 2)

    def co_authors_per_document(self):
        records = self.records.copy()
        num_authors = records[records.num_authors > 1].num_authors
        return round(num_authors.mean(), 2)

    def international_co_authorship(self):
        countries = self.records.countries.copy()
        countries = countries.dropna()
        countries = countries.str.split(";")
        countries = countries.map(len)
        return round(len(countries[countries > 1]) / len(countries) * 100, 2)

    def author_appearances(self):
        records = self.records.authors.copy()
        records = records.dropna()
        records = records.str.split(";")
        records = records.explode()
        records = records.str.strip()
        return len(records)

    def average_documents_per_author(self):
        records = self.records.authors.copy()
        records = records.dropna()
        n_records = len(records)
        records = records.str.split(";")
        records = records.explode()
        n_authors = len(records)
        return round(n_records / n_authors, 2)

    def collaboration_index(self):
        records = self.records[["authors", "num_authors"]].copy()
        records = records.dropna()
        records = records[records.num_authors > 1]
        n_records = len(records)

        n_authors = records.authors.copy()
        n_authors = n_authors.str.split(";")
        n_authors = n_authors.explode()
        n_authors = len(records)
        return round(n_authors / n_records, 2)

    def institutions(self):
        if "institutions" in self.records.columns:
            records = self.records.institutions.copy()
            records = records.dropna()
            records = records.str.split(";")
            records = records.explode()
            records = records.str.strip()
            records = records.drop_duplicates()
            return len(records)
        else:
            return pd.NA

    def institutions_1st_author(self):
        if "institution_1st_author" in self.records.columns:
            records = self.records.institution_1st_author.copy()
            records = records.dropna()
            records = records.str.split(";")
            records = records.explode()
            records = records.str.strip()
            records = records.drop_duplicates()
            return len(records)
        else:
            return pd.NA

    def countries(self):
        if "countries" in self.records.columns:
            records = self.records.countries.copy()
            records = records.dropna()
            records = records.str.split(";")
            records = records.explode()
            records = records.str.strip()
            records = records.drop_duplicates()
            return len(records)
        else:
            return pd.NA

    def countries_1st_author(self):
        if "country_1st_author" in self.records.columns:
            records = self.records.country_1st_author.copy()
            records = records.dropna()
            records = records.str.split(";")
            records = records.explode()
            records = records.str.strip()
            records = records.drop_duplicates()
            return len(records)
        else:
            return pd.NA

    #####################################################################################
    def compute_keywords_stats(self):
        self.keywords_stats = pd.DataFrame(columns=["Category", "Item", "Value"])
        self.keywords_stats.loc[0] = [
            "KEYWORDS",
            "Raw author keywords",
            self.raw_author_keywords(),
        ]
        self.keywords_stats.loc[1] = [
            "KEYWORDS",
            "Cleaned author keywords",
            self.author_keywords(),
        ]
        self.keywords_stats.loc[2] = [
            "KEYWORDS",
            "Raw index keywords",
            self.raw_index_keywords(),
        ]
        self.keywords_stats.loc[3] = [
            "KEYWORDS",
            "Cleaned index keywords",
            self.index_keywords(),
        ]

    # -----------------------------------------------------------------------------------

    def raw_author_keywords(self):
        records = self.records.raw_author_keywords.copy()
        records = records.dropna()
        records = records.str.split(";")
        records = records.explode()
        records = records.str.strip()
        records = records.drop_duplicates()
        return len(records)

    def author_keywords(self):
        records = self.records.author_keywords.copy()
        records = records.dropna()
        records = records.str.split(";")
        records = records.explode()
        records = records.str.strip()
        records = records.drop_duplicates()
        return len(records)

    def raw_index_keywords(self):
        records = self.records.raw_index_keywords.copy()
        records = records.dropna()
        records = records.str.split(";")
        records = records.explode()
        records = records.str.strip()
        records = records.drop_duplicates()
        return len(records)

    def index_keywords(self):
        records = self.records.index_keywords.copy()
        records = records.dropna()
        records = records.str.split(";")
        records = records.explode()
        records = records.str.strip()
        records = records.drop_duplicates()
        return len(records)


def main_information(directory="./"):
    """Returns main statistics of the dataset."""

    main_information = _MainInformation(directory)
    return main_information.report_

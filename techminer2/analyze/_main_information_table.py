# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Main Information Table."""

import datetime

import numpy as np
import pandas as pd

from .._read_records import read_records


class MainInformation:
    """Main information about the dataset.

    :meta private:
    """

    def __init__(self, records):
        """Constructor"""

        #
        # PARAMETERS:
        #
        self.records = records.copy()

        #
        # COMPUATIONS:
        #
        self.n_records = len(self.records)

        self.category = []
        self.item = []
        self.value = []

        self.frame = pd.DataFrame()

        self.__compute_general_information_stats()
        self.__compute_document_types_stats()
        self.__compute_authors_stats()
        self.__compute_keywords_stats()
        self.__compute_nlp_phrases_stats()
        self.__compute_descriptors_stats()
        self.__make_report()

    #
    #
    # INTERNAL METHODS
    #
    #

    def __make_report(self):
        """Make a report of the statistics."""

        frame = pd.DataFrame(
            {
                "Category": self.category,
                "Item": self.item,
                "Value": self.value,
            }
        )
        frame = frame.set_index(["Category", "Item"])
        self.frame = frame

    def insert_stats(self, category, item, value):
        """Inserts stats"""

        self.category.append(category)
        self.item.append(item)
        self.value.append(value)

    def count_unique_items(self, field):
        """Computes the number of unique items in a field."""

        if field not in self.records:
            return 0

        records = self.records[field].copy()
        records = records.dropna()
        records = records.str.split(";")
        records = records.explode()
        records = records.str.strip()
        records = records.drop_duplicates()

        return len(records)

    #
    #
    # COMPUTE GENERAL STATS
    #
    #
    def __compute_general_information_stats(self):
        """Compute general information statistics."""

        self.insert_stats(
            "GENERAL",
            "Timespan",
            self.compute_timespam(),
        )

        self.insert_stats(
            "GENERAL",
            "Documents",
            len(self.records),
        )

        self.insert_stats(
            "GENERAL",
            "Annual growth rate %",
            self.annual_growth_rate(),
        )

        self.insert_stats(
            "GENERAL",
            "Document average age",
            self.document_average_age(),
        )

        self.insert_stats(
            "GENERAL",
            "References",
            self.cited_references(),
        )
        self.insert_stats(
            "GENERAL",
            "Average citations per document",
            self.average_citations_per_document(),
        )

        self.insert_stats(
            "GENERAL",
            "Average citations per document per year",
            self.average_citations_per_document_per_year(),
        )

        self.insert_stats(
            "GENERAL",
            "Average references per document",
            self.average_references_per_document(),
        )

        self.insert_stats(
            "GENERAL",
            "Sources",
            self.sources(),
        )

        self.insert_stats(
            "GENERAL",
            "Average documents per source",
            self.average_documents_per_source(),
        )

    def compute_timespam(self):
        """Computes the timespan of the records"""
        return str(min(self.records.year)) + ":" + str(max(self.records.year))

    def annual_growth_rate(self):
        """Computes the annual growth rate"""
        n_years = max(self.records.year) - min(self.records.year) + 1
        po_ = len(self.records.year[self.records.year == min(self.records.year)])
        return round(100 * (np.power(self.n_records / po_, 1 / n_years) - 1), 2)

    def document_average_age(self):
        """Computes the average age of the documents"""
        mean_years = self.records.year.copy()
        mean_years = mean_years.dropna()
        mean_years = mean_years.mean()
        current_year = datetime.datetime.now().year
        return round(int(current_year) - mean_years, 2)

    def cited_references(self):
        """Computes the number of cited references"""
        if "global_references" in self.records.columns:
            records = self.records.global_references.copy()
            records = records.dropna()
            records = records.str.split(";")
            records = records.explode()
            records = records.str.strip()
            return len(records)
        return pd.NA

    def average_citations_per_document(self):
        """Computes the average number of citations per document"""
        if "global_citations" in self.records.columns:
            return round(self.records.global_citations.mean(), 2)
        return pd.NA

    def average_citations_per_document_per_year(self):
        """Computes the average number of citations per document per year"""
        if "global_citations" in self.records.columns:
            return round(
                self.records.global_citations.mean()
                / (self.records.year.max() - self.records.year.min() + 1),
                2,
            )
        return pd.NA

    def average_references_per_document(self):
        """Computes the average number of references per document"""

        if "global_references" in self.records.columns:
            num_references = self.records.global_references.copy()
            num_references = num_references.dropna()
            num_references = num_references.str.split(";")
            num_references = num_references.map(len)
            return round(num_references.mean(), 2)
        return pd.NA

    def sources(self):
        """Computes the number of sources"""
        if "source_title" in self.records.columns:
            records = self.records.source_title.copy()
            records = records.dropna()
            records = records.drop_duplicates()
            return len(records)
        return pd.NA

    def average_documents_per_source(self):
        """Computes the average number of documents per source"""
        if "source_title" in self.records.columns:
            sources = self.records.source_title.copy()
            sources = sources.dropna()
            n_records = len(sources)
            sources = sources.drop_duplicates()
            n_sources = len(sources)
            return round(n_records / n_sources, 2)
        return pd.NA

    #
    #
    # COMPUTE DOCUMENT TYPE STATS
    #
    #
    def __compute_document_types_stats(self):
        """Computes the document types statistics"""

        records = self.records[["document_type"]].dropna()

        document_types_count = records[["document_type"]].groupby("document_type").size()

        for document_type, count in zip(document_types_count.index, document_types_count):
            self.insert_stats(
                "DOCUMENT TYPES",
                document_type,
                count,
            )

    #
    #
    # COMPUTE AUTHOR STATS
    #
    #
    def __compute_authors_stats(self):
        """Computes the authors statistics"""

        self.insert_stats(
            "AUTHORS",
            "Authors",
            self.count_unique_items("authors"),
        )

        self.insert_stats(
            "AUTHORS",
            "Authors of single-authored documents",
            self.authors_of_single_authored_documents(),
        )

        self.insert_stats(
            "AUTHORS",
            "Single-authored documents",
            self.count_single_authored_documents(),
        )

        self.insert_stats(
            "AUTHORS",
            "Multi-authored documents",
            self.count_multi_authored_documents(),
        )
        self.insert_stats(
            "AUTHORS",
            "Authors per document",
            self.average_authors_per_document(),
        )
        self.insert_stats(
            "AUTHORS",
            "Co-authors per document",
            self.co_authors_per_document(),
        )

        self.insert_stats(
            "AUTHORS",
            "International co-authorship %",
            self.international_co_authorship(),
        )

        self.insert_stats(
            "AUTHORS",
            "Author appearances",
            self.author_appearances(),
        )
        self.insert_stats(
            "AUTHORS",
            "Documents per author",
            self.average_documents_per_author(),
        )

        self.insert_stats(
            "AUTHORS",
            "Collaboration index",
            self.collaboration_index(),
        )

        self.insert_stats(
            "AUTHORS",
            "Organizations",
            self.count_unique_items("organizations"),
        )

        self.insert_stats(
            "AUTHORS",
            "Organizations (1st author)",
            self.count_unique_items("organizations_1st_author"),
        )

        self.insert_stats(
            "AUTHORS",
            "Countries",
            self.count_unique_items("countries"),
        )

        self.insert_stats(
            "AUTHORS",
            "Countries (1st author)",
            self.count_unique_items("countries_1st_author"),
        )

    def authors_of_single_authored_documents(self):
        """Computes the number of authors of single-authored documents"""
        records = self.records[self.records["num_authors"] == 1]
        authors = records.authors.dropna()
        authors = authors.drop_duplicates()
        return len(authors)

    def count_single_authored_documents(self):
        """Computes the number of single-authored documents"""
        return len(self.records[self.records["num_authors"] == 1])

    def count_multi_authored_documents(self):
        """Computes the number of multi-authored documents"""
        return len(self.records[self.records["num_authors"] > 1])

    def average_authors_per_document(self):
        """Computes the average number of authors per document"""
        num_authors = self.records["num_authors"].dropna()
        return round(num_authors.mean(), 2)

    def co_authors_per_document(self):
        """Computes the average number of co-authors per document"""
        records = self.records.copy()
        num_authors = records[records.num_authors > 1].num_authors
        return round(num_authors.mean(), 2)

    def international_co_authorship(self):
        """Computes the percentage of international co-authorship"""
        countries = self.records.countries.copy()
        countries = countries.dropna()
        countries = countries.str.split(";")
        countries = countries.map(len)
        return round(len(countries[countries > 1]) / len(countries) * 100, 2)

    def author_appearances(self):
        """Computes the number of author appearances"""
        records = self.records.authors.copy()
        records = records.dropna()
        records = records.str.split(";")
        records = records.explode()
        records = records.str.strip()
        return len(records)

    def average_documents_per_author(self):
        """Computes the average number of documents per author"""
        records = self.records.authors.copy()
        records = records.dropna()
        n_records = len(records)
        records = records.str.split(";")
        records = records.explode()
        n_authors = len(records)
        return round(n_records / n_authors, 2)

    def collaboration_index(self):
        """Computes the collaboration index"""
        records = self.records[["authors", "num_authors"]].copy()
        records = records.dropna()
        records = records[records.num_authors > 1]
        n_records = len(records)

        n_authors = records.authors.copy()
        n_authors = n_authors.str.split(";")
        n_authors = n_authors.explode()
        n_authors = len(records)
        return round(n_authors / n_records, 2)

    #
    #
    # COMPUTE KEYWORDS STATS
    #
    #
    def __compute_keywords_stats(self):
        """Computes the keywords stats"""

        self.insert_stats(
            "KEYWORDS",
            "Raw author keywords",
            self.count_unique_items("raw_author_keywords"),
        )

        self.insert_stats(
            "KEYWORDS",
            "Cleaned author keywords",
            self.count_unique_items("author_keywords"),
        )
        self.insert_stats(
            "KEYWORDS",
            "Raw index keywords",
            self.count_unique_items("raw_index_keywords"),
        )
        self.insert_stats(
            "KEYWORDS",
            "Cleaned index keywords",
            self.count_unique_items("index_keywords"),
        )
        self.insert_stats(
            "KEYWORDS",
            "Raw keywords",
            self.count_unique_items("raw_keywords"),
        )
        self.insert_stats(
            "KEYWORDS",
            "Cleaned keywords",
            self.count_unique_items("keywords"),
        )

    #
    #
    # COMPUTE NLP PHRASES STATS
    #
    #
    def __compute_nlp_phrases_stats(self):
        """Computes the nlp phrases stats"""

        self.insert_stats(
            "NLP PHRASES",
            "Raw title NLP phrases",
            self.count_unique_items("raw_title_nlp_phrases"),
        )
        self.insert_stats(
            "NLP PHRASES",
            "Cleaned title NLP phrases",
            self.count_unique_items("title_nlp_phrases"),
        )
        self.insert_stats(
            "NLP PHRASES",
            "Raw abstract NLP phrases",
            self.count_unique_items("raw_abstract_nlp_phrases"),
        )
        self.insert_stats(
            "NLP PHRASES",
            "Cleaned abstract NLP phrases",
            self.count_unique_items("abstract_nlp_phrases"),
        )
        self.insert_stats(
            "NLP PHRASES",
            "Raw NLP phrases",
            self.count_unique_items("raw_nlp_phrases"),
        )
        self.insert_stats(
            "NLP PHRASES",
            "Cleaned NLP phrases",
            self.count_unique_items("nlp_phrases"),
        )

    #
    #
    # COMPUTE DESCRIPTOR STATS
    #
    #
    def __compute_descriptors_stats(self):
        """Computes the key concepts stats"""

        self.insert_stats(
            "DESCRIPTORS",
            "Raw descriptors",
            self.count_unique_items("raw_descriptors"),
        )
        self.insert_stats(
            "DESCRIPTORS",
            "Cleaned descriptors",
            self.count_unique_items("descriptors"),
        )


def main_information_table(
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Main information"""

    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return MainInformation(records).frame

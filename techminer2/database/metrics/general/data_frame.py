# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
General Metrics Data Frame
===============================================================================

Example:
    >>> from techminer2.thesaurus.countries import (
    ...     InitializeThesaurus as CreateCountryThesaurus,
    ...     ApplyThesaurus as ApplyCountryThesaurus,
    ... )
    >>> from techminer2.thesaurus.organizations import (
    ...     InitializeThesaurus as CreateOrganizationsThesaurus,
    ...     ApplyThesaurus as ApplyOrganizationsThesaurus,
    ... )
    >>> from techminer2.thesaurus.descriptors import (
    ...     InitializeThesaurus as CreateDescriptorsThesaurus,
    ...     ApplyThesaurus as ApplyDescriptorsThesaurus,
    ... )
    >>> from techminer2.database.metrics.general import DataFrame

    >>> # Create and appli thesauri
    >>> CreateCountryThesaurus(root_directory="example/", quiet=True).run()
    >>> ApplyCountryThesaurus(root_directory="example/", quiet=True).run()
    >>> CreateOrganizationsThesaurus(root_directory="example/", quiet=True).run()
    >>> ApplyOrganizationsThesaurus(root_directory="example/", quiet=True).run()
    >>> CreateDescriptorsThesaurus(root_directory="example/", quiet=True).run()
    >>> ApplyDescriptorsThesaurus(root_directory="example/", quiet=True).run()

    >>> # Create, configure, and run the DataFrame geneartor
    >>> processor = (
    ...     DataFrame()
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ... )
    >>> df = processor.run()
    >>> df # doctest: +NORMALIZE_WHITESPACE
                                                                      Value
    Category          Item
    GENERAL           Timespan                                    2015:2019
                      Documents                                          50
                      Annual growth rate %                           118.67
                      Document average age                             7.24
                      References                                       3213
                      Average citations per document                  162.7
                      Average citations per document per year         32.54
                      Average references per document                 64.26
                      Sources                                            41
                      Average documents per source                     1.22
    DOCUMENT TYPES    Article                                            37
                      Book                                                1
                      Conference paper                                    4
                      Editorial                                           2
                      Review                                              6
    AUTHORS           Authors                                           115
                      Authors of single-authored documents               12
                      Single-authored documents                          12
                      Multi-authored documents                           38
                      Authors per document                             2.52
                      Co-authors per document                           3.0
                      International co-authorship %                   30.61
                      Author appearances                                126
                      Documents per author                              0.4
                      Collaboration index                              3.32
                      organizations                                      90
                      Organizations (1st author)                         42
                      Countries                                          24
                      Countries (1st author)                             18
                      Regions                                             5
                      Subregions                                          9
    KEYWORDS          Author keywords (raw)                             148
                      Author keywords (cleaned)                         145
                      Index keywords (raw)                              179
                      Index keywords (cleaned)                          177
                      Keywords (raw)                                    279
                      Keywords (cleaned)                                266
    NOUNS AND PHRASES Document title nouns and phrases (raw)            125
                      Document title nouns and phrases (cleaned)        123
                      Abstract nouns and phrases (raw)                 1552
                      Abstract nouns and phrases (cleaned)             1519
                      Nouns and phrases (raw)                          1609
                      Nouns and phrases (cleaned)                      1572
    DESCRIPTORS       Descriptors (raw)                                1789
                      Descriptors (cleaned)                            1723





"""


import datetime
from dataclasses import dataclass, field

import numpy as np
import pandas as pd  # type: ignore

from ...._internals.mixins import ParamsMixin
from ..._internals.io import internal__load_filtered_records_from_database


@dataclass
class Stats:
    """:meta private:"""

    category: list = field(default_factory=list)
    item: list = field(default_factory=list)
    value: list = field(default_factory=list)


class DataFrame(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def insert_stats(self, stats, category, item, value):
        """Inserts stats"""

        stats.category.append(category)
        stats.item.append(item)
        stats.value.append(value)

        return stats

    # -------------------------------------------------------------------------
    def count_unique_terms(self, data_frame, column):

        if column not in data_frame:
            return 0

        data_frame = data_frame[column].copy()
        data_frame = data_frame.dropna()
        data_frame = data_frame.str.split(";")
        data_frame = data_frame.explode()
        data_frame = data_frame.str.strip()
        data_frame = data_frame.drop_duplicates()

        return len(data_frame)

    # -------------------------------------------------------------------------

    def run(self):

        data_frame = internal__load_filtered_records_from_database(params=self.params)

        stats = Stats()

        # =====================================================================
        #
        # COMPUTE GENERAL STATS
        #
        # =====================================================================
        stats = self.insert_stats(
            stats,
            category="GENERAL",
            item="Timespan",
            value=str(min(data_frame.year)) + ":" + str(max(data_frame.year)),
        )

        # ---------------------------------------------------------------------
        stats = self.insert_stats(
            stats,
            category="GENERAL",
            item="Documents",
            value=len(data_frame),
        )

        # ---------------------------------------------------------------------
        def annual_growth_rate():
            n_records = len(data_frame)
            n_years = max(data_frame.year) - min(data_frame.year) + 1
            po_ = len(data_frame.year[data_frame.year == min(data_frame.year)])
            return round(100 * (np.power(n_records / po_, 1 / n_years) - 1), 2)

        stats = self.insert_stats(
            stats,
            category="GENERAL",
            item="Annual growth rate %",
            value=annual_growth_rate(),
        )

        # ---------------------------------------------------------------------
        def document_average_age():
            mean_years = data_frame.year.copy()
            mean_years = mean_years.dropna()
            mean_years = mean_years.mean()
            current_year = datetime.datetime.now().year
            return round(int(current_year) - mean_years, 2)

        stats = self.insert_stats(
            stats,
            category="GENERAL",
            item="Document average age",
            value=document_average_age(),
        )

        # ---------------------------------------------------------------------
        def cited_references():
            if "raw_global_references" in data_frame.columns:
                records = data_frame.raw_global_references.copy()
                records = records.dropna()
                records = records.str.split(";")
                records = records.explode()
                records = records.str.strip()
                return len(records)
            return pd.NA

        stats = self.insert_stats(
            stats,
            category="GENERAL",
            item="References",
            value=cited_references(),
        )

        # ---------------------------------------------------------------------
        def average_citations_per_document():
            if "global_citations" in data_frame.columns:
                return round(data_frame.global_citations.mean(), 2)
            return pd.NA

        stats = self.insert_stats(
            stats,
            category="GENERAL",
            item="Average citations per document",
            value=average_citations_per_document(),
        )

        # ---------------------------------------------------------------------
        def average_citations_per_document_per_year():
            if "global_citations" in data_frame.columns:
                return round(
                    data_frame.global_citations.mean()
                    / (data_frame.year.max() - data_frame.year.min() + 1),
                    2,
                )
            return pd.NA

        stats = self.insert_stats(
            stats,
            category="GENERAL",
            item="Average citations per document per year",
            value=average_citations_per_document_per_year(),
        )

        # ---------------------------------------------------------------------
        def average_references_per_document():
            if "raw_global_references" in data_frame.columns:
                num_references = data_frame.raw_global_references.copy()
                num_references = num_references.dropna()
                num_references = num_references.str.split(";")
                num_references = num_references.map(len)
                return round(num_references.sum() / len(data_frame), 2)
            return pd.NA

        stats = self.insert_stats(
            stats,
            category="GENERAL",
            item="Average references per document",
            value=average_references_per_document(),
        )

        # ---------------------------------------------------------------------
        def n_sources():
            if "source_title" in data_frame.columns:
                records = data_frame.source_title.copy()
                records = records.dropna()
                records = records.drop_duplicates()
                return len(records)
            return pd.NA

        stats = self.insert_stats(
            stats,
            category="GENERAL",
            item="Sources",
            value=n_sources(),
        )

        # ---------------------------------------------------------------------
        def average_documents_per_source():
            if "source_title" in data_frame.columns:
                sources = data_frame.source_title.copy()
                sources = sources.dropna()
                n_records = len(sources)
                sources = sources.drop_duplicates()
                n_sources = len(sources)
                return round(n_records / n_sources, 2)
            return pd.NA

        stats = self.insert_stats(
            stats,
            category="GENERAL",
            item="Average documents per source",
            value=average_documents_per_source(),
        )

        # =====================================================================
        #
        # COMPUTE "DOCUMENT TYPE" STATS
        #
        # =====================================================================
        def compute_document_type_stats(stats):
            records = data_frame[["document_type"]].dropna()
            document_types_count = (
                records[["document_type"]].groupby("document_type").size()
            )
            for document_type, count in zip(
                document_types_count.index, document_types_count
            ):
                self.insert_stats(
                    stats,
                    category="DOCUMENT TYPES",
                    item=document_type,
                    value=count,
                )

            return stats

        stats = compute_document_type_stats(stats=stats)

        # =====================================================================
        #
        # COMPUTE AUTHOR STATS
        #
        # =====================================================================

        stats = self.insert_stats(
            stats,
            category="AUTHORS",
            item="Authors",
            value=self.count_unique_terms(
                data_frame,
                "authors",
            ),
        )

        # ---------------------------------------------------------------------
        def authors_of_single_authored_documents(data_frame):

            records = data_frame[data_frame["num_authors"] == 1]
            authors = records.authors.dropna()
            authors = authors.drop_duplicates()
            return len(authors)

        stats = self.insert_stats(
            stats,
            category="AUTHORS",
            item="Authors of single-authored documents",
            value=authors_of_single_authored_documents(data_frame),
        )

        # ---------------------------------------------------------------------
        def count_single_authored_documents(data_frame):
            """Computes the number of single-authored documents"""
            return len(data_frame[data_frame["num_authors"] == 1])

        stats = self.insert_stats(
            stats,
            category="AUTHORS",
            item="Single-authored documents",
            value=count_single_authored_documents(data_frame),
        )

        # ---------------------------------------------------------------------
        def count_multi_authored_documents(data_frame):
            """Computes the number of multi-authored documents"""
            return len(data_frame[data_frame["num_authors"] > 1])

        stats = self.insert_stats(
            stats,
            category="AUTHORS",
            item="Multi-authored documents",
            value=count_multi_authored_documents(data_frame),
        )

        # ---------------------------------------------------------------------
        def average_authors_per_document(data_frame):
            """Computes the average number of authors per document"""
            num_authors = data_frame["num_authors"].dropna()
            return round(num_authors.mean(), 2)

        stats = self.insert_stats(
            stats,
            category="AUTHORS",
            item="Authors per document",
            value=average_authors_per_document(data_frame),
        )

        # ---------------------------------------------------------------------
        def co_authors_per_document(data_frame):
            """Computes the average number of co-authors per document"""
            num_authors = data_frame[data_frame.num_authors > 1].num_authors
            return round(num_authors.mean(), 2)

        stats = self.insert_stats(
            stats,
            category="AUTHORS",
            item="Co-authors per document",
            value=co_authors_per_document(data_frame),
        )

        # ---------------------------------------------------------------------
        def international_co_authorship(data_frame):
            """Computes the percentage of international co-authorship"""
            countries = data_frame.countries.copy()
            countries = countries.dropna()
            countries = countries.str.split(";")
            countries = countries.map(len)
            return round(len(countries[countries > 1]) / len(countries) * 100, 2)

        stats = self.insert_stats(
            stats,
            category="AUTHORS",
            item="International co-authorship %",
            value=international_co_authorship(data_frame),
        )

        # ---------------------------------------------------------------------
        def author_appearances(data_frame):
            """Computes the number of author appearances"""
            data_frame = data_frame.authors.copy()
            data_frame = data_frame.dropna()
            data_frame = data_frame.str.split(";")
            data_frame = data_frame.explode()
            data_frame = data_frame.str.strip()
            return len(data_frame)

        stats = self.insert_stats(
            stats,
            category="AUTHORS",
            item="Author appearances",
            value=author_appearances(data_frame),
        )

        # ---------------------------------------------------------------------
        def average_documents_per_author(data_frame):
            """Computes the average number of documents per author"""
            data_frame = data_frame.authors.copy()
            data_frame = data_frame.dropna()
            n_records = len(data_frame)
            data_frame = data_frame.str.split(";")
            data_frame = data_frame.explode()
            n_authors = len(data_frame)
            return round(n_records / n_authors, 2)

        stats = self.insert_stats(
            stats,
            category="AUTHORS",
            item="Documents per author",
            value=average_documents_per_author(data_frame),
        )

        # ---------------------------------------------------------------------
        def collaboration_index(data_frame):
            """Computes the collaboration index"""
            n_records = data_frame[["authors", "num_authors"]].copy()
            n_records = n_records.dropna()
            n_records = n_records[data_frame.num_authors > 1]
            n_records = len(n_records)

            n_authors = data_frame.authors.copy()
            n_authors = n_authors.str.split(";")
            n_authors = n_authors.explode()
            n_authors = len(n_authors)
            return round(n_authors / n_records, 2)

        stats = self.insert_stats(
            stats,
            category="AUTHORS",
            item="Collaboration index",
            value=collaboration_index(data_frame),
        )

        # ---------------------------------------------------------------------
        stats = self.insert_stats(
            stats,
            category="AUTHORS",
            item="organizations",
            value=self.count_unique_terms(
                data_frame,
                "organizations",
            ),
        )

        # ---------------------------------------------------------------------
        stats = self.insert_stats(
            stats,
            category="AUTHORS",
            item="Organizations (1st author)",
            value=self.count_unique_terms(
                data_frame,
                "organization_1st_author",
            ),
        )

        # ---------------------------------------------------------------------
        stats = self.insert_stats(
            stats,
            category="AUTHORS",
            item="Countries",
            value=self.count_unique_terms(
                data_frame,
                "countries",
            ),
        )

        # ---------------------------------------------------------------------
        stats = self.insert_stats(
            stats,
            category="AUTHORS",
            item="Countries (1st author)",
            value=self.count_unique_terms(
                data_frame,
                "country_1st_author",
            ),
        )

        # ---------------------------------------------------------------------
        stats = self.insert_stats(
            stats,
            category="AUTHORS",
            item="Regions",
            value=self.count_unique_terms(
                data_frame,
                "regions",
            ),
        )

        # ---------------------------------------------------------------------
        stats = self.insert_stats(
            stats,
            category="AUTHORS",
            item="Subregions",
            value=self.count_unique_terms(
                data_frame,
                "subregions",
            ),
        )

        # =====================================================================
        #
        # COMPUTE KEYWORDS STATS
        #
        # =====================================================================

        stats = self.insert_stats(
            stats,
            category="KEYWORDS",
            item="Author keywords (raw)",
            value=self.count_unique_terms(
                data_frame,
                "raw_author_keywords",
            ),
        )

        stats = self.insert_stats(
            stats,
            category="KEYWORDS",
            item="Author keywords (cleaned)",
            value=self.count_unique_terms(
                data_frame,
                "author_keywords",
            ),
        )

        stats = self.insert_stats(
            stats,
            category="KEYWORDS",
            item="Index keywords (raw)",
            value=self.count_unique_terms(
                data_frame,
                "raw_index_keywords",
            ),
        )

        stats = self.insert_stats(
            stats,
            category="KEYWORDS",
            item="Index keywords (cleaned)",
            value=self.count_unique_terms(
                data_frame,
                "index_keywords",
            ),
        )

        stats = self.insert_stats(
            stats,
            category="KEYWORDS",
            item="Keywords (raw)",
            value=self.count_unique_terms(
                data_frame,
                "raw_keywords",
            ),
        )

        stats = self.insert_stats(
            stats,
            category="KEYWORDS",
            item="Keywords (cleaned)",
            value=self.count_unique_terms(
                data_frame,
                "keywords",
            ),
        )

        # =====================================================================
        #
        # COMPUTE NLP PHRASES STATS
        #
        # =====================================================================

        stats = self.insert_stats(
            stats,
            category="NOUNS AND PHRASES",
            item="Document title nouns and phrases (raw)",
            value=self.count_unique_terms(
                data_frame,
                "raw_document_title_nouns_and_phrases",
            ),
        )

        stats = self.insert_stats(
            stats,
            category="NOUNS AND PHRASES",
            item="Document title nouns and phrases (cleaned)",
            value=self.count_unique_terms(
                data_frame,
                "document_title_nouns_and_phrases",
            ),
        )

        stats = self.insert_stats(
            stats,
            category="NOUNS AND PHRASES",
            item="Abstract nouns and phrases (raw)",
            value=self.count_unique_terms(
                data_frame,
                "raw_abstract_nouns_and_phrases",
            ),
        )

        stats = self.insert_stats(
            stats,
            category="NOUNS AND PHRASES",
            item="Abstract nouns and phrases (cleaned)",
            value=self.count_unique_terms(
                data_frame,
                "abstract_nouns_and_phrases",
            ),
        )

        stats = self.insert_stats(
            stats,
            category="NOUNS AND PHRASES",
            item="Nouns and phrases (raw)",
            value=self.count_unique_terms(
                data_frame,
                "raw_nouns_and_phrases",
            ),
        )

        stats = self.insert_stats(
            stats,
            category="NOUNS AND PHRASES",
            item="Nouns and phrases (cleaned)",
            value=self.count_unique_terms(
                data_frame,
                "nouns_and_phrases",
            ),
        )

        # =====================================================================
        #
        # COMPUTE DESCRIPTOR STATS
        #
        # =====================================================================

        stats = self.insert_stats(
            stats,
            category="DESCRIPTORS",
            item="Descriptors (raw)",
            value=self.count_unique_terms(
                data_frame,
                "raw_descriptors",
            ),
        )

        stats = self.insert_stats(
            stats,
            category="DESCRIPTORS",
            item="Descriptors (cleaned)",
            value=self.count_unique_terms(
                data_frame,
                "descriptors",
            ),
        )

        # =====================================================================
        #
        # REPORT
        #
        # =====================================================================

        frame = pd.DataFrame(
            {
                "Category": stats.category,
                "Item": stats.item,
                "Value": stats.value,
            }
        )
        frame = frame.set_index(["Category", "Item"])
        return frame

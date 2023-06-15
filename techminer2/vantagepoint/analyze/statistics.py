# flake8: noqa
"""
Statistics
===============================================================================


>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> stats = vantagepoint.analyze.statistics(root_dir)
>>> stats.table_
                                                            Value
Category       Item                                              
GENERAL        Timespan                                 2016:2023
               Documents                                       52
               Annual growth rate %                         63.87
               Document average age                          2.77
               References                                    2968
               Average citations per document               10.83
               Average citations per document per year       1.35
               Average references per document              59.36
               Sources                                         46
               Average documents per source                  1.13
DOCUMENT TYPES article                                         31
               book                                             1
               book_chapter                                     9
               conference_paper                                11
AUTHORS        Authors                                        102
               Authors of single-authored documents            19
               Single-authored documents                       19
               Multi-authored documents                        33
               Authors per document                          2.29
               Co-authors per document                       3.03
               International co-authorship %                23.08
               Author appearances                             119
               Documents per author                          0.44
               Collaboration index                            1.0
               Organizations                                   81
               Organizations (1st author)                      45
               Countries                                       29
               Countries (1st author)                          25
KEYWORDS       Raw author keywords                            148
               Cleaned author keywords                        148
               Raw index keywords                             155
               Cleaned index keywords                         155
               Raw keywords                                   273
               Cleaned keywords                               271
NLP PHRASES    Raw title NLP phrases                           40
               Cleaned title NLP phrases                       40
               Raw abstract NLP phrases                       157
               Cleaned abstract NLP phrases                   149
               Raw NLP phrases                                167
               Cleaned NLP phrases                            158
KEY CONCEPTS   Raw key concepts                               373
               Cleaned key concepts                           364
            
               
>>> file_name = "sphinx/_static/bibliometrix__main_info_plot.html"               
>>> stats.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/bibliometrix__main_info_plot.html" height="800px" width="100%" frameBorder="0"></iframe>


    
>>> print(stats.prompt_)
Your task is to generate a short summary for a research paper of a table with record \\
and field statistics for a dataset of scientific publications.
<BLANKLINE>
The table below, delimited by triple backticks, provides data on the main characteristics \\
of the records and fields of the bibliographic dataset. Use the the information in the \\
table to draw conclusions. Limit your description to one paragraph in at most 60 words.
<BLANKLINE>
Table:
```
|                                                        | Value     |
|:-------------------------------------------------------|:----------|
| ('GENERAL', 'Timespan')                                | 2016:2023 |
| ('GENERAL', 'Documents')                               | 52        |
| ('GENERAL', 'Annual growth rate %')                    | 63.87     |
| ('GENERAL', 'Document average age')                    | 2.77      |
| ('GENERAL', 'References')                              | 2968      |
| ('GENERAL', 'Average citations per document')          | 10.83     |
| ('GENERAL', 'Average citations per document per year') | 1.35      |
| ('GENERAL', 'Average references per document')         | 59.36     |
| ('GENERAL', 'Sources')                                 | 46        |
| ('GENERAL', 'Average documents per source')            | 1.13      |
| ('DOCUMENT TYPES', 'article')                          | 31        |
| ('DOCUMENT TYPES', 'book')                             | 1         |
| ('DOCUMENT TYPES', 'book_chapter')                     | 9         |
| ('DOCUMENT TYPES', 'conference_paper')                 | 11        |
| ('AUTHORS', 'Authors')                                 | 102       |
| ('AUTHORS', 'Authors of single-authored documents')    | 19        |
| ('AUTHORS', 'Single-authored documents')               | 19        |
| ('AUTHORS', 'Multi-authored documents')                | 33        |
| ('AUTHORS', 'Authors per document')                    | 2.29      |
| ('AUTHORS', 'Co-authors per document')                 | 3.03      |
| ('AUTHORS', 'International co-authorship %')           | 23.08     |
| ('AUTHORS', 'Author appearances')                      | 119       |
| ('AUTHORS', 'Documents per author')                    | 0.44      |
| ('AUTHORS', 'Collaboration index')                     | 1.0       |
| ('AUTHORS', 'Organizations')                           | 81        |
| ('AUTHORS', 'Organizations (1st author)')              | 45        |
| ('AUTHORS', 'Countries')                               | 29        |
| ('AUTHORS', 'Countries (1st author)')                  | 25        |
| ('KEYWORDS', 'Raw author keywords')                    | 148       |
| ('KEYWORDS', 'Cleaned author keywords')                | 148       |
| ('KEYWORDS', 'Raw index keywords')                     | 155       |
| ('KEYWORDS', 'Cleaned index keywords')                 | 155       |
| ('KEYWORDS', 'Raw keywords')                           | 273       |
| ('KEYWORDS', 'Cleaned keywords')                       | 271       |
| ('NLP PHRASES', 'Raw title NLP phrases')               | 40        |
| ('NLP PHRASES', 'Cleaned title NLP phrases')           | 40        |
| ('NLP PHRASES', 'Raw abstract NLP phrases')            | 157       |
| ('NLP PHRASES', 'Cleaned abstract NLP phrases')        | 149       |
| ('NLP PHRASES', 'Raw NLP phrases')                     | 167       |
| ('NLP PHRASES', 'Cleaned NLP phrases')                 | 158       |
| ('KEY CONCEPTS', 'Raw key concepts')                   | 373       |
| ('KEY CONCEPTS', 'Cleaned key concepts')               | 364       |
```
<BLANKLINE>


# pylint: disable=line-too-long
"""
import datetime

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ...classes import RecordStatistics
from ...record_utils import read_records


class _Statistics:
    def __init__(
        self,
        root_dir,
        database="main",
        year_filter=None,
        cited_by_filter=None,
        **filters,
    ):
        self.directory = root_dir
        self.records = read_records(
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )
        self.n_records = len(self.records)
        self.compute_general_information_stats()
        self.compute_document_types_stats()
        self.compute_authors_stats()
        self.compute_keywords_stats()
        self.compute_nlp_phrases_stats()
        self.compute_key_concepts_stats()
        self.make_report()

    def make_report(self):
        """Make a report of the statistics."""
        pdf = pd.concat(
            [
                self.general_information_stats,
                self.document_types_stats,
                self.authors_stats,
                self.keywords_stats,
                self.nlp_phrases_stats,
                self.key_concepts_stats,
            ]
        )
        index = pd.MultiIndex.from_arrays(
            [pdf.Category, pdf.Item], names=["Category", "Item"]
        )
        self.report_ = pd.DataFrame(
            pdf.Value.tolist(), columns=["Value"], index=index
        )

    #####################################################################################
    def compute_general_information_stats(self):
        """Compute general information statistics."""
        self.general_information_stats = pd.DataFrame(
            columns=["Category", "Item", "Value"]
        )
        self.general_information_stats.loc[(0,)] = [
            "GENERAL",
            "Timespan",
            self.compute_timespam(),
        ]
        self.general_information_stats.loc[(1,)] = [
            "GENERAL",
            "Documents",
            self.documents(),
        ]
        self.general_information_stats.loc[(2,)] = [
            "GENERAL",
            "Annual growth rate %",
            self.annual_growth_rate(),
        ]
        self.general_information_stats.loc[(3,)] = [
            "GENERAL",
            "Document average age",
            self.document_average_age(),
        ]
        self.general_information_stats.loc[(4,)] = [
            "GENERAL",
            "References",
            self.cited_references(),
        ]
        self.general_information_stats.loc[(5,)] = [
            "GENERAL",
            "Average citations per document",
            self.average_citations_per_document(),
        ]
        self.general_information_stats.loc[(6,)] = [
            "GENERAL",
            "Average citations per document per year",
            self.average_citations_per_document_per_year(),
        ]
        self.general_information_stats.loc[(7,)] = [
            "GENERAL",
            "Average references per document",
            self.average_references_per_document(),
        ]
        self.general_information_stats.loc[(8,)] = [
            "GENERAL",
            "Sources",
            self.sources(),
        ]
        self.general_information_stats.loc[(9,)] = [
            "GENERAL",
            "Average documents per source",
            self.average_documents_per_source(),
        ]

    # -----------------------------------------------------------------------------------

    def compute_timespam(self):
        """Computes the timespan of the records"""

        return str(min(self.records.year)) + ":" + str(max(self.records.year))

    def documents(self):
        """Computes the number of documents"""
        return len(self.records)

    def annual_growth_rate(self):
        """Computes the annual growth rate"""
        n_years = max(self.records.year) - min(self.records.year) + 1
        po_ = len(
            self.records.year[self.records.year == min(self.records.year)]
        )
        return round(
            100 * (np.power(self.n_records / po_, 1 / n_years) - 1), 2
        )

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
        else:
            return pd.NA

    def average_citations_per_document(self):
        """Computes the average number of citations per document"""
        if "global_citations" in self.records.columns:
            return round(self.records.global_citations.mean(), 2)
        else:
            return pd.NA

    def average_citations_per_document_per_year(self):
        """Computes the average number of citations per document per year"""
        if "global_citations" in self.records.columns:
            return round(
                self.records.global_citations.mean()
                / (self.records.year.max() - self.records.year.min() + 1),
                2,
            )
        else:
            return pd.NA

    def average_references_per_document(self):
        """Computes the average number of references per document"""
        if "global_references" in self.records.columns:
            num_references = self.records.global_references.copy()
            num_references = num_references.dropna()
            num_references = num_references.str.split(";")
            num_references = num_references.map(len)
            return round(num_references.mean(), 2)
        else:
            return pd.NA

    def sources(self):
        """Computes the number of sources"""
        if "source_title" in self.records.columns:
            records = self.records.source_title.copy()
            records = records.dropna()
            records = records.drop_duplicates()
            return len(records)
        else:
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
        else:
            return pd.NA

    #####################################################################################
    def compute_document_types_stats(self):
        """Computes the document types statistics"""
        self.document_types_stats = pd.DataFrame(
            columns=["Category", "Item", "Value"]
        )
        records = self.records[["document_type"]].dropna()
        document_types_count = (
            records[["document_type"]].groupby("document_type").size()
        )
        for index, (document_type, count) in enumerate(
            zip(document_types_count.index, document_types_count)
        ):
            self.document_types_stats.loc[(index,)] = [
                "DOCUMENT TYPES",
                document_type,
                count,
            ]

    #####################################################################################
    def compute_authors_stats(self):
        """Computes the authors statistics"""
        self.authors_stats = pd.DataFrame(
            columns=["Category", "Item", "Value"]
        )
        self.authors_stats.loc[(0,)] = [
            "AUTHORS",
            "Authors",
            self.authors(),
        ]
        self.authors_stats.loc[(1,)] = [
            "AUTHORS",
            "Authors of single-authored documents",
            self.authors_of_single_authored_documents(),
        ]
        self.authors_stats.loc[(2,)] = [
            "AUTHORS",
            "Single-authored documents",
            self.count_single_authored_documents(),
        ]
        self.authors_stats.loc[(3,)] = [
            "AUTHORS",
            "Multi-authored documents",
            self.count_multi_authored_documents(),
        ]
        self.authors_stats.loc[(4,)] = [
            "AUTHORS",
            "Authors per document",
            self.average_authors_per_document(),
        ]
        self.authors_stats.loc[(5,)] = [
            "AUTHORS",
            "Co-authors per document",
            self.co_authors_per_document(),
        ]
        self.authors_stats.loc[(6,)] = [
            "AUTHORS",
            "International co-authorship %",
            self.international_co_authorship(),
        ]
        self.authors_stats.loc[(7,)] = [
            "AUTHORS",
            "Author appearances",
            self.author_appearances(),
        ]
        self.authors_stats.loc[(8,)] = [
            "AUTHORS",
            "Documents per author",
            self.average_documents_per_author(),
        ]

        self.authors_stats.loc[(9,)] = [
            "AUTHORS",
            "Collaboration index",
            self.collaboration_index(),
        ]
        self.authors_stats.loc[(10,)] = [
            "AUTHORS",
            "Organizations",
            self.organizations(),
        ]
        self.authors_stats.loc[(11,)] = [
            "AUTHORS",
            "Organizations (1st author)",
            self.organizations_1st_author(),
        ]
        self.authors_stats.loc[(12,)] = [
            "AUTHORS",
            "Countries",
            self.countries(),
        ]
        self.authors_stats.loc[(13,)] = [
            "AUTHORS",
            "Countries (1st author)",
            self.countries_1st_author(),
        ]

    # -----------------------------------------------------------------------------------

    def authors(self):
        """Computes the number of authors"""
        records = self.records.authors.copy()
        records = records.dropna()
        records = records.str.split(";")
        records = records.explode()
        records = records.str.strip()
        records = records.drop_duplicates()
        return len(records)

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

    def organizations(self):
        """Computes the number of organizations"""
        if "organizations" in self.records.columns:
            records = self.records.organizations.copy()
            records = records.dropna()
            records = records.str.split(";")
            records = records.explode()
            records = records.str.strip()
            records = records.drop_duplicates()
            return len(records)
        else:
            return pd.NA

    def organizations_1st_author(self):
        """Computes the number of organizations of 1st authors"""
        if "organization_1st_author" in self.records.columns:
            records = self.records.organization_1st_author.copy()
            records = records.dropna()
            records = records.str.split(";")
            records = records.explode()
            records = records.str.strip()
            records = records.drop_duplicates()
            return len(records)
        else:
            return pd.NA

    def countries(self):
        """Computes the number of countries"""
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
        """Computes the number of countries of 1st authors"""
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
        """Computes the keywords stats"""
        self.keywords_stats = pd.DataFrame(
            columns=["Category", "Item", "Value"]
        )
        self.keywords_stats.loc[(0,)] = [
            "KEYWORDS",
            "Raw author keywords",
            self.raw_author_keywords(),
        ]
        self.keywords_stats.loc[(1,)] = [
            "KEYWORDS",
            "Cleaned author keywords",
            self.author_keywords(),
        ]
        self.keywords_stats.loc[(2,)] = [
            "KEYWORDS",
            "Raw index keywords",
            self.raw_index_keywords(),
        ]
        self.keywords_stats.loc[(3,)] = [
            "KEYWORDS",
            "Cleaned index keywords",
            self.index_keywords(),
        ]
        self.keywords_stats.loc[(4,)] = [
            "KEYWORDS",
            "Raw keywords",
            self.raw_keywords(),
        ]
        self.keywords_stats.loc[(5,)] = [
            "KEYWORDS",
            "Cleaned keywords",
            self.keywords(),
        ]

    # -----------------------------------------------------------------------------------

    def raw_author_keywords(self):
        """Computes the number of raw author keywords"""
        records = self.records.raw_author_keywords.copy()
        records = records.dropna()
        records = records.str.split(";")
        records = records.explode()
        records = records.str.strip()
        records = records.drop_duplicates()
        return len(records)

    def author_keywords(self):
        """Computes the number of cleaned author keywords"""
        records = self.records.author_keywords.copy()
        records = records.dropna()
        records = records.str.split(";")
        records = records.explode()
        records = records.str.strip()
        records = records.drop_duplicates()
        return len(records)

    def raw_index_keywords(self):
        """Computes the number of raw index keywords"""
        if "raw_index_keywords" in self.records.columns:
            records = self.records.raw_index_keywords.copy()
            records = records.dropna()
            records = records.str.split(";")
            records = records.explode()
            records = records.str.strip()
            records = records.drop_duplicates()
            return len(records)
        else:
            return 0

    def index_keywords(self):
        """Computes the number of cleaned index keywords"""
        if "index_keywords" in self.records.columns:
            records = self.records.index_keywords.copy()
            records = records.dropna()
            records = records.str.split(";")
            records = records.explode()
            records = records.str.strip()
            records = records.drop_duplicates()
            return len(records)
        else:
            return 0

    def raw_keywords(self):
        """Computes the number of raw keywords"""
        if "raw_keywords" in self.records.columns:
            records = self.records.raw_keywords.copy()
            records = records.dropna()
            records = records.str.split(";")
            records = records.explode()
            records = records.str.strip()
            records = records.drop_duplicates()
            return len(records)
        else:
            return 0

    def keywords(self):
        """Computes the number of cleaned keywords"""
        if "keywords" in self.records.columns:
            records = self.records.keywords.copy()
            records = records.dropna()
            records = records.str.split(";")
            records = records.explode()
            records = records.str.strip()
            records = records.drop_duplicates()
            return len(records)
        else:
            return 0

    #####################################################################################
    def compute_nlp_phrases_stats(self):
        """Computes the nlp phrases stats"""
        self.nlp_phrases_stats = pd.DataFrame(
            columns=["Category", "Item", "Value"]
        )
        self.nlp_phrases_stats.loc[(0,)] = [
            "NLP PHRASES",
            "Raw title NLP phrases",
            self.raw_title_nlp_phrases(),
        ]
        self.nlp_phrases_stats.loc[(1,)] = [
            "NLP PHRASES",
            "Cleaned title NLP phrases",
            self.title_nlp_phrases(),
        ]
        self.nlp_phrases_stats.loc[(2,)] = [
            "NLP PHRASES",
            "Raw abstract NLP phrases",
            self.raw_abstract_nlp_phrases(),
        ]
        self.nlp_phrases_stats.loc[(3,)] = [
            "NLP PHRASES",
            "Cleaned abstract NLP phrases",
            self.abstract_nlp_phrases(),
        ]
        self.nlp_phrases_stats.loc[(4,)] = [
            "NLP PHRASES",
            "Raw NLP phrases",
            self.raw_nlp_phrases(),
        ]
        self.nlp_phrases_stats.loc[(5,)] = [
            "NLP PHRASES",
            "Cleaned NLP phrases",
            self.nlp_phrases(),
        ]

    # -----------------------------------------------------------------------------------

    def raw_title_nlp_phrases(self):
        """Computes the number of raw author keywords"""
        records = self.records.raw_title_nlp_phrases.copy()
        records = records.dropna()
        records = records.str.split(";")
        records = records.explode()
        records = records.str.strip()
        records = records.drop_duplicates()
        return len(records)

    def title_nlp_phrases(self):
        """Computes the number of cleaned author keywords"""
        records = self.records.title_nlp_phrases.copy()
        records = records.dropna()
        records = records.str.split(";")
        records = records.explode()
        records = records.str.strip()
        records = records.drop_duplicates()
        return len(records)

    def raw_abstract_nlp_phrases(self):
        """Computes the number of raw index keywords"""
        if "raw_abstract_nlp_phrases" in self.records.columns:
            records = self.records.raw_abstract_nlp_phrases.copy()
            records = records.dropna()
            records = records.str.split(";")
            records = records.explode()
            records = records.str.strip()
            records = records.drop_duplicates()
            return len(records)
        else:
            return 0

    def abstract_nlp_phrases(self):
        """Computes the number of cleaned index keywords"""
        if "abstract_nlp_phrases" in self.records.columns:
            records = self.records.abstract_nlp_phrases.copy()
            records = records.dropna()
            records = records.str.split(";")
            records = records.explode()
            records = records.str.strip()
            records = records.drop_duplicates()
            return len(records)
        else:
            return 0

    def raw_nlp_phrases(self):
        """Computes the number of raw index keywords"""
        if "raw_nlp_phrases" in self.records.columns:
            records = self.records.raw_nlp_phrases.copy()
            records = records.dropna()
            records = records.str.split(";")
            records = records.explode()
            records = records.str.strip()
            records = records.drop_duplicates()
            return len(records)
        else:
            return 0

    def nlp_phrases(self):
        """Computes the number of raw index keywords"""
        if "raw_nlp_phrases" in self.records.columns:
            records = self.records.nlp_phrases.copy()
            records = records.dropna()
            records = records.str.split(";")
            records = records.explode()
            records = records.str.strip()
            records = records.drop_duplicates()
            return len(records)
        else:
            return 0

    #####################################################################################
    def compute_key_concepts_stats(self):
        """Computes the key concepts stats"""
        self.key_concepts_stats = pd.DataFrame(
            columns=["Category", "Item", "Value"]
        )
        self.key_concepts_stats.loc[(0,)] = [
            "KEY CONCEPTS",
            "Raw key concepts",
            self.raw_key_concepts(),
        ]
        self.key_concepts_stats.loc[(1,)] = [
            "KEY CONCEPTS",
            "Cleaned key concepts",
            self.cleaned_key_concepts(),
        ]

    # -----------------------------------------------------------------------------------

    def raw_key_concepts(self):
        """Computes the number of raw author keywords"""
        records = self.records.raw_key_concepts.copy()
        records = records.dropna()
        records = records.str.split(";")
        records = records.explode()
        records = records.str.strip()
        records = records.drop_duplicates()
        return len(records)

    def cleaned_key_concepts(self):
        """Computes the number of cleaned author keywords"""
        records = self.records.key_concepts.copy()
        records = records.dropna()
        records = records.str.split(";")
        records = records.explode()
        records = records.str.strip()
        records = records.drop_duplicates()
        return len(records)


def make_plot(report):
    """Makes the plot"""

    def add_text_trace(fig, category, caption, row, col):
        text = (
            f'<span style="font-size: 8px;">{caption}</span><br>'
            f'<br><span style="font-size: 20px;">'
            f"{report.loc[(category, caption)].values[0]}</span>"
        )

        fig.add_trace(
            go.Scatter(
                x=[0.5],
                y=[0.5],
                text=[text],
                mode="text",
            ),
            row=row,
            col=col,
        )
        fig.update_xaxes(visible=False, row=row, col=col)
        fig.update_yaxes(visible=False, row=row, col=col)

    fig = make_subplots(rows=7, cols=3)

    add_text_trace(fig, "GENERAL", "Timespan", 1, 1)
    add_text_trace(fig, "GENERAL", "Sources", 1, 2)
    add_text_trace(fig, "GENERAL", "Documents", 1, 3)

    add_text_trace(fig, "GENERAL", "Annual growth rate %", 2, 1)
    add_text_trace(fig, "AUTHORS", "Authors", 2, 2)
    add_text_trace(
        fig, "AUTHORS", "Authors of single-authored documents", 2, 3
    )

    add_text_trace(fig, "AUTHORS", "International co-authorship %", 3, 1)
    add_text_trace(fig, "AUTHORS", "Co-authors per document", 3, 2)
    add_text_trace(fig, "GENERAL", "References", 3, 3)

    add_text_trace(fig, "KEYWORDS", "Raw author keywords", 4, 1)
    add_text_trace(fig, "KEYWORDS", "Cleaned author keywords", 4, 2)
    add_text_trace(fig, "KEYWORDS", "Raw index keywords", 4, 3)

    add_text_trace(fig, "KEYWORDS", "Raw keywords", 5, 1)
    add_text_trace(fig, "KEYWORDS", "Cleaned keywords", 5, 2)
    add_text_trace(fig, "NLP PHRASES", "Raw NLP phrases", 5, 3)

    add_text_trace(
        fig,
        "NLP PHRASES",
        "Cleaned NLP phrases",
        6,
        1,
    )

    add_text_trace(
        fig,
        "KEY CONCEPTS",
        "Raw key concepts",
        6,
        2,
    )

    add_text_trace(
        fig,
        "KEY CONCEPTS",
        "Cleaned key concepts",
        6,
        3,
    )

    add_text_trace(fig, "GENERAL", "Document average age", 7, 1)
    add_text_trace(fig, "GENERAL", "Average citations per document", 7, 2)

    fig.update_layout(showlegend=False)
    fig.update_layout(title="Main Information")
    fig.update_layout(height=800)

    return fig


def make_chatpgt_prompt(report):
    """Makes the chatpgt prompt"""
    # pylint: disable=line-too-long
    return (
        "Your task is to generate a short summary for a research paper of a table with record \\\n"
        "and field statistics for a dataset of scientific publications.\n\n"
        "The table below, delimited by triple backticks, provides data on the main characteristics \\\n"
        "of the records and fields of the bibliographic dataset. Use the the information in the \\\n"
        "table to draw conclusions. Limit your description to one paragraph in at most 60 words.\n\n"
        f"Table:\n```\n{report.to_markdown()}\n```\n"
    )


def statistics(
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Returns main statistics of the dataset.

    Args:
        root_dir (str, optional): Root directory. Defaults to "./".
        database (str, optional): Database name. Defaults to "documents".
        year_filter (tuple, optional): Year filter. Defaults to None.
        cited_by_filter (tuple, optional): Cited by filter. Defaults to None.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.

    Returns:
        RecordStatistics: RecordStatistics object.

    """

    stats = _Statistics(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    obj = RecordStatistics()
    obj.table_ = stats.report_
    obj.plot_ = make_plot(stats.report_)
    obj.prompt_ = make_chatpgt_prompt(stats.report_)

    return obj

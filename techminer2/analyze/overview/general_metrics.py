# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
General Metrics
===============================================================================

>>> from techminer2.analyze.overview import general_metrics
>>> info = general_metrics(
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> info.df_
                                                            Value
Category       Item                                              
GENERAL        Timespan                                 2016:2023
               Documents                                       52
               Annual growth rate %                         63.87
               Document average age                          2.77
               References                                     932
               Average citations per document               10.83
               Average citations per document per year       1.35
               Average references per document              20.71
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
               Organizations (1st author)                       0
               Countries                                       29
               Countries (1st author)                           0
KEYWORDS       Raw author keywords                            148
               Cleaned author keywords                        142
               Raw index keywords                             156
               Cleaned index keywords                         151
               Raw keywords                                   274
               Cleaned keywords                               253
NLP PHRASES    Raw title NLP phrases                           68
               Cleaned title NLP phrases                       68
               Raw abstract NLP phrases                       796
               Cleaned abstract NLP phrases                   743
               Raw NLP phrases                                834
               Cleaned NLP phrases                            776
DESCRIPTORS    Raw descriptors                               1041
               Cleaned descriptors                            939


>>> info.fig_.write_html("sphinx/_static/analyze/overview/general_metrics.html")

.. raw:: html

    <iframe src="../../../../_static/analyze/overview/general_metrics.html"
    height="800px" width="100%" frameBorder="0"></iframe>

>>> print(info.prompt_) # doctest: +ELLIPSIS
Your task is ...

    


"""
import datetime
from dataclasses import dataclass

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ..._read_records import read_records
from ...format_prompt_for_dataframes import format_prompt_for_dataframes


def general_metrics(
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """
    :meta private:
    """

    @dataclass
    class Result:
        df_: pd.DataFrame
        fig_: go.Figure
        prompt_: str

    data_frame = main_metrics_table(
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    prompt = main_metrics_prompt(data_frame)
    fig = general_metrics_dashboard(data_frame)

    return Result(
        df_=data_frame,
        prompt_=prompt,
        fig_=fig,
    )


def general_metrics_dashboard(
    data_frame,
):
    """
    :meta private:
    """

    def add_text_trace(fig, category, caption, row, col):
        text = (
            f'<span style="font-size: 8px;">{caption}</span><br>'
            f'<br><span style="font-size: 20px;">'
            f"{data_frame.loc[(category, caption)].values[0]}</span>"
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
    add_text_trace(fig, "AUTHORS", "Authors of single-authored documents", 2, 3)

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
        "DESCRIPTORS",
        "Raw descriptors",
        6,
        2,
    )

    add_text_trace(
        fig,
        "DESCRIPTORS",
        "Cleaned descriptors",
        6,
        3,
    )

    add_text_trace(fig, "GENERAL", "Document average age", 7, 1)
    add_text_trace(fig, "GENERAL", "Average citations per document", 7, 2)

    fig.update_layout(showlegend=False)
    fig.update_layout(title="General Metrics")
    fig.update_layout(height=800)

    return fig


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
        self.__compute_noun_phrases_stats()
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
    def __compute_noun_phrases_stats(self):
        """Computes the nlp phrases stats"""

        self.insert_stats(
            "NLP PHRASES",
            "Raw title NLP phrases",
            self.count_unique_items("raw_title_noun_phrases"),
        )
        self.insert_stats(
            "NLP PHRASES",
            "Cleaned title NLP phrases",
            self.count_unique_items("title_noun_phrases"),
        )
        self.insert_stats(
            "NLP PHRASES",
            "Raw abstract NLP phrases",
            self.count_unique_items("raw_abstract_noun_phrases"),
        )
        self.insert_stats(
            "NLP PHRASES",
            "Cleaned abstract NLP phrases",
            self.count_unique_items("abstract_noun_phrases"),
        )
        self.insert_stats(
            "NLP PHRASES",
            "Raw NLP phrases",
            self.count_unique_items("raw_noun_phrases"),
        )
        self.insert_stats(
            "NLP PHRASES",
            "Cleaned NLP phrases",
            self.count_unique_items("noun_phrases"),
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


def main_metrics_table(
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """
    :meta private:
    """

    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return MainInformation(records).frame


def main_metrics_prompt(
    data_frame,
):
    """
    :meta private:
    """
    main_text = (
        "Your task is to generate a short summary for a research paper of a "
        "table with record and field statistics for a dataset of scientific "
        "publications. The table below, delimited by triple backticks, "
        "provides data on the main characteristics of the records and fields "
        "of the bibliographic dataset. Use the the information in the table "
        "to draw conclusions. Limit your description to one paragraph in at "
        "most 100 words. "
    )

    table_text = data_frame.dropna().to_markdown()

    return format_prompt_for_dataframes(main_text, table_text)

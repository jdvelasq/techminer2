"""
Summary view
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> summary_view(directory)
                                                             value
Category       Item                                               
GENERAL        Documents:                                     1301
               Years:                                    2015-2022
               Compound annual growth rate:                86.21 %
               Average citations per document:                5.40
               Average citations per document per year:       0.67
               Total references:                             57797
               Average global references per document:          44
DOCUMENT TYPES Article:                                        780
               Book:                                            19
               Book Chapter:                                   101
               Conference Paper:                               312
               Editorial:                                       20
               Erratum:                                          2
               Letter:                                           1
               Note:                                             6
               Review:                                          58
               Short Survey:                                     2
AUTHORS        Authors:                                       2937
               Author appearances:                            3438
               Documents per author:                          0.44
               Authors per document:                          2.26
               Single-authored documents:                      315
               Multi-authored documents:                       969
               Co-authors per document:                       2.64
               Collaboration index:                           2.79
               Institutions:                                  1349
               Institutions (1st author):                      803
               Countries:                                       95
               Countries (1st author):                          84
KEYWORDS       Author Keywords (raw):                         2954
               Author Keywords (cleaned):                     2705
               Index Keywords (raw):                          2738
               Index Keywords (cleaned):                      2642
               Keywords (cleaned):                            3214
OTHERS         document_id                                    1301
               doi                                            1094
               isbn                                            280
               iso_source_name                                 639
               issn                                            513
               num_global_references                           155
               pubmed_id                                         7
               raw_authors_names                              2816
               source_name                                     649
"""
import datetime

import numpy as np
import pandas as pd

from .utils import load_filtered_documents


def _extract_terms(x, column):
    x = x.copy()
    x[column] = x[column].map(
        lambda w: w.split("; ") if not pd.isna(w) and isinstance(w, str) else w
    )
    x = x.explode(column)
    x[column] = x[column].map(lambda w: w.strip() if isinstance(w, str) else w)
    x = pd.unique(x[column].dropna())
    x = np.sort(x)
    return pd.DataFrame({column: x})


def _count_terms(records, column):
    return len(_extract_terms(records, column))


def summary_view(directory=None):
    """
    Returns an overview of the dataset.

    Parameters
    ----------
    records: pandas.DataFrame
        records object.

    Returns
    -------
    pandas.DataFrame
        Summary statistcs
    """

    records = load_filtered_documents(directory)

    records = records.copy()
    general = {}

    #
    # documents count
    #
    general["Documents:"] = str(len(records))

    #
    # range of years
    #

    n_records = len(records)

    if "pub_year" in records.columns:
        #
        # range of years
        #
        general["Years:"] = (
            str(min(records.pub_year)) + "-" + str(max(records.pub_year))
        )

        #
        # compound annual growth rate
        #
        n_years = max(records.pub_year) - min(records.pub_year) + 1
        Po = len(records.pub_year[records.pub_year == min(records.pub_year)])
        cagr = str(round(100 * (np.power(n_records / Po, 1 / n_years) - 1), 2)) + " %"
        general["Compound annual growth rate:"] = cagr

        #
        # average years from publication
        #
        mean_years = records.pub_year.copy()
        mean_years = mean_years.dropna()
        mean_years = mean_years.mean()
        current_year = datetime.datetime.now().year
        agrp = round(int(current_year) - mean_years, 2)
        general["Current years from publication:"] = agrp

    if "global_citations" in records.columns:
        #
        # average citations per document
        #
        general["Average citations per document:"] = "{:4.2f}".format(
            records["global_citations"].mean()
        )

    if "global_citations" in records.columns and "pub_year" in records.columns:
        general["Average citations per document per year:"] = "{:4.2f}".format(
            records["global_citations"].sum()
            / (len(records) * (records.pub_year.max() - records.pub_year.min() + 1))
        )

    if "cited_references" in records.columns:
        general["Cited references:"] = round(_count_terms(records, "global_references"))
        general["Average cited references per document:"] = round(
            _count_terms(records, "cited_references") / n_records
        )

    if "source_name" in records.columns:
        general["Sources:"] = round(_count_terms(records, "source_name"))
        general["Average documents per source:"] = round(
            n_records / _count_terms(records, "source_name")
        )
        records.pop("source_name")

    if "iso_source_abbreviation" in records.columns:
        general["Abbreviated Source titles:"] = round(
            _count_terms(records, "iso_source_abbreviation")
        )
        records.pop("iso_source_abbreviation")

    #
    #  Document types
    #
    document_types = {}
    if "document_type" in records.columns:
        z = records[["document_type"]].groupby("document_type").size()
        for index, value in zip(z.index, z):
            document_types[index + ":"] = value
        records.pop("document_type")

    #
    #  Authors
    #
    authors = {}

    if "authors" in records.columns:

        authors["Authors:"] = _count_terms(records, "authors")

        m = records.authors
        m = m.dropna()
        m = m.map(lambda w: w.split(";"), na_action="ignore")
        m = m.explode()
        authors["Author appearances:"] = len(m)

        authors["Documents per author:"] = round(
            n_records / _count_terms(records, "authors"), 2
        )
        authors["Authors per document:"] = round(
            _count_terms(records, "authors") / n_records, 2
        )

    if "num_authors" in records.columns:
        authors["Single-authored documents:"] = len(
            records[records["num_authors"] == 1]
        )
        authors["Multi-authored documents:"] = len(records[records["num_authors"] > 1])
        authors["Co-authors per document:"] = round(records["num_authors"].mean(), 2)
        authors["Collaboration index:"] = round(
            _count_terms(records[records.num_authors > 1], "authors")
            / len(records[records.num_authors > 1]),
            2,
        )

    if "institutions" in records.columns:
        authors["Institutions:"] = _count_terms(records, "institutions")
        records.pop("institutions")

    if "institution_1st_author" in records.columns:
        authors["Institutions (1st author):"] = _count_terms(
            records, "institution_1st_author"
        )
        records.pop("institution_1st_author")

    if "countries" in records.columns:
        authors["Countries:"] = _count_terms(records, "countries")
        if "countries" in records.columns:
            records.pop("countries")

    if "country_1st_author" in records.columns:
        authors["Countries (1st author):"] = _count_terms(records, "country_1st_author")
        records.pop("country_1st_author")

    #
    #  Keywords
    #
    keywords = {}

    if "raw_author_keywords" in records.columns:
        keywords["Raw author keywords:"] = round(
            _count_terms(records, "raw_author_keywords")
        )
        records.pop("raw_author_keywords")

    if "author_keywords" in records.columns:
        keywords["Cleaned author keywords:"] = round(
            _count_terms(records, "author_keywords")
        )
        records.pop("author_keywords")

    if "raw_index_keywords" in records.columns:
        keywords["Raw index keywords:"] = round(
            _count_terms(records, "raw_index_keywords")
        )
        records.pop("raw_index_keywords")

    if "index_keywords" in records.columns:
        keywords["Cleaned index keywords:"] = round(
            _count_terms(records, "index_keywords")
        )
        records.pop("index_keywords")

    if "keywords_cl" in records.columns:
        keywords["Keywords (cleaned):"] = round(_count_terms(records, "keywords_cl"))
        records.pop("keywords_cl")

    if "title_words" in records.columns:
        keywords["Raw title words:"] = round(_count_terms(records, "title_words"))
        records.pop("title_words")

    if "title_words_CL" in records.columns:
        keywords["Title words (cleaned):"] = round(
            _count_terms(records, "title_words_CL")
        )
        records.pop("title_words_CL")

    if "abstract_words" in records.columns:
        keywords["Abstract words (raw)"] = round(
            _count_terms(records, "abstract_words")
        )
        records.pop("abstract_words")

    if "abstract_words_cl" in records.columns:
        keywords["Abstract words (cleaned)"] = round(
            _count_terms(records, "abstract_words_cl")
        )
        records.pop("abstract_words_cl")

    #
    #  Report
    #

    if "frac_num_documents" in records.columns:
        records.pop("frac_num_documents")

    if "document_id" in records.columns:
        records.pop("document_id")

    d = []
    d += [key for key in general.keys()]
    d += [key for key in document_types.keys()]
    d += [key for key in authors.keys()]
    d += [key for key in keywords.keys()]

    v = []
    v += [general[key] for key in general.keys()]
    v += [document_types[key] for key in document_types.keys()]
    v += [authors[key] for key in authors.keys()]
    v += [keywords[key] for key in keywords.keys()]

    #
    #  Other columns in the dataset
    #

    others = {}
    for column in sorted(records.columns):

        if column + ":" in d or column in [
            "abstract_author_keywords_cl",
            "abstract_author_keywords",
            "abstract_index_keywords_cl",
            "abstract_index_keywords",
            "abstract_keywords_cl",
            "abstract_keywords",
            "abstract",
            "affiliations",
            "authors_id",
            "authors",
            "bradford_law_zone",
            "document_title",
            "global_citations",
            "global_references_count",
            "global_references",
            "isbn",
            "issn",
            "doi",
            "keywords",
            "local_citations",
            "local_references",
            "num_authors",
            "pub_year",
            "raw_keywords",
            "record_id",
            "wos_id",
        ]:
            continue

        others[column] = round(_count_terms(records, column))

    if len(others):
        d += [key for key in others.keys()]
        v += [others[key] for key in others.keys()]

    return pd.DataFrame(
        v,
        columns=["value"],
        index=pd.MultiIndex.from_arrays(
            [
                ["GENERAL"] * len(general)
                + ["DOCUMENT TYPES"] * len(document_types)
                + ["AUTHORS"] * len(authors)
                + ["KEYWORDS"] * len(keywords)
                + ["OTHERS"] * len(others),
                d,
            ],
            names=["Category", "Item"],
        ),
    )

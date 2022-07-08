"""
Import Scopus Files
===============================================================================

Import a scopus file to a working directory.

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> import_scopus_files(directory, disable_progress_bar=True)
--INFO-- Concatenating raw files in data/raw/cited_by/
--INFO-- Concatenating raw files in data/raw/references/
--INFO-- Concatenating raw files in data/raw/documents/
--INFO-- Applying scopus tags to database files
--INFO-- Formating column names in database files
--INFO-- Dropping NA columns in database files
--INFO-- Removing accents in database files
--INFO-- Creating `filter.yaml` file
--INFO-- Processing `abstract` column
--INFO-- Processing `authors_id` column
--INFO-- Processing `title` column
--INFO-- Processing `document_type` column
--INFO-- Processing `doi` column
--INFO-- Processing `eissn` column
--INFO-- Processing `global_citations` column
--INFO-- Processing `isbn` column
--INFO-- Processing `issn` column
--INFO-- Processing `raw_author_keywords` column
--INFO-- Processing `raw_authors` column
--INFO-- Processing `raw_index_keywords` column
--INFO-- Processing `source_abbr` column
--INFO-- Processing `source_name` column
--INFO-- Processing `global_references` column
--INFO-- Creating `authors` column
--INFO-- Creating `num_authors` column
--INFO-- Creating `record_no` column
--INFO-- Creating `document_id` column
--INFO-- Creating `raw_abstract_words` column
--INFO-- Creating `raw_title_words` column
--INFO-- Creating `raw_countries` column
--INFO-- Creating `country_1st_author` column
--INFO-- Creating `countries` column
--INFO-- Creating `num_global_references` column
--INFO-- Complete `source_abbr` column
--INFO-- Creating `abstract.csv` file from `documents` database
--INFO-- Creating `local_references` column
--INFO-- Creating `local_citations` column
--INFO-- Creating `bradford` column
--INFO-- Creating `references_by_document.csv` file
--INFO-- Creating `local_citations` column in references database
--INFO-- Creating a thesaurus file from `raw_author_keywords` column in all databases
--INFO-- The thesaurus file `author_keywords.txt` was created
--INFO-- Applying `author_keywords.txt` thesaurus
--INFO-- Creating a thesaurus file from `raw_index_keywords` column in all databases
--INFO-- The thesaurus file `index_keywords.txt` was created
--INFO-- Applying `index_keywords.txt` thesaurus
--INFO-- Creating `words.txt` from author/index keywords, and abstract/title words
--INFO-- Applying `words.txt` thesaurus to author/index keywords and abstract/title words
--INFO-- Creating institutions thesaurus
--INFO-- Affiliations without country detected - check file data/processed/ignored_affiliations.txt
--INFO-- Affiliations without country detected - check file data/ignored_affiliations.txt
--INFO-- Thesaurus file 'data/processed/institutions.txt' created
--INFO-- Applying thesaurus to institutions
--INFO-- The thesaurus was applied to institutions in all databases
--INFO-- Process finished!!!


"""
import glob
import os
import os.path
import sys

import numpy as np
import pandas as pd
import yaml
from nltk.tokenize import RegexpTokenizer, sent_tokenize
from tqdm import tqdm

from .apply_author_keywords_thesaurus import apply_author_keywords_thesaurus
from .apply_index_keywords_thesaurus import apply_index_keywords_thesaurus
from .apply_institutions_thesaurus import apply_institutions_thesaurus
from .apply_words_thesaurus import apply_words_thesaurus
from .create_country_thesaurus import create_country_thesaurus
from .create_institutions_thesaurus import create_institutions_thesaurus
from .create_thesaurus import create_thesaurus
from .create_words_thesaurus import create_words_thesaurus
from .extract_country import extract_country


def import_scopus_files(
    directory="./",
    disable_progress_bar=False,
):
    """Import Scopus files."""

    _create_working_directories(directory)
    #
    _create_stopwords_file(directory)
    _create_database_files(directory)
    #
    _apply_scopus2tags_to_database_files(directory)
    _format_columns_names_in_database_files(directory)
    _drop_na_columns_in_database_files(directory)
    _remove_accents_in_database_files(directory)
    _create_filter_file(directory)
    #
    _process__abstract__column(directory)
    _process__authors_id__column(directory)
    _process__title__column(directory)
    _process__document_type__column(directory)
    _process__doi__column(directory)
    _process__eissn__column(directory)
    _process__global_citations__column(directory)
    _process__isbn__column(directory)
    _process__issn__column(directory)
    _process__raw_author_keywords__column(directory)
    _process__raw_authors__column(directory)
    _process__raw_index_keywords__column(directory)
    _process__source_abbr__column(directory)
    _process__source_name__column(directory)
    _process__global_references__column(directory)
    #
    _create__authors__column(directory)
    _create__num_authors__column(directory)
    _create__record_no__column(directory)
    _create__document_id__column(directory)
    _create__raw_abstract_words__column(directory)
    _create__raw_title_words__column(directory)
    #
    #
    create_country_thesaurus(directory)
    #
    #
    _create__raw_countries__column(directory)
    _create__coutry_1st_autor__column(directory)
    _create__countries__column(directory)
    _create__num_global_references__column(directory)
    _complete__source_abbr__column(directory)
    _create__abstract_csv__file(directory)
    _create__local_references__column(
        directory, disable_progress_bar=disable_progress_bar
    )
    _create__local_citations__column(directory)
    _create__bradford__column(directory)
    #
    #
    _create_references_by_document_file(
        directory, disable_progress_bar=disable_progress_bar
    )
    _create__local_citations__column_in_references_database(directory)
    #
    create_thesaurus(
        "raw_author_keywords",
        output_file="author_keywords.txt",
        directory=directory,
    )
    apply_author_keywords_thesaurus(directory)
    #
    create_thesaurus(
        "raw_index_keywords", output_file="index_keywords.txt", directory=directory
    )
    apply_index_keywords_thesaurus(directory=directory)
    #
    create_words_thesaurus(directory=directory)
    apply_words_thesaurus(directory=directory)
    #
    create_institutions_thesaurus(directory=directory)
    apply_institutions_thesaurus(directory=directory)

    sys.stdout.write("--INFO-- Process finished!!!\n")


def _create__local_citations__column_in_references_database(directory):

    sys.stdout.write(
        "--INFO-- Creating `local_citations` column in references database\n"
    )

    references_by_document = pd.read_csv(
        os.path.join(directory, "processed", "references_by_document.csv")
    )

    local_citations_by_reference = references_by_document.groupby(
        "references_record_no", as_index=True
    ).count()

    references = pd.read_csv(os.path.join(directory, "processed", "_references.csv"))
    references = references.assign(local_citations=0)
    references.index = references.record_no
    references.loc[
        local_citations_by_reference.index, "local_citations"
    ] = local_citations_by_reference.documents_record_no
    references = references.reset_index(drop=True)
    references["local_citations"].fillna(1, inplace=True)
    references["local_citations"] = references["local_citations"].astype(int)
    file_name = os.path.join(directory, "processed", "_references.csv")
    references.to_csv(file_name, index=False)


def _create_references_by_document_file(directory, disable_progress_bar=False):

    sys.stdout.write("--INFO-- Creating `references_by_document.csv` file\n")

    references = pd.read_csv(os.path.join(directory, "processed", "_references.csv"))
    references = references.assign(authors=references.authors.str.lower())

    documents = pd.read_csv(os.path.join(directory, "processed", "_documents.csv"))

    # builds a table with:
    #   record_no  raw_reference
    #   ------------------------------------------------
    reference_by_record = documents[["record_no", "global_references"]].copy()

    reference_by_record = reference_by_record.rename(
        columns={"global_references": "raw_reference"}
    )
    reference_by_record = reference_by_record.dropna()
    reference_by_record = reference_by_record.assign(
        raw_reference=reference_by_record.raw_reference.str.split(";")
    )
    reference_by_record = reference_by_record.explode("raw_reference")
    reference_by_record = reference_by_record.assign(
        raw_reference=reference_by_record.raw_reference.str.strip()
    )
    reference_by_record = reference_by_record.assign(
        raw_reference=reference_by_record.raw_reference.str.lower()
    )
    reference_by_record = reference_by_record.sort_values("raw_reference")

    # -------------------------------------------------------------------------
    # optimized for speed
    # raw references and list of citting documents:
    reference_by_record = reference_by_record.groupby(
        ["raw_reference"], as_index=False
    ).agg(list)
    reference_by_record = reference_by_record.assign(references_record_no=np.nan)
    #
    references = references.assign(title=references.title.str.lower())
    references = references[~references.authors.isna()]

    with tqdm(total=len(references), disable=disable_progress_bar) as pbar:
        for _, row in references.iterrows():
            reference_by_record.loc[
                reference_by_record.raw_reference.str.contains(
                    row["title"], regex=False
                )
                & reference_by_record.raw_reference.str.contains(str(row["year"]))
                & reference_by_record.raw_reference.str.contains(
                    row["authors"].split(" ")[0].strip()
                ),
                "references_record_no",
            ] = row["record_no"]
            pbar.update(1)

    reference_by_record = reference_by_record.dropna()
    reference_by_record = reference_by_record.explode("record_no")
    reference_by_record = reference_by_record[
        ["record_no", "references_record_no"]
    ].copy()
    reference_by_record = reference_by_record.rename(
        columns={"record_no": "documents_record_no"}
    )
    reference_by_record = reference_by_record.reset_index(drop=True)
    reference_by_record = reference_by_record.dropna()
    reference_by_record = reference_by_record.sort_values(
        ["documents_record_no", "references_record_no"]
    )

    reference_by_record.to_csv(
        os.path.join(directory, "processed", "references_by_document.csv"), index=False
    )


def _create__num_authors__column(directory):

    sys.stdout.write("--INFO-- Creating `num_authors` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        #
        data = data.assign(num_authors=data.authors.str.split(";"))
        data = data.assign(num_authors=data.num_authors.map(len, na_action="ignore"))
        data = data.assign(
            num_authors=data.num_authors.where(~data.num_authors.isna(), 0)
        )
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _create__local_citations__column(directory):

    sys.stdout.write("--INFO-- Creating `local_citations` column\n")

    file_name = os.path.join(directory, "processed", "_documents.csv")
    documents = pd.read_csv(file_name)

    local_references = documents[["local_references"]]
    local_references = local_references.rename(
        columns={"local_references": "local_citations"}
    )
    local_references = local_references.dropna()

    local_references["local_citations"] = local_references.local_citations.str.split(
        ";"
    )
    local_references = local_references.explode("local_citations")
    local_references["local_citations"] = local_references.local_citations.str.strip()

    local_references = local_references.groupby(
        by="local_citations", as_index=True
    ).size()
    documents["local_citations"] = 0
    documents.index = documents.record_no
    documents.loc[local_references.index, "local_citations"] = local_references

    documents.to_csv(file_name, sep=",", index=False, encoding="utf-8")


def _create__local_references__column(directory, disable_progress_bar):

    sys.stdout.write("--INFO-- Creating `local_references` column\n")

    file_name = os.path.join(directory, "processed", "_documents.csv")
    documents = pd.read_csv(file_name)

    # creates a empty list which will be filled with the local references
    documents = documents.assign(local_references=[[] for _ in range(len(documents))])

    if "global_references" in documents.columns:

        #
        # Identifies if a document is a local reference using doi
        #
        with tqdm(total=len(documents.doi), disable=disable_progress_bar) as pbar:
            for document_index, doi, global_citations in zip(
                documents.index, documents.doi, documents.global_citations
            ):
                if global_citations == 0:
                    continue
                if not pd.isna(doi):
                    doi = doi.upper()
                    for j_index, references in zip(
                        documents.index, documents.global_references.tolist()
                    ):
                        if pd.isna(references) is False and doi in references.upper():
                            documents.at[j_index, "local_references"].append(
                                documents.record_no[document_index]
                            )
                pbar.update(1)

        #
        # Identifies if a document is a local reference using the title
        #
        with tqdm(total=len(documents.title), disable=disable_progress_bar) as pbar:

            for (
                document_index,
                document_title,
                document_year,
                document_citations,
            ) in zip(
                documents.index,
                documents.title.str.lower(),
                documents.year,
                documents.global_citations,
            ):

                if document_citations > 0:

                    document_title = documents.title[document_index].lower()
                    document_year = documents.year[document_index]

                    for j_index, references in zip(
                        documents.index, documents.global_references.tolist()
                    ):

                        if (
                            pd.isna(references) is False
                            and document_title in references.lower()
                        ):

                            for reference in references.split(";"):

                                if (
                                    document_title in reference.lower()
                                    and str(document_year) in reference
                                ):

                                    documents.at[j_index, "local_references"] += [
                                        documents.record_no[document_index]
                                    ]

                pbar.update(1)

        #
        # Create a string list of with the local references
        #
        documents["local_references"] = documents.local_references.apply(
            lambda x: sorted(set(x))
        )
        documents["local_references"] = documents.local_references.apply(
            lambda x: "; ".join(x) if isinstance(x, list) else x
        )

    documents.to_csv(file_name, sep=",", index=False, encoding="utf-8")


def _create__abstract_csv__file(directory):

    sys.stdout.write(
        "--INFO-- Creating `abstract.csv` file from `documents` database\n"
    )

    documents = pd.read_csv(os.path.join(directory, "processed", "_documents.csv"))

    if "abstract" in documents.columns:

        abstracts = documents[
            ["record_no", "abstract", "global_citations", "document_id"]
        ].copy()
        abstracts = abstracts.rename(columns={"abstract": "phrase"})
        abstracts = abstracts.dropna()
        abstracts = abstracts.assign(phrase=abstracts.phrase.str.replace(";", "."))
        abstracts = abstracts.assign(phrase=abstracts.phrase.map(sent_tokenize))
        abstracts = abstracts.explode("phrase")
        abstracts = abstracts.assign(phrase=abstracts.phrase.str.strip())
        abstracts = abstracts[abstracts.phrase.str.len() > 0]
        abstracts = abstracts.assign(
            line_no=abstracts.groupby(["record_no"]).cumcount()
        )
        abstracts = abstracts[
            ["record_no", "line_no", "phrase", "global_citations", "document_id"]
        ]
        file_name = os.path.join(directory, "processed", "abstracts.csv")
        abstracts.to_csv(file_name, index=False)


def _process__global_references__column(directory):

    sys.stdout.write("--INFO-- Processing `global_references` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "global_references" in data.columns:
            data = data.assign(
                global_references=data.global_references.str.replace(
                    "https://doi.org/", ""
                )
            )
            data = data.assign(
                global_references=data.global_references.str.replace(
                    "http://dx.doi.org/", ""
                )
            )
        data.to_csv(file, sep=",", index=False, encoding="utf-8")


def _create__num_global_references__column(directory):

    sys.stdout.write("--INFO-- Creating `num_global_references` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "global_references" in data.columns:
            data = data.assign(
                num_global_references=data.global_references.str.split(";")
            )
            data.num_global_references = data.num_global_references.map(
                lambda x: len(x) if isinstance(x, list) else 0
            )
        data.to_csv(file, sep=",", index=False, encoding="utf-8")


def _create__bradford__column(directory):

    sys.stdout.write("--INFO-- Creating `bradford` column\n")

    file_path = os.path.join(directory, "processed", "_documents.csv")
    data = pd.read_csv(file_path, encoding="utf-8")

    indicators = data[["source_title", "global_citations"]]
    indicators = indicators.assign(num_documents=1)
    indicators = indicators.groupby(["source_title"], as_index=False).sum()
    indicators = indicators.sort_values(
        by=["num_documents", "global_citations"], ascending=False
    )
    indicators = indicators.assign(
        cum_num_documents=indicators["num_documents"].cumsum()
    )

    num_documents = indicators["num_documents"].sum()
    indicators = indicators.reset_index(drop=True)
    indicators = indicators.assign(zone=3)
    indicators.zone = indicators.zone.where(
        indicators.cum_num_documents >= int(num_documents * 2 / 3), 2
    )
    indicators.zone = indicators.zone.where(
        indicators.cum_num_documents >= int(num_documents / 3), 1
    )
    source2zone = dict(zip(indicators.source_title, indicators.zone))
    data = data.assign(bradford=data["source_title"].map(source2zone))
    data.to_csv(file_path, sep=",", encoding="utf-8", index=False)


def _create__countries__column(directory):

    sys.stdout.write("--INFO-- Creating `countries` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "raw_countries" in data.columns:
            data = data.assign(countries=data["raw_countries"].str.split(";"))
            data = data.assign(
                countries=data["countries"].map(
                    lambda x: "; ".join(set(x)) if isinstance(x, list) else x
                )
            )

        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _create__coutry_1st_autor__column(directory):

    sys.stdout.write("--INFO-- Creating `country_1st_author` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "raw_countries" in data.columns:
            data = data.assign(
                country_1st_author=data["raw_countries"].str.split(";").str[0]
            )
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _create__raw_countries__column(directory):
    sys.stdout.write("--INFO-- Creating `raw_countries` column\n")
    extract_country(
        directory=directory,
        input_col="affiliations",
        output_col="raw_countries",
    )


def _extract_keywords_from_database_files(directory):
    keywords_list = []
    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "raw_index_keywords" in data.columns:
            keywords_list += data.raw_index_keywords.dropna().tolist()
        if "raw_author_keywords" in data.columns:
            keywords_list += data.raw_author_keywords.dropna().tolist()
    keywords_list = pd.DataFrame({"keyword": keywords_list})
    keywords_list = keywords_list.assign(keyword=keywords_list.keyword.str.split(";"))
    keywords_list = keywords_list.explode("keyword")
    keywords_list = keywords_list.keyword.str.strip()
    keywords_list = keywords_list.drop_duplicates()
    keywords_list = keywords_list.reset_index(drop=True)
    return keywords_list


def _select_compound_keywords(keywords_list):
    keywords_list = keywords_list.to_frame()
    keywords_list = keywords_list.assign(
        is_compound=keywords_list.keyword.str.contains(" ")
    )
    keywords_list = keywords_list[keywords_list.is_compound]
    keywords_list = keywords_list[["keyword"]]
    return keywords_list


def _load_nltk_stopwords():
    module_path = os.path.dirname(__file__)
    file_path = os.path.join(module_path, "files/nltk_stopwords.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        nltk_stopwords = [line.strip() for line in file]
    return nltk_stopwords


def _create__raw_abstract_words__column(directory):

    sys.stdout.write("--INFO-- Creating `raw_abstract_words` column\n")

    #
    keywords = _extract_keywords_from_database_files(directory)
    keywords = _select_compound_keywords(keywords)
    nltk_stopwords = _load_nltk_stopwords()
    tokenizer = RegexpTokenizer(r"\w+")
    #

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        #
        if "abstract" not in data.columns:
            continue

        data = data.assign(raw_abstract_words=data.abstract.str.lower())
        data = data.assign(
            raw_abstract_words=data.raw_abstract_words.str.replace("-", "ZZZ")
        )
        for word in keywords.keyword:
            data.raw_abstract_words = data.raw_abstract_words.str.replace(
                word, word.replace(" ", "_"), regex=False
            )
        data = data.assign(
            raw_abstract_words=data.raw_abstract_words.map(
                tokenizer.tokenize, na_action="ignore"
            )
        )
        data = data.assign(
            raw_abstract_words=data.raw_abstract_words.map(
                lambda x: [word for word in x if word not in nltk_stopwords],
                na_action="ignore",
            )
        )

        data = data.assign(
            raw_abstract_words=data.raw_abstract_words.map(
                "; ".join, na_action="ignore"
            ),
        )
        data = data.assign(
            raw_abstract_words=data.raw_abstract_words.str.replace("_", " ")
        )
        data = data.assign(
            raw_abstract_words=data.raw_abstract_words.str.replace("ZZZ", "-")
        )
        data = data.assign(
            raw_abstract_words=data.raw_abstract_words.str.replace(" ;", ";")
        )
        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _create__raw_title_words__column(directory):

    sys.stdout.write("--INFO-- Creating `raw_title_words` column\n")

    #
    keywords = _extract_keywords_from_database_files(directory)
    keywords = _select_compound_keywords(keywords)
    nltk_stopwords = _load_nltk_stopwords()
    tokenizer = RegexpTokenizer(r"\w+")
    #

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        #
        data = data.assign(raw_title_words=data.title.str.lower())
        data = data.assign(raw_title_words=data.raw_title_words.str.replace("-", "ZZZ"))
        for word in keywords.keyword:
            data.raw_title_words = data.raw_title_words.str.replace(
                word, word.replace(" ", "_"), regex=False
            )
        data = data.assign(raw_title_words=data.raw_title_words.map(tokenizer.tokenize))
        data = data.assign(
            raw_title_words=data.raw_title_words.map(
                lambda x: [word for word in x if word not in nltk_stopwords]
            )
        )

        data = data.assign(raw_title_words=data.raw_title_words.map("; ".join))
        data = data.assign(raw_title_words=data.raw_title_words.str.replace("_", " "))
        data = data.assign(raw_title_words=data.raw_title_words.str.replace("ZZZ", "-"))
        data = data.assign(raw_title_words=data.raw_title_words.str.replace(" ;", ";"))
        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _create__record_no__column(directory):

    sys.stdout.write("--INFO-- Creating `record_no` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        #
        data = data.assign(
            record_no=data.sort_values("global_citations", ascending=False)
            .groupby("year")
            .cumcount()
        )
        data = data.assign(record_no=data.record_no.map(lambda x: str(x).zfill(4)))
        data = data.assign(record_no=data.year.astype(str) + "-" + data.record_no)
        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False)

    return data


def _create__document_id__column(directory):

    sys.stdout.write("--INFO-- Creating `document_id` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        #
        wos_ref = data.authors.map(
            lambda x: x.split("; ")[0].strip() if not pd.isna(x) else "[anonymous]"
        )
        wos_ref = wos_ref + data.authors.map(
            lambda x: (" et al" if len(x.split("; ")) > 0 else "")
            if not pd.isna(x)
            else ""
        )
        wos_ref = wos_ref + ", " + data.year.map(str)
        wos_ref = wos_ref + ", " + data.source_abbr
        data["document_id"] = wos_ref.copy()
        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _create_filter_file(directory):

    sys.stdout.write("--INFO-- Creating `filter.yaml` file\n")

    file_name = os.path.join(directory, "processed/_documents.csv")
    documents = pd.read_csv(file_name, encoding="utf-8")

    filter_ = {}
    filter_["first_year"] = int(documents.year.min())
    filter_["last_year"] = int(documents.year.max())
    filter_["min_citations"] = 0
    filter_["max_citations"] = int(documents.global_citations.max())
    filter_["bradford"] = 3

    document_types = documents.document_type.dropna().unique()
    for document_type in document_types:
        document_type = document_type.lower()
        document_type = document_type.replace(" ", "_")
        filter_[str(document_type)] = True

    yaml_filename = os.path.join(directory, "processed", "filter.yaml")
    with open(yaml_filename, "wt", encoding="utf-8") as yaml_file:
        yaml.dump(filter_, yaml_file, sort_keys=True)


def _complete__source_abbr__column(directory):

    sys.stdout.write("--INFO-- Complete `source_abbr` column\n")

    name2iso = {}
    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))

    # builds the dictionary
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "source_abbr" in data.columns and "source_name" in data.columns:
            current_name2iso = {
                name: abbr
                for name, abbr in zip(data.source_name, data.source_abbr)
                if name is not pd.NA and abbr is not pd.NA
            }
            name2iso = {**name2iso, **current_name2iso}

    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "source_abbr" in data.columns and "source_name" in data.columns:
            data.source_abbr = np.where(
                data.source_abbr.isna(),
                data.source_name.map(lambda x: name2iso.get(x, x)),
                data.source_abbr,
            )
            data.source_abbr = data.source_abbr.str.replace(" JOUNAL ", " J ")
            data.source_abbr = data.source_abbr.str.replace(" AND ", "")
            data.source_abbr = data.source_abbr.str.replace(" IN ", "")
            data.source_abbr = data.source_abbr.str.replace(" OF ", "")
            data.source_abbr = data.source_abbr.str.replace(" ON ", "")
            data.source_abbr = data.source_abbr.str.replace(" THE ", "")

        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _create__authors__column(directory):
    #
    def load_authors_names():
        files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
        data = [
            pd.read_csv(file, encoding="utf-8")[["raw_authors", "authors_id"]]
            for file in files
        ]
        data = pd.concat(data)
        data = data.dropna()
        return data

    #
    def build_dict_names(data):

        data = data.copy()

        data = data.assign(authors_and_ids=data.raw_authors + "#" + data.authors_id)
        data.authors_and_ids = data.authors_and_ids.str.split("#")
        data.authors_and_ids = data.authors_and_ids.apply(
            lambda x: (x[0].split(";"), x[1].split(";"))
        )
        data.authors_and_ids = data.authors_and_ids.apply(
            lambda x: list(zip(x[0], x[1]))
        )
        data = data.explode("authors_and_ids")
        data.authors_and_ids = data.authors_and_ids.apply(
            lambda x: (x[0].strip(), x[1].strip())
        )
        data = data.reset_index(drop=True)
        data = data[["authors_and_ids"]]
        data["author"] = data.authors_and_ids.apply(lambda x: x[0])
        data["author_id"] = data.authors_and_ids.apply(lambda x: x[1])
        data = data.drop(columns=["authors_and_ids"])
        data = data.drop_duplicates()
        data = data.sort_values(by=["author"])
        data = data.assign(counter=data.groupby(["author"]).cumcount())
        data = data.assign(author=data.author + "/" + data.counter.astype(str))
        data.author = data.author.str.replace("/0", "")
        author_id2name = dict(zip(data.author_id, data.author))
        return author_id2name

    #
    def repair_names(author_id2name):
        files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
        for file in files:
            data = pd.read_csv(file, encoding="utf-8")
            data = data.assign(authors=data.authors_id.copy())
            data = data.assign(authors=data.authors.str.replace(";", "; "))
            for author_id, author in author_id2name.items():
                data = data.assign(authors=data.authors.str.replace(author_id, author))
            data.to_csv(file, sep=",", encoding="utf-8", index=False)

    #
    sys.stdout.write("--INFO-- Creating `authors` column\n")

    data = load_authors_names()
    author_id2name = build_dict_names(data)
    repair_names(author_id2name)


def _process__source_abbr__column(directory):

    sys.stdout.write("--INFO-- Processing `source_abbr` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "source_abbr" in data.columns:
            data.source_abbr = data.source_abbr.str.upper()
            data.source_abbr = data.source_abbr.str.replace(".", "")
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _process__raw_index_keywords__column(directory):

    sys.stdout.write("--INFO-- Processing `raw_index_keywords` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "raw_index_keywords" in data.columns:
            data.raw_index_keywords = data.raw_index_keywords.str.lower()
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _process__raw_author_keywords__column(directory):

    sys.stdout.write("--INFO-- Processing `raw_author_keywords` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "raw_author_keywords" in data.columns:
            data.raw_author_keywords = data.raw_author_keywords.str.lower()
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _process__global_citations__column(directory):

    sys.stdout.write("--INFO-- Processing `global_citations` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "global_citations" in data.columns:
            data.global_citations = data.global_citations.fillna(0)
            data.global_citations = data.global_citations.astype(int)
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _process__raw_authors__column(directory):

    sys.stdout.write("--INFO-- Processing `raw_authors` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "raw_authors" in data.columns:
            data.raw_authors = data.raw_authors.map(
                lambda x: pd.NA if x == "[No author name available]" else x
            )
            data.raw_authors = data.raw_authors.str.replace(",", ";", regex=False)
            data.raw_authors = data.raw_authors.str.replace(".", "", regex=False)
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _process__title__column(directory):

    sys.stdout.write("--INFO-- Processing `title` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "title" in data.columns:
            data["title"] = data.title.str.replace(r"\[.*", "", regex=True)
            data["title"] = data.title.str.strip()
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _process__abstract__column(directory):

    sys.stdout.write("--INFO-- Processing `abstract` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "abstract" in data.columns:
            data["abstract"] = data.abstract.str.lower()
            data["abstract"] = data.abstract.where(
                data.abstract == "[no abstract available]", pd.NA
            )
            data["abstract"] = data.abstract.str.replace(r"\u00a9.*", "", regex=True)

        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _process__authors_id__column(directory):

    sys.stdout.write("--INFO-- Processing `authors_id` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "document_type" in data.columns:
            data["authors_id"] = data.authors_id.str.replace(";$", "", regex=True)
            data["authors_id"] = data.authors_id.map(
                lambda x: pd.NA if x == "[No author id available]" else x
            )
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _process__document_type__column(directory):

    sys.stdout.write("--INFO-- Processing `document_type` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "document_type" in data.columns:
            data = data.copy()
            data["document_type"] = data.document_type.str.replace(" ", "_")
            data["document_type"] = data.document_type.str.lower()
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _process__source_name__column(directory):

    sys.stdout.write("--INFO-- Processing `source_name` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "source_name" in data.columns:
            data.source_name = data.source_name.str.upper()
            data.source_name = data.source_name.str.replace(r"[^\w\s]", "", regex=True)
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _process__issn__column(directory):

    sys.stdout.write("--INFO-- Processing `issn` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "issn" in data.columns:
            data.issn = data.issn.str.replace("-", "", regex=True)
            data.issn = data.issn.str.upper()
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _process__isbn__column(directory):

    sys.stdout.write("--INFO-- Processing `isbn` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "isbn" in data.columns:
            data.isbn = data.isbn.str.replace("-", "", regex=True)
            data.isbn = data.isbn.str.upper()
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _process__eissn__column(directory):

    sys.stdout.write("--INFO-- Processing `eissn` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "eissn" in data.columns:
            data.eissn = data.eissn.str.replace("-", "", regex=True)
            data.eissn = data.eissn.str.upper()
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _process__doi__column(directory):

    sys.stdout.write("--INFO-- Processing `doi` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "doi" in data.columns:
            data.doi = data.doi.str.upper()
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _remove_accents_in_database_files(directory):

    sys.stdout.write("--INFO-- Removing accents in database files\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        cols = data.select_dtypes(include=[np.object]).columns
        data[cols] = data[cols].apply(
            lambda x: x.str.normalize("NFKD")
            .str.encode("ascii", errors="ignore")
            .str.decode("utf-8")
        )
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _create_stopwords_file(directory):
    with open(
        os.path.join(directory, "processed", "stopwords.txt"), "w", encoding="utf-8"
    ) as file:
        file.write("")
        file.close()


def _drop_na_columns_in_database_files(directory):

    sys.stdout.write("--INFO-- Dropping NA columns in database files\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        data = data.dropna(axis=1, how="all")
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _format_columns_names_in_database_files(directory):
    """Format column names in database files."""

    sys.stdout.write("--INFO-- Formating column names in database files\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        data = data.rename(
            columns={
                col: col.replace(".", "").replace(" ", "_").lower()
                for col in data.columns
            }
        )
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _apply_scopus2tags_to_database_files(directory):

    sys.stdout.write("--INFO-- Applying scopus tags to database files\n")

    scopus2tags = _load_scopus2tags_as_dict()
    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        data.rename(columns=scopus2tags, inplace=True)
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _load_scopus2tags_as_dict():
    module_path = os.path.dirname(__file__)
    file_path = os.path.join(module_path, "files/scopus2tags.csv")
    names_dict = {}
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.replace("\n", "").split(",")
            name = line[0].strip()
            tag = line[1].strip()
            names_dict[name] = tag

    return names_dict


def _create_database_files(directory):
    folders = os.listdir(os.path.join(directory, "raw"))
    folders = [f for f in folders if os.path.isdir(os.path.join(directory, "raw", f))]
    for folder in folders:
        data = _concat_raw_csv_files(os.path.join(directory, "raw", folder))
        data.to_csv(
            os.path.join(directory, "processed", "_" + folder + ".csv"),
            sep=",",
            encoding="utf-8",
            index=False,
        )


def _concat_raw_csv_files(path):
    """Load raw csv files in a directory."""

    sys.stdout.write(f"--INFO-- Concatenating raw files in {path}/\n")

    files = [f for f in os.listdir(path) if f.endswith(".csv")]
    if len(files) == 0:
        raise FileNotFoundError(f"No CSV files found in {path}")
    data = []
    for file_name in files:
        data.append(
            pd.read_csv(
                os.path.join(path, file_name),
                encoding="utf-8",
                error_bad_lines=False,
                warn_bad_lines=True,
            )
        )

    data = pd.concat(data, ignore_index=True)
    data = data.drop_duplicates()

    return data


def _create_working_directories(directory):
    if not os.path.exists(os.path.join(directory, "processed")):
        os.makedirs(os.path.join(directory, "processed"))
    if not os.path.exists(os.path.join(directory, "reports")):
        os.makedirs(os.path.join(directory, "reports"))


# def _process__affiliations__column(documents):
#     if "affiliations" in documents.columns:
#         documents = documents.copy()
#         documents["countries"] = map_(documents, "affiliations", extract_country)

#         documents["countries"] = documents.countries.map(
#             lambda w: "; ".join(set(w.split("; "))) if isinstance(w, str) else w
#         )
#     return documents


# ----< Local references >-----------------------------------------------------


def _make_documents(scopus, cited_by, references):

    links_scopus = scopus.Link.copy()
    links_cited_by = cited_by.Link.copy()
    links_references = references.Link.copy()

    links_cited_by_unique = set(links_cited_by) - set(links_scopus)
    links_references_unique = set(links_references) - set(links_scopus)
    links_cited_by_common = set(links_scopus) & set(links_cited_by)
    links_references_common = set(links_scopus) & set(links_references)

    # citing documents not in the main collection
    cited_by.index = cited_by.Link
    cited_by = cited_by.loc[links_cited_by_unique, :]
    cited_by["main_group"] = False
    cited_by["citing_group"] = True
    cited_by["references_group"] = False

    # references not in the main collection
    references.index = references.Link
    references = references.loc[links_references_unique, :]
    references["main_group"] = False
    references["citing_group"] = False
    references["references_group"] = True
    references.loc[:, "References"] = np.nan

    scopus.index = scopus.Link
    scopus["main_group"] = True
    scopus["citing_group"] = False
    scopus["references_group"] = False
    scopus.loc[links_cited_by_common, "citing_group"] = True
    scopus.loc[links_references_common, "references_group"] = True

    documents = pd.concat(
        [
            scopus,
            cited_by,
            references,
        ],
        ignore_index=True,
    )

    documents = documents.reset_index(drop=True)

    documents["main_group"] = documents.main_group.astype(bool)
    documents["citing_group"] = documents.citing_group.astype(bool)
    documents["references_group"] = documents.references_group.astype(bool)

    return documents

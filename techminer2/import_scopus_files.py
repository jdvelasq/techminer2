"""
Import Scopus Files
===============================================================================

Import a scopus file to a working directory.

>>> from techminer2 import *
>>> directory = "data/"
>>> import_scopus_files(directory, disable_progress_bar=True)
- INFO - 248 raw records found in data/raw/documents.
- INFO - Searching local references using DOI ...
- INFO - Searching local references using document titles ...
- INFO - Consolidating local references ...
- INFO - Computing local citations ...
- INFO - Computing Bradford Law Zones ...
- INFO - Main abstract texts saved to data/processed/abstracts.csv
- INFO - Creating institutions thesaurus ...
- INFO - Affiliations without country detected - check file data/processed/ignored_affiliations.txt
- INFO - Affiliations without country detected - check file data/ignored_affiliations.txt
- INFO - Thesaurus file 'data/processed/institutions.txt' created.
- INFO - Creating keywords thesaurus ...
- INFO - Thesaurus file 'data/processed/keywords.txt' created.
- INFO - Applying thesaurus to institutions ...
- INFO - Extract and cleaning institutions.
- INFO - Extracting institution of first author ...
- INFO - Documents saved/merged to 'data/processed/documents.csv'
- INFO - The thesaurus was applied to institutions.
- INFO - Applying thesaurus to 'raw_author_keywords' column ...
- INFO - Applying thesaurus to 'raw_index_keywords' column...
- INFO - Applying thesaurus to 'raw_nlp_document_title' column...
- INFO - Applying thesaurus to 'raw_nlp_abstract' column...
- INFO - Applying thesaurus to 'raw_nlp_phrases' column...
- INFO - Documents saved/merged to 'data/processed/documents.csv'
- INFO - The thesaurus was applied to all keywords.
- INFO - Process finished!!!


"""


import os
import os.path

# -----< NLP Phrases >----------------------------------------------
import string

import numpy as np
import pandas as pd
import yaml
from nltk.tokenize import sent_tokenize
from textblob import TextBlob
from tqdm import tqdm

from . import logging
from ._read_raw_csv_files import read_raw_csv_files
from ._read_records import read_all_records
from .clean_institutions import clean_institutions
from .clean_keywords import clean_keywords
from .create_institutions_thesaurus import create_institutions_thesaurus
from .create_keywords_thesaurus import create_keywords_thesaurus
from .extract_country import extract_country
from .map_ import map_


def import_scopus_files(
    directory="./",
    use_nlp_phrases=False,
    disable_progress_bar=False,
):
    _check_output_folders(directory)
    _create_documents_csv_file(directory, disable_progress_bar)
    _create_abstracts_csv_file(directory)
    _create_stopwords_file(directory)
    _create_filter_file(directory)
    create_institutions_thesaurus(directory=directory)
    create_keywords_thesaurus(
        directory=directory,
        use_nlp_phrases=use_nlp_phrases,
    )
    clean_institutions(directory=directory)
    clean_keywords(directory=directory)
    logging.info("Process finished!!!")


def _check_output_folders(directory):
    if not os.path.exists(os.path.join(directory, "processed")):
        os.makedirs(os.path.join(directory, "processed"))
    if not os.path.exists(os.path.join(directory, "reports")):
        os.makedirs(os.path.join(directory, "reports"))


def _create_filter_file(directory):

    documents = read_all_records(directory)

    filter_ = {}
    filter_["first_year"] = int(documents.pub_year.min())
    filter_["last_year"] = int(documents.pub_year.max())
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


def _create_stopwords_file(directory):
    open(
        os.path.join(directory, "processed", "stopwords.txt"),
        "a",
        encoding="utf-8",
    ).close()


def _create_abstracts_csv_file(directory):

    documents = read_all_records(directory)

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
        logging.info(f"Main abstract texts saved to {file_name}")

    else:

        logging.info(f"`abstract` column not found in  `processed/documents.csv` file")


def _create_documents_csv_file(directory, disable_progress_bar):
    documents = read_raw_csv_files(os.path.join(directory, "raw", "documents"))
    documents = documents.dropna(axis=1, how="all")
    documents = _delete_and_rename_columns(documents)
    documents = _process__abstract__column(documents)
    documents = _process__document_title__column(documents)
    documents = _remove_accents(documents)
    documents = _process__authors_id__column(documents)
    documents = _process__raw_authors_names__column(documents)
    documents = _disambiguate_authors(documents)
    documents = _process__doi__column(documents)
    documents = _process__source_name__column(documents)
    documents = _process__iso_source_name__column(documents)
    documents = _search_for_new_iso_source_name(documents)
    documents = _complete__iso_source_name__colum(documents)
    documents = _repair__iso_source_name__column(documents)
    documents = _create__record_no__column(documents)
    documents = _create__document_id__column(documents)
    documents = _process__document_type__column(documents)
    documents = _process__affiliations__column(documents)
    documents = _process__author_keywords__column(documents)
    documents = _process__index_keywords__column(documents)
    documents = _create__keywords__column(documents)
    documents = _create__nlp_phrases__column(documents)
    documents = _process__global_citations__column(documents)
    documents = _process__global_references__column(documents)
    documents = _process__eissn__column(documents)
    documents = _process__issn__column(documents)
    documents = documents.assign(local_references=[[] for _ in range(len(documents))])
    documents = _create_local_references_using_doi(
        documents, disable_progress_bar=disable_progress_bar
    )
    documents = _create_local_references_using_title(
        documents, disable_progress_bar=disable_progress_bar
    )
    documents = _consolidate_local_references(documents)
    documents = _compute_local_citations(documents)
    documents = _compute_bradford_law_zones(documents)

    documents.to_csv(
        os.path.join(directory, "processed", "documents.csv"),
        sep=",",
        encoding="utf-8",
        index=False,
    )


def _check_nlp_phrase(phrase):

    valid_tag_types = [
        ["JJ", "JJ", "NN"],
        ["JJ", "JJ", "NNS"],
        ["JJ", "NN", "NN", "NN"],
        ["JJ", "NN", "NN"],
        ["JJ", "NN", "NNS"],
        ["JJ", "NN"],
        ["JJ", "NNS", "NN"],
        ["JJ", "NNS"],
        ["JJ"],
        ["NN", "CC", "NN"],
        ["NN", "CD"],
        ["NN", "IN", "NN"],
        ["NN", "IN", "NNS"],
        ["NN", "JJ", "NN"],
        ["NN", "NN", "NN"],
        ["NN", "NN", "NNS"],
        ["NN", "NN"],
        ["NN", "NNS"],
        ["NN", "TO", "VB"],
        ["NN", "VBG"],
        ["NN"],
        ["VBG", "NN"],
        ["VBG", "NNS"],
        ["VBG"],
        ["VBN", "NN", "NN"],
        ["VBN", "NN"],
    ]

    if phrase[0] in string.punctuation:
        return False

    if phrase[0].isdigit():
        return False

    tags = [tag[1] for tag in TextBlob(phrase).tags]

    if tags not in valid_tag_types:
        return False

    return True


# -----< Dataset Trasformations >----------------------------------------------
def _delete_and_rename_columns(documents):
    documents = documents.copy()

    module_path = os.path.dirname(__file__)
    file_path = os.path.join(module_path, "files/scopus2tags.csv")

    columns_to_tags = {}
    columns_to_delete = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.replace("\n", "").split(",")
            name = line[0].strip()
            if len(line) == 2:
                tag = line[1].strip()
                columns_to_tags[name] = tag
            else:
                columns_to_delete.append(name)

    documents.rename(columns=columns_to_tags, inplace=True)
    documents.drop(columns=columns_to_delete, errors="ignore", inplace=True)

    return documents


def _remove_accents(documents):
    documents = documents.copy()
    cols = documents.select_dtypes(include=[np.object]).columns
    documents[cols] = documents[cols].apply(
        lambda x: x.str.normalize("NFKD")
        .str.encode("ascii", errors="ignore")
        .str.decode("utf-8")
    )

    return documents


# -----< Isolated Column Processing >------------------------------------------


def _process__document_type__column(documents):
    if "document_type" in documents.columns:
        documents = documents.copy()
        documents["document_type"] = documents.document_type.str.replace(" ", "_")
        documents["document_type"] = documents.document_type.str.lower()
    return documents


def _process__abstract__column(documents):
    if "abstract" in documents.columns:
        # ---------------------------------------------------------------------
        module_path = os.path.dirname(__file__)
        file_path = os.path.join(module_path, "files/nlp_phrases.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            nlp_stopwords = [line.strip() for line in file]
        # ---------------------------------------------------------------------
        documents = documents.copy()
        documents.abstract = documents.abstract.str.lower()
        documents.loc[
            documents.abstract == "[no abstract available]", "abstract"
        ] = pd.NA
        documents.abstract = documents.abstract.map(
            lambda x: x[0 : x.find("\u00a9")] if not pd.isna(x) else x
        )
        documents = documents.assign(
            raw_nlp_abstract=documents.abstract.map(
                lambda x: "; ".join(
                    [
                        phrase
                        for phrase in TextBlob(x).noun_phrases
                        if phrase not in nlp_stopwords
                        and _check_nlp_phrase(phrase) is True
                    ]
                )
                if pd.isna(x) is False
                else x
            )
        )
    return documents


def _process__affiliations__column(documents):
    if "affiliations" in documents.columns:
        documents = documents.copy()
        documents["countries"] = map_(documents, "affiliations", extract_country)
        documents["country_1st_author"] = documents.countries.map(
            lambda w: w.split("; ")[0] if isinstance(w, str) else w
        )
        documents["countries"] = documents.countries.map(
            lambda w: "; ".join(set(w.split("; "))) if isinstance(w, str) else w
        )
    return documents


def _process__author_keywords__column(documents):
    if "raw_author_keywords" in documents.columns:
        documents = documents.copy()
        documents.raw_author_keywords = documents.raw_author_keywords.str.lower()
    return documents


def _process__authors_id__column(documents):
    documents = documents.copy()
    documents["authors_id"] = documents.authors_id.map(
        lambda w: pd.NA if w == "[No author id available]" else w
    )
    documents["authors_id"] = documents.authors_id.map(
        lambda x: x[:-1] if isinstance(x, str) and x[-1] == ";" else x
    )
    return documents


def _process__document_title__column(documents):
    documents = documents.copy()
    documents.document_title = documents.document_title.map(
        lambda x: x[0 : x.find("[")] if pd.isna(x) is False and x[-1] == "]" else x
    )
    # ---------------------------------------------------------------------
    module_path = os.path.dirname(__file__)
    file_path = os.path.join(module_path, "files/nlp_phrases.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        nlp_stopwords = [line.strip() for line in file]
    # ---------------------------------------------------------------------
    documents = documents.assign(
        raw_nlp_document_title=documents.document_title.map(
            lambda x: "; ".join(
                [
                    phrase
                    for phrase in TextBlob(x).noun_phrases
                    if phrase not in nlp_stopwords and _check_nlp_phrase(phrase) is True
                ]
            )
            if pd.isna(x) is False
            else x
        )
    )
    return documents


def _process__doi__column(documents):
    if "doi" in documents.columns:
        documents = documents.copy()
        documents.doi = documents.doi.str.upper()
    return documents


def _process__eissn__column(documents):
    if "eissn" in documents.columns:
        documents = documents.copy()
        documents.eissn = documents.eissn.str.replace("-", "", regex=True)
        documents.eissn = documents.eissn.str.upper()
    return documents


def _process__global_citations__column(documents):
    documents = documents.copy()
    documents.global_citations = documents.global_citations.fillna(0)
    documents.global_citations = documents.global_citations.astype(int)
    return documents


def _process__global_references__column(documents):
    if "global_references" in documents.columns:
        documents = documents.copy()
        documents["global_references"] = documents.global_references.map(
            lambda w: w.replace("https://doi.org/", "") if isinstance(w, str) else w
        )
        documents["global_references"] = documents.global_references.map(
            lambda w: w.replace("http://dx.doi.org/", "") if isinstance(w, str) else w
        )
        documents["num_global_references"] = documents.global_references.map(
            lambda x: len(x.split("; ")) if not pd.isna(x) else 0
        )
    return documents


def _process__index_keywords__column(documents):
    if "raw_index_keywords" in documents.columns:
        documents = documents.copy()
        documents.raw_index_keywords = documents.raw_index_keywords.str.lower()
    return documents


def _create__keywords__column(documents):
    # -----------------------------------------------------------------------------------
    def augment_list(documents, topics):
        documents = documents.copy()
        topics = topics.str.split(";")
        topics = topics.map(
            lambda x: [w.strip() for w in x] if isinstance(x, list) else x
        )
        documents = documents.assign(
            raw_keywords=documents.raw_keywords
            + topics.map(lambda x: x if isinstance(x, list) else [])
        )
        return documents

    # -----------------------------------------------------------------------------------
    documents = documents.assign(raw_keywords=[[] for _ in range(len(documents))])

    if "raw_index_keywords" in documents.columns:
        documents = augment_list(
            documents=documents, topics=documents.raw_index_keywords.copy()
        )

    if "raw_author_keywords" in documents.columns:
        documents = augment_list(
            documents=documents, topics=documents.raw_author_keywords.copy()
        )

    documents.raw_keywords = documents.raw_keywords.map(
        lambda x: "; ".join(sorted(set(x))) if isinstance(x, list) else x
    )

    documents.raw_keywords = documents.raw_keywords.map(
        lambda x: pd.NA if len(x) == 0 else x
    )

    return documents


def _create__nlp_phrases__column(documents):
    # -----------------------------------------------------------------------------------
    def augment_list(documents, topics):
        documents = documents.copy()
        topics = topics.str.split(";")
        topics = topics.map(
            lambda x: [w.strip() for w in x] if isinstance(x, list) else x
        )
        documents = documents.assign(
            raw_nlp_phrases=documents.raw_nlp_phrases
            + topics.map(lambda x: x if isinstance(x, list) else [])
        )
        return documents

    # -----------------------------------------------------------------------------------
    documents = documents.assign(raw_nlp_phrases=[[] for _ in range(len(documents))])

    if "raw_index_keywords" in documents.columns:
        documents = augment_list(
            documents=documents, topics=documents.raw_index_keywords.copy()
        )

    if "raw_author_keywords" in documents.columns:
        documents = augment_list(
            documents=documents, topics=documents.raw_author_keywords.copy()
        )

    if "raw_nlp_document_title" in documents.columns:
        documents = augment_list(
            documents=documents, topics=documents.raw_nlp_document_title.copy()
        )

    if "raw_nlp_abstract" in documents.columns:
        documents = augment_list(
            documents=documents, topics=documents.raw_nlp_abstract.copy()
        )

    documents.raw_nlp_phrases = documents.raw_nlp_phrases.map(
        lambda x: "; ".join(sorted(set(x))) if isinstance(x, list) else x
    )

    documents.raw_nlp_phrases = documents.raw_nlp_phrases.map(
        lambda x: pd.NA if len(x) == 0 else x
    )

    return documents


def _process__iso_source_name__column(documents):
    if "ISO_Source_Name" in documents.columns:
        documents = documents.copy()
        documents.ISO_Source_Name = documents.ISO_Source_Name.str.upper()
        documents.ISO_Source_Name = documents.ISO_Source_Name.map(
            lambda x: x.replace(".", "") if not pd.isna(x) else x
        )
    return documents


def _search_for_new_iso_source_name(documents):
    # search new iso source names not included in files/iso_source_names.csv
    if "ISO_Source_Name" in documents.columns:

        # iso souce names in the current file
        documents = documents.copy()
        documents.ISO_Source_Name = documents.ISO_Source_Name.str.upper()
        documents.ISO_Source_Name = documents.ISO_Source_Name.map(
            lambda x: x.replace(".", "") if not pd.isna(x) else x
        )
        current_iso_names = documents[["source_name", "ISO_Source_Name"]].copy()
        current_iso_names = current_iso_names.assign(
            source_name=current_iso_names.source_name.str.strip()
        )
        current_iso_names = current_iso_names.assign(
            iso_source_name=current_iso_names.ISO_Source_Name.str.strip()
        )
        current_iso_names = current_iso_names.dropna()
        current_iso_names = current_iso_names.sort_values(
            by=["source_name", "ISO_Source_Name"]
        )
        current_iso_names = current_iso_names.drop_duplicates("source_name")

        # adds the abbreviations the the current file
        module_path = os.path.dirname(__file__)
        file_path = os.path.join(module_path, "files/iso_source_names.csv")
        pdf = pd.read_csv(file_path, sep=",")
        pdf = pd.concat([pdf, current_iso_names])
        pdf = pdf.sort_values(by=["source_name", "ISO_Source_Name"])
        pdf = pdf.drop_duplicates("source_name")
        pdf.to_csv(file_path, index=False)
    return documents


def _complete__iso_source_name__colum(documents):

    if "ISO_Source_Name" in documents.columns:
        #
        # Loads existent iso source names and make a dictionary
        # to translate source names to iso source names
        #
        module_path = os.path.dirname(__file__)
        file_path = os.path.join(module_path, "files/iso_source_names.csv")
        pdf = pd.read_csv(file_path, sep=",")
        existent_names = dict(zip(pdf.source_name, pdf.ISO_Source_Name))

        # complete iso source names
        documents = documents.copy()
        documents.ISO_Source_Name = [
            abb
            if not pd.isna(abb)
            else (existent_names[name] if name in existent_names.keys() else abb)
            for name, abb in zip(documents.source_name, documents.ISO_Source_Name)
        ]
    return documents


def _repair__iso_source_name__column(documents):
    if "ISO_Source_Name" in documents.columns:
        documents = documents.copy()
        documents.ISO_Source_Name = [
            "--- " + name[:25] if pd.isna(abb) and not pd.isna(name) else abb
            for name, abb in zip(documents.source_name, documents.ISO_Source_Name)
        ]
        documents = documents.assign(
            iso_source_name=documents.ISO_Source_Name.map(
                lambda x: x[:29] if isinstance(x, str) else x
            )
        )
    return documents


def _process__issn__column(documents):
    if "issn" in documents.columns:
        documents = documents.copy()
        documents["issn"] = documents.issn.astype(str)
        documents.issn = documents.issn.str.replace("-", "", regex=True)
        documents.issn = documents.issn.str.upper()
    return documents


def _process__raw_authors_names__column(documents):
    documents = documents.copy()
    if "raw_authors_names" in documents.columns:
        documents.raw_authors_names = documents.raw_authors_names.map(
            lambda x: pd.NA if x == "[No author name available]" else x
        )

        documents.raw_authors_names = documents.raw_authors_names.str.replace(
            ", ", "; ", regex=False
        )
        documents.raw_authors_names = documents.raw_authors_names.str.replace(
            ".", "", regex=False
        )

        documents["num_authors"] = documents.raw_authors_names.apply(
            lambda x: len(x.split(";")) if not pd.isna(x) else 0
        )
        documents["frac_num_documents"] = documents.raw_authors_names.map(
            lambda x: 1.0 / len(x.split(";")) if not pd.isna(x) else 0
        )

    return documents


def _process__source_name__column(documents):
    documents = documents.copy()
    if "source_name" in documents.columns:
        documents.source_name = documents.source_name.str.upper()
        documents.source_name = documents.source_name.str.replace(
            r"[^\w\s]", "", regex=True
        )
    return documents


# ----< Drop duplicates >------------------------------------------------------


def _drop_duplicates(documents):
    documents = documents.copy()
    if "doi" in documents.columns:
        duplicated_doi = (documents.doi.duplicated()) & (~documents.doi.isna())
        documents = documents[~duplicated_doi]

    if (
        "authors" in documents.columns
        and "document_title" in documents.columns
        and "pub_year" in documents.columns
        and "source_name" in documents.columns
    ):
        subset = ("authors", "document_title", "pub_year", "source_name")
        documents = documents.drop_duplicates(subset=subset)
    return documents


def _report_duplicate_titles(raw_data, directory):
    duplicates = (
        raw_data.document_title.duplicated(keep=False) & ~raw_data.document_title.isna()
    )
    if duplicates.any():
        file_name = directory + "duplicates.csv"
        duplicates = raw_data[duplicates].copy()
        duplicates = duplicates.sort_values(by=["document_title"])
        duplicates.to_csv(file_name, sep=",", encoding="utf-8", index=False)
        logging.info(
            f"Duplicate rows found in {directory}documents.csv - Records saved to {file_name}"
        )


def _create__record_no__column(documents):
    documents = documents.copy()
    documents = documents.assign(
        record_no=documents.sort_values("global_citations", ascending=False)
        .groupby("pub_year")
        .cumcount()
    )
    documents = documents.assign(
        record_no=documents.record_no.map(lambda x: str(x).zfill(4))
    )
    documents = documents.assign(
        record_no=documents.pub_year.astype(str) + "-" + documents.record_no
    )

    return documents


# ----< Local references >-----------------------------------------------------
def _create_local_references_using_doi(documents, disable_progress_bar=False):

    if "global_references" in documents.columns:
        logging.info("Searching local references using DOI ...")
        documents = documents.copy()
        with tqdm(total=len(documents.doi), disable=disable_progress_bar) as pbar:
            for i_index, doi in zip(documents.index, documents.doi):
                if not pd.isna(doi):
                    doi = doi.upper()
                    for j_index, references in zip(
                        documents.index, documents.global_references.tolist()
                    ):
                        if pd.isna(references) is False and doi in references.upper():
                            documents.at[j_index, "local_references"].append(
                                documents.record_no[i_index]
                            )
                pbar.update(1)
    return documents


def _create_local_references_using_title(documents, disable_progress_bar=False):

    if "global_references" in documents.columns:
        logging.info("Searching local references using document titles ...")
        documents = documents.copy()

        with tqdm(
            total=len(documents.document_title), disable=disable_progress_bar
        ) as pbar:

            for i_index in documents.index:

                document_title = documents.document_title[i_index].lower()
                pub_year = documents.pub_year[i_index]

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
                                and str(pub_year) in reference
                            ):

                                documents.at[j_index, "local_references"] += [
                                    documents.record_no[i_index]
                                ]
                pbar.update(1)

    return documents


def _consolidate_local_references(documents):
    logging.info("Consolidating local references ...")
    documents["local_references"] = documents.local_references.apply(
        lambda x: sorted(set(x))
    )
    documents["local_references"] = documents.local_references.apply(
        lambda x: "; ".join(x) if isinstance(x, list) else x
    )
    return documents


def _compute_local_citations(documents):
    """
    Computes local citations.

    """
    logging.info("Computing local citations ...")

    documents = documents.assign(
        local_references=[
            None if len(local_reference) == 0 else local_reference
            for local_reference in documents.local_references
        ]
    )

    local_references = documents[["local_references"]]
    local_references = local_references.rename(
        columns={"local_references": "local_citations"}
    )
    local_references = local_references.dropna()

    local_references["local_citations"] = local_references.local_citations.map(
        lambda w: w.split("; ")
    )
    local_references = local_references.explode("local_citations")
    local_references = local_references.groupby(
        by="local_citations", as_index=True
    ).size()
    documents["local_citations"] = 0
    documents.index = documents.record_no
    documents.loc[local_references.index, "local_citations"] = local_references
    documents.index = list(range(len(documents)))

    return documents


def _compute_bradford_law_zones(documents):
    """
    Computes bradford law zones.

    """
    logging.info("Computing Bradford Law Zones ...")
    documents = documents.copy()

    # Counts number of documents per source_name
    documents_per_source = documents[
        [
            "source_name",
            "record_no",
        ]
    ].copy()
    documents_per_source = documents_per_source.assign(num_documents=1)
    documents_per_source = documents_per_source.groupby(
        "source_name", as_index=False
    ).agg({"num_documents": np.sum})
    documents_per_source = documents_per_source[["source_name", "num_documents"]]
    documents_per_source = documents_per_source.sort_values(
        ["num_documents"], ascending=False
    )
    documents_per_source[
        "cum_num_documents"
    ] = documents_per_source.num_documents.cumsum()

    dict_ = dict(
        zip(documents_per_source.source_name, documents_per_source.num_documents)
    )

    # Bradford law zones (1, 2, 3)
    bradford_core_sources = int(len(documents) / 3)
    documents_per_source["zone"] = documents_per_source.cum_num_documents.map(
        lambda x: 3
        if x > 2 * bradford_core_sources
        else (2 if x > bradford_core_sources else 1)
    )

    # Assigns zone to each document
    dict_ = dict(zip(documents_per_source.source_name, documents_per_source.zone))

    documents["bradford_law_zone"] = documents.source_name.map(
        lambda x: dict_[x], na_action="ignore"
    )

    return documents


def _disambiguate_authors(documents):

    # pylint: disable=unsubscriptable-object
    authors_ids = documents[["raw_authors_names", "authors_id"]].copy()
    authors_ids = authors_ids.dropna()
    authors_ids = {
        b: a for a, b in zip(authors_ids.raw_authors_names, authors_ids.authors_id)
    }
    authors_ids = {
        k: list(zip(k.split(";"), v.split("; "))) for k, v in authors_ids.items()
    }
    pdf = pd.DataFrame(
        {
            "authors_full": list(authors_ids.values()),
        }
    )
    pdf = pdf.explode("authors_full")
    pdf = pdf.drop_duplicates()
    pdf = pdf.assign(name=pdf.authors_full.map(lambda x: x[1]))
    pdf = pdf.assign(id=pdf.authors_full.map(lambda x: x[0]))
    pdf = pdf.reset_index()
    pdf = pdf.assign(
        counter=pdf.sort_values("id", ascending=True).groupby(["name"]).cumcount()
    )

    pdf = pdf.assign(name=pdf.name + "/" + pdf.counter.astype(str))
    new_names = dict(zip(pdf.id, pdf.name))

    #
    documents_names = documents.authors_id.copy()
    documents_names = documents_names.map(
        lambda x: x.split(";") if not pd.isna(x) else x
    )
    documents_names = documents_names.map(
        lambda x: "; ".join([new_names[y] for y in x]) if isinstance(x, list) else x
    )
    documents_names = documents_names.str.replace("/0", "")
    documents["authors"] = documents_names.copy()

    return documents


def _create__document_id__column(documents):

    wos_ref = documents.authors.map(
        lambda x: x.split("; ")[0].strip() if not pd.isna(x) else "[anonymous]"
    )

    wos_ref = wos_ref + documents.authors.map(
        lambda x: (" et al" if len(x.split("; ")) > 0 else "") if not pd.isna(x) else ""
    )

    wos_ref = wos_ref + ", " + documents.pub_year.map(str)
    wos_ref = wos_ref + ", " + documents.iso_source_name
    documents["document_id"] = wos_ref.copy()
    return documents


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

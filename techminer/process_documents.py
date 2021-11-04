"""
Records file processing.
===============================================================================
"""

import os
from os.path import isfile

import numpy as np
import pandas as pd
import yaml

from .clean_institution_fields import clean_institution_fields
from .clean_keywords_fields import clean_keywords_fields
from .create_institutions_thesaurus import create_institutions_thesaurus
from .create_keywords_thesaurus import create_keywords_thesaurus
from .utils import explode, load_documents, logging, save_records_to_project_directory

# from techminer.utils.explode import explode


def _create_document_id(documents):
    """
    Creates record id.

    """
    documents = documents.assign(
        document_id=documents.sort_values("global_citations", ascending=False)
        .groupby("pub_year")
        .cumcount()
        + 1
    )
    documents = documents.assign(
        document_id=documents.record_id.map(lambda x: str(x).zfill(4))
    )
    documents = documents.assign(
        document_id=documents.pub_year.astype(str) + "-" + documents.record_id
    )
    return documents


def _create_local_references_using_doi(records):
    """
    Creates local references using DOI.

    """
    logging.info("Searching local references using DOI ...")

    for i_index, doi in enumerate(records.doi):
        if not pd.isna(doi):
            doi = doi.upper()
            for j_index, references in enumerate(records.global_references.tolist()):
                if pd.isna(references) is False and doi in references.upper():
                    records.at[j_index, "local_references"].append(
                        records.record_id[i_index]
                    )
    return records


def _create_local_references_using_title(records):
    """
    Creates local references.

    """
    logging.info("Searching local references using document titles ...")

    for i_index, _ in enumerate(records.document_title):

        document_title = records.document_title[i_index].lower()
        pub_year = records.pub_year[i_index]

        for j_index, references in enumerate(records.global_references.tolist()):

            if pd.isna(references) is False and document_title in references.lower():

                for reference in references.split(";"):

                    if (
                        document_title in reference.lower()
                        and str(pub_year) in reference
                    ):

                        records.at[j_index, "local_references"] += [
                            records.record_id[i_index]
                        ]
    return records


def _consolidate_local_references(records):
    """
    Consolidates local references.

    """
    logging.info("Consolidating local references ...")
    records = records.assign(local_references=[[] for _ in range(len(records))])
    records["local_references"] = records.local_references.apply(
        lambda x: sorted(set(x))
    )
    records["local_references"] = records.local_references.apply(
        lambda x: "; ".join(x) if isinstance(x, list) else x
    )
    return records


def _compute_local_citations(records):
    """
    Computes local citations.

    """
    logging.info("Computing local citations ...")

    records = records.assign(
        local_references=[
            None if len(local_reference) == 0 else local_reference
            for local_reference in records.local_references
        ]
    )

    local_references = records[["local_references"]]
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
    records["local_citations"] = 0
    records.index = records.record_id
    records.loc[local_references.index, "local_citations"] = local_references
    records.index = list(range(len(records)))

    return records


def _compute_bradford_law_zones(records):
    """
    Computes bradford law zones.

    """
    logging.info("Computing Bradford Law Zones ...")

    x = records.copy()

    #
    # Counts number of documents per publication_name
    #
    x["num_documents"] = 1
    x = explode(
        x[
            [
                "publication_name",
                "num_documents",
                "record_id",
            ]
        ],
        "publication_name",
        sep=None,
    )
    m = x.groupby("publication_name", as_index=False).agg(
        {
            "num_documents": np.sum,
        }
    )
    m = m[["publication_name", "num_documents"]]
    m = m.sort_values(["num_documents"], ascending=False)
    m["cum_num_documents"] = m.num_documents.cumsum()
    dict_ = {
        source_title: num_documents
        for source_title, num_documents in zip(m.publication_name, m.num_documents)
    }

    #
    # Number of source titles by number of documents
    #
    g = m[["num_documents"]]
    g = g.assign(num_publications=1)
    g = g.groupby(["num_documents"], as_index=False).agg(
        {
            "num_publications": np.sum,
        }
    )
    g["total_num_documents"] = g["num_documents"] * g["num_publications"]
    g = g.sort_values(["num_documents"], ascending=False)
    g["cum_num_documents"] = g["total_num_documents"].cumsum()

    #
    # Bradford law zones
    #
    bradford_core_sources = int(len(records) / 3)
    g["bradford_law_zone"] = g["cum_num_documents"]
    g["bradford_law_zone"] = g.bradford_law_zone.map(
        lambda w: 3
        if w > 2 * bradford_core_sources
        else (2 if w > bradford_core_sources else 1)
    )

    bradford_dict = {
        num_documents: zone
        for num_documents, zone in zip(g.num_documents, g.bradford_law_zone)
    }

    #
    # Computes bradford zone for each document
    #
    records["bradford_law_zone"] = records.publication_name

    records["bradford_law_zone"] = records.bradford_law_zone.map(
        lambda x: dict_[x.strip()], na_action="ignore"
    )
    records["bradford_law_zone"] = records.bradford_law_zone.map(
        lambda x: bradford_dict[x], na_action="ignore"
    )

    records["bradford_law_zone"] = records.bradford_law_zone.fillna(3)

    return records


def _update_filter_file(documents, directory):

    yaml_filename = os.path.join(directory, "filter.yaml")

    if isfile(yaml_filename):
        with open(yaml_filename, "r", encoding="utf-8") as yaml_file:
            filter_ = yaml.load(yaml_file, Loader=yaml.FullLoader)
    else:
        filter_ = {}

    filter_["years"] = [0, documents.year.max()]
    filter_["citations"] = [0, documents.global_citations.max()]
    filter_["bradford"] = [1, documents.bradford_law_zone.max()]

    document_types = documents.document_type.unique()
    for document_type in document_types:
        document_type = document_type.lower()
        document_type = document_type.replace(" ", "_")
        filter_[document_type] = True

    with open(yaml_filename, "wt", encoding="utf-8") as yaml_file:
        yaml.dump(filter_, yaml_file, sort_keys=True)


def process_records(directory):
    """
    This method is used to process the records

    :param directory:
    :return:
        None
    """
    if directory[-1] != "/":
        directory += "/"

    stopwords_file = directory + "stopwords.txt"

    # pylint: disable=consider-using-with
    open(stopwords_file, "a", encoding="utf-8").close()

    logging.info("Processing records ...")

    create_institutions_thesaurus(records_path=directory)
    create_keywords_thesaurus(records_path=directory)

    records = load_documents(documents_directory=directory)
    records = _create_document_id(records)
    records = records.assign(local_references=[[] for _ in range(len(records))])
    records = _create_local_references_using_doi(records)
    records = _create_local_references_using_title(records)
    records = _consolidate_local_references(records)
    records = _compute_local_citations(records)
    records = _compute_bradford_law_zones(records)
    save_records_to_directory(records, records_path=records_path)

    clean_institution_fields(records_path=records_path)
    clean_keywords_fields(records_path=records_path)

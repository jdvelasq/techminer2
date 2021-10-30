from os.path import isfile

import numpy as np
import pandas as pd
from techminer.data.create_institutions_thesaurus import create_institutions_thesaurus
from techminer.data.create_keywords_thesaurus import create_keywords_thesaurus
from techminer.features.apply_institutions_thesaurus import apply_institutions_thesaurus
from techminer.features.apply_keywords_thesaurus import apply_keywords_thesaurus
from techminer.utils import logging
from techminer.utils.explode import explode


class DatastoreTransformations:
    """
    This class is used to transform the data from the records
    """

    def __init__(self, directory="./"):
        """
        This method is used to initialize the class
        :param directory:
        :return:
        """
        self.records = None
        self.directory = directory
        if self.directory[-1] != "/":
            self.directory += "/"

    def load_records(self):
        """
        Loads records.

        """
        filename = self.directory + "records.csv"
        if isfile(filename):
            self.records = pd.read_csv(filename, sep=",", encoding="utf-8")
        else:
            self.records = pd.DataFrame()

        logging.info("Datastore " + filename + " loaded.")

    def create_historiograph_id(self):
        """
        Creates a new historiograph id.

        """
        logging.info("Generating historiograph ID ...")
        self.records = self.records.assign(
            historiograph_id=self.records.pub_year.map(str)
            + "-"
            + self.records.groupby(["pub_year"], as_index=False)["authors"]
            .cumcount()
            .map(str)
        )

    def delete_existent_local_references(self):
        """
        Deletes local references.

        """
        # if  "local_references" in self.records.columns:
        logging.info("Deleting existent local references ...")
        self.records["local_references"] = [[] for _ in range(len(self.records))]

    def create_local_references_using_doi(self):
        """
        Creates local references.

        """

        logging.info("Searching local references using DOI ...")

        for i_index, doi in enumerate(self.records.doi):
            if not pd.isna(doi):
                doi = doi.upper()
                for j_index, references in enumerate(
                    self.records.global_references.tolist()
                ):
                    if pd.isna(references) is False and doi in references.upper():
                        self.records.at[j_index, "local_references"].append(
                            self.records.historiograph_id[i_index]
                        )

    def create_local_references_using_title(self):
        """
        Creates local references.

        """
        logging.info("Searching local references using document titles ...")

        for i_index, _ in enumerate(self.records.document_title):

            document_title = self.records.document_title[i_index].lower()
            pub_year = self.records.pub_year[i_index]

            for j_index, references in enumerate(
                self.records.global_references.tolist()
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

                            self.records.at[j_index, "local_references"] += [
                                self.records.historiograph_id[i_index]
                            ]

    def compute_local_citations(self):
        """
        Computes local citations.

        """
        logging.info("Computing local citations ...")

        self.records = self.records.assign(
            local_references=[
                None if len(local_reference) == 0 else local_reference
                for local_reference in self.records.local_references
            ]
        )

        local_references = self.records[["local_references"]]
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
        self.records["local_citations"] = 0
        self.records.index = self.records.historiograph_id
        self.records.loc[local_references.index, "local_citations"] = local_references
        self.records.index = list(range(len(self.records)))

    def consolidate_local_references(self):
        """
        Consolidates local references.

        """
        logging.info("Consolidating local references ...")
        self.records["local_references"] = self.records.local_references.apply(
            lambda x: sorted(set(x))
        )
        self.records["local_references"] = self.records.local_references.apply(
            lambda x: "; ".join(x) if isinstance(x, list) else x
        )

    def compute_bradford_law_zones(self):
        """
        Computes bradford law zones.

        """
        logging.info("Computing Bradford Law Zones ...")

        self.records["id"] = range(len(self.records))

        x = self.records.copy()

        #
        # Counts number of documents per publication_name
        #
        x["num_documents"] = 1
        x = explode(
            x[
                [
                    "publication_name",
                    "num_documents",
                    "id",
                ]
            ],
            "publication_name",
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
        bradford_core_sources = int(len(self.records) / 3)
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
        self.records["bradford_law_zone"] = self.records.publication_name

        self.records["bradford_law_zone"] = self.records.bradford_law_zone.map(
            lambda w: dict_[w.strip()], na_action="ignore"
        )
        self.records["bradford_law_zone"] = self.records.bradford_law_zone.map(
            lambda w: bradford_dict[w], na_action="ignore"
        )

    def create_KW_exclude(self):
        filename = self.directory + "stopwords.txt"
        if not isfile(filename):
            open(filename, "a", encoding="utf-8").close()

    def save_records(self):
        """
        Saves records.

        """
        filename = self.directory + "records.csv"
        self.records.to_csv(filename, sep=",", encoding="utf-8", index=False)
        logging.info("Datastore saved to " + filename)


def process_records(directory):
    """
    This method is used to process the records

    :param directory:
    :return:
    """
    logging.info("Processing records ...")
    records = DatastoreTransformations(directory)
    records.load_records()
    records.create_historiograph_id()
    records.delete_existent_local_references()
    records.create_local_references_using_doi()
    records.create_local_references_using_title()
    records.consolidate_local_references()
    records.compute_local_citations()
    records.compute_bradford_law_zones()
    records.create_KW_exclude()
    #
    records.save_records()
    #
    create_institutions_thesaurus(directory=directory)
    apply_institutions_thesaurus(directory=directory)
    create_keywords_thesaurus(directory=directory)
    apply_keywords_thesaurus(directory=directory)
    logging

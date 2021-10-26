import logging
from os.path import exists, isfile

import numpy as np
import pandas as pd
from techminer.utils.apply_institutions_thesaurus import apply_institutions_thesaurus
from techminer.utils.create_institutions_thesaurus import create_institutions_thesaurus
from techminer.utils.create_keywords_thesaurus import create_keywords_thesaurus
from techminer.utils.explode import explode


class DatastoreTransformations:
    """
    This class is used to transform the data from the datastore
    """

    def __init__(self, datastorepath="./"):
        """
        This method is used to initialize the class
        :param datastorepath:
        :return:
        """
        self.datastore = None
        self.datastorepath = datastorepath
        if self.datastorepath[-1] != "/":
            self.datastorepath += "/"

    def load_datastore(self):
        """
        Loads datastore.

        """
        filename = self.datastorepath + "datastore.csv"
        logging.info("Loading datastore from %s", filename)
        if isfile(filename):
            self.datastore = pd.read_csv(filename, sep=",", encoding="utf-8")
        else:
            self.datastore = pd.DataFrame()

    def create_historiograph_id(self):
        """
        Creates a new historiograph id.

        """
        logging.info("Generating historiograph ID")
        self.datastore = self.datastore.assign(
            historiograph_id=self.datastore.pub_year.map(str)
            + "-"
            + self.datastore.groupby(["pub_year"], as_index=False)["authors"]
            .cumcount()
            .map(str)
        )

    def delete_existent_local_references(self):
        """
        Deletes local references.

        """
        if "local_references" in self.datastore.columns:
            logging.info("Deleting existent local references")
            self.datastore["local_references"] = [
                [] for _ in range(len(self.datastore))
            ]

    def create_local_references_using_doi(self):
        """
        Creates local references.

        """

        logging.info("Searching local references using DOI")

        for i_index, doi in enumerate(self.datastore.doi):
            if not pd.isna(doi):
                doi = doi.upper()
                for j_index, references in enumerate(
                    self.datastore.global_references.tolist()
                ):
                    if pd.isna(references) is False and doi in references.upper():
                        self.datastore.at[j_index, "local_references"].append(
                            self.datastore.historiograph_id[i_index]
                        )

    def create_local_references_using_title(self):
        """
        Creates local references.

        """
        logging.info("Searching local references using title")

        for i_index, _ in enumerate(self.datastore.document_title):

            document_title = self.datastore.document_title[i_index].lower()
            pub_year = self.datastore.pub_year[i_index]

            for j_index, references in enumerate(
                self.datastore.global_references.tolist()
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

                            self.datastore.at[j_index, "local_references"] += [
                                self.datastore.historiograph_id[i_index]
                            ]

    def compute_local_citations(self):
        """
        Computes local citations.

        """
        logging.info("Computing local citations")

        local_references = self.datastore[["local_references"]]
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
        self.datastore["local_citations"] = 0
        self.datastore.index = self.datastore.historiograph_id
        self.datastore.loc[local_references.index, "local_citations"] = local_references
        self.datastore.index = list(range(len(self.datastore)))

    def consolidate_local_references(self):
        """
        Consolidates local references.

        """
        logging.info("Consolidating local references")
        self.datastore["local_references"] = self.datastore.local_references.apply(
            lambda x: sorted(set(x))
        )
        self.datastore["local_references"] = self.datastore.local_references.apply(
            lambda x: "; ".join(x) if isinstance(x, list) else x
        )

    def compute_bradford_law_zones(self):
        """
        Computes bradford law zones.

        """
        logging.info("Computing Bradford Law Zones ...")

        self.datastore["id"] = range(len(self.datastore))

        x = self.datastore.copy()

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
        bradford_core_sources = int(len(self.datastore) / 3)
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
        self.datastore["bradford_law_zone"] = self.datastore.publication_name

        self.datastore["bradford_law_zone"] = self.datastore.bradford_law_zone.map(
            lambda w: dict_[w.strip()], na_action="ignore"
        )
        self.datastore["bradford_law_zone"] = self.datastore.bradford_law_zone.map(
            lambda w: bradford_dict[w], na_action="ignore"
        )

    def create_KW_exclude(self):
        filename = self.datastorepath + "KW_ignore.txt"
        if isfile(filename):
            open(filename, "a").close()

    def save_datastore(self):
        """
        Saves datastore.

        """
        filename = self.datastorepath + "datastore.csv"
        logging.info("Saving datastore to %s", filename)
        self.datastore.to_csv(filename, sep=",", encoding="utf-8", index=False)


def process_datastore(datastorepath="./"):
    """
    This method is used to process the datastore

    :param datastorepath:
    :return:
    """
    datastore = DatastoreTransformations(datastorepath)
    datastore.load_datastore()
    datastore.create_historiograph_id()
    # datastore.delete_existent_local_references()
    # datastore.create_local_references_using_doi()
    # datastore.create_local_references_using_title()
    # datastore.consolidate_local_references()
    # datastore.compute_local_citations()
    datastore.compute_bradford_law_zones()
    datastore.create_KW_exclude()
    #
    datastore.save_datastore()
    #
    create_institutions_thesaurus(datastorepath=datastorepath)
    apply_institutions_thesaurus(datastorepath=datastorepath)
    create_keywords_thesaurus(datastorepath=datastorepath)
    apply_keywords_thesaurus(datastorepath=datastorepath)

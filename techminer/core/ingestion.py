"""
Data Importers
===============================================================================

"""
import logging
import unicodedata
from os.path import dirname, isfile, join

import pandas as pd
from techminer.utils.extract_country_name import extract_country_name
from techminer.utils.map import map_

logging.basicConfig(format="%(levelname)s - %(message)s", level=logging.DEBUG)

#
# ETL:
#    Extracts data from raw data sources
#    Transforms data into a common format
#    Loads data into a common format
#


def _strip_accents(text):
    try:
        text = unicode(text, "utf-8")
    except NameError:  # unicode is a default on python 3
        pass

    if isinstance(text, str):
        text = (
            unicodedata.normalize("NFD", text).encode("ascii", "ignore").decode("utf-8")
        )
        return str(text)

    return text


# ----< Generic Importer >-----------------------------------------------------


class _ETLpipeline:
    """
    Base class for ETL pipelines.

    """

    def __init__(self, filepath, filetype, datastorepath="./"):
        self.filepath = filepath
        self.filetype = filetype
        self.datastorepath = datastorepath
        if self.datastorepath[-1] != "/":
            self.datastorepath += "/"
        #
        self.raw_data = None
        self.tagsfile = None
        self.columns2tags = None
        self.columns2delete = None
        self.datastore = None

    def extract_data(self):
        """
        Imports data from a raw data source.

        """
        logging.info("----------< Extractig data from %s >-----------", self.filepath)

    def load_tags(self):
        """
        Loads tags from a tags file.

        """
        #
        module_path = dirname(__file__)
        filepath = join(module_path, "../data/" + self.tagsfile)
        #
        columns2tags = {}
        columns2delete = []
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                line = line.replace("\n", "").split(",")
                name = line[0].strip()
                if len(line) == 2:
                    tag = line[1].strip()
                    columns2tags[name] = tag
                else:
                    columns2delete.append(name)

        self.columns2tags = columns2tags
        self.columns2delete = columns2delete

    def rename_columns(self):
        """
        Renames columns.

        """
        logging.info("Renaming columns")
        for name, tag in self.columns2tags.items():
            self.raw_data.rename(columns={name: tag}, inplace=True)

    def delete_columns(self):
        """
        Deletes columns.

        """
        logging.info("Deleting innecesary columns")
        self.raw_data.drop(columns=self.columns2delete, inplace=True, errors="ignore")

    def format_strip_accents(self):
        """
        Strips accents from the dataframe.

        """
        logging.info("Replacing accents")
        self.raw_data.applymap(_strip_accents, na_action="ignore")

    def format_publication_name(self):
        """
        Formats Publication_Name into a common format.

        """
        if "publication_name" in self.raw_data.columns:
            logging.info("Formating publication_name")
            self.raw_data.publication_name = self.raw_data.publication_name.str.upper()
            self.raw_data.publication_name = self.raw_data.publication_name.str.replace(
                r"[^\w\s]", "", regex=True
            )

    def format_issn(self):
        """
        Formats ISSN into a common format.

        """
        if "issn" in self.raw_data.columns:
            logging.info("Formating ISSN")
            self.raw_data.issn = self.raw_data.issn.str.replace("-", "", regex=True)
            self.raw_data.issn = self.raw_data.issn.str.upper()

    def format_eissn(self):
        """
        Formats eISSN into a common format.

        """
        if "eissn" in self.raw_data.columns:
            logging.info("Formating eISSN")
            self.raw_data.eissn = self.raw_data.eissn.str.replace("-", "", regex=True)
            self.raw_data.eissn = self.raw_data.eissn.str.upper()

    def format_doi(self):
        """
        Formats DOI into a common format.

        """
        if "doi" in self.raw_data.columns:
            logging.info("Formatting DOI to upper case")
            self.raw_data.doi = self.raw_data.doi.str.upper()

    def format_keywords(self):
        """
        Formats keywords.

        """
        for column in ["author_keywords", "index_keywords"]:
            if column in self.raw_data.columns:
                logging.info("Formatting %s", column)
                self.raw_data[column] = self.raw_data[column].str.replace(
                    "[^\w\s]", "", regex=True
                )
                self.raw_data[column] = self.raw_data[column].map(
                    lambda x: x.replace("; ", "; ") if not pd.isna(x) else x
                )
                self.raw_data[column] = self.raw_data[column].str.lower()

    def replace_invalid_author_name(self):
        """
        Replaces no author name with "Unknown"

        """
        logging.info("Removing [No author name available]")
        self.raw_data.replace(
            to_replace="[No author name available]", value=None, inplace=True
        )
        logging.info("Removing [Anonymous]")
        self.raw_data.replace(to_replace="[Anonymous]", value=None, inplace=True)

    def remove_copyright(self):
        """
        Removes copyright text from abstracts.

        """
        if "abstract" in self.raw_data.columns:
            logging.info("Removing copyright")
            self.raw_data.abstract = self.raw_data.abstract.map(
                lambda x: x[0 : x.find("\u00a9")] if not pd.isna(x) else x
            )

    def clean_document_title(self):
        """
        Cleans document title.

        """
        logging.info("Cleaning document title")
        self.raw_data.document_title = self.raw_data.document_title.map(
            lambda x: x[0 : x.find("[")] if pd.isna(x) is False and x[-1] == "]" else x
        )

    def fill_na_with_zero_in_global_citations(self):
        """
        Fills na with zero in global citations.

        """
        if "global_citations" in self.raw_data.columns:
            logging.info("Filling na with zero in global citations")
            self.raw_data.global_citations = self.raw_data.global_citations.fillna(0)
            self.raw_data.global_citations = self.raw_data.global_citations.astype(int)

    def count_num_authors_per_document(self):
        """
        Counts the number of authors per document

        """
        logging.info("Counting number of authors per document")
        self.raw_data["num_authors"] = self.raw_data.authors.apply(
            lambda x: len(x.split(";")) if not pd.isna(x) else 0
        )

    def compute_frac_number_of_documents(self):
        """
        Computes the fraction of documents per author.

        """
        logging.info("Computing fraction of documents")
        self.raw_data["frac_num_documents"] = self.raw_data.authors.map(
            lambda x: 1.0 / len(x.split("; ")) if not pd.isna(x) else 0
        )

    def format_iso_source_abbreviation(self):
        """
        Formats ISO Source Abbreviation into a common format.

        """
        if "iso_source_abbreviation" in self.raw_data.columns:
            logging.info("Formating ISO source abbreviation")
            self.raw_data.iso_source_abbreviation = (
                self.raw_data.iso_source_abbreviation.str.upper()
            )
            self.raw_data.iso_source_abbreviation = (
                self.raw_data.iso_source_abbreviation.map(
                    lambda x: x.replace(".", "") if not pd.isna(x) else x
                )
            )

    def fillna_iso_source_abbreviation(self):
        """
        Completes ISO Source Abbreviation.

        """

        def load_global_abbreviations():
            """
            Loads global abbreviations.

            """
            module_path = dirname(__file__)
            filename = join(module_path, "../data/iso_sources.csv")
            iso_sources = pd.read_csv(filename, sep=",", encoding="utf-8")
            name2abb_global = {
                publication_name: iso_abbreviation
                for publication_name, iso_abbreviation in zip(
                    iso_sources.publication_name, iso_sources.iso_source_abbreviation
                )
            }
            return name2abb_global

        def load_local_abbreviations():
            """
            Loads local abbreviations.

            """
            name2abb_local = {
                publication_name: iso_abbreviation
                for publication_name, iso_abbreviation in zip(
                    self.raw_data.publication_name,
                    self.raw_data.iso_source_abbreviation,
                )
            }
            return name2abb_local

        def fillna_iso_source_abbreviation(name2abb):
            """
            Fills na with global abbreviation.

            """
            self.raw_data.iso_source_abbreviation = self.raw_data.publication_name.map(
                lambda x: name2abb[x] if not pd.isna(x) else x
            )

        def save_new_iso_source_abbreviations(name2abb_local, name2abb_global):
            """
            Saves new abbreviations.

            """
            #
            # Extracs abbreviations from global and local abbreviations
            #
            new_abbreviations = set(name2abb_local.keys()) - set(name2abb_global.keys())
            new_abbreviations = {key: name2abb_local[key] for key in new_abbreviations}

            #
            #
            #
            filename = self.datastorepath + "iso_sources.csv"
            if isfile(filename):
                iso_sources = pd.read_csv(filename, sep=",", encoding="utf-8")
                iso_sources = {
                    publication_name: iso_abbreviation
                    for publication_name, iso_abbreviation in zip(
                        iso_sources.publication_name,
                        iso_sources.iso_source_abbreviation,
                    )
                }
            else:
                iso_sources = {}

            #
            # Updates current new abbreviations
            #
            new_abbreviations = {**new_abbreviations, **iso_sources}
            publication_name = [key for key in new_abbreviations.keys()]
            iso_source_abbreviation = [value for value in new_abbreviations.values()]

            new_df = pd.DataFrame(
                {
                    "publication_name": publication_name,
                    "iso_source_abbreviation": iso_source_abbreviation,
                }
            )
            new_df.to_csv(filename, sep=",", encoding="utf-8", index=False)

        if "iso_source_abbreviation" in self.raw_data.columns:

            logging.info("Filling na with global abbreviation")
            name2abb_global = load_global_abbreviations()
            name2abb_local = load_local_abbreviations()
            name2abb = {**name2abb_global, **name2abb_local}
            fillna_iso_source_abbreviation(name2abb)
            save_new_iso_source_abbreviations(name2abb_local, name2abb_global)

    def extract_country_names(self):

        if "affiliations" in self.raw_data.columns:
            logging.info("Extracting country names ...")
            self.raw_data["countries"] = map_(
                self.raw_data, "affiliations", extract_country_name
            )

    def extract_country_first_author(self):

        if "countries" in self.raw_data.columns:

            logging.info("Extracting country of first author ...")
            self.raw_data["country_1st_author"] = self.raw_data.countries.map(
                lambda w: w.split("; ")[0] if isinstance(w, str) else w
            )

    #
    #
    # ---< Procedures to merge data > ------------------------------------------
    #
    #
    def load_datastore(self):
        """
        Loads datastore.

        """
        filename = self.datastorepath + "datastore.csv"
        if isfile(filename):
            self.datastore = pd.read_csv(filename, sep=",", encoding="utf-8")
        else:
            self.datastore = pd.DataFrame()

    def concat(self):
        """
        Concatenates data.

        """
        self.datastore = pd.concat([self.datastore, self.raw_data])

    def drop_doi_duplicates(self):
        """
        Drops duplicates.

        """
        duplicated_doi = (self.datastore.doi.duplicated()) & (
            ~self.datastore.doi.isna()
        )
        self.datastore = self.datastore[~duplicated_doi]

    def drop_author_title_year_publication_name_duplicates(self):
        """
        Drop duplicates.

        """
        subset = ("authors", "document_title", "pub_year", "publication_name")
        self.datastore.drop_duplicates(subset=subset, inplace=True)

    def save_duplicates(self):
        """
        Saves duplicates.

        """
        duplicates = (
            self.datastore.document_title.duplicated(keep=False)
            & ~self.datastore.document_title.isna()
        )
        if duplicates.any():
            filename = self.datastorepath + "duplicates.csv"
            duplicates = self.datastore[duplicates].copy()
            duplicates.sort_values(by=["document_title"], inplace=True)
            duplicates.to_csv(filename, sep=",", encoding="utf-8", index=False)
            logging.warning(
                "Duplicate rows found in %s - Records saved to %s",
                self.datastorepath + "datastore.csv",
                filename,
            )

    def save_datastore(self):
        """
        Saves datastore.

        """
        filename = self.datastorepath + "datastore.csv"
        self.datastore.to_csv(filename, sep=",", encoding="utf-8", index=False)


# ----< Scopus >-----------------------------------------------------


class _ScopusETL(_ETLpipeline):
    def __init__(self, filepath, filetype, datastorepath):
        super().__init__(filepath, filetype, datastorepath)
        self.tagsfile = "scopus2tags.csv"

    def extract_data(self):
        """
        Imports data from a Scopus CSV file.

        """
        super().extract_data()
        self.raw_data = pd.read_csv(
            self.filepath, encoding="utf-8", on_bad_lines="skip"
        )

    def format_authors(self):
        """
        Formats Authors into a common format.
        """
        if "authors" in self.raw_data.columns:
            self.raw_data.authors = self.raw_data.authors.str.replace(
                r", ", "; ", regex=True
            )
            self.raw_data.authors = self.raw_data.authors.str.replace(
                r".", "", regex=True
            )


# ----< WoS >-----------------------------------------------------


class _WoSETL(_ETLpipeline):
    def __init__(self, filepath, filetype, datastorepath):
        super().__init__(filepath, filetype, datastorepath)
        self.tagsfile = "wos2tags.csv"

    def extract_data(self):
        """
        Imports data from a WoS text file.

        """

        def load_wosrecords():
            records = []
            record = {}
            key = None
            value = []
            with open(self.filepath, "rt", encoding="utf-8") as file:
                for line in file:
                    line = line.replace("\n", "")
                    if line.strip() == "ER":
                        if len(record) > 0:
                            records.append(record)
                        record = {}
                        key = None
                        value = []
                    elif len(line) >= 2 and line[:2] == "  ":
                        line = line[2:]
                        line = line.strip()
                        value.append(line)

                    elif (
                        len(line) >= 2
                        and line[:2] != "  "
                        and line[:2] not in ["FN", "VR"]
                    ):
                        if key is not None:
                            record[key] = ";".join(value)
                        key = line[:2].strip()
                        value = [line[2:].strip()]

            return records

        def wosrecords2df(wosrecords):
            pdf = pd.DataFrame()
            for record in wosrecords:
                record = {key: [value] for key, value in record.items()}
                row = pd.DataFrame(record)
                pdf = pd.concat(
                    [pdf, row],
                    ignore_index=True,
                )
            return pdf

        super().extract_data()
        self.raw_data = wosrecords2df(wosrecords=load_wosrecords())

    def format_authors(self):
        """

        Formats Authors into a common format.

        """
        if "authors" in self.raw_data.columns:
            self.raw_data.authors = self.raw_data.authors.str.replace(
                ",", "", regex=True
            )


# ----< Dimensions >-------------------------------------------------


class _DimensionsETL(_ETLpipeline):
    def __init__(self, filepath, filetype, datastorepath):
        super().__init__(filepath, filetype, datastorepath)
        self.tagsfile = "dimensions2tags.csv"

    def extract_data(self):
        """
        Imports data from a Dimensions CSV file.

        """
        super().extract_data()
        self.raw_data = pd.read_csv(self.filepath, skiprows=1)

    def format_authors(self):
        """
        Formats Authors into a common format.

        """

        def format_authorslits(authorslist):

            authorslist = authorslist.split(";")
            authorslist = [author.strip() for author in authorslist]

            surnames = [
                author.split(",")[0] if "," in author else author.split(" ")[0]
                for author in authorslist
            ]
            names = [
                author.split(",")[1] if "," in author else author.split(" ")[0]
                for author in authorslist
            ]

            names = [name.strip() for name in names]
            names = [name.split() for name in names]
            names = [
                [name_part[0] for name_part in name] for name in names if len(name) > 0
            ]
            names = ["".join(part_name) for name in names for part_name in name]

            authorslist = [
                surname + " " + name for surname, name in zip(surnames, names)
            ]
            authorslist = "; ".join(authorslist)
            return authorslist

        if "authors" in self.raw_data.columns:
            self.raw_data.authors = self.raw_data.authors.apply(
                lambda x: format_authorslits(x) if not pd.isnull(x) else None,
            )


# ----< Generic >-------------------------------------------------


def _import_dataset(filepath, filetype, datastorepath):
    """
    Imports a dataset.

    """
    if filetype == "scopus":
        return _ScopusETL(filepath, filetype, datastorepath)
    if filetype == "wos":
        return _WoSETL(filepath, filetype, datastorepath)
    if filetype == "dimensions":
        return _DimensionsETL(filepath, filetype, datastorepath)
    raise NotImplementedError


def _import_dataset_file(filepath, filetype, datastorepath):
    """
    Imports a dataset file.

    """
    if isfile(filepath):
        return _import_dataset(filepath, filetype, datastorepath)
    else:
        raise FileNotFoundError


def load_file(filepath, filetype, datastorepath):
    """
    Loads a dataset file.

    """
    dataset = _import_dataset_file(filepath, filetype, datastorepath)
    dataset.load_tags()
    dataset.extract_data()
    dataset.rename_columns()
    dataset.delete_columns()
    dataset.format_strip_accents()
    dataset.format_publication_name()
    dataset.format_issn()
    dataset.format_eissn()
    dataset.format_authors()
    dataset.format_doi()
    dataset.format_iso_source_abbreviation()
    dataset.fillna_iso_source_abbreviation()
    dataset.format_keywords()
    dataset.remove_copyright()
    dataset.clean_document_title()
    dataset.replace_invalid_author_name()
    dataset.count_num_authors_per_document()
    dataset.compute_frac_number_of_documents()
    dataset.extract_country_names()
    dataset.extract_country_first_author()

    #
    dataset.load_datastore()
    dataset.concat()
    dataset.drop_doi_duplicates()
    dataset.drop_author_title_year_publication_name_duplicates()
    dataset.save_duplicates()
    dataset.save_datastore()
    return dataset.raw_data

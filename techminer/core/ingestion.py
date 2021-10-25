"""
Data Importers
===============================================================================

"""
import logging
from os.path import dirname, isfile, join

import pandas as pd

logging.basicConfig(format="%(levelname)s - %(message)s", level=logging.DEBUG)

#
# ETL:
#    Extracts data from raw data sources
#    Transforms data into a common format
#    Loads data into a common format
#

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
        logging.info("Extractig data from %s", self.filepath)

    def load_tags(self):
        """
        Loads tags from a tags file.

        """

        module_path = dirname(__file__)
        filepath = join(module_path, "../data/" + self.tagsfile)

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
        for name, tag in self.columns2tags.items():
            self.raw_data.rename(columns={name: tag}, inplace=True)

    def delete_columns(self):
        """
        Deletes columns.

        """
        self.raw_data.drop(columns=self.columns2delete, inplace=True, errors="ignore")

    def format_publication_name(self):
        """
        Formats Publication_Name into a common format.

        """
        if "publication_name" in self.raw_data.columns:
            self.raw_data.publication_name = self.raw_data.publication_name.str.upper()
            self.raw_data.publication_name = self.raw_data.publication_name.str.replace(
                r"[^\w\s]", "", regex=True
            )

    def format_issn(self):
        """
        Formats ISSN into a common format.

        """
        if "issn" in self.raw_data.columns:
            self.raw_data.issn = self.raw_data.issn.str.replace("-", "", regex=True)
            self.raw_data.issn = self.raw_data.issn.str.upper()

    def format_eissn(self):
        """
        Formats eISSN into a common format.

        """
        if "eissn" in self.raw_data.columns:
            self.raw_data.eissn = self.raw_data.eissn.str.replace("-", "", regex=True)
            self.raw_data.eissn = self.raw_data.eissn.str.upper()

    def format_doi(self):
        """
        Formats DOI into a common format.

        """
        if "doi" in self.raw_data.columns:
            self.raw_data.doi = self.raw_data.doi.str.upper()

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
    dataset.format_publication_name()
    dataset.format_issn()
    dataset.format_eissn()
    dataset.format_authors()
    dataset.format_doi()
    dataset.load_datastore()
    dataset.concat()
    dataset.drop_doi_duplicates()
    dataset.drop_author_title_year_publication_name_duplicates()
    dataset.save_duplicates()
    dataset.save_datastore()
    return dataset.raw_data

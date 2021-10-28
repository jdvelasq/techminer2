"""
Datastore preparation module.

"""

import re
from os import mkdir
from os.path import dirname, isfile, join

import pandas as pd
from techminer.utils.extract_country_name import extract_country_name
from techminer.utils.logging_info import logging_info
from techminer.utils.map import map_
from techminer.utils.text import remove_accents
from techminer.utils.thesaurus import load_file_as_dict
from tqdm import tqdm


class _BaseImporter:
    """
    Base class for ETL pipelines.

    """

    def __init__(self, source, filetype, directory):
        self.source = source
        self.filetype = filetype
        self.directory = directory
        if self.directory[-1] != "/":
            self.directory += "/"
        #
        self.raw_data = None
        self.tagsfile = None
        self.columns2tags = None
        self.columns2delete = None
        self.iso_source_abbreviations = None

    def check_directory(self):
        """
        Checks if directory exists.

        """
        if not isfile(self.directory):
            mkdir(self.directory)

    def extract_data(self):
        """
        Imports data from a raw data source.

        """
        raise NotImplementedError

    def load_tags(self):
        """
        Loads tags from a tags file.

        """
        #
        module_path = dirname(__file__)
        filepath = join(module_path, "../config_data/" + self.tagsfile)
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

    def format_dataset(self):
        """
        Formats dataset.

        """
        logging_info("Formatting dataset ...")
        self.raw_data = self.raw_data.rename(columns=self.columns2tags)
        self.raw_data = self.raw_data.drop(columns=self.columns2delete, errors="ignore")
        self.raw_data.applymap(lambda x: remove_accents(x) if isinstance(x, str) else x)

    def load_iso_source_abbreviations(self):
        """
        Loads ISO source abbreviations.

        """
        module_path = dirname(__file__)
        filepath = join(module_path, "../config_data/iso_source_abbreviations.csv")
        pdf = pd.read_csv(filepath, sep=",")
        self.iso_source_abbreviations = dict(
            zip(pdf.publication_name, pdf.iso_source_abbreviation)
        )

    def format_authors(self):
        """
        Imports data from a raw data source.

        """
        raise NotImplementedError

    def format_columns(self):
        """
        Formats imported columns.

        """
        logging_info("Formatting columns ...")

        if "abstract" in self.raw_data.columns:
            self.raw_data.abstract = self.raw_data.abstract.str.lower()
            self.raw_data.abstract = self.raw_data.abstract.map(
                lambda x: x[0 : x.find("\u00a9")] if not pd.isna(x) else x
            )

        if "author_keywords" in self.raw_data.columns:
            self.raw_data.author_keywords = self.raw_data.author_keywords.str.lower()

        if "document_title" in self.raw_data.columns:
            self.raw_data.document_title = self.raw_data.document_title.map(
                lambda x: x[0 : x.find("[")]
                if pd.isna(x) is False and x[-1] == "]"
                else x
            )

        if "doi" in self.raw_data.columns:
            self.raw_data.doi = self.raw_data.doi.str.upper()

        if "issn" in self.raw_data.columns:
            self.raw_data.issn = self.raw_data.issn.str.replace("-", "", regex=True)
            self.raw_data.issn = self.raw_data.issn.str.upper()

        if "eissn" in self.raw_data.columns:
            self.raw_data.eissn = self.raw_data.eissn.str.replace("-", "", regex=True)
            self.raw_data.eissn = self.raw_data.eissn.str.upper()

        if "global_citations" in self.raw_data.columns:
            self.raw_data.global_citations = self.raw_data.global_citations.fillna(0)
            self.raw_data.global_citations = self.raw_data.global_citations.astype(int)

        if "global_references" in self.raw_data.columns:
            self.raw_data["global_references"] = self.raw_data.global_references.map(
                lambda w: w.replace("https://doi.org/", "") if isinstance(w, str) else w
            )
            self.raw_data["global_references"] = self.raw_data.global_references.map(
                lambda w: w.replace("http://dx.doi.org/", "")
                if isinstance(w, str)
                else w
            )

        if "index_keywords" in self.raw_data.columns:
            self.raw_data.index_keywords = self.raw_data.index_keywords.str.lower()

        if "publication_name" in self.raw_data.columns:
            self.raw_data.publication_name = self.raw_data.publication_name.str.upper()
            self.raw_data.publication_name = self.raw_data.publication_name.str.replace(
                r"[^\w\s]", "", regex=True
            )

        if "iso_source_abbreviation" in self.raw_data.columns:
            self.raw_data.iso_source_abbreviation = (
                self.raw_data.iso_source_abbreviation.str.upper()
            )
            self.raw_data.iso_source_abbreviation = (
                self.raw_data.iso_source_abbreviation.map(
                    lambda x: x.replace(".", "") if not pd.isna(x) else x
                )
            )
            iso_abbreviations = self.raw_data[
                ["publication_name", "iso_source_abbreviation"]
            ]
            iso_abbreviations = iso_abbreviations.drop_duplicates()
            iso_abbreviations = iso_abbreviations.dropna()
            iso_abbreviations = {
                name: abb
                for name, abb in zip(
                    iso_abbreviations.publication_name,
                    iso_abbreviations.iso_source_abbreviation,
                )
            }
            iso_abbreviations = {
                **self.iso_source_abbreviations,
                **iso_abbreviations,
            }
            self.raw_data.iso_source_abbreviation = (
                self.raw_data.iso_source_abbreviation.map(
                    lambda x: iso_abbreviations[x] if pd.isna(x) else x
                )
            )
            new_abbreviations = set(iso_abbreviations.values()) - set(
                self.iso_source_abbreviations.values()
            )
            new_abbreviations = {
                key: iso_abbreviations[key] for key in new_abbreviations
            }
            self.iso_source_abbreviations = {
                **self.iso_source_abbreviations,
                **new_abbreviations,
            }
            if len(new_abbreviations):
                filename = self.directory + "new_iso_source_abbreviations.csv"
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
                new_abbreviations = {**new_abbreviations, **iso_sources}
                new_abbreviations = pd.DataFrame(
                    {
                        "publication_name": list(new_abbreviations.keys()),
                        "iso_source_abbreviation": list(new_abbreviations.values()),
                    }
                )
                new_abbreviations.to_csv(
                    filename, sep=",", encoding="utf-8", index=False
                )

    def compute_new_columns(self):
        """
        Calculate computed columns.

        """
        logging_info("Computing new columns ...")

        if "authors" in self.raw_data:

            self.raw_data["num_authors"] = self.raw_data.authors.apply(
                lambda x: len(x.split(";")) if not pd.isna(x) else 0
            )

            self.raw_data["frac_num_documents"] = self.raw_data.authors.map(
                lambda x: 1.0 / len(x.split("; ")) if not pd.isna(x) else 0
            )

        if "affiliations" in self.raw_data.columns:
            self.raw_data["countries"] = map_(
                self.raw_data, "affiliations", extract_country_name
            )

            self.raw_data["country_1st_author"] = self.raw_data.countries.map(
                lambda w: w.split("; ")[0] if isinstance(w, str) else w
            )

            self.raw_data["countries"] = self.raw_data.countries.map(
                lambda w: "; ".join(set(w.split("; "))) if isinstance(w, str) else w
            )

        if "global_references" in self.raw_data.columns:

            self.raw_data[
                "global_references_count"
            ] = self.raw_data.global_references.map(
                lambda x: len(x.split("; ")) if not pd.isna(x) else 0
            )

    def drop_duplicates(self):
        """
        Drops duplicates based on DOI and document title and authors.

        """
        logging_info("Dropping duplicates ...")

        if "doi" in self.raw_data.columns:
            duplicated_doi = (self.raw_data.doi.duplicated()) & (
                ~self.raw_data.doi.isna()
            )
            self.raw_data = self.raw_data[~duplicated_doi]

        if (
            "authors" in self.raw_data.columns
            and "document_title" in self.raw_data.columns
            and "pub_year" in self.raw_data.columns
            and "publication_name" in self.raw_data.columns
        ):
            subset = ("authors", "document_title", "pub_year", "publication_name")
            self.raw_data = self.raw_data.drop_duplicates(subset=subset)

    def report_duplicate_titles(self):
        """
        Report duplicate documents.

        """
        duplicates = (
            self.raw_data.document_title.duplicated(keep=False)
            & ~self.raw_data.document_title.isna()
        )
        if duplicates.any():
            filename = self.directory + "duplicates.csv"
            duplicates = self.raw_data[duplicates].copy()
            duplicates = duplicates.sort_values(by=["document_title"])
            duplicates.to_csv(filename, sep=",", encoding="utf-8", index=False)
            logging_info(
                f"Duplicate rows found in {self.directory}records.csv - Records saved to {filename}"
            )

    def translate_british_to_amerian(self):
        """
        Translate british spelling to american spelling.

        """
        if "abstract" in self.raw_data.columns:
            logging_info("Transforming British to American ...")
            module_path = dirname(__file__)
            filename = join(module_path, "../config_data/bg2am.data")
            bg2am = load_file_as_dict(filename)
            with tqdm(total=len(bg2am.keys())) as pbar:

                for british_word, american_word in bg2am.items():
                    match = re.compile(f"\\b{british_word}\\b")
                    self.raw_data = self.raw_data.applymap(
                        lambda x: match.sub(american_word[0], x)
                        if isinstance(x, str)
                        else x
                    )
                    pbar.update(1)

    def save_records(self):
        """
        Save processed records to csv.

        """
        filename = self.directory + "records.csv"

        #
        # merges the current dataframe with the existing dataframe
        #
        if isfile(filename):
            current_datastore = pd.read_csv(filename, encoding="utf-8")
            if "record_id" in current_datastore.columns:
                current_datastore.pop("record_id")
            self.raw_data = pd.concat([current_datastore, self.raw_data])
            self.raw_data = self.raw_data.drop_duplicates()

        self.raw_data["record_id"] = range(len(self.raw_data))
        self.raw_data.to_csv(filename, sep=",", encoding="utf-8", index=False)
        logging_info(f"Records saved/merged to '{filename}'")

    def run(self):
        """
        Runs the importer.

        """
        self.check_directory()
        self.extract_data()
        self.load_tags()
        self.format_dataset()
        self.load_iso_source_abbreviations()
        self.format_authors()
        self.format_columns()
        self.compute_new_columns()
        self.drop_duplicates()
        self.report_duplicate_titles()
        self.translate_british_to_amerian()
        self.save_records()

    # --- Computed columns ----------------------------------------------------

    # def disambiguate_author_names(self):
    #     """
    #     Disambiguate Author Names

    #     """

    #     if "authors" in self.raw_data.columns and "authors_id" in self.raw_data.columns:

    #         logging_info("Disambiguate author names ...")

    #         self.raw_data["authors"] = self.raw_data.authors.map(
    #             lambda x: x[:-1] if not pd.isna(x) and x[-1] == ";" else x
    #         )

    #         self.raw_data["authors_id"] = self.raw_data.authors_id.map(
    #             lambda x: x[:-1] if not pd.isna(x) and x[-1] == ";" else x
    #         )

    #         data = self.raw_data[["authors", "authors_id"]]
    #         data = data.dropna()

    #         data["*info*"] = [(a, b) for (a, b) in zip(data.authors, data.authors_id)]

    #         data["*info*"] = data["*info*"].map(
    #             lambda w: [
    #                 (u.strip(), v.strip())
    #                 for u, v in zip(w[0].split(";"), w[1].split(";"))
    #             ]
    #         )

    #         data = data[["*info*"]].explode("*info*")
    #         data = data.reset_index(drop=True)

    #         names_ids = {}
    #         for idx in range(len(data)):

    #             author_name = data.at[idx, "*info*"][0]
    #             author_id = data.at[idx, "*info*"][1]

    #             if author_name in names_ids.keys():

    #                 if author_id not in names_ids[author_name]:
    #                     names_ids[author_name] = names_ids[author_name] + [author_id]
    #             else:
    #                 names_ids[author_name] = [author_id]

    #         ids_names = {}
    #         for author_name in names_ids.keys():
    #             suffix = 0
    #             for author_id in names_ids[author_name]:
    #                 if suffix > 0:
    #                     ids_names[author_id] = author_name + "(" + str(suffix) + ")"
    #                 else:
    #                     ids_names[author_id] = author_name
    #                 suffix += 1

    #         self.raw_data["authors"] = self.raw_data.authors_id.map(
    #             lambda z: ";".join([ids_names[w.strip()] for w in z.split(";")])
    #             if not pd.isna(z)
    #             else z
    #         )


# ----< Scopus >-----------------------------------------------------


class ScopusImporter(_BaseImporter):
    """
    Importer for Scopus CSV files.

    """

    def __init__(self, source, filetype, directory):
        super().__init__(source, filetype, directory)
        self.tagsfile = "scopus2tags.csv"

    def extract_data(self):
        """
        Imports data from a Scopus CSV file.

        """
        logging_info(f"Reading file '{self.source}' ...")
        self.raw_data = pd.read_csv(
            self.source, encoding="utf-8", error_bad_lines=False
        )
        # on_bad_lines="skip")

    def format_authors(self):
        """
        Formats Authors into a common format.
        """

        if "authors" in self.raw_data.columns:
            logging_info("Formating authors ...")
            self.raw_data.authors = self.raw_data.authors.map(
                lambda x: pd.NA if x == "[No author name available]" else x
            )

            self.raw_data.authors = self.raw_data.authors.str.replace(
                ", ", "; ", regex=False
            )
            self.raw_data.authors = self.raw_data.authors.str.replace(
                ".", "", regex=False
            )

        if "authors_id" in self.raw_data.columns:
            logging_info("Formating authors_id ...")
            self.raw_data["authors_id"] = self.raw_data.authors_id.map(
                lambda w: pd.NA if w == "[No author id available]" else w
            )
            self.raw_data["authors_id"] = self.raw_data.authors_id.map(
                lambda x: x[:-1] if isinstance(x, str) and x[-1] == ";" else x
            )

            authors_ids = self.raw_data[["authors", "authors_id"]].dropna()
            authors_ids = {
                b: a for a, b in zip(authors_ids.authors, authors_ids.authors_id)
            }

            authors_ids = {
                k: list(zip(k.split(";"), v.split("; ")))
                for k, v in authors_ids.items()
            }
            authors_ids = {
                k: ["/".join([b, a]) for a, b in v] for k, v in authors_ids.items()
            }
            authors_ids = {k: "; ".join(v) for k, v in authors_ids.items()}

            self.raw_data["authors_id"] = self.raw_data.authors_id.map(
                lambda x: authors_ids[x] if x in authors_ids.keys() else x
            )


# ----< WoS >-----------------------------------------------------


class WoSImporter(_BaseImporter):
    """
    Web of Science importer.

    """

    def __init__(self, source, filetype, directory):
        super().__init__(source, filetype, directory)
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
            with open(self.source, "rt", encoding="utf-8") as file:
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
                            record[key] = "; ".join(value)
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


class DimensionsImporter(_BaseImporter):
    """
    Imports raw CSV from dimensions.ai


    """

    def __init__(self, source, filetype, directory):
        super().__init__(source, filetype, directory)
        self.tagsfile = "dimensions2tags.csv"

    def extract_data(self):
        """
        Imports data from a Dimensions CSV file.

        """
        self.raw_data = pd.read_csv(self.source, skiprows=1)

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

            logging_info("Removing [Anonymous]")
            self.raw_data.authors = self.raw_data.authors.map(
                lambda x: pd.NA if not pd.isna(x) and x == "[Anonymous]" else x
            )


# ----< Generic >-------------------------------------------------


def create_import_object(source, filetype, directory):
    """
    Creates an import object based on the filetype.

    """
    if filetype == "scopus":
        return ScopusImporter(source, filetype, directory)
    if filetype == "wos":
        return WoSImporter(source, filetype, directory)
    if filetype == "dimensions":
        return DimensionsImporter(source, filetype, directory)
    raise NotImplementedError


def import_records(source, filetype, directory):
    """
    Imports a dataset file.

    """
    if isfile(source):
        create_import_object(source, filetype, directory).run()
        logging_info(f"The file '{source}' was successfully imported.")
    else:
        raise FileNotFoundError

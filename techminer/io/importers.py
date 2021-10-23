"""
Data Importers
===============================================================================

"""

from os.path import dirname, join

import pandas as pd


class _Importer:
    def __init__(self, filepath, dbsource, logpath="./logs/") -> None:
        self.filepath_ = filepath
        self.logpath_ = logpath
        self.dbsource_ = dbsource
        self.base_df_ = None
        self.df_ = None
        self.names2delete_ = None
        self.names2tags_ = None

    def _load_tags(self):
        """Loads predefined tags names"""
        if self.dbsource_ == "scopus":
            filename = "scopus2tags.data"
        elif self.dbsource_ == "wos":
            filename = "wos2tags.data"
        elif self.dbsource_ == "dimensions":
            filename = "dimensions2tags.data"
        else:
            raise ValueError("Unknown database source")

        module_path = dirname(__file__)
        filepath = join(module_path, "../data/" + filename)

        names2tags = {}
        names2delete = []
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                line = line.replace("\n", "").split(",")
                name = line[0].strip()
                if len(line) == 2:
                    tag = line[1].strip()
                    names2tags[name] = tag
                else:
                    names2delete.append(name)

        self.names2tags_ = names2tags
        self.names2delete_ = names2delete

    def _load_scopus_file(self):
        """Loads data from scopus file"""
        self.df_ = pd.read_csv(self.filepath_)

    def _load_dimensions_file(self):
        """Loads data from dimensions file"""
        self.df_ = pd.read_csv(self.filepath_, skiprows=1)

    def _load_wos_file(self):
        """Loads data from WoS file"""

        def load_wosrecords():
            records = []
            record = {}
            key = None
            value = []
            with open(self.filepath_, "rt", encoding="utf-8") as file:
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

        self.df_ = wosrecords2df(wosrecords=load_wosrecords())

    def _load_file(self):
        """Loads data from file"""
        if self.dbsource_ == "scopus":
            self._load_scopus_file()
        elif self.dbsource_ == "wos":
            self._load_wos_file()
        elif self.dbsource_ == "dimensions":
            self._load_dimensions_file()
        else:
            raise ValueError("Unknown database source")

    def _process_columns(self):
        """Rename columns using"""
        self.df_.rename(columns=self.names2tags_, inplace=True)
        selected_columns = [
            column for column in self.df_.columns if column not in self.names2delete_
        ]
        self.df_ = self.df_[selected_columns]

    def _normalize_colums(self):
        """Normalizes columns"""
        # Publication Name
        if "SO" in self.df_.columns:
            self.df_.SO = self.df_.SO.str.upper()
            self.df_.SO = self.df_.SO.str.replace(r"[^\w\s]", "")

        # eISSN
        if "EI" in self.df_.columns:
            self.df_.EI = self.df_.EI.str.replace("-", "")
            self.df_.EI = self.df_.EI.str.upper()
        # ISSN
        if "SN" in self.df_.columns:
            self.df_.SN = self.df_.SN.str.replace("-", "")
            self.df_.SN = self.df_.SN.str.upper()
        else:
            print(self.filepath_)

    def import_data(self):
        """Imports data"""
        self._load_tags()
        self._load_file()
        self._process_columns()
        self._normalize_colums()


def import_from_scopus(filepath):
    """Loads raw Scopus CSV file"""
    importer = _Importer(filepath=filepath, dbsource="scopus", logpath="./logs/")
    importer.import_data()
    return importer.df_


def import_from_wos(filepath):
    """Loads raw WoS/Clarrivate text file"""
    importer = _Importer(filepath=filepath, dbsource="wos", logpath="./logs/")
    importer.import_data()
    return importer.df_


def import_from_dimensions(filepath):
    """Loads raw Dimensinos.ai CSV file"""
    importer = _Importer(filepath=filepath, dbsource="dimensions", logpath="./logs/")
    importer.import_data()
    return importer.df_

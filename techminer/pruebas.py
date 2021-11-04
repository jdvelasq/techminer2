def import_raw_data_file(file_path):
    """
    Loads all files from a directory and returns a list of files.
    """
    import json

    with open(file_path) as json_file:
        return json.load(json_file)


def load_data_from_raw(raw_path):
    """
    Loads all files from a directory and returns a list of files.
    """
    import json

    with open(raw_path) as json_file:
        return json.load(json_file)


def load_data_from_scopus(scopus_path):
    """
    Loads all files from a directory and returns a list of files.
    """
    import json

    with open(scopus_path) as json_file:
        return json.load(json_file)


def process_data_from_csvfile(csvfile_path):
    """
    Loads all files from a directory and returns a list of files.
    """
    import csv

    with open(csvfile_path, "r") as csv_file:
        reader = csv.reader(csv_file)
        return list(reader)


def process_data_from_csv(csv_path):
    """
    Loads all files from a directory and returns a list of files.
    """
    import csv

    with open(csv_path, "r") as csv_file:
        reader = csv.reader(csv_file)
        return list(reader)


def process_data_from_table(table_path):
    """
    Loads all files from a directory and returns a list of files.
    """
    import pandas as pd

    return pd.read_csv(table_path)


def process_data_from_recordsdb(recordsdb_path):
    """
    Loads all files from a directory and returns a list of files.
    """
    import sqlite3

    conn = sqlite3.connect(recordsdb_path)
    c = conn.cursor()
    c.execute("SELECT * FROM records")
    return c.fetchall()


def process_data_from_records(records):
    """
    Loads all files from a directory and returns a list of files.
    """
    return records


def load_data_from_dir(dir_path):
    """
    Loads all files from a directory and returns a list of files.
    """
    import os

    files = []
    for file in os.listdir(dir_path):
        if file.endswith(".txt"):
            files.append(file)
    return files


def load_data_from_csv(csv_path):
    """
    Loads all files from a directory and returns a list of files.
    """
    import csv

    with open(csv_path, "r") as csv_file:
        reader = csv.reader(csv_file)
        return list(reader)


def process_data_from_db(db_path):
    """
    Loads all files from a directory and returns a list of files.
    """
    import sqlite3

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM data")
    return c.fetchall()


def process_data_from_datafile(datafile_path):
    """
    Loads all files from a directory and returns a list of files.
    """
    import json

    with open(datafile_path) as json_file:
        return json.load(json_file)


def load_data_from_records_directory(records_directory):
    """
    Loads all files from a directory and returns a list of files.
    """
    import os

    files = []
    for file in os.listdir(records_directory):
        if file.endswith(".json"):
            files.append(file)
    return files

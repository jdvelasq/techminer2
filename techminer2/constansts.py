"""Constants for techminer2."""

# Define the names of databases
CITED_BY_DATABASE = "cited_by"
MAIN_DATABASE = "main"
REFERENCES_DATABASE = "references"

DATABASE_NAMES_TO_FILE_NAMES = {
    CITED_BY_DATABASE: "_cited_by.csv.zip",
    MAIN_DATABASE: "_main.csv.zip",
    REFERENCES_DATABASE: "_references.csv.zip",
}


DATABASE_NAMES = [
    CITED_BY_DATABASE,
    MAIN_DATABASE,
    REFERENCES_DATABASE,
]

TEST_DIR = "tmp/"

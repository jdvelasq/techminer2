# flake8: noqa# flake8: noqa
"""
Import Raw Data
===============================================================================

Import a scopus data file in the working directory.


>>> root_dir = "data/regtech/"

>>> import techminer2plus 
>>> techminer2plus.ingest.ingest_raw_data(root_dir, disable_progress_bar=True)
--INFO-- Concatenating raw files in data/regtech/raw-data/cited_by/
--INFO-- Concatenating raw files in data/regtech/raw-data/references/
--INFO-- Concatenating raw files in data/regtech/raw-data/main/
--INFO-- Applying scopus tags to database files
--INFO-- Formatting column names in database files
--INFO-- Repairing authors ID
--INFO-- Repairing bad separators in keywords
--INFO-- Dropping NA columns in database files
--INFO-- Removed columns: {'page_count'}
--INFO-- Processing text columns (remove accents)
--INFO-- Processing text columns (remove stranger chars)
--INFO-- Removing records with `raw_authors` in ['Anon', '[No author name available]']
--INFO-- Removed 1 records
--INFO-- Processing `authors_id` column
--INFO-- Processing `document_type` column
--INFO-- Processing `eissn` column
--INFO-- Processing `global_citations` column
--INFO-- Processing `isbn` column
--INFO-- Processing `issn` column
--INFO-- Processing `raw_authors` column
--INFO-- Processing `source_name` column
--INFO-- Mask `source_abbr` column with `source_name`
--INFO-- Processing `source_abbr` column
--INFO-- Processing `doi` column
--INFO-- Disambiguating `authors` column
--INFO-- Copying `authors` column to `num_authors`
--INFO-- Processing `num_authors` column
--INFO-- Copying `global_references` column to `num_global_references`
--INFO-- Processing `num_global_references` column
--INFO-- Creating `article` column
--INFO-- Processing `raw_author_keywords` column
--INFO-- Processing `raw_index_keywords` column
--INFO-- Concatenating `raw_author_keywords` and `raw_index_keywords` columns to `raw_keywords`
--INFO-- Processing `title` column
--INFO-- Copying `title` column to `raw_title_nlp_phrases`
--INFO-- Processing `raw_title_nlp_phrases` column
--INFO-- Processing `abstract` column
--INFO-- Copying `abstract` column to `raw_abstract_nlp_phrases`
--INFO-- Processing `raw_abstract_nlp_phrases` column
--INFO-- Concatenating `raw_title_nlp_phrases` and `raw_abstract_nlp_phrases` columns to `raw_nlp_phrases`
--INFO-- Processing `raw_nlp_phrases` column
--INFO-- Concatenating `raw_nlp_phrases` and `raw_keywords` columns to `raw_descriptors`
--INFO-- Processing `raw_descriptors` column
--INFO-- Searching `references` using DOI
--INFO-- Searching `references` using (year, title, author)
--INFO-- Searching `references` using (title)
--INFO-- Creating `local_citations` column in references database
--INFO-- Creating `local_citations` column in documents database
--INFO-- The data/regtech/countries.txt thesaurus file was created
--INFO-- Creating `descriptors.txt` from author/index keywords, and abstract/title nlp phrases
--INFO-- The data/regtech/organizations.txt thesaurus file was created
--INFO-- The data/regtech/countries.txt thesaurus file was applied to affiliations in all databases
--INFO-- Applying `descriptors.txt` thesaurus to author/index keywords and abstract/title words
--INFO-- The data/regtech/organizations.txt thesaurus file was applied to affiliations in all databases
--INFO-- Process finished!!!
--INFO-- data/regtech/databases/_references.csv: 909 imported records
--INFO-- data/regtech/databases/_main.csv: 52 imported records
--INFO-- data/regtech/databases/_cited_by.csv: 387 imported records

>>> import pandas as pd
>>> from pprint import pprint
>>> import textwrap
>>> my_list = pd.read_csv(root_dir + "databases/_main.csv", encoding="utf-8").columns.tolist()
>>> wrapped_list = textwrap.fill(", ".join(sorted(my_list)), width=79)
>>> print(wrapped_list)
abstract, abstract_nlp_phrases, affiliations, art_no, article, author_keywords,
authors, authors_id, authors_with_affiliations, coden, correspondence_address,
countries, country_1st_author, descriptors, document_type, doi, eid,
global_citations, global_references, index_keywords, isbn, issn, issue,
keywords, link, local_citations, local_references, nlp_phrases, num_authors,
num_global_references, open_access, organization_1st_author, organizations,
page_end, page_start, publication_stage, raw_abstract_nlp_phrases,
raw_author_keywords, raw_authors, raw_authors_id, raw_countries,
raw_descriptors, raw_index_keywords, raw_keywords, raw_nlp_phrases,
raw_organizations, raw_title_nlp_phrases, source, source_abbr, source_title,
title, title_nlp_phrases, volume, year






>>> recors = pd.read_csv(root_dir + "databases/_main.csv", encoding="utf-8")
>>> print(recors[["raw_authors_id", "authors_id"]].head().to_markdown())
|    | raw_authors_id                                                           | authors_id                                                                                                                                            |
|---:|:-------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | 57194137877;57694114300;35369323900;                                     | 000000000000057194137877;000000000000057694114300;000000000000035369323900                                                                            |
|  1 | 58065730600;25928338900;57212494182;                                     | 000000000000058065730600;000000000000025928338900;000000000000057212494182                                                                            |
|  2 | 9633912200;57203071719;                                                  | 000000000000009633912200;000000000000057203071719                                                                                                     |
|  3 | 57211924905;57218104231;56779331500;56645203200;57439248400;56291956400; | 000000000000057211924905;000000000000057218104231;000000000000056779331500;000000000000056645203200;000000000000057439248400;000000000000056291956400 |
|  4 | 57206840410;57226162166;57189220315;                                     | 000000000000057206840410;000000000000057226162166;000000000000057189220315                                                                            |

    


# pylint: disable=line-too-long
"""
import glob
import os
import pathlib

import pandas as pd
from textblob import TextBlob
from tqdm import tqdm

from ..refine import (
    apply_countries_thesaurus,
    apply_descriptors_thesaurus,
    apply_organizations_thesaurus,
)

# from ..reports import abstracts_report
from .create_countries_thesaurus import create_countries_thesaurus
from .create_descriptors_thesaurus import create_descriptors_thesaurus
from .create_organizations_thesaurus import create_organizations_thesaurus

KEYWORDS_MAX_LENGTH = 50


def ingest_raw_data(
    root_dir="./", disable_progress_bar=False, **document_types
):
    """
    Import a Scopus data file in the working directory.

    Args:
        root_dir (str): The root directory to import the data to.
        disable_progress_bar (bool): Whether to disable the progress bar.
        **document_types: Keyword arguments specifying the document types to import.

    Returns:
        None
    """

    #
    #
    # Phase 1: Preparing database files
    #
    #
    create_working_directories(root_dir)
    create_stopword_txt_file(root_dir)
    create_database_files(root_dir)
    rename_scopus_columns_in_database_files(root_dir)
    format_columns_names_in_database_files(root_dir)
    repair_authors_id_in_database_files(root_dir)
    repair_bad_separators_in_keywords(root_dir)

    discarded_types = [
        key.lower()
        for key, value in document_types.items()
        if isinstance(value, bool) and value is False
    ]

    remove_records(root_dir, "document_type", discarded_types)
    drop_empty_columns_in_database_files(root_dir)

    #
    #
    # Phase 2: Process each column in isolation
    #
    #

    process_text_columns(
        root_dir,
        lambda x: x.str.normalize("NFKD")
        .str.encode("ascii", errors="ignore")
        .str.decode("utf-8"),
        "remove accents",
    )

    process_text_columns(
        root_dir,
        lambda x: x.str.replace("\n", "")
        .str.replace("\r", "")
        .str.replace("&lpar;", "(")
        .str.replace("&rpar;", ")")
        .replace("&colon;", ":"),
        "remove stranger chars",
    )

    remove_records(
        root_dir,
        "raw_authors",
        ["Anon", "[No author name available]"],
    )

    process_column(
        root_dir,
        "authors_id",
        lambda x: x.str.replace(";$", "", regex=True).mask(
            x == "[No author id available]", pd.NA
        ),
    )

    process_column(
        root_dir,
        "document_type",
        lambda x: x.str.lower().str.replace(" ", "_"),
    )

    process_column(
        root_dir,
        "eissn",
        lambda x: x.astype(str).str.replace("-", "", regex=True).str.upper(),
    )

    process_column(
        root_dir,
        "global_citations",
        lambda x: x.fillna(0).astype(int),
    )

    process_column(
        root_dir,
        "isbn",
        lambda x: x.astype(str).str.replace("-", "", regex=True).str.upper(),
    )

    process_column(
        root_dir,
        "issn",
        lambda x: x.astype(str).str.replace("-", "", regex=True).str.upper(),
    )

    process_column(
        root_dir,
        "raw_authors",
        lambda x: x.mask(x == "[No author name available]", pd.NA)
        .str.replace(",", ";", regex=False)
        .str.replace(".", "", regex=False),
    )

    process_column(
        root_dir,
        "source_name",
        lambda x: x.str.upper().str.replace(r"[^\w\s]", "", regex=True),
    )

    mask_column(
        root_dir,
        "source_abbr",
        "source_name",
    )

    process_column(
        root_dir,
        "source_abbr",
        lambda x: x.str.upper()
        .str.replace(".", "", regex=False)
        .str.replace(" JOURNAL ", " J ")
        .str.replace(" AND ", "")
        .str.replace(" IN ", "")
        .str.replace(" OF ", "")
        .str.replace(" ON ", "")
        .str.replace(" THE ", "")
        .str[:29],
    )

    process_column(
        root_dir,
        "doi",
        lambda x: x.str.replace("https://doi.org/", "", regex=False)
        .str.replace("http://dx.doi.org/", "", regex=False)
        .str.upper(),
    )

    disambiguate_author_names(root_dir)

    copy_to_column(root_dir, "authors", "num_authors")
    process_column(
        root_dir,
        "num_authors",
        lambda x: x.str.split(";").map(len).fillna(0).astype(int),
    )

    copy_to_column(root_dir, "global_references", "num_global_references")
    process_column(
        root_dir,
        "num_global_references",
        lambda x: x.str.split(";").str.len().fillna(0).astype(int),
    )

    create__article__column(root_dir)

    #
    #
    # Phase 3: Keywords & noun phrases & abstracts
    #
    #
    # In the context of topic modeling for research abstracts, it is generally
    # more common and beneficial to use "noun phrases" extracted using text
    # mining techniques rather than relying solely on provided "keywords" for
    # the given document.
    #
    # Research abstracts often contain technical and domain-specific
    # language, making it challenging to accurately capture the main topics
    # and themes using only manually assigned or provided keywords. On the
    # other hand, using text mining techniques to extract noun phrases can
    # help uncover more nuanced and contextually relevant phrases that better
    # represent the content of the abstracts.
    #
    # Text mining techniques, such as part-of-speech tagging, noun phrase
    # chunking, or natural language processing algorithms, can identify
    # meaningful noun phrases that may not be explicitly listed as keywords.
    # These extracted noun phrases can provide a more comprehensive
    # representation of the topics present in the research abstracts,
    # allowing for more accurate and informative topic modeling.
    #
    # Therefore, leveraging text mining techniques to extract noun phrases is
    # often preferred over relying solely on provided keywords when
    # conducting topic modeling on research abstracts.
    #

    #
    #
    # Prepare author/index keywords:
    # To upper() and replace spaces with underscores
    # Merge author/index keywords into a single column
    #
    process_column(
        root_dir,
        "raw_author_keywords",
        lambda x: x.str.upper()
        .str.split(";")
        .map(
            lambda w: "; ".join(
                sorted(
                    z.strip()
                    .replace("&", "AND")
                    .replace("   ", "  ")
                    .replace("  ", " ")
                    .replace(" ", "_")
                    .replace("/", "_")
                    .replace("\\", "_")
                    .replace(".", "_")
                    .replace(",", "_")
                    .replace("'", "_")
                    .replace("-", "_")
                    .replace("__", "_")
                    .replace("_(", " (")
                    for z in w
                )
            ),
            na_action="ignore",
        ),
    )
    process_column(
        root_dir,
        "raw_index_keywords",
        lambda x: x.str.upper()
        .str.split(";")
        .map(
            lambda w: "; ".join(
                sorted(
                    z.strip()
                    .replace("&", "AND")
                    .replace("   ", "  ")
                    .replace("  ", " ")
                    .replace(" ", "_")
                    .replace("/", "_")
                    .replace("\\", "_")
                    .replace(".", "_")
                    .replace(",", "_")
                    .replace("'", "_")
                    .replace("-", "_")
                    .replace("__", "_")
                    .replace("_(", " (")
                    for z in w
                )
            ),
            na_action="ignore",
        ),
    )
    concatenate_columns(
        root_dir,
        "raw_keywords",
        "raw_author_keywords",
        "raw_index_keywords",
    )

    #
    # Prepare title:
    # To lower() & remove brackets & remove multiple spaces & strip
    #
    process_column(
        root_dir,
        "title",
        lambda x: x.str.replace(r"\[.*", "", regex=True)
        .str.replace("   ", "  ")
        .str.replace("  ", " ")
        .str.strip()
        .str.lower(),
    )

    #
    # Technological Emergence Indicators using Emergence Score
    # Garner et al. 2017.
    # ------------------------------------------------------------------------
    #
    # Suitable terms for determining emergence are presented both in title and
    # the abstract. This allows to augment the list of terms given by the
    # authors/index keywords
    #

    #
    # Step 1: Create a candidate list of title nlp phrases
    #
    copy_to_column(root_dir, "title", "raw_title_nlp_phrases")
    process_column(
        root_dir,
        "raw_title_nlp_phrases",
        lambda x: x.astype(str)
        .map(lambda z: TextBlob(z).noun_phrases)
        .map(set, na_action="ignore")
        .map(sorted, na_action="ignore")
        .map(lambda x: [z for z in x if z != "nan"])
        .str.join("; ")
        .str.upper()
        .replace("   ", "  ")
        .replace("  ", " ")
        .str.replace(" ", "_")
        .str.replace("/", "_")
        .str.replace("\\", "_")
        .str.replace(".", "_")
        .str.replace(",", "_")
        .str.replace("'", "_")
        .str.replace("-", "_")
        .str.replace("__", "_")
        .str.replace(";_", "; ")
        .map(lambda x: pd.NA if x == "" else x),
    )

    #
    # Step 2: Create a candidate list of abstract nlp phrases
    #
    process_column(
        root_dir,
        "abstract",
        lambda x: x.mask(x == "[no abstract available]", pd.NA).str.lower(),
    )

    copy_to_column(root_dir, "abstract", "raw_abstract_nlp_phrases")
    process_column(
        root_dir,
        "raw_abstract_nlp_phrases",
        lambda x: x.astype(str)
        .map(lambda z: TextBlob(z).noun_phrases)
        .map(sorted, na_action="ignore")
        .map(set, na_action="ignore")
        .map(lambda x: [z for z in x if z != "nan"])
        .str.join("; ")
        .str.upper()
        .replace("   ", "  ")
        .replace("  ", " ")
        .str.replace(" ", "_")
        .str.replace("/", "_")
        .str.replace("\\", "_")
        .str.replace(".", "_")
        .str.replace(",", "_")
        .str.replace("'", "_")
        .str.replace("-", "_")
        .str.replace("__", "_")
        .str.replace(";_", "; ")
        .map(lambda x: pd.NA if x == "" else x),
    )

    #
    # Step 3: Filter terms in title and abstract nlp phrases
    #
    filter_nlp_phrases(root_dir)

    #
    # Continue normal processing ....
    #
    concatenate_columns(
        root_dir,
        "raw_nlp_phrases",
        "raw_title_nlp_phrases",
        "raw_abstract_nlp_phrases",
    )

    process_column(
        root_dir,
        "raw_nlp_phrases",
        lambda x: x.astype(str)
        .str.split("; ")
        .apply(lambda x: sorted(set(x)))
        .apply(lambda x: [z for z in x if z != "nan"])
        .str.join("; ")
        .apply(lambda x: pd.NA if x == "" else x),
    )

    concatenate_columns(
        root_dir,
        "raw_descriptors",
        "raw_nlp_phrases",
        "raw_keywords",
    )

    process_column(
        root_dir,
        "raw_descriptors",
        lambda x: x.astype(str)
        .str.split("; ")
        .apply(lambda x: sorted(set(x)))
        .apply(lambda x: [z for z in x if z != "nan"])
        .str.join("; ")
        .apply(lambda x: pd.NA if x == "" else x),
    )

    transform_abstract_keywords_to_underscore(root_dir)

    #
    #
    # Phase 4: References
    #
    #
    create_references(root_dir, disable_progress_bar)
    create__local_citations__column_in_references_database(root_dir)
    create__local_citations__column_in_documents_database(root_dir)

    #
    #
    # Phase 5: Thesaurus files
    #
    #
    create_countries_thesaurus(root_dir)
    create_descriptors_thesaurus(root_dir)
    create_organizations_thesaurus(root_dir)

    apply_countries_thesaurus(root_dir)
    apply_descriptors_thesaurus(root_dir)
    apply_organizations_thesaurus(root_dir)

    print("--INFO-- Process finished!!!")

    ## abstracts_report(root_dir=root_dir, file_name="imported_records.txt")
    report_imported_records_per_file(root_dir)


#
#
# End of main function
#
#


def create_working_directories(root_dir):
    """
    Create the working directories for the Scopus data.

    Args:
        root_dir (str): The root directory to create the directories in.

    Returns:
        None

    :meta private:
    """
    for directory in ["databases", "reports"]:
        directory_path = os.path.join(root_dir, directory)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)


def create_stopword_txt_file(root_dir):
    """
    Create an empty stopwords.txt file if it doesn't exist.

    Args:
        root_dir (str): The root directory containing the processed directory.

    Returns:
        None

    :meta private:
    """
    file_path = os.path.join(root_dir, "stopwords.txt")

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8"):
            pass


def create_database_files(root_dir):
    """
    Create processed CSV files from raw CSV files.

    Args:
        root_dir (str): The root directory containing the raw and processed directories.

    Returns:
        None

    :meta private:
    """
    raw_dir = os.path.join(root_dir, "raw-data")
    processed_dir = os.path.join(root_dir, "databases")

    folders = get_subdirectories(raw_dir)
    for folder in folders:
        data = concat_raw_csv_files(os.path.join(raw_dir, folder))
        file_name = f"_{folder}.csv"
        file_path = os.path.join(processed_dir, file_name)
        data.to_csv(file_path, sep=",", encoding="utf-8", index=False)

    file_path = os.path.join(root_dir, "databases/_DO_NOT_TOUCH_.txt")
    with open(file_path, "w", encoding="utf-8"):
        pass


def get_subdirectories(directory):
    """
    Get a list of subdirectories in a directory.

    Args:
        directory (str): The directory to get the subdirectories from.

    Returns:
        A list of subdirectories.

    :meta private:
    """
    subdirectories = os.listdir(directory)
    subdirectories = [
        f for f in subdirectories if os.path.isdir(os.path.join(directory, f))
    ]
    return subdirectories


def concat_raw_csv_files(path, quiet=False):
    """
    Concatenate raw CSV files in a directory.

    Args:
        path (str): The path to the directory containing the raw CSV files.
        quiet (bool): Whether to suppress output.

    Returns:
        A pandas DataFrame containing the concatenated data.

    :meta private:
    """
    if not quiet:
        print(f"--INFO-- Concatenating raw files in {path}/")

    files = get_csv_files(path)
    if not files:
        raise FileNotFoundError(f"No CSV files found in {path}")

    data = []
    for file_name in files:
        file_path = os.path.join(path, file_name)
        data.append(
            pd.read_csv(file_path, encoding="utf-8", on_bad_lines="skip")
        )

    data = pd.concat(data, ignore_index=True)
    data = data.drop_duplicates()

    return data


def get_csv_files(directory):
    """
    Get a list of CSV files in a directory.

    Args:
        directory (str): The directory to get the CSV files from.

    Returns:
        A list of CSV files.

    :meta private:
    """
    csv_files = os.listdir(directory)
    csv_files = [f for f in csv_files if f.endswith(".csv")]
    return csv_files


def rename_scopus_columns_in_database_files(root_dir):
    """Rename Scopus columns in the processed CSV files.

    The name equivalences are stored in a repository file.




    :meta private:
    """
    print("--INFO-- Applying scopus tags to database files")

    owner = "jdvelasq"
    repo = "techminer2"
    path = "settings/scopus2tags.csv"
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{path}"

    tags = pd.read_csv(url, encoding="utf-8")
    tags["scopus"] = tags["scopus"].str.strip()
    tags["techminer"] = tags["techminer"].str.strip()
    scopus2tags = dict(zip(tags["scopus"], tags["techminer"]))

    processed_dir = pathlib.Path(root_dir) / "databases"
    files = list(processed_dir.glob("_*.csv"))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        data.rename(columns=scopus2tags, inplace=True)
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def filter_nlp_phrases(root_dir):
    """Filter nlp phrases in abstract and title

    :meta private:
    """

    def get_nlp_phrases(column):
        databases_dir = pathlib.Path(root_dir) / "databases"
        files = list(databases_dir.glob("_*.csv"))
        nlp_phrases = set()
        for file in files:
            data = pd.read_csv(file, encoding="utf-8")
            if column not in data.columns:
                continue
            file_nlp_phrases = data[column].dropna()
            file_nlp_phrases = (
                file_nlp_phrases.dropna()
                .str.split(";")
                .explode()
                .str.strip()
                .drop_duplicates()
                .to_list()
            )
            nlp_phrases.update(file_nlp_phrases)
        return nlp_phrases

    def apply_filter_to_nlp_phrases(column, selected_nlp_phrases):
        """Apply filter to nlp phrases to the specicied column"""

        databases_dir = pathlib.Path(root_dir) / "databases"
        files = list(databases_dir.glob("_*.csv"))

        for file in files:
            data = pd.read_csv(file, encoding="utf-8")
            if column not in data.columns:
                continue
            data[column] = (
                data[column]
                .astype(str)
                .str.split("; ")
                .map(lambda x: [w.strip() for w in x])
                .map(lambda x: [w for w in x if w in selected_nlp_phrases])
                .map(lambda x: [w for w in x if w != "nan"])
                .map(lambda x: "; ".join(sorted(x)))
                .map(lambda x: pd.NA if x == "" else x)
            )
            data.to_csv(file, sep=",", encoding="utf-8", index=False)

    #
    # Main code:
    #

    # Obtain the raw nlp phrases
    raw_keywords = get_nlp_phrases("raw_keywords")
    raw_title_nlp_phrases = get_nlp_phrases("raw_title_nlp_phrases")
    raw_abstract_nlp_phrases = get_nlp_phrases("raw_abstract_nlp_phrases")

    # nlp phrases appearing in the title and abstract
    selected_nlp_phrases = raw_title_nlp_phrases & raw_abstract_nlp_phrases

    # adds raw keywords
    selected_nlp_phrases.update(raw_keywords)

    apply_filter_to_nlp_phrases(
        "raw_title_nlp_phrases",
        selected_nlp_phrases,
    )

    apply_filter_to_nlp_phrases(
        "raw_abstract_nlp_phrases",
        selected_nlp_phrases,
    )


def format_columns_names_in_database_files(root_dir: str) -> None:
    """
    Format column names in database files.

    Args:
        root_dir: The root directory containing the processed CSV files.

    Returns:
        None

    :meta private:
    """
    print("--INFO-- Formatting column names in database files")

    processed_dir = pathlib.Path(root_dir) / "databases"
    files = list(processed_dir.glob("_*.csv"))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        data = format_column_names(data)
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def format_column_names(data: pd.DataFrame) -> pd.DataFrame:
    """
    Format column names in a pandas DataFrame.

    Args:
        data: The pandas DataFrame to format.

    Returns:
        The pandas DataFrame with formatted column names.

    :meta private:
    """
    return data.rename(
        columns={
            col: col.replace(".", "").replace(" ", "_").lower()
            for col in data.columns
        }
    )


def repair_authors_id_in_database_files(root_dir: str) -> None:
    """
    Repair authors IDs in the processed CSV files.

    Args:
        root_dir: The root directory containing the processed CSV files.

    Returns:
        None

    :meta private:
    """
    print("--INFO-- Repairing authors ID")

    processed_dir = pathlib.Path(root_dir) / "databases"
    files = list(processed_dir.glob("_*.csv"))
    max_length = get_max_authors_id_length(files)
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        data["authors_id"] = repair_authors_id(
            data["raw_authors_id"], max_length
        )
        data.to_csv(file, index=False, encoding="utf-8")


def get_max_authors_id_length(files: list) -> int:
    """
    Get the maximum length of authors IDs in a list of CSV files.

    Args:
        files: A list of CSV files.

    Returns:
        The maximum length of authors IDs.

    :meta private:
    """
    lengths = []
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        ids = data["raw_authors_id"].copy()
        ids = ids.str.rstrip(";")
        ids = ids.str.split(";")
        ids = ids.explode()
        ids = ids.drop_duplicates()
        ids = ids.str.strip()
        ids = ids.str.len()
        lengths.append(ids.max())
    return max(lengths)


def repair_authors_id(authors_id: pd.Series, max_length: int) -> pd.Series:
    """
    Repair authors IDs in a pandas Series.

    Args:
        authors_id: The pandas Series containing authors IDs.
        max_length: The maximum length of authors IDs.

    Returns:
        The pandas Series with repaired authors IDs.

    :meta private:
    """

    return (
        authors_id.str.rstrip(";")
        .str.split(";")
        .apply(lambda x: [i.strip() for i in x])
        .apply(lambda x: [i.rjust(max_length, "0") for i in x])
        .str.join(";")
    )


def repair_bad_separators_in_keywords(root_dir):
    """Repair keywords with bad separators in the processed CSV files.

    In Scopus, keywords are separated by semicolons. However, some records
    contain keywords separated by commas. This function repairs these
    keywords.

    Args:
        root_dir: The root directory containing the processed CSV files.

    Returns:
        None

    :meta private:
    """
    print("--INFO-- Repairing bad separators in keywords")
    processed_dir = pathlib.Path(root_dir) / "databases"
    files = list(processed_dir.glob("_*.csv"))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        for column in ["raw_index_keywords", "raw_authors_keywords"]:
            if column in data.columns:
                data[column] = repair_keywords_in_column(data[column])
        data.to_csv(file, index=False, encoding="utf-8")


def repair_keywords_in_column(raw_keywords: pd.Series) -> pd.Series:
    """Repair keywords in a pandas Series.


    :meta private:
    """
    keywords = raw_keywords.copy()
    keywords = keywords.dropna()
    keywords = keywords.str.split("; ").explode().str.strip().drop_duplicates()
    keywords = keywords[keywords.str.len() > KEYWORDS_MAX_LENGTH]
    if len(keywords) > 0:
        for keyword in keywords:
            print(f"--WARNING-- Keyword with bad separator: {keyword}")
            raw_keywords = raw_keywords.str.replace(
                keyword, keyword.replace(",", ";")
            )
    return raw_keywords


def remove_records(root_dir, col_name, values_to_remove):
    """Remove records with a given value in a given column.

    Args:
        root_dir (str): root directory.
        col_name (str): column name.
        values_to_remove (list): values to remove.

    :meta private:
    """
    if len(values_to_remove) == 0:
        return
    print(f"--INFO-- Removing records with `{col_name}` in {values_to_remove}")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        org_length = len(data)
        data = data[~data[col_name].isin(values_to_remove)]
        new_length = len(data)
        if org_length != new_length:
            print(f"--INFO-- Removed {org_length - new_length} records")
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def drop_empty_columns_in_database_files(root_dir):
    """Drop NA columns in database files.

    :meta private:
    """

    print("--INFO-- Dropping NA columns in database files")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        original_cols = data.columns.copy()
        data = data.dropna(axis=1, how="all")
        if len(data.columns) != len(original_cols):
            removed_cols = set(original_cols) - set(data.columns)
            print(f"--INFO-- Removed columns: {removed_cols}")
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def process_text_columns(root_dir, process_func, msg):
    """Process text columns in all database files.

    Args:
        root_dir (str): root directory.
        process_func (function): function to be applied to each column.

    :meta private:
    """
    print(f"--INFO-- Processing text columns ({msg})")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        cols = data.select_dtypes(include=["object"]).columns
        for col in cols:
            data[col] = process_func(data[col])
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def process_column(root_dir, column_name, process_func):
    """Process a column in all database files.

    Args:
        root_dir (str): root directory.
        column_name (str): column name.
        process_func (function): function to be applied to the column.

    Returns:
        None

    :meta private:
    """
    print(f"--INFO-- Processing `{column_name}` column")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if column_name in data.columns:
            data[column_name] = process_func(data[column_name])
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def mask_column(root_dir, masked_col, rep_col):
    """Mask a column in all database files.

    :meta private:
    """
    print(f"--INFO-- Mask `{masked_col}` column with `{rep_col}`")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if masked_col in data.columns and rep_col in data.columns:
            data[masked_col].mask(data[masked_col].isnull(), data[rep_col])
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def disambiguate_author_names(root_dir):
    """Create the authors column.

    :meta private:
    """

    #
    def load_authors_names():
        files = list(glob.glob(os.path.join(root_dir, "databases/_*.csv")))
        data = [
            pd.read_csv(file, encoding="utf-8")[["raw_authors", "authors_id"]]
            for file in files
        ]
        data = pd.concat(data)
        data = data.dropna()
        return data

    #
    def build_dict_names(data):
        data = data.copy()

        data = data.assign(
            authors_and_ids=data.raw_authors + "#" + data.authors_id
        )
        data.authors_and_ids = data.authors_and_ids.str.split("#")
        data.authors_and_ids = data.authors_and_ids.apply(
            lambda x: (x[0].split(";"), x[1].split(";"))
        )
        data.authors_and_ids = data.authors_and_ids.apply(
            lambda x: list(zip(x[0], x[1]))
        )
        data = data.explode("authors_and_ids")
        data.authors_and_ids = data.authors_and_ids.apply(
            lambda x: (x[0].strip(), x[1].strip())
        )
        data = data.reset_index(drop=True)
        data = data[["authors_and_ids"]]
        data["author"] = data.authors_and_ids.apply(lambda x: x[0])
        data["author_id"] = data.authors_and_ids.apply(lambda x: x[1])
        data = data.drop(columns=["authors_and_ids"])
        data = data.drop_duplicates()
        data = data.sort_values(by=["author"])
        data = data.assign(counter=data.groupby(["author"]).cumcount())
        data = data.assign(author=data.author + "/" + data.counter.astype(str))
        data.author = data.author.str.replace("/0", "")
        author_id2name = dict(zip(data.author_id, data.author))
        return author_id2name

    def repair_names(author_id2name):
        files = list(glob.glob(os.path.join(root_dir, "databases/_*.csv")))
        # total_items = len(files)
        for file in files:
            data = pd.read_csv(file, encoding="utf-8")
            data = data.assign(authors=data.authors_id.copy())
            data["authors"] = data["authors"].str.split(";")
            data["authors"] = data["authors"].map(
                lambda x: [author_id2name[id] for id in x]
            )
            data["authors"] = data["authors"].str.join("; ")
            data.to_csv(file, sep=",", encoding="utf-8", index=False)

    #
    print("--INFO-- Disambiguating `authors` column")
    data = load_authors_names()
    author_id2name = build_dict_names(data)
    repair_names(author_id2name)


def copy_to_column(root_dir, src, dest):
    """Copy a column in all database files.

    :meta private:
    """
    print(f"--INFO-- Copying `{src}` column to `{dest}`")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if src in data.columns:
            data[dest] = data[src]
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def concatenate_columns(root_dir, dest, column_name1, column_name2):
    """Concatenate two columns in all database files.

    :meta private:
    """
    print(
        f"--INFO-- Concatenating `{column_name1}` and `{column_name2}` columns to `{dest}`"
    )

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if column_name1 in data.columns and column_name2 in data.columns:
            src = data[column_name1].astype(str).str.split("; ")
            dst = data[column_name2].astype(str).str.split("; ")
            con = src + dst
            con = con.map(lambda x: [z for z in x if z != "nan"])
            con = con.map(lambda x: sorted(set(x)), na_action="ignore")
            con = con.map(lambda x: "; ".join(x), na_action="ignore")
            con = con.map(lambda x: x if x != "" else pd.NA)
            data[dest] = con

        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def create__article__column(root_dir):
    """Create a WoS style reference column.

    :meta private:
    """
    #
    # First Author, year, source_abbr, 'V'volumne, 'P'page_start, ' DOI ' doi
    #
    print("--INFO-- Creating `article` column")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        #
        wos_ref = data.authors.map(
            lambda x: x.split("; ")[0].strip()
            if not pd.isna(x)
            else "[Anonymous]"
        )
        wos_ref += ", " + data.year.map(str)
        wos_ref += ", " + data.source_abbr
        wos_ref += data.volume.map(
            lambda x: ", V" + str(x).replace(".0", "")
            if not pd.isna(x)
            else ""
        )
        wos_ref += data.page_start.map(
            lambda x: ", P" + str(x).replace(".0", "")
            if not pd.isna(x)
            else ""
        )
        # wos_ref += data.doi.map(lambda x: ", DOI " + str(x) if not pd.isna(x) else "")
        data["article"] = wos_ref.copy()
        data = data.drop_duplicates(subset=["article"])
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def create_references(directory, disable_progress_bar=False):
    """Create references from `documents.csv` or `_references.csv` file.

    :meta private:
    """

    references_path = os.path.join(directory, "databases/_references.csv")
    if os.path.exists(references_path):
        create_referneces_from_references_csv_file(
            directory, disable_progress_bar
        )
    else:
        create_references_from_documents_csv_file(
            directory, disable_progress_bar
        )


def create_references_from_documents_csv_file(
    directory, disable_progress_bar=False
):
    """Create references from `documents.csv` file.

    :meta private:
    """

    print("--INFO-- Creating references from  `_main.csv` file.")

    documents_path = os.path.join(directory, "databases/_main.csv")
    documents = pd.read_csv(documents_path)

    # references como aparecen en los articulos
    raw_cited_references = documents.global_references.copy()
    raw_cited_references = raw_cited_references.str.lower()
    raw_cited_references = raw_cited_references.str.split(";")
    raw_cited_references = raw_cited_references.explode()
    raw_cited_references = raw_cited_references.str.strip()
    raw_cited_references = raw_cited_references.dropna()
    raw_cited_references = raw_cited_references.drop_duplicates()
    raw_cited_references = raw_cited_references.reset_index(drop=True)

    # record in document.csv ---> reference
    thesaurus = {t: None for t in raw_cited_references.tolist()}

    # references = pd.read_csv(references_path)

    # marcador para indicar si la referencia fue encontrada
    references = documents.copy()
    references["found"] = False

    # busqueda por doi
    print("--INFO-- Searching `references` using DOI")
    with tqdm(total=len(references), disable=disable_progress_bar) as pbar:
        for doi, article in zip(references.doi, references.article):
            for key in thesaurus.keys():
                if thesaurus[key] is None:
                    if not pd.isna(doi) and doi in key:
                        thesaurus[key] = article
                        references.loc[references.doi == doi, "found"] = True
            pbar.update(1)

    # Reduce la base de búsqueda
    references = references[~references.found]

    # Busqueda por (año, autor y tttulo)
    print("--INFO-- Searching `references` using (year, title, author)")
    with tqdm(total=len(references), disable=disable_progress_bar) as pbar:
        for article, year, authors, title in zip(
            references.article,
            references.year,
            references.authors,
            references.title,
        ):
            year = str(year)
            author = authors.split()[0].lower()
            title = (
                title.lower()
                .replace(".", "")
                .replace(",", "")
                .replace(":", "")
                .replace(";", "")
                .replace("-", " ")
                .replace("'", "")
            )

            for key in thesaurus.keys():
                if thesaurus[key] is None:
                    text = key
                    text = (
                        text.lower()
                        .replace(".", "")
                        .replace(",", "")
                        .replace(":", "")
                        .replace(";", "")
                        .replace("-", " ")
                        .replace("'", "")
                    )

                    if (
                        author in text
                        and str(year) in text
                        and title[:29] in text
                    ):
                        thesaurus[key] = article
                        references.found[references.article == article] = True
                    elif (
                        author in text
                        and str(year) in text
                        and title[-29:] in text
                    ):
                        thesaurus[key] = article
                        references.found[references.article == article] = True

            pbar.update(1)

    # Reduce la base de búsqueda
    references = references[~references.found]

    # Busqueda por titulo
    print("--INFO-- Searching `references` using (title)")
    with tqdm(total=len(references), disable=disable_progress_bar) as pbar:
        for article, title in zip(
            references.article,
            references.title,
        ):
            title = (
                title.lower()
                .replace(".", "")
                .replace(",", "")
                .replace(":", "")
                .replace(";", "")
                .replace("-", " ")
                .replace("'", "")
            )

            for key in thesaurus.keys():
                text = key
                text = (
                    text.lower()
                    .replace(".", "")
                    .replace(",", "")
                    .replace(":", "")
                    .replace(";", "")
                    .replace("-", " ")
                    .replace("'", "")
                )

                if title in text:
                    thesaurus[key] = article
                    references.found[references.article == article] = True

            pbar.update(1)
    #
    # Crea la columna de referencias locales
    #
    documents["local_references"] = documents.global_references.copy()
    documents["local_references"] = documents["local_references"].str.lower()
    documents["local_references"] = documents["local_references"].str.split(
        ";"
    )
    documents["local_references"] = documents["local_references"].map(
        lambda x: [t.strip() for t in x] if isinstance(x, list) else x
    )
    documents["local_references"] = documents["local_references"].map(
        lambda x: [thesaurus.get(t, "") for t in x]
        if isinstance(x, list)
        else x
    )
    documents["local_references"] = documents["local_references"].map(
        lambda x: [t for t in x if t is not None] if isinstance(x, list) else x
    )
    documents["local_references"] = documents["local_references"].str.join(
        "; "
    )
    documents["local_references"] = documents["local_references"].map(
        lambda x: pd.NA if x == "" else x
    )
    #
    documents.to_csv(documents_path, index=False)


def create_referneces_from_references_csv_file(
    directory, disable_progress_bar=False
):
    """Create the references from the references.csv file.

    :meta private:
    """

    references_path = os.path.join(directory, "databases/_references.csv")

    if not os.path.exists(references_path):
        print(f"--WARN-- The  file {references_path} does not exists.")
        print("--WARN-- Some functionalities are disabled.")
        return

    references = pd.read_csv(references_path)

    documents_path = os.path.join(directory, "databases/_main.csv")
    documents = pd.read_csv(documents_path)

    # references como aparecen en los articulos
    raw_cited_references = documents.global_references.copy()
    raw_cited_references = raw_cited_references.str.lower()
    raw_cited_references = raw_cited_references.str.split(";")
    raw_cited_references = raw_cited_references.explode()
    raw_cited_references = raw_cited_references.str.strip()
    raw_cited_references = raw_cited_references.dropna()
    raw_cited_references = raw_cited_references.drop_duplicates()
    raw_cited_references = raw_cited_references.reset_index(drop=True)

    # raw_cited_reference --> article
    thesaurus = {t: None for t in raw_cited_references.tolist()}

    # marcador para indicar si la referencia fue encontrada
    references["found"] = False

    # busqueda por doi
    print("--INFO-- Searching `references` using DOI")
    with tqdm(total=len(references), disable=disable_progress_bar) as pbar:
        for doi, article in zip(references.doi, references.article):
            for key in thesaurus.keys():
                if thesaurus[key] is None:
                    if not pd.isna(doi) and doi in key:
                        thesaurus[key] = article
                        references.loc[references.doi == doi, "found"] = True
            pbar.update(1)

    # Reduce la base de búsqueda
    references = references[~references.found]

    # Busqueda por (año, autor y tttulo)
    print("--INFO-- Searching `references` using (year, title, author)")
    with tqdm(total=len(references), disable=disable_progress_bar) as pbar:
        for article, year, authors, title in zip(
            references.article,
            references.year,
            references.authors,
            references.title,
        ):
            if (
                pd.isna(authors)
                or pd.isna(year)
                or pd.isna(title)
                or pd.isna(article)
            ):
                continue

            year = str(year)
            author = authors.split()[0].lower()
            title = (
                title.lower()
                .replace(".", "")
                .replace(",", "")
                .replace(":", "")
                .replace(";", "")
                .replace("-", " ")
                .replace("'", "")
            )

            for key in thesaurus.keys():
                if thesaurus[key] is None:
                    text = key
                    text = (
                        text.lower()
                        .replace(".", "")
                        .replace(",", "")
                        .replace(":", "")
                        .replace(";", "")
                        .replace("-", " ")
                        .replace("'", "")
                    )

                    if (
                        author in text
                        and str(year) in text
                        and title[:29] in text
                    ):
                        thesaurus[key] = article
                        references.loc[
                            references.article == article, "found"
                        ] = True
                    elif (
                        author in text
                        and str(year) in text
                        and title[-29:] in text
                    ):
                        thesaurus[key] = article
                        references.loc[
                            references.article == article, "found"
                        ] = True

            pbar.update(1)

    # Reduce la base de búsqueda
    references = references[~references.found]

    # Busqueda por titulo
    print("--INFO-- Searching `references` using (title)")
    with tqdm(total=len(references), disable=disable_progress_bar) as pbar:
        for article, title in zip(
            references.article,
            references.title,
        ):
            if isinstance(title, str):
                title = (
                    title.lower()
                    .replace(".", "")
                    .replace(",", "")
                    .replace(":", "")
                    .replace(";", "")
                    .replace("-", " ")
                    .replace("'", "")
                )

                for key in thesaurus.keys():
                    text = key
                    text = (
                        text.lower()
                        .replace(".", "")
                        .replace(",", "")
                        .replace(":", "")
                        .replace(";", "")
                        .replace("-", " ")
                        .replace("'", "")
                    )
                    if title in text:
                        thesaurus[key] = article
                        references.loc[
                            references.article == article, "found"
                        ] = True

            pbar.update(1)
    #
    # Crea la columna de referencias locales
    #
    documents["local_references"] = documents.global_references.copy()
    documents["local_references"] = documents["local_references"].str.lower()
    documents["local_references"] = documents["local_references"].str.split(
        ";"
    )
    documents["local_references"] = documents["local_references"].map(
        lambda x: [t.strip() for t in x] if isinstance(x, list) else x
    )
    documents["local_references"] = documents["local_references"].map(
        lambda x: [thesaurus.get(t, "") for t in x]
        if isinstance(x, list)
        else x
    )
    documents["local_references"] = documents["local_references"].map(
        lambda x: [t for t in x if t is not None] if isinstance(x, list) else x
    )
    documents["local_references"] = documents["local_references"].str.join(
        "; "
    )
    documents["local_references"] = documents["local_references"].map(
        lambda x: pd.NA if x == "" else x
    )
    #
    documents.to_csv(documents_path, index=False)


def create__local_citations__column_in_references_database(directory):
    """Create `local_citations` column in references database

    :meta private:
    """

    references_path = os.path.join(directory, "databases", "_references.csv")
    if not os.path.exists(references_path):
        return

    print("--INFO-- Creating `local_citations` column in references database")

    # counts the number of citations for each local reference
    documents_path = os.path.join(directory, "databases", "_main.csv")
    documents = pd.read_csv(documents_path)
    local_references = documents.local_references.copy()
    local_references = local_references.dropna()
    local_references = local_references.str.split(";")
    local_references = local_references.explode()
    local_references = local_references.str.strip()
    local_references = local_references.value_counts()
    values_dict = local_references.to_dict()

    # assigns the number of citations to each reference in references database

    references = pd.read_csv(references_path)
    references["local_citations"] = references.article
    references["local_citations"] = references["local_citations"].map(
        values_dict
    )
    references["local_citations"] = references["local_citations"].fillna(0)

    # saves the new column in the references database
    references.to_csv(references_path, index=False)


def create__local_citations__column_in_documents_database(root_dir):
    """Create `local_citations` column in documents database

    :meta private:
    """

    print("--INFO-- Creating `local_citations` column in documents database")

    # counts the number of citations for each local reference
    documents_path = os.path.join(root_dir, "databases", "_main.csv")
    documents = pd.read_csv(documents_path)
    local_references = documents.local_references.copy()
    local_references = local_references.dropna()
    local_references = local_references.str.split(";")
    local_references = local_references.explode()
    local_references = local_references.str.strip()
    local_references = local_references.value_counts()
    values_dict = local_references.to_dict()

    # assigns the number of citations to each document in documents database
    documents["local_citations"] = documents.article
    documents["local_citations"] = documents["local_citations"].map(
        values_dict
    )
    documents["local_citations"] = documents["local_citations"].fillna(0)

    # saves the new column in the references database
    documents.to_csv(documents_path, index=False)


def report_imported_records_per_file(root_dir):
    """Report the number of imported records per file.

    Args:
        root_dir (str): root directory.

    :meta private:
    """

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        print(f"--INFO-- {file}: {len(data.index)} imported records")


def transform_abstract_keywords_to_underscore(root_dir):
    """Transform keywords in abstracts to uppercase

    :meta private:
    """

    def get_raw_descriptors():
        """Returns a pandas Series with all NLP phrases in the database files"""
        processed_dir = pathlib.Path(root_dir) / "databases"
        files = list(processed_dir.glob("_*.csv"))
        descriptors = []
        for file in files:
            data = pd.read_csv(file, encoding="utf-8")
            if "raw_nlp_phrases" not in data.columns:
                continue
            candidate_descriptors = data["raw_descriptors"].copy()
            candidate_descriptors = (
                candidate_descriptors.dropna()
                .str.replace("_", " ")
                .str.lower()
            )
            descriptors.append(candidate_descriptors)
        descriptors = pd.concat(descriptors)
        descriptors = (
            descriptors.str.split("; ").explode().str.strip().drop_duplicates()
        )
        # nlp_phrases = nlp_phrases[nlp_phrases.str.contains(" ")]
        return descriptors

    def clean(descriptors):
        """Remove abbreviations from NLP phrases"""

        descriptors = descriptors.copy()

        # remove abbreviations
        descriptors = descriptors.str.replace(
            r"\(.*\)", "", regex=True
        ).replace(r"\[].*\]", "", regex=True)

        # strage characters
        descriptors = (
            descriptors.str.replace(r'"', "", regex=True)
            .str.replace("'", "", regex=False)
            .str.replace("#", "", regex=False)
            .str.replace("!", "", regex=False)
            .str.strip()
        )

        descriptors = descriptors[descriptors != ""]
        return descriptors

    def sort_by_num_words(descriptors):
        """Sort keywords by number of words"""

        descriptors = descriptors.copy()
        frame = descriptors.to_frame()
        frame["length"] = frame[descriptors.name].str.split(" ").map(len)
        frame = frame.sort_values(
            ["length", descriptors.name], ascending=[False, True]
        )
        descriptors = frame[descriptors.name].copy()
        return descriptors

    def replace_in_abstracts_and_titles(root_dir, descriptors):
        """Replace keywords in abstracts"""

        descriptors = descriptors.copy()
        descriptors = "|".join(descriptors.values)
        regex = r"\b(" + descriptors + r")\b"

        documents_path = pathlib.Path(root_dir) / "databases/_main.csv"
        documents = pd.read_csv(documents_path, encoding="utf-8")
        for col in ["abstract", "title"]:
            hyphenated_words = documents[col].str.findall(r"\b\w+-\w+\b").sum()
            hyphenated_words = r"\b(" + "|".join(hyphenated_words) + r")\b"
            documents[col] = (
                documents[col]
                .str.replace("-", " ")
                .str.replace(
                    regex, lambda x: x.group().upper().replace(" ", "_")
                )
            )
            documents[col] = documents[col].str.replace(
                hyphenated_words.replace("-", " "),
                lambda x: x.group().replace(" ", "-"),
            )

        documents.to_csv(documents_path, index=False)

    #
    # Main code:
    #
    descriptors = get_raw_descriptors()
    descriptors = clean(descriptors)
    descriptors = sort_by_num_words(descriptors)
    replace_in_abstracts_and_titles(root_dir, descriptors)

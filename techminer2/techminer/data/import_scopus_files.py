# flake8: noqa# flake8: noqa
"""
Import Scopus Files
===============================================================================

Import a scopus file to a working directory.


>>> directory = "data/regtech/"

>>> from techminer2 import techminer
>>> techminer.data.import_scopus_files(directory, disable_progress_bar=True)
--INFO-- Concatenating raw files in data/regtech/raw/cited_by/
--INFO-- Concatenating raw files in data/regtech/raw/references/
--INFO-- Concatenating raw files in data/regtech/raw/documents/
--INFO-- Applying scopus tags to database files
--INFO-- Formating column names in database files
--INFO-- Repairing authors ID
--INFO-- Dropping NA columns in database files
--INFO-- Processing text columns
--INFO-- Processing text columns
--INFO-- Removing records with `raw_authors` in ['Anon', '[No author name available]']
--INFO-- Processing `abstract` column
--INFO-- Processing `authors_id` column
--INFO-- Processing `title` column
--INFO-- Processing `document_type` column
--INFO-- Processing `doi` column
--INFO-- Processing `eissn` column
--INFO-- Processing `global_citations` column
--INFO-- Processing `isbn` column
--INFO-- Processing `issn` column
--INFO-- Processing `raw_authors` column
--INFO-- Mask `source_abbr` column with `source_name`
--INFO-- Processing `source_abbr` column
--INFO-- Processing `source_name` column
--INFO-- Processing `doi` column
--INFO-- Processing `raw_author_keywords` column
--INFO-- Processing `raw_index_keywords` column
--INFO-- Creating `authors` column
--INFO-- Copying `authors` column to `num_authors`
--INFO-- Processing `num_authors` column
--INFO-- Copying `global_references` column to `num_global_references`
--INFO-- Processing `num_global_references` column
--INFO-- Concatenating `raw_author_keywords` and `raw_index_keywords` columns to `raw_keywords`
--INFO-- Copying `abstract` column to `noun_phrases`
--INFO-- Processing `noun_phrases` column
--INFO-- Creating `authors` column
--INFO-- Copying `authors` column to `num_authors`
--INFO-- Processing `num_authors` column
--INFO-- Creating `article` column
--INFO-- Copying `global_references` column to `num_global_references`
--INFO-- Processing `num_global_references` column
--INFO-- Creating `abstract.csv` file from `documents` database
--INFO-- Creating `bradford` column
--INFO-- Process finished!!!
--INFO-- data/regtech/processed/_documents.csv: 52 imported records
--INFO-- data/regtech/processed/_references.csv: 909 imported records
--INFO-- data/regtech/processed/_cited_by.csv: 387 imported records


>>> import pandas as pd
>>> raw = pd.read_csv("data/regtech/raw/documents/scopus.csv")
>>> records = pd.read_csv("data/regtech/processed/_documents.csv")

>>> raw.DOI.head(), records.doi.head() 


# pylint: disable=line-too-long
"""
import glob
import os
import os.path
import sys

import numpy as np
import pandas as pd
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize
from textblob import TextBlob
from tqdm import tqdm

from ... import vantagepoint


#
#
# Main code:
#
#
def import_scopus_files(
    root_dir="./",
    disable_progress_bar=False,
    **document_types,
):
    """Import Scopus files."""

    #
    #
    # Phase 1: Preparing database files
    #
    #
    create_working_directories(root_dir)
    create_emtpy_stopwords_txt_file(root_dir)
    create_database_files(root_dir)
    rename_scopus_columns_in_database_files(root_dir)
    format_columns_names_in_database_files(root_dir)
    repair_authors_id(root_dir)

    _check_raw_keywords_len(root_dir)

    # Remove records with document types specified by the user
    document_types_to_discard = [
        key.lower()
        for key, value in document_types.items()
        if isinstance(value, bool) and value is False
    ]
    remove_records(
        root_dir,
        "document_type",
        document_types_to_discard,
    )

    drop_empty_columns_in_database_files(root_dir)

    #
    #
    # Phase 2: Process each column in isolation
    #
    #

    # Remove accents
    process_text_columns(
        root_dir,
        lambda x: x.str.normalize("NFKD")
        .str.encode("ascii", errors="ignore")
        .str.decode("utf-8"),
    )

    # Remove stranger chars
    process_text_columns(
        root_dir,
        lambda x: x.str.replace("\n", "")
        .str.replace("\r", "")
        .str.replace("&lpar;", "(")
        .str.replace("&rpar;", ")")
        .replace("&colon;", ":"),
    )

    # Remove records with anonymous authors
    remove_records(
        root_dir,
        "raw_authors",
        ["Anon", "[No author name available]"],
    )

    process_column(
        root_dir,
        "abstract",
        lambda x: x.mask(x == "[no abstract available]", pd.NA).str.lower(),
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
        "title",
        lambda x: x.str.replace(r"\[.*", "", regex=True).str.strip(),
    )

    process_column(
        root_dir,
        "document_type",
        lambda x: x.str.lower().str.replace(" ", "_"),
    )

    process_column(
        root_dir,
        "doi",
        lambda x: x.str.upper(),
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

    mask_columna(
        root_dir,
        "source_abbr",
        "source_name",
    )

    process_column(
        root_dir,
        "source_abbr",
        lambda x: x.str.upper().str.replace(".", "", regex=False).str[:29],
    )

    process_column(
        root_dir,
        "source_name",
        lambda x: x.str.upper().str.replace(r"[^\w\s]", "", regex=True),
    )

    process_column(
        root_dir,
        "doi",
        lambda x: x.str.replace(
            "https://doi.org/", "", regex=False
        ).str.replace("http://dx.doi.org/", "", regex=False),
    )

    process_column(
        root_dir,
        "raw_author_keywords",
        lambda x: x.str.lower()
        .str.split(";")
        .map(
            lambda w: "; ".join(sorted(z.strip() for z in w)),
            na_action="ignore",
        ),
    )

    process_column(
        root_dir,
        "raw_index_keywords",
        lambda x: x.str.lower()
        .str.split(";")
        .map(
            lambda w: "; ".join(sorted(z.strip() for z in w)),
            na_action="ignore",
        ),
    )

    create__authors__column(root_dir, disable_progress_bar)

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

    #
    #
    # Phase 3: Create raw_keywords columns
    #
    #
    concatenate_columns(
        root_dir,
        "raw_keywords",
        "raw_author_keywords",
        "raw_index_keywords",
    )

    #
    #
    # Phase 4: Noun phrases
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
    copy_to_column(root_dir, "abstract", "noun_phrases")
    process_column(
        root_dir,
        "noun_phrases",
        lambda x: x.map(lambda z: TextBlob(z).noun_phrases)
        .map(set)
        .map(sorted)
        .str.join("; "),
    )

    #
    #
    #

    #

    #
    #
    # Phase 5: Thesaurus
    #
    #

    # vantagepoint.refine.create_keywords_thesaurus(root_dir=root_dir)
    # vantagepoint.refine.apply_keywords_thesaurus(root_dir)
    #
    # -------------------------------------------------------------------------
    # vantagepoint.refine.create_countries_thesaurus(root_dir)
    # vantagepoint.refine.apply_countries_thesaurus(root_dir)
    #

    # _create__abstract_csv__file(root_dir)
    #
    create__article__column(root_dir)
    _create__bradford__column(root_dir)
    #
    # WoS References ----------------------------------------------------------
    # _create_references(root_dir, disable_progress_bar)
    # _create__local_citations__column_in_references_database(root_dir)
    # _create__local_citations__column_in_documents_database(root_dir)
    #
    # Organizations ------------------------------------------------------------
    # vantagepoint.refine.create_organizations_thesaurus(root_dir=root_dir)
    # vantagepoint.refine.apply_organizations_thesaurus(root_dir=root_dir)

    sys.stdout.write("--INFO-- Process finished!!!\n")
    report_imported_records_per_file(root_dir)


def process_column(root_dir, column_name, process_func):
    """Process a column in all database files.

    Args:
        root_dir (str): root directory.
        column_name (str): column name.
        process_func (function): function to be applied to the column.

    Returns:
        None

    .. ignore::
    """
    sys.stdout.write(f"--INFO-- Processing `{column_name}` column\n")

    files = list(glob.glob(os.path.join(root_dir, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if column_name in data.columns:
            data[column_name] = process_func(data[column_name])
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def copy_to_column(root_dir, src, dest):
    """Copy a column in all database files.

    .. ignore::
    """
    sys.stdout.write(f"--INFO-- Copying `{src}` column to `{dest}`\n")

    files = list(glob.glob(os.path.join(root_dir, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if src in data.columns:
            data[dest] = data[src]
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def mask_columna(root_dir, masked_col, rep_col):
    """Mask a column in all database files.

    .. ignore::
    """
    sys.stdout.write(f"--INFO-- Mask `{masked_col}` column with `{rep_col}`\n")

    files = list(glob.glob(os.path.join(root_dir, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if masked_col in data.columns and rep_col in data.columns:
            data[masked_col].mask(data[masked_col].isnull(), data[rep_col])
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def concatenate_columns(root_dir, dest, column_name1, column_name2):
    """Concatenate two columns in all database files.

    .. ignore::
    """
    sys.stdout.write(
        f"--INFO-- Concatenating `{column_name1}` and `{column_name2}` columns to `{dest}`\n"
    )

    files = list(glob.glob(os.path.join(root_dir, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if column_name1 in data.columns and column_name2 in data.columns:
            data[dest] = data[column_name1].str.split("; ") + data[
                column_name2
            ].str.split("; ")
            data[dest] = data[dest].map(
                lambda x: list(set(x)), na_action="ignore"
            )
            data[dest] = data[dest].map(
                lambda x: "; ".join(x), na_action="ignore"
            )
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def process_text_columns(root_dir, process_func):
    """Process text columns in all database files.

    Args:
        root_dir (str): root directory.
        process_func (function): function to be applied to each column.

    .. ignore::
    """
    sys.stdout.write("--INFO-- Processing text columns\n")

    files = list(glob.glob(os.path.join(root_dir, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        cols = data.select_dtypes(include=["object"]).columns
        for col in cols:
            data[col] = process_func(data[col])
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def create_emtpy_stopwords_txt_file(root_dir):
    """
    Create an empty stopwords.txt file if it doesn't exist.

    Args:
        root_dir (str): The root directory containing the processed directory.

    .. ignore::
    """
    file_path = os.path.join(root_dir, "processed/stopwords.txt")
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8"):
            pass


def report_imported_records_per_file(root_dir):
    """Report the number of imported records per file.

    Args:
        root_dir (str): root directory.

    .. ignore::
    """

    files = list(glob.glob(os.path.join(root_dir, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        sys.stdout.write(
            f"--INFO-- {file}: {len(data.index)} imported records\n"
        )


def create_working_directories(root_dir):
    """
    Create the working directories if they don't exist.

    Args:
        root_dir (str): The root directory for the working directories.

    .. ignore::
    """
    processed_dir = os.path.join(root_dir, "processed")
    reports_dir = os.path.join(root_dir, "reports")

    create_directory(processed_dir)
    create_directory(reports_dir)


def create_directory(directory):
    """Create a directory if it doesn't exist.

    Args:
        directory (str): The directory to create.

    .. ignore::
    """
    if not os.path.exists(directory):
        os.makedirs(directory)


def remove_records(root_dir, col_name, values_to_remove):
    """Remove records with a given value in a given column.

    Args:
        root_dir (str): root directory.
        col_name (str): column name.
        values_to_remove (list): values to remove.

    .. ignore::
    """
    if len(values_to_remove) == 0:
        return
    sys.stdout.write(
        f"--INFO-- Removing records with `{col_name}` in {values_to_remove}\n"
    )

    files = list(glob.glob(os.path.join(root_dir, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        data = data[~data[col_name].isin(values_to_remove)]
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def create_database_files(root_dir):
    """Create the database files.

    .. ignore::
    """

    folders = os.listdir(os.path.join(root_dir, "raw"))
    folders = [
        f for f in folders if os.path.isdir(os.path.join(root_dir, "raw", f))
    ]
    for folder in folders:
        data = concat_raw_csv_files(os.path.join(root_dir, "raw", folder))
        data.to_csv(
            os.path.join(root_dir, "processed", "_" + folder + ".csv"),
            sep=",",
            encoding="utf-8",
            index=False,
        )


def concat_raw_csv_files(path, quiet=False):
    """Load raw csv files in a directory.

    .. ignore::
    """

    if quiet is False:
        sys.stdout.write(f"--INFO-- Concatenating raw files in {path}/\n")

    files = [f for f in os.listdir(path) if f.endswith(".csv")]
    if len(files) == 0:
        raise FileNotFoundError(f"No CSV files found in {path}")
    data = []
    for file_name in files:
        data.append(
            pd.read_csv(
                os.path.join(path, file_name),
                encoding="utf-8",
                on_bad_lines="skip",
                # warn_bad_lines=True,
            )
        )

    data = pd.concat(data, ignore_index=True)
    data = data.drop_duplicates()

    return data


def rename_scopus_columns_in_database_files(root_dir):
    """Rename Scopus columns in the processed CSV files.

    The name equivalences are stored in a repository file.

    .. ignore::
    """

    sys.stdout.write("--INFO-- Applying scopus tags to database files\n")

    owner = "jdvelasq"
    repo = "techminer2"
    path = "settings/scopus2tags.csv"
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{path}"

    tags = pd.read_csv(url, encoding="utf-8")
    tags["scopus"] = tags["scopus"].str.strip()
    tags["techminer"] = tags["techminer"].str.strip()
    scopus2tags = dict(zip(tags["scopus"], tags["techminer"]))

    files = list(glob.glob(os.path.join(root_dir, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        data.rename(columns=scopus2tags, inplace=True)
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def format_columns_names_in_database_files(root_dir):
    """Format column names in database files.

    .. ignore::
    """

    sys.stdout.write("--INFO-- Formating column names in database files\n")

    files = list(glob.glob(os.path.join(root_dir, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        data = data.rename(
            columns={
                col: col.replace(".", "").replace(" ", "_").lower()
                for col in data.columns
            }
        )
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def drop_empty_columns_in_database_files(root_dir):
    """Drop NA columns in database files.

    .. ignore::
    """

    sys.stdout.write("--INFO-- Dropping NA columns in database files\n")

    files = list(glob.glob(os.path.join(root_dir, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        data = data.dropna(axis=1, how="all")
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def repair_authors_id(directory):
    """Repair authors ID.

    .. ignore::
    """

    def compute_max_key_length():
        lenghts = []
        for file in files:
            data = pd.read_csv(file, encoding="utf-8")
            ids = data["authors_id"].copy()
            ids = ids.map(lambda x: x[:-1] if x[-1] == ";" else x)
            ids = ids.str.split(";")
            ids = ids.explode()
            ids = ids.drop_duplicates()
            ids = ids.str.strip()
            ids = ids.str.len()
            lenghts.append(ids.max())
        return max(lenghts)

    #
    # Main code:
    #
    sys.stdout.write("--INFO-- Repairing authors ID\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    max_length = compute_max_key_length()

    for file in files:
        data = pd.read_csv(file, encoding="utf-8")

        data["authors_id"] = (
            data["authors_id"]
            .str.replace(";$", "", regex=True)
            .str.split(";")
            .apply(lambda x: [i.strip() for i in x])
            .apply(lambda x: [i.ljust(max_length, "0") for i in x])
            .str.join(";")
        )
        data.to_csv(file, index=False, encoding="utf-8")


def create__authors__column(directory, disable_progress_bar):
    """Create the authors column.

    .. ignore::
    """

    #
    def load_authors_names():
        files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
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

    def repair_names(author_id2name, disable_progress_bar):
        files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
        total_items = len(files)
        for file in files:
            data = pd.read_csv(file, encoding="utf-8")
            data = data.assign(authors=data.authors_id.copy())
            data["authors"] = data["authors"].str.split(";")
            data["authors"] = data["authors"].map(
                lambda x: [author_id2name[id] for id in x]
            )
            data["authors"] = data["authors"].map(lambda x: "; ".join(x))
            data.to_csv(file, sep=",", encoding="utf-8", index=False)

    #
    sys.stdout.write("--INFO-- Creating `authors` column\n")
    data = load_authors_names()
    author_id2name = build_dict_names(data)
    repair_names(author_id2name, disable_progress_bar)


def create__article__column(directory):
    """Create a WoS style reference column.

    .. ignore::
    """
    #
    # First Author, year, source_abbr, 'V'volumne, 'P'page_start, ' DOI ' doi
    #
    sys.stdout.write("--INFO-- Creating `article` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
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


######################


def _check_raw_keywords_len(directory):
    folders = os.listdir(os.path.join(directory, "raw"))
    folders = [
        f for f in folders if os.path.isdir(os.path.join(directory, "raw", f))
    ]
    for folder in folders:
        path = os.path.join(directory, "raw", folder)
        files = [f for f in os.listdir(path) if f.endswith(".csv")]
        if len(files) == 0:
            raise FileNotFoundError(f"No CSV files found in {path}")
        for file_name in files:
            raw_df = pd.read_csv(
                os.path.join(path, file_name),
                encoding="utf-8",
                on_bad_lines="skip",
            )

            for column in ["Author Keywords", "Index Keywords"]:
                if column in raw_df.columns:
                    keywords = raw_df[column].dropna()
                    keywords = keywords[
                        keywords.map(lambda x: isinstance(x, str))
                    ]
                    keywords = keywords.str.split(";")
                    keywords = keywords.explode()
                    keywords = keywords.reset_index(drop=True)
                    keywords = keywords.str.strip()
                    keywords = keywords[keywords.str.len() > 50]

                    if len(keywords):
                        newindex = (
                            keywords.str.len()
                            .sort_values(ascending=False)
                            .index
                        )
                        keywords = keywords.reindex(newindex)
                        for keyword in keywords:
                            raw_df[column] = raw_df[column].replace(
                                keyword, keyword.replace(",", ";")
                            )

                        raw_df.to_csv(
                            os.path.join(path, file_name),
                            encoding="utf-8",
                            index=False,
                        )


def _create_extract_raw_words_from_column(
    directory, source_column, dest_column
):
    roots = _extract_keywords_roots_from_database_files(directory).to_list()

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        #
        if source_column not in data.columns:
            continue

        sys.stdout.write(
            f"--INFO-- Creating `{dest_column}` column in {file}\n"
        )

        text = data[["article", source_column]].copy()
        text = text.dropna()

        text[source_column] = text[source_column].str.lower().copy()

        text["raw_words"] = text[source_column].map(
            lambda x: TextBlob(x).noun_phrases
        )
        text = text.explode("raw_words")
        text = text.dropna()
        text["keys"] = text["raw_words"].str.split()
        s = PorterStemmer()
        text["keys"] = text["keys"].map(lambda x: [s.stem(y) for y in x])
        text["keys"] = text["keys"].map(set)
        text["keys"] = text["keys"].map(sorted)
        text["keys"] = text["keys"].map(lambda x: " ".join(x))

        text["found"] = text["keys"].map(lambda x: x in roots)
        text = text[text["found"] == True]

        text = text[["article", "raw_words"]]
        text = text.groupby("article", as_index=False).aggregate(
            lambda x: list(x)
        )
        text["raw_words"] = text["raw_words"].map(set)
        text["raw_words"] = text["raw_words"].map(sorted)
        text["raw_words"] = text["raw_words"].str.join("; ")

        # convert the pandas series to a dictionary
        values_dict = dict(zip(text.article, text.raw_words))
        data[dest_column] = data["article"].map(
            lambda x: values_dict.get(x, pd.NA)
        )
        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _create__raw_words__column(directory):
    sys.stdout.write("--INFO-- Creating `raw_words` column\n")

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        #
        data["raw_words"] = ""
        data["raw_words"] = data["raw_words"].str.split(";")

        for column in [
            "raw_author_keywords",
            "raw_index_keywords",
            "raw_abstract_words",
            "raw_title_words",
        ]:
            if column in data.columns:
                text = data[column]
                text = text.fillna("")
                text = text.str.replace("; ", ";")
                text = text.str.split(";")

                data["raw_words"] += text

        data["raw_words"] = data["raw_words"].map(lambda x: sorted(set(x)))
        data["raw_words"] = data["raw_words"].map(
            lambda x: [y for y in x if y != ""]
        )
        data["raw_words"] = data["raw_words"].map(
            lambda x: pd.NA if len(x) == 0 else x
        )
        data["raw_words"] = data["raw_words"].str.join("; ")
        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False)


def _create__local_citations__column_in_documents_database(directory):
    sys.stdout.write(
        "--INFO-- Creating `local_citations` column in documents database\n"
    )

    # counts the number of citations for each local reference
    documents_path = os.path.join(directory, "processed", "_documents.csv")
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


def _create__local_citations__column_in_references_database(directory):
    references_path = os.path.join(directory, "processed", "_references.csv")
    if not os.path.exists(references_path):
        return

    sys.stdout.write(
        "--INFO-- Creating `local_citations` column in references database\n"
    )

    # counts the number of citations for each local reference
    documents_path = os.path.join(directory, "processed", "_documents.csv")
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


def _create_references(directory, disable_progress_bar=False):
    references_path = os.path.join(directory, "processed/_references.csv")
    if os.path.exists(references_path):
        _create_referneces_from_references_csv_file(
            directory, disable_progress_bar
        )
    else:
        _create_references_from_documents_csv_file(
            directory, disable_progress_bar
        )


def _create_references_from_documents_csv_file(
    directory, disable_progress_bar=False
):
    sys.stdout.write(
        "--INFO-- Creating references from  `documents.csv` file.\n"
    )

    documents_path = os.path.join(directory, "processed/_documents.csv")
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
    sys.stdout.write("--INFO-- Searching `references` using DOI\n")
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
    sys.stdout.write(
        "--INFO-- Searching `references` using (year, title, author)\n"
    )
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
    sys.stdout.write("--INFO-- Searching `references` using (title)\n")
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


def _create_referneces_from_references_csv_file(
    directory, disable_progress_bar=False
):
    references_path = os.path.join(directory, "processed/_references.csv")

    if not os.path.exists(references_path):
        sys.stdout.write(
            f"--WARN-- The  file {references_path} does not exists.\n"
        )
        sys.stdout.write("--WARN-- Some functionalities are disabled.\n")
        return

    references = pd.read_csv(references_path)

    documents_path = os.path.join(directory, "processed/_documents.csv")
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
    sys.stdout.write("--INFO-- Searching `references` using DOI\n")
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
    sys.stdout.write(
        "--INFO-- Searching `references` using (year, title, author)\n"
    )
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
    sys.stdout.write("--INFO-- Searching `references` using (title)\n")
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


def _create__abstract_csv__file(directory):
    sys.stdout.write(
        "--INFO-- Creating `abstract.csv` file from `documents` database\n"
    )

    documents = pd.read_csv(
        os.path.join(directory, "processed", "_documents.csv")
    )

    if "abstract" in documents.columns:
        abstracts = documents[
            ["article", "abstract", "global_citations"]
        ].copy()
        abstracts = abstracts.rename(columns={"abstract": "phrase"})
        abstracts = abstracts.dropna()
        abstracts = abstracts.assign(
            phrase=abstracts.phrase.str.replace(";", ".")
        )
        abstracts = abstracts.assign(
            phrase=abstracts.phrase.map(sent_tokenize)
        )
        abstracts = abstracts.explode("phrase")
        abstracts = abstracts.assign(phrase=abstracts.phrase.str.strip())
        abstracts = abstracts[abstracts.phrase.str.len() > 0]
        abstracts = abstracts.assign(
            line_no=abstracts.groupby(["article"]).cumcount()
        )
        abstracts = abstracts[
            ["article", "line_no", "phrase", "global_citations"]
        ]
        file_name = os.path.join(directory, "processed", "abstracts.csv")
        abstracts.to_csv(file_name, index=False)


# def _create__num_global_references__column(directory):
#     sys.stdout.write("--INFO-- Creating `num_global_references` column\n")

#     files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
#     for file in files:
#         data = pd.read_csv(file, encoding="utf-8")
#         if "global_references" in data.columns:
#             data = data.assign(
#                 num_global_references=data.global_references.str.split(";")
#             )
#             data.num_global_references = data.num_global_references.map(
#                 lambda x: len(x) if isinstance(x, list) else 0
#             )
#         data.to_csv(file, sep=",", index=False, encoding="utf-8")


def _create__bradford__column(directory):
    sys.stdout.write("--INFO-- Creating `bradford` column\n")

    file_path = os.path.join(directory, "processed", "_documents.csv")
    data = pd.read_csv(file_path, encoding="utf-8")

    indicators = data[["source_title", "global_citations"]]
    indicators = indicators.assign(num_documents=1)
    indicators = indicators.groupby(["source_title"], as_index=False).sum()
    indicators = indicators.sort_values(
        by=["num_documents", "global_citations"], ascending=False
    )
    indicators = indicators.assign(
        cum_num_documents=indicators["num_documents"].cumsum()
    )

    num_documents = indicators["num_documents"].sum()
    indicators = indicators.reset_index(drop=True)
    indicators = indicators.assign(zone=3)
    indicators.zone = indicators.zone.where(
        indicators.cum_num_documents >= int(num_documents * 2 / 3), 2
    )
    indicators.zone = indicators.zone.where(
        indicators.cum_num_documents >= int(num_documents / 3), 1
    )
    source2zone = dict(zip(indicators.source_title, indicators.zone))
    data = data.assign(bradford=data["source_title"].map(source2zone))
    data.to_csv(file_path, sep=",", encoding="utf-8", index=False)


def _extract_keywords_roots_from_database_files(directory):
    keywords_list = []

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        for column in ["raw_author_keywords", "raw_index_keywords"]:
            if column in data.columns:
                keywords_list.append(data[column])

    if len(keywords_list) == 0:
        return

    keywords_list = pd.concat(keywords_list)
    keywords_list = keywords_list.dropna()
    keywords_list = keywords_list.str.split(";")
    keywords_list = keywords_list.explode()
    keywords_list = keywords_list.str.strip()
    keywords_list = keywords_list.drop_duplicates()

    keywords_list = keywords_list.str.replace(r"\[.+\]", "", regex=True)
    keywords_list = keywords_list.str.replace(r"\(.+\)", "", regex=True)
    keywords_list = keywords_list.str.replace(r"-", " ", regex=False)
    keywords_list = keywords_list.str.replace(r"&", " ", regex=False)

    # list of single words
    keywords_list = keywords_list.str.split()
    s = PorterStemmer()
    keywords_list = keywords_list.map(lambda x: [s.stem(y) for y in x])
    keywords_list = keywords_list.map(set)
    keywords_list = keywords_list.map(sorted)
    keywords_list = keywords_list.map(lambda x: " ".join(x))

    return keywords_list


def _extract_keywords_from_database_files(directory):
    keywords_list = []
    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "raw_index_keywords" in data.columns:
            keywords_list += data.raw_index_keywords.dropna().tolist()
        if "raw_author_keywords" in data.columns:
            keywords_list += data.raw_author_keywords.dropna().tolist()
    keywords_list = pd.DataFrame({"keyword": keywords_list})
    keywords_list = keywords_list.assign(
        keyword=keywords_list.keyword.str.split(";")
    )
    keywords_list = keywords_list.explode("keyword")
    keywords_list = keywords_list.keyword.str.strip()
    keywords_list = keywords_list.drop_duplicates()
    keywords_list = keywords_list.reset_index(drop=True)
    return keywords_list


def _complete__source_abbr__column(directory):
    sys.stdout.write("--INFO-- Complete `source_abbr` column\n")

    name2iso = {}
    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))

    # builds the dictionary
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "source_abbr" in data.columns and "source_name" in data.columns:
            current_name2iso = {
                name: abbr
                for name, abbr in zip(data.source_name, data.source_abbr)
                if name is not pd.NA and abbr is not pd.NA
            }
            name2iso = {**name2iso, **current_name2iso}

    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "source_abbr" in data.columns and "source_name" in data.columns:
            data.source_abbr = np.where(
                data.source_abbr.isna(),
                data.source_name.map(lambda x: name2iso.get(x, x)),
                data.source_abbr,
            )
            data.source_abbr = data.source_abbr.str.replace(" JOURNAL ", " J ")
            data.source_abbr = data.source_abbr.str.replace(" AND ", "")
            data.source_abbr = data.source_abbr.str.replace(" IN ", "")
            data.source_abbr = data.source_abbr.str.replace(" OF ", "")
            data.source_abbr = data.source_abbr.str.replace(" ON ", "")
            data.source_abbr = data.source_abbr.str.replace(" THE ", "")

            data.to_csv(file, sep=",", encoding="utf-8", index=False)

    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "source_abbr" in data.columns:
            for long_word, short_word in [
                ("FINANCE", "FIN"),
                ("FINANCIAL", "FIN"),
                ("TECHNOLOGY", "TECHNOL"),
                ("CONTROL", "CTRL"),
                ("COMPLIANCE", "COMPL"),
                ("WORKSHOP", "WKSHP"),
                ("REGULATION", "REGUL"),
                ("SUPPORT", "SUPP"),
                ("LECTURE", "LECT"),
            ]:
                data.source_abbr = data.source_abbr.str.replace(
                    long_word, short_word
                )

            data.to_csv(file, sep=",", encoding="utf-8", index=False)

    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "source_abbr" in data.columns:
            data.source_abbr = data.source_abbr.str[:29]
            data.to_csv(file, sep=",", encoding="utf-8", index=False)

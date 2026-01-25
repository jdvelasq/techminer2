from pathlib import Path

import pandas as pd  # type: ignore


def _load_authors_data(dataframe):
    authors_data = dataframe[["authors", "authors_id"]].copy()
    authors_data = authors_data.dropna()
    return authors_data


def _generate_author_and_author_id_dataframe(authors_data):

    authors_data = authors_data.copy()

    # Combine authors and authors_id into a single column
    authors_data = authors_data.assign(
        authors_and_ids=authors_data.authors + "#" + authors_data.authors_id
    )
    authors_data = authors_data[["authors_and_ids"]]

    # Split the combined column into separate author and author_id pairs
    authors_data.authors_and_ids = authors_data.authors_and_ids.str.split("#")
    authors_data.authors_and_ids = authors_data.authors_and_ids.apply(
        lambda x: (x[0].split(";"), x[1].split(";"))
    )
    authors_data.authors_and_ids = authors_data.authors_and_ids.apply(
        lambda x: list(zip(x[0], x[1]))
    )

    # Explode the list of tuples into separate rows
    authors_data = authors_data.explode("authors_and_ids")

    # Strip whitespace from author and author_id
    authors_data.authors_and_ids = authors_data.authors_and_ids.apply(
        lambda x: (x[0].strip(), x[1].strip())
    )

    # Reset index and split the tuples into separate columns
    authors_data = authors_data.reset_index(drop=True)
    authors_data["author"] = authors_data.authors_and_ids.apply(lambda x: x[0])
    authors_data["author_id"] = authors_data.authors_and_ids.apply(lambda x: x[1])

    # Drop the combined column and remove duplicates
    authors_data = authors_data.drop(columns=["authors_and_ids"])
    authors_data = authors_data.drop_duplicates()

    return authors_data


def _build_dict_names(dataframe):

    dataframe = dataframe.sort_values(by=["author"])
    dataframe = dataframe.assign(counter=dataframe.groupby(["author"]).cumcount())
    dataframe = dataframe.assign(
        author=dataframe.author + "/" + dataframe.counter.astype(str)
    )
    dataframe.author = dataframe.author.str.replace("/0", "")
    author_id2name = dict(zip(dataframe.author_id, dataframe.author))

    return author_id2name


def _normalize(dataframe: pd.DataFrame) -> pd.Series:

    authors_data = _load_authors_data(dataframe)
    authors_df = _generate_author_and_author_id_dataframe(authors_data)
    author_id2name = _build_dict_names(authors_df)
    dataframe = dataframe.assign(authors=dataframe.authors_id.copy())
    dataframe["authors"] = dataframe["authors"].str.split(";")
    dataframe["authors"] = dataframe["authors"].map(
        lambda x: [author_id2name[id.strip()] for id in x],
        na_action="ignore",
    )
    dataframe["authors"] = dataframe["authors"].str.join("; ")

    return dataframe["authors"].copy()


def normalize_author_names(root_directory: str) -> int:

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    dataframe["authors"] = _normalize(dataframe)

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )

    return len(dataframe["authors"].dropna())

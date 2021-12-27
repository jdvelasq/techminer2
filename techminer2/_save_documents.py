import os


def save_documents(documents, directory):

    if directory is None:
        directory = "/workspaces/techminer-api/tests/data/"

    filename = os.path.join(directory, "documents.csv")
    documents.to_csv(
        filename,
        sep=",",
        encoding="utf-8",
        index=False,
    )

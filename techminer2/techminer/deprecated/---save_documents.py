import os
import sys


def save_documents(documents, directory="./"):

    filename = os.path.join(directory, "processed", "_documents.csv")
    documents.to_csv(
        filename,
        sep=",",
        encoding="utf-8",
        index=False,
    )
    sys.stdout.write(f"--INFO-- Documents saved/merged to `{filename}`\n")

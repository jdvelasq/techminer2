"""
Replace text in column
===============================================================================



"""
import os.path

import pandas as pd


def tm2__replace(
    criterion,
    to_replace,
    value,
    directory="./",
):
    """Replace text in columns."""

    file_path = os.path.join(directory, "processed/_documents.csv")
    records = pd.read_csv(file_path, encoding="utf-8")
    records[criterion] = records[criterion].str.replace(to_replace, value)
    records.to_csv(file_path, sep=",", encoding="utf-8", index=False)

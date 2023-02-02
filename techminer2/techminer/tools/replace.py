"""
Replace text in column
===============================================================================

>>> directory = "data/regtech/"

>>> from techminer2 import techminer
>>> techminer.tools.replace(
...     criterion="abstract", 
...     to_replace=[
...         "2015, the author(s).", 
...         "copyright  2014 by asme.",
...     ], 
...     value="", 
...     directory=directory,
... )


"""
import os.path

import pandas as pd


def replace(
    criterion,
    to_replace,
    value,
    directory="./",
):
    """Replace text in columns."""

    file_path = os.path.join(directory, "processed/_documents.csv")
    records = pd.read_csv(file_path, encoding="utf-8")
    if isinstance(to_replace, str):
        to_replace = [to_replace]
    for text in to_replace:
        records[criterion] = records[criterion].str.replace(text, value)
    records.to_csv(file_path, sep=",", encoding="utf-8", index=False)

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


# Replace text in columns
# INPUTS:
#     criterion: columns to replace text in
#     to_replace: text to replace
#     value: replacement text
#     directory: path to directory containing data
# OUTPUTS:
#     None


def replace(
    criterion,
    to_replace,
    value,
    directory="./",
):
    """Replace text in columns."""

    # Load the data
    file_path = os.path.join(directory, "processed/_documents.csv")
    records = pd.read_csv(file_path, encoding="utf-8")

    # If the text to replace is a string, convert it into a list
    if isinstance(to_replace, str):
        to_replace = [to_replace]

    # Replace the text
    for text in to_replace:
        try:
            records[criterion] = records[criterion].str.replace(text, value)
        except AttributeError as exc:
            raise ValueError("Column does not exist.") from exc
        except KeyError as exc:
            raise ValueError("Replacement text does not exist.") from exc

    # Save the updated data
    try:
        records.to_csv(file_path, sep=",", encoding="utf-8", index=False)
    except IOError as exc:
        raise IOError("File path does not exist.") from exc

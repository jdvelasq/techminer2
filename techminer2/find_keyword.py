"""
Find Keyword
===============================================================================

Finds a string in the terms of a column of a document collection.

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> find_keyword(contains='artificial intelligence', directory=directory)
artificial intelligence
     artificial intelligence
     artificial intelligence (ai)
artificial intelligence systems
artificial intelligence technologies
     artificial intelligence technologies
     artificial intelligence technology
forthcoming artificial intelligence revolution
novel artificial intelligence


"""
from os.path import isfile, join

import pandas as pd

from .thesaurus import load_file_as_dict


def find_keyword(
    contains=None,
    startswith=None,
    endswith=None,
    directory="./",
):
    """
    Find keywords in thesaurus.

    """

    thesaurus_file = join(directory, "keywords.txt")
    if isfile(thesaurus_file):
        th = load_file_as_dict(thesaurus_file)
    else:
        raise FileNotFoundError("The file {} does not exist.".format(thesaurus_file))

    reversed_th = {value: key for key, values in th.items() for value in values}

    df = pd.DataFrame(
        {
            "text": reversed_th.keys(),
            "key": reversed_th.values(),
        }
    )

    if contains is not None:
        df = df[df.text.str.contains(contains)]
    elif startswith is not None:
        df = df[df.text.str.startswith(startswith)]
    elif endswith is not None:
        df = df[df.text.str.endswith(endswith)]
    else:
        raise ValueError("No filter provided")

    keys = df.key.drop_duplicates()

    th = {key: th[key] for key in sorted(keys)}

    for key in sorted(th.keys()):
        print(key)
        if len(th[key]) > 1:
            for value in sorted(th[key]):
                print("    ", value)

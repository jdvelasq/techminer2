"""
Functions for handling the datastore.


"""

from os.path import isfile

import pandas as pd


def load_datastore(datastoredir="./", fileerror=True):
    """
    Loads datastore.

    """
    if datastoredir[-1] != "/":
        datastoredir += "/"
    datastorefile = datastoredir + "datastore.csv"
    if not isfile(datastorefile):
        if fileerror:
            raise FileNotFoundError("The file {} does not exist.".format(datastorefile))
        return pd.DataFrame()

    datastore = pd.read_csv(datastorefile, sep=",", encoding="utf-8")
    return datastore

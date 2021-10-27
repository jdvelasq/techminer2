from os.path import isfile

import pandas as pd
from src.utils.logging_info import logging_info
from src.utils.map import map_
from src.utils.thesaurus import read_textfile


def apply_keywords_thesaurus(datastoredir="./"):

    if datastoredir[-1] != "/":
        datastoredir += "/"

    datastorefile = datastoredir + "datastore.csv"
    if isfile(datastorefile):
        datastore = pd.read_csv(datastorefile)
    else:
        raise FileNotFoundError("The file {} does not exist.".format(datastorefile))

    thesaurus_file = datastoredir + "TH_keywords.txt"
    if isfile(thesaurus_file):
        th = read_textfile(thesaurus_file)
        th = th.compile_as_dict()
    else:
        raise FileNotFoundError("The file {} does not exist.".format(datastorefile))

    #
    # Author keywords cleaning
    #
    if "author_aeywords" in datastore.columns:
        datastore["author_keywords_cl"] = map_(
            datastore, "author_keywords", th.apply_as_dict
        )

    ##
    ## Index keywords cleaning
    ##
    if "index_keywords" in datastore.columns:
        datastore["index_keywords_cl"] = map_(
            datastore, "index_keywords", th.apply_as_dict
        )

    ##
    ## keywords new field creation
    ##
    if "author_keywords" in datastore.columns and "index_keywords" in datastore.columns:
        datastore["keywords"] = (
            datastore.author_keywords.map(lambda w: "" if pd.isna(w) else w)
            + ";"
            + datastore.index_keywords.map(lambda w: "" if pd.isna(w) else w)
        )
        datastore["keywords"] = datastore.keywords.map(
            lambda w: None if w[0] == ";" and len(w) == 1 else w
        )
        datastore["keywords"] = datastore.keywords.map(
            lambda w: w[1:] if w[0] == ";" else w, na_action="ignore"
        )
        datastore["keywords"] = datastore.keywords.map(
            lambda w: w[:-1] if w[-1] == ";" else w, na_action="ignore"
        )
        datastore["keywords"] = datastore.keywords.map(
            lambda w: ";".join(sorted(set(w.split(";")))), na_action="ignore"
        )

    ##
    ## keywords_cl new field creation
    ##
    if (
        "author_keywords_cl" in datastore.columns
        and "index_keywords_cl" in datastore.columns
    ):
        datastore["keywords_cl"] = (
            datastore.author_keywords_cl.map(lambda w: "" if pd.isna(w) else w)
            + ";"
            + datastore.index_keywords_cl.map(lambda w: "" if pd.isna(w) else w)
        )
        datastore["keywords_cl"] = datastore.keywords_cl.map(
            lambda w: pd.NA if w[0] == ";" and len(w) == 1 else w
        )
        datastore["keywords_cl"] = datastore.keywords_cl.map(
            lambda w: w[1:] if w[0] == ";" else w, na_action="ignore"
        )
        datastore["keywords_cl"] = datastore.keywords_cl.map(
            lambda w: w[:-1] if w[-1] == ";" else w, na_action="ignore"
        )
        datastore["keywords_cl"] = datastore.keywords_cl.map(
            lambda w: ";".join(sorted(set(w.split(";")))), na_action="ignore"
        )

    ##
    ## Title keywords
    ##
    if "title_keywords" in datastore.columns:
        datastore["title_keywords_cl"] = map_(
            datastore, "title_keywords", th.apply_as_dict
        )

    ##
    ## Abstract
    ##
    for column in [
        "abstract_author_keywords",
        "abstract_index_keywords",
        "abstract_keywords",
    ]:
        if column in datastore.columns:
            datastore[column + "_cl"] = map_(datastore, column, th.apply_as_dict)

    ##
    ## Saves!
    ##
    datastore.to_csv(datastorefile, index=False)

    logging_info("The thesaurus was applied to keywords.")

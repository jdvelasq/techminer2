from os.path import isfile

import pandas as pd
from techminer.utils import logging
from techminer.utils.map import map_
from techminer.utils.thesaurus import read_textfile


def apply_institutions_thesaurus(records, directory="./"):

    data = records

    if directory[-1] != "/":
        directory = directory + "/"

    ##
    ## Loads the thesaurus
    ##
    thesaurus_file = directory + "institutions.txt"
    th = read_textfile(thesaurus_file)
    th = th.compile_as_dict()

    ##
    ## Copy affiliations to institutions
    ##
    data["institutions"] = data.affiliations.map(
        lambda w: w.lower().strip(), na_action="ignore"
    )

    ##
    ## Cleaning
    ##
    logging.info("Extract and cleaning institutions.")
    data["institutions"] = map_(
        data, "institutions", lambda w: th.apply_as_dict(w, strict=True)
    )

    logging.info("Extracting institution of first author ...")
    data["institution_1st_author"] = data.institutions.map(
        lambda w: w.split(";")[0] if isinstance(w, str) else w
    )

    logging.info("The thesaurus was applied to institutions.")

    return data

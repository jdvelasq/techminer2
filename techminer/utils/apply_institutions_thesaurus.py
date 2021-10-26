import logging
from os.path import isfile

import pandas as pd
from techminer.core.thesaurus import read_textfile

# from techminer.core.logging_info import logging_info
from techminer.utils.map import map_


def apply_institutions_thesaurus(datastorepath="./"):

    if datastorepath[-1] != "/":
        datastorepath = datastorepath + "/"

    datastorefile = datastorepath + "datastore.csv"
    if isfile(datastorefile):
        data = pd.read_csv(datastorefile)
    else:
        raise FileNotFoundError("The file {} does not exist.".format(datastorefile))

    data = pd.read_csv(datastorefile)

    ##
    ## Loads the thesaurus
    ##
    thesaurus_file = datastorepath + "TH_institutions.txt"
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

    ##
    ## Finish!
    ##
    data.to_csv(datastorefile, index=False)

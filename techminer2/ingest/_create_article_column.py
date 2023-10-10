"""Create WoS style article column in databases."""


import glob
import os

import numpy as np
import pandas as pd

from ._message import message


def create_article_column(root_dir):
    """Create a WoS style reference column.

    :meta private:
    """
    #
    # First Author, year, abbr_source_title, 'V'volumne, 'P'page_start, ' DOI ' doi
    #
    message("Creating `article` column")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        #
        wos_ref = data.authors.map(
            lambda x: x.split("; ")[0].strip() if not pd.isna(x) else "[Anonymous]"
        )
        #
        #
        abbr_source_title = data.abbr_source_title.copy()
        abbr_source_title = (
            abbr_source_title.str.upper()
            .str.replace("JOURNAL", "J")
            .str.replace(" OF ", " ")
            .str.replace(".", "")
            .str.replace(" - ", " ")
            .str.replace(",", "")
            .str.replace(":", "")
            .str.replace("-", "")
        )
        #
        #
        wos_ref += ", " + data.year.map(str)
        #
        ## wos_ref += ", " + abbr_source_title.map(lambda x: x if not pd.isna(x) else "")
        abbr_title_isna = abbr_source_title.map(pd.isna)
        wos_ref += ", " + np.where(
            abbr_title_isna,
            data.source_title.str[:29]
            .str.upper()
            .str.replace("JOURNAL", "J")
            .str.replace(" OF ", " ")
            .str.replace(".", "")
            .str.replace(" - ", " ")
            .str.replace(",", "")
            .str.replace(":", "")
            .str.replace("-", "")
            .map(lambda x: x if not pd.isna(x) else ""),
            abbr_source_title,
        )
        #
        wos_ref += data.volume.map(
            lambda x: ", V" + str(x).replace(".0", "") if not pd.isna(x) else ""
        )
        wos_ref += data.page_start.map(
            lambda x: ", P" + str(x).replace(".0", "") if not pd.isna(x) else ""
        )
        #
        index = wos_ref[wos_ref.duplicated()].index
        if len(index) > 0:
            wos_ref.loc[index] += ", " + data.document_title.loc[index].str[
                :29
            ].str.upper().str.replace(".", "").str.replace(" - ", " ").str.replace(
                ",", ""
            ).str.replace(
                ":", ""
            ).str.replace(
                "-", ""
            ).str.replace(
                "'", ""
            )

        #
        data["article"] = wos_ref.copy()
        data = data.drop_duplicates(subset=["article"])
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")

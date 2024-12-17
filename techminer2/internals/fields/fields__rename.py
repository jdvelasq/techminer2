# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import glob
import os.path

import pandas as pd  # type: ignore

from ..._dtypes import DTYPES


def fields__rename(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir,
):
    rename = {source: dest}

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip", dtype=DTYPES)
        data = data.rename(columns=rename)
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")

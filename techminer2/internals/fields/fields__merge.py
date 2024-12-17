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


def fields__merge(
    sources,
    dest,
    #
    # DATABASE PARAMS:
    root_dir,
):
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        #
        # Load data
        data = pd.read_csv(file, encoding="utf-8", compression="zip", dtype=DTYPES)

        #
        # Merge fields
        new_field = None
        for field in sources:
            if field in data.columns:
                if new_field is None:
                    new_field = data[field].astype(str).str.split("; ")
                else:
                    new_field = new_field + data[field].astype(str).str.split("; ")

        #
        # Remove duplicates and sort
        new_field = new_field.map(lambda x: [z for z in x if z != "nan"])
        new_field = new_field.map(lambda x: sorted(set(x)), na_action="ignore")
        new_field = new_field.map("; ".join, na_action="ignore")
        new_field = new_field.map(lambda x: x if x != "" else pd.NA)

        #
        # Create the new field
        data[dest] = new_field

        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")

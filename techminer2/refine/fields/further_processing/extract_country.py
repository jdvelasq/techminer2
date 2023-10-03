# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Extract Country
===============================================================================

>>> from techminer2.refine.fields.further_processing import extract_country
>>> extract_country(
...     src_field="affiliations",
...     dst_field="countries_from_affiliations",
...     root_dir="example",
... )

>>> # TEST:  
>>> from techminer2.analyze import performance_metrics
>>> performance_metrics(
...     field='countries_from_affiliations',
...     metric='OCC',
...     top_n=10,
...     root_dir="example/", 
... ).df_['OCC'].head()
countries_from_affiliations
United Kingdom    7
Australia         7
United States     6
Ireland           5
China             5
Name: OCC, dtype: int64

>>> from techminer2.refine.fields import delete_field
>>> delete_field(
...     field="countries_from_affiliations",
...     root_dir="example",
... )


"""
import glob
import os.path

import numpy as np
import pandas as pd
import pkg_resources

from ...._common.thesaurus_lib import load_system_thesaurus_as_dict
from ..protected_fields import PROTECTED_FIELDS


def extract_country(
    src_field,
    dst_field,
    root_dir,
):
    """
    :meta private:
    """

    if dst_field in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dst_field}` is protected")

    #
    # Loads the thesaurus
    data_path = pkg_resources.resource_filename("techminer2", "thesauri_data/countries.txt")
    thesaurus = load_system_thesaurus_as_dict(data_path)
    names = list(thesaurus.keys())

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        if src_field in data.columns:
            data[dst_field] = data[src_field].copy()
            data[dst_field] = data[dst_field].replace(np.nan, pd.NA)
            data[dst_field] = data[dst_field].str.split("; ")
            data[dst_field] = data[dst_field].map(
                lambda x: [
                    thesaurus[name][0] if name in y.lower() else pd.NA for y in x for name in names
                ],
                na_action="ignore",
            )
            data[dst_field] = data[dst_field].map(
                lambda x: [y for y in x if y is not pd.NA], na_action="ignore"
            )
            data[dst_field] = data[dst_field].map(
                lambda x: pd.NA if x == [] else x, na_action="ignore"
            )
            data[dst_field] = data[dst_field].map(
                lambda x: pd.NA if x is pd.NA else list(set(x)), na_action="ignore"
            )
            data[dst_field] = data[dst_field].str.join("; ")
            data[dst_field] = data[dst_field].map(
                lambda x: pd.NA if x == "" else x, na_action="ignore"
            )
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")

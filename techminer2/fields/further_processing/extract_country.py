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

>>> from techminer2.fields.further_processing import extract_country
>>> extract_country(
...     source="affiliations",
...     dest="countries_from_affiliations",
...     root_dir="example",
... )

>>> # TEST:  
>>> from techminer2.metrics import performance_metrics
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

>>> from techminer2.fields import delete_field
>>> delete_field(
...     field="countries_from_affiliations",
...     root_dir="example",
... )


"""
import glob
import os

import numpy as np
import pandas as pd

from ...thesaurus._core.load_thesaurus_as_dict import load_thesaurus_as_dict
from ..protected_fields import PROTECTED_FIELDS


def extract_country(
    source,
    dest,
    root_dir,
):
    """:meta private:"""

    if dest in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dest}` is protected")

    _extract_country(
        source=source,
        dest=dest,
        root_dir=root_dir,
    )


def _extract_country(
    source,
    dest,
    root_dir,
):
    #
    # Loads the thesaurus
    thesaurus_path = os.path.join(root_dir, "thesauri/countries.the.txt")
    thesaurus = load_thesaurus_as_dict(thesaurus_path)
    names = list(thesaurus.keys())

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        if source in data.columns:
            data[dest] = data[source].copy()
            data[dest] = data[dest].replace(np.nan, pd.NA)
            data[dest] = data[dest].str.split("; ")
            data[dest] = data[dest].map(
                lambda x: [thesaurus[name][0] if name in y.lower() else pd.NA for y in x for name in names],
                na_action="ignore",
            )
            data[dest] = data[dest].map(lambda x: [y for y in x if y is not pd.NA], na_action="ignore")
            data[dest] = data[dest].map(lambda x: pd.NA if x == [] else x, na_action="ignore")
            data[dest] = data[dest].map(lambda x: pd.NA if x is pd.NA else list(set(x)), na_action="ignore")
            data[dest] = data[dest].str.join("; ")
            data[dest] = data[dest].map(lambda x: pd.NA if x == "" else x, na_action="ignore")
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")

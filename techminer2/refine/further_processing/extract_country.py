# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Extraact Country
===============================================================================

>>> from techminer2.refine.further_processing import extract_country

>>> extract_country(
...     src_field="affilieations",
...     dst_field="countries_from_affiliations",
...     root_dir="example",
... )

>>> from techminer2.refine import delete_field
>>> delete_field(
...     field="author_keywords_renamed",
...     root_dir="example",
... )


"""
import glob
import os.path

import pandas as pd
import pkg_resources

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

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        if src_field in data.columns:
            data[dst_field] = data[src_field].copy()
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")

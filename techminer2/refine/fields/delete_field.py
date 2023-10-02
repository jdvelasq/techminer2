# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Delete a Field
===============================================================================

>>> from techminer2.refine.fields import copy_field, rename_field, delete_field
>>> copy_field(
...     src_field="author_keywords",
...     dst_field="author_keywords_copy",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

>>> delete_field(
...     field="author_keywords_copy",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )



"""
import glob
import os.path

import pandas as pd

from .protected_fields import PROTECTED_FIELDS


def delete_field(
    field,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """
    if field in PROTECTED_FIELDS:
        raise ValueError(f"Field `{field}` is protected")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        data = data.drop(field, axis=1)
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")

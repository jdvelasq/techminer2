"""
Apply Thesaurus
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"
>>> create_thesaurus(
...     column="author_keywords",
...     thesaurus_file="test_thesaurus.txt",
...     sep="; ",
...     directory=directory,
... )
- INFO - Creating thesaurus ...
- INFO - Thesaurus file 'data/processed/test_thesaurus.txt' created.

>>> apply_thesaurus(
...     thesaurus_file="keywords.txt", 
...     input_column="author_keywords",
...     output_column="author_keywords_thesaurus", 
...     strict=False,
...     directory=directory,
... )
- INFO - The thesaurus file 'keywords.txt' was applied to column 'author_keywords'.


"""
import os

from . import logging
from ._read_records import read_filtered_records
from .map_ import map_
from .thesaurus import read_textfile


def apply_thesaurus(
    thesaurus_file,
    input_column,
    output_column,
    strict,
    directory="./",
):
    def apply_strict(x):
        return thesaurus.apply_as_dict(x, strict=True)

    def apply_unstrict(x):
        return thesaurus.apply_as_dict(x, strict=False)

    documents = read_filtered_records(directory)
    thesaurus = read_textfile(os.path.join(directory, "processed", thesaurus_file))
    thesaurus = thesaurus.compile_as_dict()
    if strict:
        documents[output_column] = map_(documents, input_column, apply_strict)
    else:
        documents[output_column] = map_(documents, input_column, apply_unstrict)
    documents.to_csv(os.path.join(directory, "processed", "documents.csv"), index=False)
    logging.info(
        f"The thesaurus file '{thesaurus_file}' was applied to column '{input_column}'."
    )

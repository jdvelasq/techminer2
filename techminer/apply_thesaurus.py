"""
Thesaurus --- apply
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> create_thesaurus(directory, 
... column="keywords", 
... thesaurus_file="test_thesaurus.txt", 
... sep="; ")
2021-11-08 18:50:25 - INFO - Creating thesaurus ...
2021-11-08 18:50:26 - INFO - Thesaurus file '/workspaces/techminer-api/tests/data/test_thesaurus.txt' created.
>>> apply_thesaurus(directory, 
... thesaurus_file="keywords.txt", 
... input_column="author_keywords",
... output_column="author_keywords_thesaurus", 
... strict=False)
2021-11-08 18:51:19 - INFO - The thesaurus file 'keywords.txt' was applied to column 'author_keywords'.


"""
import os

import pandas as pd

from .utils import load_filtered_documents, logging, map_
from .utils.thesaurus import read_textfile


def apply_thesaurus(
    directory,
    thesaurus_file,
    input_column,
    output_column,
    strict,
):
    def apply_strict(x):
        return thesaurus.apply_as_dict(x, strict=True)

    def apply_unstrict(x):
        return thesaurus.apply_as_dict(x, strict=False)

    documents = load_filtered_documents(directory)
    thesaurus = read_textfile(os.path.join(directory, thesaurus_file))
    thesaurus = thesaurus.compile_as_dict()
    if strict:
        documents[output_column] = map_(documents, input_column, apply_strict)
    else:
        documents[output_column] = map_(documents, input_column, apply_unstrict)
    documents.to_csv(os.path.join(directory, "documents.csv"), index=False)
    logging.info(
        f"The thesaurus file '{thesaurus_file}' was applied to column '{input_column}'."
    )

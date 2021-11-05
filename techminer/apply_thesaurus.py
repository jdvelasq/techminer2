"""
Apply thesaurus
===============================================================================

"""
import os

import pandas as pd

from techminer.utils import load_filtered_documents, map_
from techminer.utils.thesaurus import read_textfile


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

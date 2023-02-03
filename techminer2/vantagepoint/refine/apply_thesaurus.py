"""
Apply Thesaurus
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.refine.create_thesaurus(
...     criterion="author_keywords",
...     output_file="test_keywords.txt",
...     directory=directory,
... )
--INFO-- Creating a thesaurus file from `author_keywords` column in all databases
--INFO-- The thesaurus file `test_keywords.txt` was created


>>> vantagepoint.refine.apply_thesaurus(
...     thesaurus_file="test_keywords.txt",
...     input_criterion="author_keywords",
...     output_criterion="author_keywords_thesaurus",
...     directory=directory,
... )
--INFO-- The thesaurus was applied to all databases


"""
import glob
import os
import sys

import pandas as pd

from ..._thesaurus import read_textfile


def apply_thesaurus(
    thesaurus_file,
    input_criterion,
    output_criterion,
    directory="./",
):
    """Apply a thesaurus to a column of a dataframe."""

    thesaurus_file = os.path.join(directory, "processed", thesaurus_file)

    th = read_textfile(thesaurus_file)
    th = th.compile_as_dict()

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        #
        if input_criterion in data.columns:
            data[output_criterion] = data[input_criterion].str.split(";")

            data[output_criterion] = data[output_criterion].map(
                lambda x: [th.apply_as_dict(y.strip()) for y in x]
                if isinstance(x, list)
                else x
            )

            data[output_criterion] = data[output_criterion].map(
                lambda x: sorted(set(x)) if isinstance(x, list) else x
            )

            data[output_criterion] = data[output_criterion].str.join("; ")

        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False)

    ####
    # def apply_strict(text):
    #     return thesaurus.apply_as_dict(text, strict=True)

    # def apply_unstrict(text):
    #     return thesaurus.apply_as_dict(text, strict=False)

    # thesaurus_file = os.path.join(directory, "processed", thesaurus_file)
    # thesaurus = read_textfile(thesaurus_file)
    # thesaurus = thesaurus.compile_as_dict()

    # files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    # for file in files:
    #     data = pd.read_csv(file, encoding="utf-8")
    #     if strict:
    #         data[output_column] = map_(data, input_column, apply_strict)
    #     else:
    #         data[output_column] = map_(data, input_column, apply_unstrict)
    #     data.to_csv(file, sep=",", encoding="utf-8", index=False)

    sys.stdout.write("--INFO-- The thesaurus was applied to all databases\n")

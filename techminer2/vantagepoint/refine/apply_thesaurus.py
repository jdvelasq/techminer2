"""
Apply Thesaurus 
===============================================================================


>>> from techminer2 import *
>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.refine.create_thesaurus(
...     criterion="author_keywords",
...     output_file="test_keywords.txt",
...     root_dir=root_dir,
... )
--INFO-- Creating a thesaurus file from `author_keywords` column in all \
databases
--INFO-- The thesaurus file `test_keywords.txt` was created


>>> vantagepoint.refine.apply_thesaurus(
...     thesaurus_file="test_keywords.txt",
...     input_criterion="author_keywords",
...     output_criterion="author_keywords_thesaurus",
...     root_dir=root_dir,
... )
--INFO-- The thesaurus was applied to all databases


"""
import glob
import os
import sys

import pandas as pd

# from ..._thesaurus import read_textfile


def apply_thesaurus(
    thesaurus_file,
    input_criterion,
    output_criterion,
    root_dir="./",
):
    """Apply a thesaurus to a column of a dataframe."""

    thesaurus_file = os.path.join(root_dir, "processed", thesaurus_file)

    ths = read_textfile(thesaurus_file)
    ths = ths.compile_as_dict()

    files = list(glob.glob(os.path.join(root_dir, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        #
        if input_criterion in data.columns:
            data[output_criterion] = data[input_criterion].str.split(";")

            data[output_criterion] = data[output_criterion].map(
                lambda x: [ths.apply_as_dict(y.strip()) for y in x]
                if isinstance(x, list)
                else x
            )

            data[output_criterion] = data[output_criterion].map(
                lambda x: sorted(set(x)) if isinstance(x, list) else x
            )

            data[output_criterion] = data[output_criterion].str.join("; ")

        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False)

    sys.stdout.write("--INFO-- The thesaurus was applied to all databases\n")

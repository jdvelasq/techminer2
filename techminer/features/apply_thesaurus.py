from os.path import isfile

import pandas as pd
from techminer.data.records import load_records
from techminer.utils import logging
from techminer.utils.map import map_
from techminer.utils.thesaurus import read_textfile


def apply_thesaurus(
    directory_or_records, thesaurus_file, column, sep="; ", strict=True, verbose=False
):
    """
    Applies a thesaurus to a column of a dataframe.

    Parameters
    ----------
    directory_or_records: str
        path to the directory or the records object.
    thesaurus_file: str
        Path to the thesaurus file.
    column: str
        Name of the column to be processed.
    strict: bool
        If True, thesaurus entries are only applied if they are present in the
        column. If False, thesaurus entries are applied to all the column values.
    sep: str
        Separator of the records column.

    Returns
    -------
    pandas.DataFrame
        Dataframe with thesaurus applied.
    """
    if isinstance(directory_or_records, str):
        records = load_records(directory_or_records)
    else:
        records = directory_or_records

    if isfile(thesaurus_file):

        th = read_textfile(thesaurus_file)
        th = th.compile_as_dict()
    else:
        raise FileNotFoundError(f"The file {thesaurus_file} does not exist.")

    if column not in records.columns:
        raise ValueError(f"The column {column} does not exist in the records.")

    if verbose:
        logging.info("Applying thesaurus to {}".format(column))

    result = map_(records, column, th.apply_as_dict, strict)

    return result

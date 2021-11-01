"""
Apply Thesaurus
===============================================================================

"""
import pandas as pd

from techminer.utils import load_records, map_, save_records
from techminer.utils.thesaurus import read_textfile


def _apply_thesaurus_from_records(
    records,
    thesaurus_filepath,
    input_column,
    output_column,
    strict,
):
    def apply_strict(x):
        return thesaurus.apply_as_dict(x, strict=True)

    def apply_unstrict(x):
        return thesaurus.apply_as_dict(x, strict=False)

    thesaurus = read_textfile(thesaurus_filepath)
    thesaurus = thesaurus.compile_as_dict()

    if strict:
        records[output_column] = map_(records, input_column, apply_strict)
    else:
        records[output_column] = map_(records, input_column, apply_unstrict)

    return records


def _apply_thesaurus_from_directory(
    directory,
    thesaurus_filepath,
    input_column,
    output_column,
    strict,
):
    return _apply_thesaurus_from_records(
        records=load_records(directory),
        thesaurus_filepath=thesaurus_filepath,
        input_column=input_column,
        output_column=output_column,
        strict=strict,
    )


def apply_thesaurus(
    directory_or_records,
    thesaurus_filepath,
    input_column,
    output_column,
    strict=True,
):
    """
    Apply a thesaurus to a column.



    """
    if isinstance(directory_or_records, str):
        records = _apply_thesaurus_from_directory(
            directory=directory_or_records,
            thesaurus_filepath=thesaurus_filepath,
            input_column=input_column,
            output_column=output_column,
            strict=strict,
        )
        save_records(records, directory_or_records)
    elif isinstance(directory_or_records, pd.DataFrame):
        return _apply_thesaurus_from_records(
            records=directory_or_records,
            thesaurus_filepath=thesaurus_filepath,
            input_column=input_column,
            output_column=output_column,
            strict=strict,
        )
    else:
        raise TypeError("directory_or_records must be a string or a pandas.DataFrame")

"""
Apply Thesaurus
===============================================================================

"""
import pandas as pd

from techminer.utils import (
    load_records_from_project_directory,
    load_thesaurus_from_textfile,
    map_,
    save_records_to_project_directory,
)
from techminer.utils.thesaurus import read_textfile


def apply_thesaurus(
    project_directory,
    thesaurus_file,
    input_column,
    output_column,
    strict,
):
    def apply_strict(x):
        return thesaurus.apply_as_dict(x, strict=True)

    def apply_unstrict(x):
        return thesaurus.apply_as_dict(x, strict=False)

    records = load_records_from_project_directory(project_directory)
    thesaurus = load_thesaurus_from_textfile(project_directory, textfile=thesaurus_file)

    thesaurus = thesaurus.compile_as_dict()

    if strict:
        records[output_column] = map_(records, input_column, apply_strict)
    else:
        records[output_column] = map_(records, input_column, apply_unstrict)

    save_records_to_project_directory(records, project_directory)


# def apply_thesaurus(
#     project_directory,
#     thesaurus_filepath,
#     input_column,
#     output_column,
#     strict,
# ):
#     return _apply_thesaurus_from_records(
#         records=load_records_from_project_directory(project_directory),
#         thesaurus_filepath=thesaurus_filepath,
#         input_column=input_column,
#         output_column=output_column,
#         strict=strict,
#     )


# def apply_thesaurus(
#     project_directory,
#     thesaurus_filepath,
#     input_column,
#     output_column,
#     strict=True,
# ):
#     """
#     Apply a thesaurus to a column.


#     """
#     if isinstance(project_directory, str):
#         records = _apply_thesaurus_from_directory(
#             directory=project_directory,
#             thesaurus_filepath=thesaurus_filepath,
#             input_column=input_column,
#             output_column=output_column,
#             strict=strict,
#         )
#         save_records_to_project_directory(records, project_directory)
#         return
#     elif isinstance(project_directory, pd.DataFrame):
#         return _apply_thesaurus_from_records(
#             records=project_directory,
#             thesaurus_filepath=thesaurus_filepath,
#             input_column=input_column,
#             output_column=output_column,
#             strict=strict,
#         )
#     else:

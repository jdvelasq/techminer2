# CODE_REVIEW: 2026-01-26

from tm2p._internals import Params

from ..step import Step


def build_scaffolding_steps(params: Params) -> list[Step]:

    from .compress_raw_files import compress_raw_files
    from .create_database_files import create_database_files
    from .create_project_structure import create_project_structure
    from .drop_empty_columns import drop_empty_columns
    from .remove_non_english_abstracts import remove_non_english_abstracts
    from .rename_columns import rename_columns
    from .validate_required_columns import validate_required_columns

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Creating project structure",
            function=create_project_structure,
            kwargs=common_kwargs,
        ),
        Step(
            name="Removing non-English abstracts",
            function=remove_non_english_abstracts,
            kwargs=common_kwargs,
            count_message="{count} records with non-English abstracts removed",
        ),
        Step(
            name="Compressing raw files",
            function=compress_raw_files,
            kwargs=common_kwargs,
            count_message="{count} raw files compressed",
        ),
        Step(
            name="Creating database files",
            function=create_database_files,
            kwargs=common_kwargs,
            count_message="{count} records created in database files",
        ),
        Step(
            name="Renaming columns",
            function=rename_columns,
            kwargs=common_kwargs,
            count_message="{count} files with renamed columns",
        ),
        Step(
            name="Dropping empty columns",
            function=drop_empty_columns,
            kwargs=common_kwargs,
            count_message="{count} empty columns dropped",
        ),
        Step(
            name="Validating required columns",
            function=validate_required_columns,
            kwargs=common_kwargs,
            count_message="{count} files with all required columns",
        ),
    ]

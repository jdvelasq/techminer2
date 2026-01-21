# pylint: disable=import-outside-toplevel
from techminer2.io._internals.scaffolding import (
    compress_raw_files,
    create_database_files,
    create_project_structure,
    drop_empty_columns,
    remove_non_english_abstracts,
)

from .step import Step


def build_scaffolding_steps(params) -> list[Step]:

    from techminer2.io._internals.scaffolding import rename_columns

    return [
        Step(
            name="Creating project structure",
            function=create_project_structure,
            kwargs={"root_directory": params.root_directory},
        ),
        Step(
            name="Removing non-English abstracts",
            function=remove_non_english_abstracts,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} records with non-English abstracts removed",
        ),
        Step(
            name="Compressing raw files",
            function=compress_raw_files,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} raw files compressed",
        ),
        Step(
            name="Creating database files",
            function=create_database_files,
            kwargs={"root_directory": params.root_directory},
            count_message="Created {count} records in database files",
        ),
        Step(
            name="Renaming columns",
            function=rename_columns,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} files with renamed columns",
        ),
        Step(
            name="Dropping empty columns",
            function=drop_empty_columns,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} empty columns dropped",
        ),
    ]

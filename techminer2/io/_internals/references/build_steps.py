# CODE_REVIEW: 2026-01-26

from techminer2 import Field

from ...._internals import Params
from ..step import Step


def build_reference_steps(params: Params) -> list[Step]:

    from ..authors.calculate_numauth import calculate_numauth
    from .assign_recid import assign_recid
    from .assign_recno import assign_recno
    from .calculate_numref_global import calculate_numref_global
    from .create_citcount_local import create_citcount_local

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name=f"Assigning '{Field.RECNO.value}'",
            function=assign_recno,
            kwargs=common_kwargs,
            count_message="{count} record numbers assigned",
        ),
        Step(
            name=f"Assigning '{Field.RECID.value}'",
            function=assign_recid,
            kwargs=common_kwargs,
            count_message="{count} record IDs assigned",
        ),
        Step(
            name=f"Calculating '{Field.NUMAUTH.value}'",
            function=calculate_numauth,
            kwargs=common_kwargs,
            count_message="{count} records calculated",
        ),
        Step(
            name=f"Calculating '{Field.NUMREF_GLOBAL.value}'",
            function=calculate_numref_global,
            kwargs=common_kwargs,
            count_message="{count} reference counts calculated",
        ),
        Step(
            name=f"Creating '{Field.CITCOUNT_LOCAL.value}'",
            function=create_citcount_local,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
    ]


# TODO: _preprocess_references(root_directory)
# TODO: _preprocess_record_id(root_directory)

# TODO: _preprocess_global_references(root_directory)  # ok
# TODO: _preprocess_local_references(root_directory)  # ok
# TODO: _preprocess_local_citations(root_directory)  # ok
# TODO: _preprocess_references(root_directory)

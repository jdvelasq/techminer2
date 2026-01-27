# CODE_REVIEW: 2026-01-26

from ...._internals.params_mixin import Params
from ..step import Step


def build_other_information_steps(params: Params) -> list[Step]:

    from .assign_record_id import assign_record_id
    from .assign_record_no import assign_record_no
    from .calculate_num_authors import calculate_num_authors
    from .calculate_num_global_references import calculate_num_global_references
    from .normalize_casregnumber import normalize_casregnumber
    from .normalize_conference_code import normalize_conference_code
    from .normalize_conference_date import normalize_conference_date
    from .normalize_conference_location import normalize_conference_location
    from .normalize_conference_name import normalize_conference_name
    from .normalize_manufacturers import normalize_manufacturers
    from .normalize_molecular_sequence_numbers import (
        normalize_molecular_sequence_numbers,
    )
    from .normalize_tradenames import normalize_tradenames

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Normalizing tradenames",
            function=normalize_tradenames,
            kwargs=common_kwargs,
            count_message="{count} tradenames normalized",
        ),
        Step(
            name="Normalizing manufacturers",
            function=normalize_manufacturers,
            kwargs=common_kwargs,
            count_message="{count} manufacturers normalized",
        ),
        Step(
            name="Normalizing CAS reg numbers",
            function=normalize_casregnumber,
            kwargs=common_kwargs,
            count_message="{count} CAS reg numbers normalized",
        ),
        Step(
            name="Normalizing molecular sequence numbers",
            function=normalize_molecular_sequence_numbers,
            kwargs=common_kwargs,
            count_message="{count} molecular sequence numbers normalized",
        ),
        Step(
            name="Normalizing conference codes",
            function=normalize_conference_code,
            kwargs=common_kwargs,
            count_message="{count} conference codes normalized",
        ),
        Step(
            name="Normalizing conference dates",
            function=normalize_conference_date,
            kwargs=common_kwargs,
            count_message="{count} conference dates normalized",
        ),
        Step(
            name="Normalizing conference locations",
            function=normalize_conference_location,
            kwargs=common_kwargs,
            count_message="{count} conference locations normalized",
        ),
        Step(
            name="Normalizing conference names",
            function=normalize_conference_name,
            kwargs=common_kwargs,
            count_message="{count} conference names normalized",
        ),
        Step(
            name="Assigning record number",
            function=assign_record_no,
            kwargs=common_kwargs,
            count_message="{count} record numbers assigned",
        ),
        Step(
            name="Assigning record ID",
            function=assign_record_id,
            kwargs=common_kwargs,
            count_message="{count} record IDs assigned",
        ),
        Step(
            name="Calculating number of authors per record",
            function=calculate_num_authors,
            kwargs=common_kwargs,
            count_message="{count} authors counts calculated",
        ),
        Step(
            name="Calculating number of references per record",
            function=calculate_num_global_references,
            kwargs=common_kwargs,
            count_message="{count} reference counts calculated",
        ),
    ]


# TODO: _preprocess_references(root_directory)
# TODO: _preprocess_record_id(root_directory)

# TODO: _preprocess_global_references(root_directory)  # ok
# TODO: _preprocess_local_references(root_directory)  # ok
# TODO: _preprocess_local_citations(root_directory)  # ok
# TODO: _preprocess_references(root_directory)

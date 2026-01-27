# CODE_REVIEW: 2026-01-26

from ...._internals.params_mixin import Params
from ..step import Step


def build_other_information_steps(params: Params) -> list[Step]:

    from .assign_record_id import assign_record_id
    from .assign_record_no import assign_record_no
    from .calculate_num_authors import calculate_num_authors
    from .calculate_num_global_references import calculate_num_global_references

    common_kwargs = {"root_directory": params.root_directory}

    return [
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

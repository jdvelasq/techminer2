# pylint: disable=import-outside-toplevel


from .step import Step


def build_other_information_steps(params) -> list[Step]:

    from techminer2.io._internals.pipeline.other_information import (
        assign_record_no,
        calculate_num_authors,
        calculate_num_global_references,
    )

    return [
        Step(
            name="Assigning record numbers",
            function=assign_record_no,
            kwargs={"root_directory": params.root_directory},
            count_message="Record numbers assigned",
        ),
        Step(
            name="Calculating number of authors",
            function=calculate_num_authors,
            kwargs={"root_directory": params.root_directory},
            count_message="Number of authors calculated",
        ),
        Step(
            name="Calculating number of global references",
            function=calculate_num_global_references,
            kwargs={"root_directory": params.root_directory},
            count_message="Number of global references calculated",
        ),
    ]


# _preprocess_references(root_directory)
# _preprocess_record_id(root_directory)

# _preprocess_global_references(root_directory)  # ok
# _preprocess_local_references(root_directory)  # ok
# _preprocess_local_citations(root_directory)  # ok
# _preprocess_references(root_directory)
# _preprocess_global_citations(root_directory)

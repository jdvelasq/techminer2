# pylint: disable=import-outside-toplevel


from ..step import Step


def build_other_information_steps(params) -> list[Step]:

    from .assign_record_id import assign_record_id
    from .assign_record_no import assign_record_no
    from .calculate_num_authors import calculate_num_authors
    from .calculate_num_global_references import calculate_num_global_references

    return [
        Step(
            name="Assigning record number",
            function=assign_record_no,
            kwargs={"root_directory": params.root_directory},
            count_message="Record number assigned",
        ),
        Step(
            name="Assigning record ID",
            function=assign_record_id,
            kwargs={"root_directory": params.root_directory},
            count_message="Record ID assigned",
        ),
        Step(
            name="Calculating number of authors per record",
            function=calculate_num_authors,
            kwargs={"root_directory": params.root_directory},
            count_message="Number of authors per record calculated",
        ),
        Step(
            name="Calculating number of references per record",
            function=calculate_num_global_references,
            kwargs={"root_directory": params.root_directory},
            count_message="Number of references per record calculated",
        ),
    ]


# _preprocess_references(root_directory)
# _preprocess_record_id(root_directory)

# _preprocess_global_references(root_directory)  # ok
# _preprocess_local_references(root_directory)  # ok
# _preprocess_local_citations(root_directory)  # ok
# _preprocess_references(root_directory)

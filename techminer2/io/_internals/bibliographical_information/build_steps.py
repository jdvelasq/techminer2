# pylint: disable=import-outside-toplevel


from ..step import Step

# _preprocess_document_type(root_directory)
# _preprocess_countries(root_directory)  # ok
# _preprocess_organizations(root_directory)  # ok
# _preprocess_descriptors(root_directory)  # ok


def build_bibliographical_information_steps(params) -> list[Step]:

    from .create_raw_keywords import create_raw_keywords
    from .normalize_abbr_source_title import normalize_abbr_source_title
    from .normalize_document_type import normalize_document_type
    from .normalize_eissn import normalize_eissn
    from .normalize_global_citations import normalize_global_citations
    from .normalize_isbn import normalize_isbn
    from .normalize_issn import normalize_issn
    from .normalize_source_title import normalize_source_title
    from .normalize_subject_areas import normalize_subject_areas

    return [
        Step(
            name="Normalizing Document Type",
            function=normalize_document_type,
            kwargs={"root_directory": params.root_directory},
            count_message="Document types normalized",
        ),
        Step(
            name="Normalizing EISSN",
            function=normalize_eissn,
            kwargs={"root_directory": params.root_directory},
            count_message="EISSN normalized",
        ),
        Step(
            name="Normalizing Global Citations",
            function=normalize_global_citations,
            kwargs={"root_directory": params.root_directory},
            count_message="Global citations normalized",
        ),
        Step(
            name="Normalizing ISBN",
            function=normalize_isbn,
            kwargs={"root_directory": params.root_directory},
            count_message="ISBN normalized",
        ),
        Step(
            name="Normalizing ISSN",
            function=normalize_issn,
            kwargs={"root_directory": params.root_directory},
            count_message="ISSN normalized",
        ),
        Step(
            name="Normalizing Source Title",
            function=normalize_source_title,
            kwargs={"root_directory": params.root_directory},
            count_message="Source titles normalized",
        ),
        Step(
            name="Normalizing Abbreviated Source Title",
            function=normalize_abbr_source_title,
            kwargs={"root_directory": params.root_directory},
            count_message="Abbreviated Source titles normalized",
        ),
        Step(
            name="Normalizing Subject Areas",
            function=normalize_subject_areas,
            kwargs={"root_directory": params.root_directory},
            count_message="Subject Areas normalized",
        ),
        # ----------------------------------------
        Step(
            name="Creating Raw Keywords",
            function=create_raw_keywords,
            kwargs={"root_directory": params.root_directory},
            count_message="Raw keywords created",
        ),
    ]

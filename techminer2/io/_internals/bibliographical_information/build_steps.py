# pylint: disable=import-outside-toplevel


from ..step import Step

# _preprocess_countries(root_directory)  # ok
# _preprocess_organizations(root_directory)  # ok
# _preprocess_descriptors(root_directory)  # ok


def build_bibliographical_information_steps(params) -> list[Step]:

    from .normalize_abbr_source_title import normalize_abbr_source_title
    from .normalize_affiliations import normalize_affiliations
    from .normalize_correspondence_address import normalize_correspondence_address
    from .normalize_editors import normalize_editors
    from .normalize_eissn import normalize_eissn
    from .normalize_isbn import normalize_isbn
    from .normalize_issn import normalize_issn
    from .normalize_language import normalize_language
    from .normalize_publisher import normalize_publisher
    from .normalize_pubmed_id import normalize_pubmed_id
    from .normalize_subject_areas import normalize_subject_areas

    return [
        Step(
            name="Normalizing affiliations",
            function=normalize_affiliations,
            kwargs={"root_directory": params.root_directory},
            count_message="Affiliations normalized",
        ),
        Step(
            name="Normalizing EISSN",
            function=normalize_eissn,
            kwargs={"root_directory": params.root_directory},
            count_message="EISSN normalized",
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
            name="Normalizing PubMed ID",
            function=normalize_pubmed_id,
            kwargs={"root_directory": params.root_directory},
            count_message="PubMed ID normalized",
        ),
        Step(
            name="Normalizing publishers",
            function=normalize_publisher,
            kwargs={"root_directory": params.root_directory},
            count_message="Publishers normalized",
        ),
        Step(
            name="Normalizing editors",
            function=normalize_editors,
            kwargs={"root_directory": params.root_directory},
            count_message="Editors normalized",
        ),
        Step(
            name="Normalizing correspondence address",
            function=normalize_correspondence_address,
            kwargs={"root_directory": params.root_directory},
            count_message="Correspondence address normalized",
        ),
        Step(
            name="Normalizing language",
            function=normalize_language,
            kwargs={"root_directory": params.root_directory},
            count_message="Language normalized",
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
    ]

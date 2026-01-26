# pylint: disable=import-outside-toplevel


from ..step import Step


def build_citation_information_steps(params) -> list[Step]:

    from .normalize_author_names import normalize_author_names
    from .normalize_authors import normalize_authors
    from .normalize_authors_id import normalize_authors_id
    from .normalize_document_type import normalize_document_type
    from .normalize_doi import normalize_doi
    from .normalize_eid import normalize_eid
    from .normalize_global_citation_count import normalize_global_citation_count
    from .normalize_issue import normalize_issue
    from .normalize_open_access import normalize_open_access
    from .normalize_pages import normalize_pages
    from .normalize_publication_stage import normalize_publication_stage
    from .normalize_source_title import normalize_source_title
    from .normalize_volume import normalize_volume
    from .normalize_year import normalize_year

    return [
        Step(
            name="Normalizing authors ID",
            function=normalize_authors_id,
            kwargs={"root_directory": params.root_directory},
            count_message="Authors ID normalized",
        ),
        Step(
            name="Normalizing authors",
            function=normalize_authors,
            kwargs={"root_directory": params.root_directory},
            count_message="Authors normalized",
        ),
        Step(
            name="Normalizing author names",
            function=normalize_author_names,
            kwargs={"root_directory": params.root_directory},
            count_message="Author names normalized",
        ),
        Step(
            name="Normalizing year",
            function=normalize_year,
            kwargs={"root_directory": params.root_directory},
            count_message="Years normalized",
        ),
        Step(
            name="Normalizing EID",
            function=normalize_eid,
            kwargs={"root_directory": params.root_directory},
            count_message="EIDs normalized",
        ),
        Step(
            name="Normalizing source title",
            function=normalize_source_title,
            kwargs={"root_directory": params.root_directory},
            count_message="Source titles normalized",
        ),
        Step(
            name="Normalizing volume",
            function=normalize_volume,
            kwargs={"root_directory": params.root_directory},
            count_message="Volumes normalized",
        ),
        Step(
            name="Normalizing issue",
            function=normalize_issue,
            kwargs={"root_directory": params.root_directory},
            count_message="Issues normalized",
        ),
        Step(
            name="Normalizing pages",
            function=normalize_pages,
            kwargs={"root_directory": params.root_directory},
            count_message="Pages normalized",
        ),
        Step(
            name="Normalizing global citation count",
            function=normalize_global_citation_count,
            kwargs={"root_directory": params.root_directory},
            count_message="Global citation count normalized",
        ),
        Step(
            name="Normalizing document type",
            function=normalize_document_type,
            kwargs={"root_directory": params.root_directory},
            count_message="Document types normalized",
        ),
        Step(
            name="Normalizing publication stage",
            function=normalize_publication_stage,
            kwargs={"root_directory": params.root_directory},
            count_message="Publication stages normalized",
        ),
        Step(
            name="Normalizing DOI",
            function=normalize_doi,
            kwargs={"root_directory": params.root_directory},
            count_message="DOI normalized",
        ),
        Step(
            name="Normalizing open access",
            function=normalize_open_access,
            kwargs={"root_directory": params.root_directory},
            count_message="Open access normalized",
        ),
    ]

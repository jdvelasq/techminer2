# CODE_REVIEW: 2026-01-26

from ...._internals import Params
from ..operations import DataFile
from ..step import Step


def build_citation_information_steps(params: Params) -> list[Step]:

    from .disambiguate_authors import disambiguate_authors
    from .normalize_author_ids import normalize_author_ids
    from .normalize_authors import normalize_authors
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

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Normalizing author IDs in main.csv.zip",
            function=normalize_author_ids,
            kwargs={
                "root_directory": params.root_directory,
                "file": DataFile.MAIN,
            },
            count_message="{count} author IDs normalized",
        ),
        Step(
            name="Normalizing author IDs in references.csv.zip",
            function=normalize_author_ids,
            kwargs={
                "root_directory": params.root_directory,
                "file": DataFile.REFERENCES,
            },
            count_message="{count} author IDs normalized",
        ),
        Step(
            name="Normalizing authors in main.csv.zip",
            function=normalize_authors,
            kwargs={
                "root_directory": params.root_directory,
                "file": DataFile.MAIN,
            },
            count_message="{count} author records normalized",
        ),
        Step(
            name="Normalizing authors in references.csv.zip",
            function=normalize_authors,
            kwargs={
                "root_directory": params.root_directory,
                "file": DataFile.REFERENCES,
            },
            count_message="{count} author records normalized",
        ),
        Step(
            name="Disambiguating author names",
            function=disambiguate_authors,
            kwargs=common_kwargs,
            count_message="{count} author names disambiguated",
        ),
        Step(
            name="Normalizing year",
            function=normalize_year,
            kwargs=common_kwargs,
            count_message="{count} year records normalized",
        ),
        Step(
            name="Normalizing EID",
            function=normalize_eid,
            kwargs=common_kwargs,
            count_message="{count} EID records normalized",
        ),
        Step(
            name="Normalizing source title",
            function=normalize_source_title,
            kwargs=common_kwargs,
            count_message="{count} source title records normalized",
        ),
        Step(
            name="Normalizing volume",
            function=normalize_volume,
            kwargs=common_kwargs,
            count_message="{count} volume records normalized",
        ),
        Step(
            name="Normalizing issue",
            function=normalize_issue,
            kwargs=common_kwargs,
            count_message="{count} issue records normalized",
        ),
        Step(
            name="Normalizing pages",
            function=normalize_pages,
            kwargs=common_kwargs,
            count_message="{count} page records normalized",
        ),
        Step(
            name="Normalizing global citation count",
            function=normalize_global_citation_count,
            kwargs=common_kwargs,
            count_message="{count} global citation count records normalized",
        ),
        Step(
            name="Normalizing document type",
            function=normalize_document_type,
            kwargs=common_kwargs,
            count_message="{count} document type records normalized",
        ),
        Step(
            name="Normalizing publication stage",
            function=normalize_publication_stage,
            kwargs=common_kwargs,
            count_message="{count} publication stage records normalized",
        ),
        Step(
            name="Normalizing DOI",
            function=normalize_doi,
            kwargs=common_kwargs,
            count_message="{count} DOI records normalized",
        ),
        Step(
            name="Normalizing open access",
            function=normalize_open_access,
            kwargs=common_kwargs,
            count_message="{count} open access records normalized",
        ),
    ]

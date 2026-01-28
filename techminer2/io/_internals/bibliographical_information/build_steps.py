# CODE_REVIEW: 2026-01-26

from techminer2._internals.params_mixin import Params

from ..step import Step


def build_bibliographical_information_steps(params: Params) -> list[Step]:

    from .normalize_affiliations import normalize_affiliations
    from .normalize_correspondence_address import normalize_correspondence_address
    from .normalize_editors import normalize_editors
    from .normalize_eissn import normalize_eissn
    from .normalize_isbn import normalize_isbn
    from .normalize_issn import normalize_issn
    from .normalize_language import normalize_language
    from .normalize_publisher import normalize_publisher
    from .normalize_pubmed_id import normalize_pubmed_id
    from .normalize_source_title_abbr import normalize_source_title_abbr
    from .normalize_subject_areas import normalize_subject_areas

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Normalizing affiliations",
            function=normalize_affiliations,
            kwargs=common_kwargs,
            count_message="{count} affiliations normalized",
        ),
        Step(
            name="Normalizing EISSN",
            function=normalize_eissn,
            kwargs=common_kwargs,
            count_message="{count} EISSN entries normalized",
        ),
        Step(
            name="Normalizing ISBN",
            function=normalize_isbn,
            kwargs=common_kwargs,
            count_message="{count} ISBN entries normalized",
        ),
        Step(
            name="Normalizing ISSN",
            function=normalize_issn,
            kwargs=common_kwargs,
            count_message="{count} ISSN entries normalized",
        ),
        Step(
            name="Normalizing PubMed ID",
            function=normalize_pubmed_id,
            kwargs=common_kwargs,
            count_message="{count} PubMed IDs normalized",
        ),
        Step(
            name="Normalizing publishers",
            function=normalize_publisher,
            kwargs=common_kwargs,
            count_message="{count} publishers normalized",
        ),
        Step(
            name="Normalizing editors",
            function=normalize_editors,
            kwargs=common_kwargs,
            count_message="{count} editors normalized",
        ),
        Step(
            name="Normalizing correspondence address",
            function=normalize_correspondence_address,
            kwargs=common_kwargs,
            count_message="{count} correspondence addresses normalized",
        ),
        Step(
            name="Normalizing language",
            function=normalize_language,
            kwargs=common_kwargs,
            count_message="{count} language entries normalized",
        ),
        Step(
            name="Normalizing abbreviated source title",
            function=normalize_source_title_abbr,
            kwargs=common_kwargs,
            count_message="{count} abbreviated source titles normalized",
        ),
        Step(
            name="Normalizing subject areas",
            function=normalize_subject_areas,
            kwargs={
                "issn_column": "issn",
                "eissn_column": "eissn",
                "target": "subject_areas",
                "root_directory": params.root_directory,
            },
            count_message="{count} subject areas normalized",
        ),
    ]

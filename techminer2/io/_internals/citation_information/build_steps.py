# pylint: disable=import-outside-toplevel


from ..step import Step


def build_citation_information_steps(params) -> list[Step]:

    from .normalize_doi import normalize_doi

    return [
        Step(
            name="Normalizing DOI",
            function=normalize_doi,
            kwargs={"root_directory": params.root_directory},
            count_message="DOI normalized",
        ),
        # _preprocess_source_title(root_directory)
        # _preprocess_abbr_source_title(root_directory)
        # _preprocess_authors_id(root_directory)
        # _preprocess_authors(root_directory)
        # _preprocess_author_names(root_directory)
    ]

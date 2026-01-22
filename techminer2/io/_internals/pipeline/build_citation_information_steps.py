# pylint: disable=import-outside-toplevel


from .step import Step


def build_citation_information_steps(params) -> list[Step]:

    from techminer2.io._internals.pipeline.citation_information import (
        normalize_doi,
        normalize_tokenized_abstract,
        normalize_tokenized_document_title,
    )

    return [
        Step(
            name="Tokenizing document titles",
            function=normalize_tokenized_document_title,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} document titles tokenized",
        ),
        Step(
            name="Tokenizing abstracts",
            function=normalize_tokenized_abstract,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} abstracts tokenized",
        ),
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

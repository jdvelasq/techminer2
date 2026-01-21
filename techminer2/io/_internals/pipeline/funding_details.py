# pylint: disable=import-outside-toplevel


from .step import Step


def build_funding_details_steps(params) -> list[Step]:

    from techminer2.scopus._internals.funding_details import (
        normalize_doi,
        normalize_tokenized_abstract,
        normalize_tokenized_document_title,
    )

    return []

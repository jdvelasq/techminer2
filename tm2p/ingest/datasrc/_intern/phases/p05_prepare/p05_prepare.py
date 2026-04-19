# CODE_REVIEW: 2026-01-26

from tm2p._intern import Params

from ...step import Step


def p05_prepare(params: Params) -> list[Step]:

    from .s01_separators import s01_separators
    from .s02_renam_col import s02_renam_col
    from .s03_drop_empty_col import s03_drop_empty_col
    from .s04_lcs import s04_lcs
    from .s05_gcs import s05_gcs
    from .s06_doi import s06_doi
    from .s07_pubtype import s07_pubtype
    from .s08_doctype import s08_doctype
    from .s09_database import s09_database
    from .s10_asjc import s10_asjc

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Formating separators",
            function=s01_separators,
            kwargs=common_kwargs,
        ),
        Step(
            name="Renaming columns",
            function=s02_renam_col,
            kwargs=common_kwargs,
        ),
        Step(
            name="Dropping empty columns",
            function=s03_drop_empty_col,
            kwargs=common_kwargs,
        ),
        Step(
            name="Setting LCS value",
            function=s04_lcs,
            kwargs=common_kwargs,
        ),
        Step(
            name="Formating GCS value",
            function=s05_gcs,
            kwargs=common_kwargs,
        ),
        Step(
            name="Formating DOI value",
            function=s06_doi,
            kwargs=common_kwargs,
        ),
        Step(
            name="Formating publication type value",
            function=s07_pubtype,
            kwargs=common_kwargs,
        ),
        Step(
            name="Formating document type value",
            function=s08_doctype,
            kwargs=common_kwargs,
        ),
        Step(
            name="Setting database value",
            function=s09_database,
            kwargs=common_kwargs,
        ),
        Step(
            name="Formating ASJC value",
            function=s10_asjc,
            kwargs=common_kwargs,
        ),
    ]

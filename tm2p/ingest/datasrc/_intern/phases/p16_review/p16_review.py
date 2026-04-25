# CODE_REVIEW: 2026-01-26


from tm2p._intern import Params

from ...step import Step


def p16_review(params: Params) -> list[Step]:

    from .s01_extract_abstract_suffixes import s01_extract_abstract_suffixes
    from .s02_extract_abstract_prefixes import s02_extract_abstract_prefixes
    from .s03_extract_section_headers import s03_extract_section_headers
    from .s04_extract_acronyms import s04_extract_acronyms
    from .s05_generate_review_table import s05_generate_review_table

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Extracting abstract suffixes",
            function=s01_extract_abstract_suffixes,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting abstract prefixes",
            function=s02_extract_abstract_prefixes,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting section headers",
            function=s03_extract_section_headers,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting acronyms",
            function=s04_extract_acronyms,
            kwargs=common_kwargs,
        ),
        Step(
            name="Generating review table",
            function=s05_generate_review_table,
            kwargs=common_kwargs,
        ),
    ]

# CODE_REVIEW: 2026-01-26

from tm2p._intern import Params

from ...step import Step


def p06_openalex(params: Params) -> list[Step]:

    from .s01_auth_full_name_openalex import s01_auth_full_name_openalex
    from .s94_auth_with_affil_openalex import s02_auth_with_affil_openalex
    from .s95_auth_raw_openalex import s03_auth_raw_openalex
    from .s96_orcid_openalex import s04_orcid_openalex

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Formating AUTH_FULL_NAME",
            function=s01_auth_full_name_openalex,
            kwargs=common_kwargs,
        ),
        # Step(
        #     name="Formating AUTH_WITH_AFFIL",
        #     function=s02_auth_with_affil_openalex,
        #     kwargs=common_kwargs,
        # ),
        # Step(
        #     name="Formating AUTH_RAW",
        #     function=s03_auth_raw_openalex,
        #     kwargs=common_kwargs,
        # ),
        # Step(
        #     name="Formating ORCID",
        #     function=s04_orcid_openalex,
        #     kwargs=common_kwargs,
        # ),
    ]

# CODE_REVIEW: 2026-01-26

from tm2p._intern import Params

from ...step import Step


def p06_pubmed(params: Params) -> list[Step]:

    from .s01_auth_full_name_pubmed import s01_auth_full_name_pubmed
    from .s94_auth_with_affil_pubmed import s02_auth_with_affil_pubmed
    from .s96_auth_raw_pubmed import s03_auth_raw_pubmed
    from .s96_orcid_pubmed import s04_orcid_pubmed

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Formating AUTH_FULL_NAME",
            function=s01_auth_full_name_pubmed,
            kwargs=common_kwargs,
        ),
        # Step(
        #     name="Formating AUTH_WITH_AFFIL",
        #     function=s02_auth_with_affil_pubmed,
        #     kwargs=common_kwargs,
        # ),
        # Step(
        #     name="Formating AUTH_RAW",
        #     function=s03_auth_raw_pubmed,
        #     kwargs=common_kwargs,
        # ),
        # Step(
        #     name="Formating ORCID",
        #     function=s04_orcid_pubmed,
        #     kwargs=common_kwargs,
        # ),
    ]

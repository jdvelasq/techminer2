# CODE_REVIEW: 2026-01-26

from tm2p._intern import Params

from ...step import Step


def p06_scopus(params: Params) -> list[Step]:

    from .s01_auth_full_name_scopus import s01_auth_full_name_scopus
    from .s94_auth_with_affil_scopus import s02_auth_with_affil_scopus
    from .s95_auth_raw_scopus import s03_auth_raw_scopus
    from .s96_orcid_scopus import s04_orcid_scopus

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Formating AUTH_FULL_NAME",
            function=s01_auth_full_name_scopus,
            kwargs=common_kwargs,
        ),
        # Step(
        #     name="Formating AUTH_WITH_AFFIL",
        #     function=s02_auth_with_affil_scopus,
        #     kwargs=common_kwargs,
        # ),
        # Step(
        #     name="Formating AUTH_RAW",
        #     function=s03_auth_raw_scopus,
        #     kwargs=common_kwargs,
        # ),
        # Step(
        #     name="Formating ORCID",
        #     function=s04_orcid_scopus,
        #     kwargs=common_kwargs,
        # ),
    ]

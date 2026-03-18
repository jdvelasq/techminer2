# CODE_REVIEW: 2026-01-26

from tm2p._intern import Params

from ...step import Step


def p06_wos(params: Params) -> list[Step]:

    # from .s01_auth_full_name_wos import s01_auth_full_name_wos
    from .s94_auth_with_affil_wos import s02_auth_with_affil_wos
    from .s95_auth_raw_wos import s03_auth_raw_wos
    from .s96_orcid_wos import s04_orcid_wos

    common_kwargs = {"root_directory": params.root_directory}

    return [
        # Step(
        #     name="Formating AUTH_FULL_NAME",
        #     function=s01_auth_full_name_wos,
        #     kwargs=common_kwargs,
        # ),
        # Step(
        #     name="Formating AUTH_WITH_AFFIL",
        #     function=s02_auth_with_affil_wos,
        #     kwargs=common_kwargs,
        # ),
        # Step(
        #     name="Formating AUTH_RAW",
        #     function=s03_auth_raw_wos,
        #     kwargs=common_kwargs,
        # ),
        # Step(
        #     name="Formating ORCID",
        #     function=s04_orcid_wos,
        #     kwargs=common_kwargs,
        # ),
    ]

# CODE_REVIEW: 2026-01-26

from tm2p._intern import Params

from ...step import Step


def p06_auth(params: Params) -> list[Step]:

    from .s01_auth_full_name import s01_auth_full_name_wos
    from .s02_auth_raw import s02_auth_raw
    from .s03_disambiguate import s03_disambiguate
    from .s04_auth_with_affil import s04_auth_with_affil
    from .s05_n_auth import s05_n_auth
    from .s06_auth_first import s06_auth_first
    from .s07_auth_norm import s07_auth_norm

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Formating AUTH_FULL_NAME",
            function=s01_auth_full_name_wos,
            kwargs=common_kwargs,
        ),
        Step(
            name="Formating AUTH_RAW",
            function=s02_auth_raw,
            kwargs=common_kwargs,
        ),
        Step(
            name="Desambiguating AUTH_RAW",
            function=s03_disambiguate,
            kwargs=common_kwargs,
        ),
        Step(
            name="Generating AUTH_WITH_AFFIL",
            function=s04_auth_with_affil,
            kwargs=common_kwargs,
        ),
        Step(
            name="Generating N_AUTH",
            function=s05_n_auth,
            kwargs=common_kwargs,
        ),
        Step(
            name="Generating AUTH_FIRST",
            function=s06_auth_first,
            kwargs=common_kwargs,
        ),
        Step(
            name="Generating AUTH_NORM",
            function=s07_auth_norm,
            kwargs=common_kwargs,
        ),
    ]

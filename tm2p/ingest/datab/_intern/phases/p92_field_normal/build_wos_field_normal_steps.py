# CODE_REVIEW: 2026-01-26

from tm2p._intern import Params

from ...step import Step


def build_wos_field_normal_steps(params: Params) -> list[Step]:

    from .s02_authid_wos import s02_authid_wos
    from .s03_auth_norm import s03_auth_norm

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Repairing AUTHID",
            function=s02_authid_wos,
            kwargs=common_kwargs,
        ),
        Step(
            name="Disambiguating AUTH_NORM",
            function=s03_auth_norm,
            kwargs=common_kwargs,
        ),
    ]

# CODE_REVIEW: 2026-01-26

from tm2p._intern import Params

from ...step import Step


def p03_pars(params: Params) -> list[Step]:

    from .s01_pars import s01_pars

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Parsing data",
            function=s01_pars,
            kwargs=common_kwargs,
        ),
    ]

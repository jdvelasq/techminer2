# CODE_REVIEW: 2026-01-26

from tm2p._intern import Params

from ...step import Step


def p07_affil(params: Params) -> list[Step]:

    from .s01_affil import s01_affil

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Formating AFFIL",
            function=s01_affil,
            kwargs=common_kwargs,
        ),
    ]

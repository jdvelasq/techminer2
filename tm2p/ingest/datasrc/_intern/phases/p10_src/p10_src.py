# CODE_REVIEW: 2026-01-26

from tm2p._intern import Params

from ...step import Step


def p10_src(params: Params) -> list[Step]:

    from .s01_src import s01_src
    from .s02_src_iso4 import s02_src_iso4

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Formating SRC",
            function=s01_src,
            kwargs=common_kwargs,
        ),
        Step(
            name="Formating SRC_ISO4",
            function=s02_src_iso4,
            kwargs=common_kwargs,
        ),
    ]

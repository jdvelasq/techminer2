# CODE_REVIEW: 2026-01-26


from tm2p._intern import Params

from ...step import Step


def p02_compress(params: Params) -> list[Step]:

    common_kwargs = {"root_directory": params.root_directory}

    from .s01_compress import s01_compress

    return [
        Step(
            name="Compressing raw data",
            function=s01_compress,
            kwargs=common_kwargs,
        ),
    ]

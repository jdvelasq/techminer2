# CODE_REVIEW: 2026-01-26

from techminer2 import Field
from techminer2._internals import Params

from ..step import Step


def build_affiliation_steps(params: Params) -> list[Step]:

    from .normalize_affil_raw import normalize_affil_raw

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name=f"Normalizing '{Field.AFFIL_RAW.value}'",
            function=normalize_affil_raw,
            kwargs=common_kwargs,
            count_message="{count} records normalized",
        ),
    ]

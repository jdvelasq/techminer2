# CODE_REVIEW: 2026-01-26


from ...._internals import Params
from ..step import Step


def build_funding_details_steps(params: Params) -> list[Step]:

    from .normalize_funding_details import normalize_funding_details
    from .normalize_funding_texts import normalize_funding_texts
    from .normalize_sponsors import normalize_sponsors

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Normalizing funding details",
            function=normalize_funding_details,
            kwargs=common_kwargs,
            count_message="{count} funding details normalized",
        ),
        Step(
            name="Normalizing funding text",
            function=normalize_funding_texts,
            kwargs=common_kwargs,
            count_message="{count} funding text normalized",
        ),
        Step(
            name="Normalizing sponsors",
            function=normalize_sponsors,
            kwargs=common_kwargs,
            count_message="{count} sponsors normalized",
        ),
    ]

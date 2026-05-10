# CODE_REVIEW: 2026-01-26

from tm2p._intern import Params

from ...step import Step


def p04_filter(params: Params) -> list[Step]:

    from .s01_non_english_abstr import s01_non_english_abstr

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Removing non-English abstracts from WoS data",
            function=s01_non_english_abstr,
            kwargs=common_kwargs,
            count_message="{count} records removed",
        ),
    ]

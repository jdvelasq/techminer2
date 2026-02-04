# CODE_REVIEW: 2026-01-26

from techminer2 import Field

from ...._internals import Params
from ..step import Step


def build_source_title_steps(params: Params) -> list[Step]:

    from .assign_subjarea import assign_subjarea
    from .normalize_srctitle_abbr_raw import normalize_srctitle_abbr_raw
    from .normalize_srctitle_raw import normalize_srctitle_raw

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name=f"Normalizing {Field.SUBJ_AREA.value}",
            function=assign_subjarea,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
        Step(
            name=f"Normalizing {Field.SRC_TITLE_ABBR_RAW.value}",
            function=normalize_srctitle_abbr_raw,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
        Step(
            name=f"Normalizing {Field.SRC_TITLE_RAW.value}",
            function=normalize_srctitle_raw,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
    ]

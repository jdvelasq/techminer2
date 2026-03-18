# CODE_REVIEW: 2026-01-26

from tm2p import Field
from tm2p._intern import Params

from ...step import Step


def p15_cit_ref(params: Params) -> list[Step]:

    from .s01_normal_glob_ref import s01_normal_glob_ref
    from .s02_lcr_norm import s02_lcr_norm
    from .s03_lcs import s03_lcs

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name=f"Normalizing '{Field.GCR_FREE_TEXT.value}'",
            function=s01_normal_glob_ref,
            kwargs=common_kwargs,
            count_message="{count} references normalized",
        ),
        Step(
            name=f"Normalizing '{Field.LCR_NORM.value}'",
            function=s02_lcr_norm,
            kwargs=common_kwargs,
            count_message="{count} references normalized",
        ),
        Step(
            name=f"Compute '{Field.LCS.value}'",
            function=s03_lcs,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
    ]

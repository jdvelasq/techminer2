# CODE_REVIEW: 2026-01-26


from tm2p._intern import Params

from ...step import Step


def p15_cit_ref(params: Params) -> list[Step]:

    from .s01_gcr_wos_format import s01_gcr_wos_format
    from .s02_lcr_wos_format import s02_lcr_wos_format
    from .s03_lcs import s03_lcs
    from .s04_n_gcr import s04_n_gcr
    from .s05_n_lcr import s05_n_lcr

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Normalizing GCR_FREE_TEXT",
            function=s01_gcr_wos_format,
            kwargs=common_kwargs,
            count_message="{count} references normalized",
        ),
        Step(
            name="Normalizing LCR_WOS_FORMAT",
            function=s02_lcr_wos_format,
            kwargs=common_kwargs,
            count_message="{count} references normalized",
        ),
        Step(
            name="Compute LCS",
            function=s03_lcs,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
        Step(
            name="Compute N_GCR",
            function=s04_n_gcr,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
        Step(
            name="Compute N_LCR",
            function=s05_n_lcr,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
    ]

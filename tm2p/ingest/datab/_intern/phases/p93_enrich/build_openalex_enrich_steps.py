# CODE_REVIEW: 2026-01-26

from tm2p._intern import Params

from ...step import Step


def build_openalex_enrich_steps(params: Params) -> list[Step]:

    from ..p06_auth.s05_n_auth import s05_n_auth
    from ..p06_auth.s06_auth_first import s06_auth_first
    from .s04_ctry_openalex import s04_ctry_openalex
    from .s05_ctry_first import s05_ctry_first
    from .s06_region import s06_region
    from .s07_subregion import s07_subregion
    from .s08_ctry_iso3 import s08_ctry_iso3
    from .s09_org_openalex import s09_org_openalex
    from .s10_org_first import s10_org_first
    from .s99_n_gcr_openalex import s03_n_gcr_openalex

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Calulating N_AUTH",
            function=s05_n_auth,
            kwargs=common_kwargs,
        ),
        Step(
            name="Creating AUTH_FIRST",
            function=s06_auth_first,
            kwargs=common_kwargs,
        ),
        Step(
            name="Calculating N_GCR",
            function=s03_n_gcr_openalex,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting CTRY",
            function=s04_ctry_openalex,
            kwargs=common_kwargs,
        ),
        Step(
            name="Assigning CTRY_FIRST",
            function=s05_ctry_first,
            kwargs=common_kwargs,
        ),
        Step(
            name="Assigning REGION",
            function=s06_region,
            kwargs=common_kwargs,
        ),
        Step(
            name="Assigning SUBREGION",
            function=s07_subregion,
            kwargs=common_kwargs,
        ),
        Step(
            name="Assigning CTRY_ISO3",
            function=s08_ctry_iso3,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting ORG",
            function=s09_org_openalex,
            kwargs=common_kwargs,
        ),
        Step(
            name="Assigning ORG_FIRST",
            function=s10_org_first,
            kwargs=common_kwargs,
        ),
    ]

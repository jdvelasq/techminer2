# CODE_REVIEW: 2026-01-26

from tm2p._intern import Params

from ...step import Step


def p09_ctry(params: Params) -> list[Step]:

    from .s01_ctry import s01_ctry
    from .s02_ctry_thesaurus import s02_ctry_thesaurus
    from .s03_ctry_first import s03_ctry_first
    from .s04_ctry import s04_ctry
    from .s05_ctry_iso3 import s05_ctry_iso3
    from .s06_ctry_iso3_first import s06_ctry_iso3_first
    from .s07_region import s07_region
    from .s08_subregion import s08_subregion

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Extracting CTRY",
            function=s01_ctry,
            kwargs=common_kwargs,
        ),
        Step(
            name="Creating CTRY Thesaurus",
            function=s02_ctry_thesaurus,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting CTRY_FIRST",
            function=s03_ctry_first,
            kwargs=common_kwargs,
        ),
        Step(
            name="Cleaning CTRY",
            function=s04_ctry,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting CTRY_ISO3",
            function=s05_ctry_iso3,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting CTRY_ISO3_FIRST",
            function=s06_ctry_iso3_first,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting REGION",
            function=s07_region,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting SUBREGION",
            function=s08_subregion,
            kwargs=common_kwargs,
        ),
    ]

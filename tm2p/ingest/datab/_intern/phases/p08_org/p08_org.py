# CODE_REVIEW: 2026-01-26

from tm2p._intern import Params

from ...step import Step


def p08_org(params: Params) -> list[Step]:

    from .s01_org import s01_org
    from .s02_org_lwta import s02_org_lwta
    from .s03_org_thesaurus import s03_org_thesaurus
    from .s04_org_first import s04_org_first
    from .s05_org import s05_org

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Extracting ORG",
            function=s01_org,
            kwargs=common_kwargs,
        ),
        Step(
            name="Creating ORG abbreviations",
            function=s02_org_lwta,
            kwargs=common_kwargs,
        ),
        Step(
            name="Creating ORG Thesaurus",
            function=s03_org_thesaurus,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting ORG_FIRST",
            function=s04_org_first,
            kwargs=common_kwargs,
        ),
        Step(
            name="Cleaning ORG",
            function=s05_org,
            kwargs=common_kwargs,
        ),
    ]

# CODE_REVIEW: 2026-01-26

from tm2p._intern import Params

from ...step import Step


def p08_org(params: Params) -> list[Step]:

    from .s01_org_thesaurus import s01_org_thesaurus
    from .s02_org_first import s02_org_first
    from .s03_org_set import s03_org_set

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Extracting ORG",
            function=s01_org_thesaurus,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting ORG_FIRST",
            function=s02_org_first,
            kwargs=common_kwargs,
        ),
        Step(
            name="Cleaning ORG",
            function=s03_org_set,
            kwargs=common_kwargs,
        ),
    ]

# CODE_REVIEW: 2026-01-26

from techminer2 import CorpusField
from techminer2._internals import Params

from ..step import Step


def build_affiliation_steps(params: Params) -> list[Step]:

    from .assign_region import assign_region
    from .assign_subregion import assign_subregion
    from .extract_organizations_and_countries import extract_organizations_and_countries

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name=f"Extracting '{CorpusField.COUNTRY.value}' and '{CorpusField.ORG.value}'",
            function=extract_organizations_and_countries,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
        Step(
            name=f"Assigning '{CorpusField.REGION.value}'",
            function=assign_region,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
        Step(
            name=f"Assigning '{CorpusField.SUBREGION.value}'",
            function=assign_subregion,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
    ]

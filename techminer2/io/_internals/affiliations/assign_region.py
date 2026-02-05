from techminer2 import CorpusField
from techminer2._constants import COUNTRY_TO_REGION
from techminer2.operations.transform_column import transform_column


def _process(series):

    series = series.copy()
    series = series.str.split("; ")
    series = series.apply(
        lambda countries: "; ".join(
            sorted(
                set(COUNTRY_TO_REGION.get(country, "[N/A]") for country in countries)
            )
        )
    )
    series = series.str.join("; ")
    return series


def assign_region(root_directory: str) -> int:

    return transform_column(
        source=CorpusField.COUNTRY,
        target=CorpusField.REGION,
        function=_process,
        root_directory=root_directory,
    )

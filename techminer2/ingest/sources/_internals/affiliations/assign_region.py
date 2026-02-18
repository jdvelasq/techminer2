from techminer2 import CorpusField
from techminer2._internals.package_data import load_builtin_mapping
from techminer2.ingest.operations.transform_column import transform_column


def _process(series):

    country_to_region = load_builtin_mapping("country_to_region.json")

    series = series.copy()
    series = series.str.split("; ")
    series = series.apply(
        lambda countries: "; ".join(
            sorted(
                set(
                    item
                    for country in countries
                    for item in (
                        country_to_region.get(country, "[N/A]")
                        if isinstance(country_to_region.get(country, "[N/A]"), str)
                        else country_to_region.get(country, "[N/A]")
                    )
                    if isinstance(item, str)
                    for item in ([item] if isinstance(item, str) else item)
                )
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

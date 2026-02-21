from dataclasses import replace

from techminer2._internals import Params
from techminer2.ingest.extract._helpers.values import extract_values


def extract_difference(params: Params) -> list[str]:

    set_a = set(
        extract_values(replace(params, source_field=params.source_fields[0])).term
    )
    set_b = set(
        extract_values(replace(params, source_field=params.source_fields[1])).term
    )
    return sorted(set_a.difference(set_b))

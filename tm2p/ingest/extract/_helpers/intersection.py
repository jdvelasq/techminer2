from dataclasses import replace

from tm2p._internals import Params
from tm2p.ingest.extract._helpers.values import extract_values


def extract_intersection(params: Params) -> list[str]:

    set_a = set(
        extract_values(replace(params, source_field=params.source_fields[0])).term
    )
    set_b = set(
        extract_values(replace(params, source_field=params.source_fields[1])).term
    )
    return sorted(set_a.intersection(set_b))

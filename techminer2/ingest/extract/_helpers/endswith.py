from techminer2._internals import Params
from techminer2.ingest.extract._helpers.values import extract_values


def extract_endswith(params: Params) -> list[str]:

    df = extract_values(params)
    return (
        df[df.term.str.endswith(params.pattern)]
        .dropna()
        .sort_values("term", ascending=True)
        .term.tolist()
    )

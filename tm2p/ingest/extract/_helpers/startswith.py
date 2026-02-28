from tm2p._internals import Params
from tm2p.ingest.extract._helpers.values import extract_values


def extract_startswith(params: Params) -> list[str]:

    df = extract_values(params)
    return (
        df[df.term.str.startswith(params.pattern)]
        .dropna()
        .sort_values("term", ascending=True)
        .term.tolist()
    )

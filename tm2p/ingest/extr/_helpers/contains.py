from tm2p._intern import Params
from tm2p.ingest.extr._helpers.values import extract_values


def extract_contains(params: Params) -> list[str]:

    df = extract_values(params)
    return (
        df[
            df.term.str.contains(
                pat=params.pattern,
                case=params.case_sensitive,
                flags=params.regex_flags,
                regex=params.regex_search,
            )
        ]
        .dropna()
        .sort_values("term", ascending=True)
        .term.tolist()
    )

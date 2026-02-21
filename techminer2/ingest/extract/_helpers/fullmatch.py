from techminer2._internals import Params
from techminer2.ingest.extract._helpers.values import extract_values


def extract_fullmatch(params: Params) -> list[str]:

    df = extract_values(params)
    return (
        df[
            df.term.str.fullmatch(
                pat=params.pattern,
                case=params.case_sensitive,
                flags=params.regex_flags,
            )
        ]
        .dropna()
        .sort_values("term", ascending=True)
        .term.tolist()
    )

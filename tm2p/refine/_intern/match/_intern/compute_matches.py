import pandas as pd  # type: ignore

from tm2p.enum import ThField
from tm2p._intern import Params

PREFERRED = ThField.PREFERRED.value
SIGNATURE = ThField.SIGNATURE.value


def compute_matches(thesaurus_df: pd.DataFrame, params: Params) -> dict[str, list[str]]:

    from tm2p.portfolio.performance_metrics.item_metrics import Metrics

    metrics = Metrics().update(**params.__dict__).run()
    counters = dict(zip(metrics.index, metrics.COUNTERS))

    mapping_df = thesaurus_df[[SIGNATURE, PREFERRED]].copy()
    mapping_df = mapping_df.drop_duplicates()

    mapping_df[PREFERRED] = mapping_df[PREFERRED].apply(
        lambda x: counters.get(x, x + " 0:0")
    )
    mapping_df["METRICS"] = mapping_df[PREFERRED].apply(
        lambda x: x.split(" ")[-1].strip() if x and x[0] != "#" else "0"
    )
    mapping_df["LENGTH"] = mapping_df[PREFERRED].apply(
        lambda x: len(x.split(" ")) if x and x[0] != "#" else 0
    )
    mapping_df = mapping_df.sort_values(
        ["METRICS", "LENGTH"], ascending=[False, True]
    )  #  type: ignore
    mapping_df.pop("METRICS")
    mapping_df.pop("LENGTH")

    grouped = mapping_df.groupby(SIGNATURE, as_index=False).agg({PREFERRED: list})
    matches = {
        pref[0]: pref[1:]
        for sign, pref in zip(grouped[SIGNATURE].values, grouped[PREFERRED].values)
        if len(pref) > 1
    }
    return matches

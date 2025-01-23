# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


def internal__compute_impact_metrics(records, indicators, field):
    """Computes the impact indicators."""

    records = records.copy()
    records = records[[field, "global_citations"]].dropna()

    records[field] = records[field].str.split(";")
    records = records.explode(field)
    records[field] = records[field].str.strip()
    records = records.sort_values([field, "global_citations"], ascending=[True, False])
    records = records.reset_index(drop=True)

    records = records.assign(
        cumcount_=records.sort_values("global_citations", ascending=False)
        .groupby(field)
        .cumcount()
        + 1
    )

    records = records.assign(cumcount_2=records.cumcount_.map(lambda w: w * w))

    h_indexes = records.query("global_citations >= cumcount_")
    h_indexes = h_indexes.groupby(field, as_index=True).agg({"cumcount_": "max"})
    h_indexes = h_indexes.rename(columns={"cumcount_": "h_index"})
    indicators.loc[h_indexes.index, "h_index"] = h_indexes.astype(int)
    indicators["h_index"] = indicators["h_index"].fillna(0)

    g_indexes = records.query("global_citations >= cumcount_2")
    g_indexes = g_indexes.groupby(field, as_index=True).agg({"cumcount_": "max"})
    g_indexes = g_indexes.rename(columns={"cumcount_": "g_index"})
    indicators.loc[g_indexes.index, "g_index"] = g_indexes.astype(int)
    indicators["g_index"] = indicators["g_index"].fillna(0)

    indicators = indicators.assign(m_index=indicators.h_index / indicators.age)
    indicators["m_index"] = indicators.m_index.round(decimals=2)

    return indicators

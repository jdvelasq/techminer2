# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


def internal__compute_impact_metrics(data_frame, grouped, field):
    """Computes the impact indicators."""

    data_frame = data_frame.copy()
    data_frame = data_frame[[field, "global_citations"]].dropna()

    data_frame[field] = data_frame[field].str.split(";")
    data_frame = data_frame.explode(field)
    data_frame[field] = data_frame[field].str.strip()
    data_frame = data_frame.sort_values(
        [field, "global_citations"], ascending=[True, False]
    )
    data_frame = data_frame.reset_index(drop=True)

    data_frame = data_frame.assign(
        cumcount_=data_frame.sort_values("global_citations", ascending=False)
        .groupby(field)
        .cumcount()
        + 1
    )

    data_frame = data_frame.assign(cumcount_2=data_frame.cumcount_.map(lambda w: w * w))

    h_indexes = data_frame.query("global_citations >= cumcount_")
    h_indexes = h_indexes.groupby(field, as_index=True).agg({"cumcount_": "max"})
    h_indexes = h_indexes.rename(columns={"cumcount_": "h_index"})
    grouped.loc[h_indexes.index, "h_index"] = h_indexes.astype(int)
    grouped["h_index"] = grouped["h_index"].fillna(0)

    g_indexes = data_frame.query("global_citations >= cumcount_2")
    g_indexes = g_indexes.groupby(field, as_index=True).agg({"cumcount_": "max"})
    g_indexes = g_indexes.rename(columns={"cumcount_": "g_index"})
    grouped.loc[g_indexes.index, "g_index"] = g_indexes.astype(int)
    grouped["g_index"] = grouped["g_index"].fillna(0)

    grouped = grouped.assign(m_index=grouped.h_index / grouped.age)
    grouped["m_index"] = grouped.m_index.round(decimals=2)

    return grouped

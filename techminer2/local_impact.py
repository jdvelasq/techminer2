from .cleveland_px import cleveland_px
from .impact_indicators import impact_indicators


def local_impact(
    column,
    impact_measure="h_index",
    top_n=20,
    directory="./",
    title=None,
):
    """computes local impact"""

    if impact_measure not in [
        "h_index",
        "g_index",
        "m_index",
        "global_citations",
    ]:
        raise ValueError(
            "Impact measure must be one of: h_index, g_index, m_index, global_citations"
        )

    indicators = impact_indicators(directory=directory, column=column)
    indicators = indicators.sort_values(by=impact_measure, ascending=False)
    indicators = indicators.head(top_n)

    indicators = indicators.reset_index()
    column_names = {
        column: column.replace("_", " ").title() for column in indicators.columns
    }
    indicators = indicators.rename(columns=column_names)

    return cleveland_px(
        dataframe=indicators,
        x_label=impact_measure.replace("_", " ").title(),
        y_label=column.replace("_", " ").title(),
        title=title,
    )

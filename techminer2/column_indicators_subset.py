def column_indicators_subset(
    column,
    indicators,
    metric,
    top_n,
    sort_values=None,
    sort_index=None,
):
    indicators = indicators.copy()
    indicators = indicators.reset_index()

    order_by_sequence = {
        "num_documents": [
            "num_documents",
            "global_citations",
            "local_citations",
            column,
        ],
        "global_citations": [
            "global_citations",
            "num_documents",
            "local_citations",
            column,
        ],
        "local_citations": [
            "local_citations",
            "num_documents",
            "global_citations",
            column,
        ],
    }

    order_by = order_by_sequence[metric]

    indicators.sort_values(
        by=order_by, ascending=[False, False, False, True], inplace=True
    )

    indicators = indicators.head(top_n)

    if sort_values is not None and sort_index is not None:
        raise ValueError("Only one of sort_values and sort_index can be specified")

    if sort_values is not None:
        by = sort_values["by"]
        by = order_by_sequence[by]
        ascending = sort_values["ascending"]
        ascending = [ascending] * 3 + [True]

        indicators = indicators.sort_values(by=by, ascending=ascending)

    indicators = indicators.set_index(column)

    if sort_index is not None:
        indicators = indicators.sort_index(**sort_index)

    return indicators

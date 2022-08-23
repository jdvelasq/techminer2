from .tm2__indicators_by_topic import tm2__indicators_by_topic


def tm2__column_indicators_by_metric(
    column,
    min_occ=None,
    max_occ=None,
    top_n=None,
    directory="./",
    metric="num_documents",
    file_name="documents.csv",
):
    indicators = tm2__indicators_by_topic(
        criterion=column, directory=directory, database=file_name
    )
    if min_occ is not None:
        indicators = indicators[indicators.num_documents >= min_occ]
    if max_occ is not None:
        indicators = indicators[indicators.num_documents <= max_occ]
    indicators = indicators.sort_values(metric, ascending=False)
    if top_n is not None:
        indicators = indicators.head(top_n)
    return indicators

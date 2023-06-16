from .indicators_by_field import indicators_by_field


def column_indicators_by_metric(
    column,
    min_occ=None,
    max_occ=None,
    top_n=None,
    directory="./",
    metric="num_documents",
    file_name="documents.csv",
):
    indicators = indicators_by_field(
        field=column, root_dir=directory, database=file_name
    )
    if min_occ is not None:
        indicators = indicators[indicators.num_documents >= min_occ]
    if max_occ is not None:
        indicators = indicators[indicators.num_documents <= max_occ]
    indicators = indicators.sort_values(metric, ascending=False)
    if top_n is not None:
        indicators = indicators.head(top_n)
    return indicators

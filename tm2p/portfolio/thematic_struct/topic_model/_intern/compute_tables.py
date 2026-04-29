import pandas as pd  # type: ignore

from tm2p._intern import Params
from tm2p.portfolio.thematic_struct.tfidf.matrix import Matrix as TfIdf


def compute_tables(params: Params):

    use_counters = params.use_counters

    tf_matrix = TfIdf().update(**params.__dict__).using_counters(True).run()
    params.decomposition_algorithm.fit(tf_matrix)  # type: ignore

    components_by_item = _get_components_by_theme(params, tf_matrix)

    names = _get_names(components_by_item)

    components_by_item = _sort_components_by_item(components_by_item, names)
    documents_by_theme = _get_documents_by_theme(params, tf_matrix, names)

    if use_counters is False:
        components_by_item.columns = [
            " ".join(col.split(" ")[:-1]) for col in components_by_item.columns
        ]

    return components_by_item, documents_by_theme


def _get_documents_by_theme(params, tf_matrix, names):
    documents_by_theme = pd.DataFrame(
        params.decomposition_algorithm.transform(tf_matrix),  # type: ignore
        index=tf_matrix.index,
        columns=range(params.decomposition_algorithm.n_components),  # type: ignore
    )
    documents_by_theme.columns.name = "THEME"
    documents_by_theme.index.name = "DOCUMENT"
    documents_by_theme = documents_by_theme.rename(columns=names)
    documents_by_theme = documents_by_theme.sort_index(axis=1)
    return documents_by_theme


def _sort_components_by_item(components_by_item, names):
    components_by_item = components_by_item.rename(index=names)
    components_by_item = components_by_item.sort_index(axis=0)
    return components_by_item


def _get_names(components_by_item):

    first_items = []

    for i_row in range(components_by_item.shape[0]):
        sorting_indices = components_by_item.iloc[i_row, :].sort_values(ascending=False)
        components_by_item = components_by_item[sorting_indices.index]
        first_items.append(
            (
                components_by_item.columns[0],
                components_by_item.columns[1],
                components_by_item.columns[2],
                i_row,
            )
        )

    def f(x):

        first, second, third, _ = x

        first_counters = first.split(" ")[-1]
        first_occ = first_counters.split(":")[0]
        first_gcs = first_counters.split(":")[1]

        second_counters = second.split(" ")[-1]
        second_occ = second_counters.split(":")[0]
        second_gcs = second_counters.split(":")[1]

        third_counters = third.split(" ")[-1]
        third_occ = third_counters.split(":")[0]
        third_gcs = third_counters.split(":")[1]

        return (
            first_occ,
            first_gcs,
            first,
            second_occ,
            second_gcs,
            second,
            third_occ,
            third_gcs,
            third,
        )

    first_items = sorted(first_items, key=f, reverse=True)
    names = {pos: i_row for i_row, (_, _, _, pos) in enumerate(first_items)}

    return names


def _get_components_by_theme(params, tf_matrix):

    components_by_item = pd.DataFrame(
        params.decomposition_algorithm.components_,  # type: ignore
        index=range(params.decomposition_algorithm.n_components),  # type: ignore
        columns=tf_matrix.columns,
    )

    components_by_item.columns.name = "ITEM"
    components_by_item.index.name = "COMPONENT"

    return components_by_item

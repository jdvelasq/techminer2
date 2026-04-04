"""
ClusterCenters
===============================================================================

Smoke test:
    >>> from sklearn.decomposition import PCA
    >>> pca = PCA(
    ...     n_components=5,
    ...     whiten=False,
    ...     svd_solver="auto",
    ...     tol=0.0,
    ...     iterated_power="auto",
    ...     n_oversamples=10,
    ...     power_iteration_normalizer="auto",
    ...     random_state=0,
    ... )
    >>> from tm2p import Field, ItemOrderBy
    >>> from tm2p.portfolio.thematic_structure.factorial_analysis.second_order import ClusterCenters
    >>> df = (
    ...     ClusterCenters()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.CONCEPT_NORM)
    ...     .having_items_in_top(50)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # DECOMPOSITION:
    ...     .using_decomposition_algorithm(pca)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.to_string())  # doctest: +NORMALIZE_WHITESPACE
    DIM                                   0         1         2         3         4
    fintech 616:134697            -0.243830  1.258902  2.264450  0.790662  0.619498
    finance 248:59876             -0.144920  2.084726  0.899789  0.783267  0.491208
    financial technology 99:18568  0.586608  1.279925  2.374991  2.880104  0.445145
    regulators 33:8452             0.142353  0.563703  0.758863  0.556512  1.061248


"""

from tm2p._intern import Params, ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p.enum import Field

from .item_to_cluster import ItemToCluster
from .items_by_dimension import ItemsByDimension

GCS = Field.GCS.value
OCC = "OCC"


class ClusterCenters(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = ItemsByDimension().update(**self.params.__dict__).run()
        i2c_mapping = ItemToCluster().update(**self.params.__dict__).run()

        df["CLUSTER"] = df.index.map(i2c_mapping)
        df = df.groupby("CLUSTER").mean()
        df.index = _compute_occ_and_gcs(self.params, i2c_mapping)

        return df


def _compute_occ_and_gcs(params: Params, i2c_mapping: dict):

    field = params.source_field.value

    i2c = {
        " ".join(item.split(" ")[:-1]): cluster for item, cluster in i2c_mapping.items()
    }

    df = load_filtered_main_csv_zip(params)
    df = df[[field, GCS]]
    df[OCC] = 1

    df[field] = df[field].str.split("; ")
    df = df.explode(field)  # type: ignore
    df[field] = df[field].str.strip()
    df["CLUSTER"] = df[field].map(lambda x: i2c.get(x, None))
    df = df.dropna()
    df = df.groupby("CLUSTER").agg({OCC: "sum", GCS: "sum"})

    i2n = {}
    for item, cluster in i2c_mapping.items():
        if cluster not in i2n:
            i2n[cluster] = item
        else:
            current_occ = int(i2n[cluster].split(" ")[-1].split(":")[0])
            current_gcs = int(i2n[cluster].split(" ")[-1].split(":")[1])
            item_occ = int(item.split(" ")[-1].split(":")[0])
            item_gcs = int(item.split(" ")[-1].split(":")[1])
            if item_occ > current_occ or (
                item_occ == current_occ and item_gcs > current_gcs
            ):
                i2n[cluster] = item

    i2n = {key: " ".join(value.split(" ")[:-1]) for key, value in i2n.items()}

    occ_gcs = [
        f"{i2n[int(i)]} {int(occ)}:{int(gcs)}"
        for i, occ, gcs in zip(df.index, df[OCC], df[GCS])
    ]

    return occ_gcs

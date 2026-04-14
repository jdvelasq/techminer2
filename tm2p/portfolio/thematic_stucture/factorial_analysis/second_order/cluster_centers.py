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
    >>> from tm2p.enum import Field, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.factorial_analysis.second_order import ClusterCenters
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
    ...     .using_minimum_item_co_occurrence(1)
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
    DIM                  0         1         2         3         4
    0 616:134697 -0.243830  1.258902  2.264450  0.790662  0.619498
    1 248:59876  -0.144920  2.084726  0.899789  0.783267  0.491208
    2 99:18568    0.586608  1.279925  2.374991  2.880104  0.445145
    3 33:8452     0.142353  0.563703  0.758863  0.556512  1.061248


"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field

from ..first_order.cluster_centers import _compute_occ_and_gcs
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
        i2c = ItemToCluster().update(**self.params.__dict__).run()

        df["CLUSTER"] = df.index.map(i2c)
        df = df.groupby("CLUSTER").mean()
        df.index = _compute_occ_and_gcs(self.params, i2c)

        return df

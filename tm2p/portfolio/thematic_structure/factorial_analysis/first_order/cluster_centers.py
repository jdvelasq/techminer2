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
    >>> from tm2p.enum import Field, UnitOrderBy
    >>> from tm2p.portfolio.thematic_stucture.factorial_analysis.first_order import ClusterCenters
    >>> df = (
    ...     ClusterCenters()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.CONCEPT_NORM)
    ...     .having_top_n_units(50)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # DECOMPOSITION:
    ...     .using_decomposition_algorithm(pca)
    ...     #
    ...     # TFIDF:
    ...     .using_binary_item_frequencies(False)
    ...     .using_tfidf_norm(None)
    ...     .using_tfidf_smooth_idf(False)
    ...     .using_tfidf_sublinear_tf(False)
    ...     .using_tfidf_use_idf(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.to_string())  # doctest: +NORMALIZE_WHITESPACE
    DIM                 0         1         2         3         4
    0 200:46633  0.035293  0.056406  0.001443 -0.007858  0.009859
    1 209:47043 -0.009322 -0.000832 -0.095635 -0.010942 -0.011048
    2 171:35598  0.053512 -0.014615  0.014651 -0.007385 -0.030657
    3 282:65597  0.011562 -0.027787 -0.029043 -0.004600  0.078268
    4 134:26722 -0.019021 -0.004472 -0.003820 -0.097122  0.014566


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
        i2c = ItemToCluster().update(**self.params.__dict__).run()

        df["CLUSTER"] = df.index.map(i2c)
        df = df.groupby("CLUSTER").mean()
        df.index = _compute_occ_and_gcs(self.params, i2c)

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

    occ_gcs = [
        f"{int(i)} {int(occ)}:{int(gcs)}"
        for i, occ, gcs in zip(df.index, df[OCC], df[GCS])
    ]

    return occ_gcs

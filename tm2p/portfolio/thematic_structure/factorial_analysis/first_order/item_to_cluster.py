"""
ItemToCluster
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
    >>> from tm2p.portfolio.thematic_stucture.factorial_analysis.first_order import ItemToCluster
    >>> mapping = (
    ...     ItemToCluster()
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
    >>> from pprint import pprint
    >>> pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'artificial intelligence 014:02936': 0,
     'banking 025:04625': 1,
     'banks 031:06740': 1,
     'blockchain 017:04405': 0,
     'china 033:06419': 0,
     'consumers 017:03475': 3,
    ...

"""

import numpy as np

from tm2p._intern import ParamsMixin
from tm2p.portfolio.thematic_structure.factorial_analysis.first_order.items_by_dimension import (
    ItemsByDimension,
)

THRESHOLD = 0.5


class ItemToCluster(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        embedding = ItemsByDimension().update(**self.params.__dict__).run()
        abs_embedding = np.abs(embedding)
        factor_assignment = abs_embedding.values.argmax(axis=1)  # type: ignore
        factor_assignment = [int(x) for x in factor_assignment]
        i2c = dict(zip(embedding.index, factor_assignment))

        clusters = {}
        for item, cluster in i2c.items():
            clusters.setdefault(cluster, []).append(item)

        values = list(clusters.values())

        def f(x):
            return (
                len(x),
                x[0].split(" ")[-1].split(":")[0],
                x[0].split(" ")[-1].split(":")[1],
                x[0],
            )

        sorted_values = sorted(values, key=f, reverse=True)
        i2c = {}
        for cluster, items in enumerate(sorted_values):
            for item in items:
                i2c[item] = cluster

        return i2c

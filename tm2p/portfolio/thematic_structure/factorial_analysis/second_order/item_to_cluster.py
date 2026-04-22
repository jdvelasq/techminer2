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
    >>> from tm2p.portfolio.thematic_stucture.factorial_analysis.second_order import ItemToCluster
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
    ...     .using_minimum_pair_co_occurrence(1)
    ...     #
    ...     # DECOMPOSITION:
    ...     .using_decomposition_algorithm(pca)
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
    {'artificial intelligence 014:02936': 1,
     'banking 025:04625': 0,
     'banks 031:06740': 0,
     'blockchain 017:04405': 1,
     'china 033:06419': 0,
     'consumers 017:03475': 0,
     'countries 010:02793': 0,
     'covid-19 012:02097': 0,
     'cryptocurrencies 010:04061': 1,
     'customers 013:02933': 0,
    ...

"""

import numpy as np

from tm2p._intern import ParamsMixin
from tm2p.portfolio.thematic_structure.factorial_analysis.second_order.items_by_dimension import (
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
        mapping = dict(zip(embedding.index, factor_assignment))

        clusters = {}
        for item, cluster in mapping.items():
            clusters.setdefault(cluster, []).append(item)

        values = list(clusters.values())

        def f(x):
            return (
                len(x),
                x[0].split(" ")[-1].split(":")[0],
                x[0].split(" ")[-1].split(":")[1],
            )

        sorted_values = sorted(values, key=f, reverse=True)
        mapping = {}
        for cluster, items in enumerate(sorted_values):
            for item in items:
                mapping[item] = cluster

        return mapping

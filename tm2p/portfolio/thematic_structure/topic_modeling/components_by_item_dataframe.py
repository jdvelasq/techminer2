"""
Components by Term Frame
===============================================================================

Smoke tests:
    >>> from sklearn.decomposition import LatentDirichletAllocation
    >>> lda = LatentDirichletAllocation(
    ...     n_components=10,
    ...     learning_decay=0.7,
    ...     learning_offset=50.0,
    ...     max_iter=10,
    ...     batch_size=128,
    ...     evaluate_every=-1,
    ...     perp_tol=0.1,
    ...     mean_change_tol=0.001,
    ...     max_doc_update_iter=100,
    ...     random_state=0,
    ... )
    >>> from tm2p.enum import ItemOrderBy, Field
    >>> from tm2p.portfolio.thematic_structure.topic_modeling import ComponentsByItemDataFrame
    >>> df = (
    ...     ComponentsByItemDataFrame()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.CONCEPT_NORM)
    ...     .having_items_in_top(50)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DECOMPOSITION:
    ...     .using_decomposition_algorithm(lda)
    ...     .using_top_items_by_theme(5)
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
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df
    term       fintech 157:34856  ...  the emergence 010:01933
    component                     ...
    0                  21.047484  ...                 0.100005
    1                  38.575909  ...                 3.099910
    2                  14.623242  ...                 0.100000
    3                  10.610498  ...                 0.100000
    4                   4.579642  ...                 0.100022
    5                  15.809338  ...                 0.100012
    6                  18.323350  ...                 4.100031
    7                  15.558222  ...                 0.100000
    8                  10.942926  ...                 1.099976
    9                   7.929388  ...                 2.100044
    <BLANKLINE>
    [10 rows x 50 columns]


"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p.portfolio.thematic_structure.tfidf.matrix import Matrix as TfIdf


class ComponentsByItemDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        tf_matrix = TfIdf().update(**self.params.__dict__).run()

        self.params.decomposition_algorithm.fit(tf_matrix)  # type: ignore

        frame = pd.DataFrame(
            self.params.decomposition_algorithm.components_,  # type: ignore
            index=range(self.params.decomposition_algorithm.n_components),  # type: ignore
            columns=tf_matrix.columns,
        )

        frame.columns.name = "term"
        frame.index.name = "component"

        return frame

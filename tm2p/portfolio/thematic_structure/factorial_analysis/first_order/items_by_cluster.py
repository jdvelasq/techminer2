"""
ItemsByCluster
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
    >>> from tm2p.papers.thematic.first_order_factors import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
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
    >>> print(df.to_string())  # doctest: +NORMALIZE_WHITESPACE
                                        0                                          1                                  2                                 3                                 4
    0                     china 033:06419                            banks 031:06740                  finance 050:10972                 fintech 157:34856    financial technology 052:09484
    1                the impact 021:04968                             data 026:05921               technology 026:04985              innovation 033:07734     financial inclusion 022:04623
    2                  evidence 018:03900                  the development 026:05689  sustainable development 018:02898      financial services 031:07105                the role 015:02528
    3                blockchain 017:04405                          banking 025:04625        fintech companies 014:03279               consumers 017:03475            policymakers 013:01987
    4       fintech development 015:03625                        customers 013:02933           sustainability 014:02486         economic growth 012:01976  financial institutions 012:02923
    5                  research 014:03510                         services 012:03614                  the use 013:03451  the financial industry 011:04250    the financial sector 010:03244
    6   artificial intelligence 014:02936                       regulators 012:02416         fintech services 013:02241  information technology 011:03183           the emergence 010:01933
    7             green finance 013:03038                         covid-19 012:02097                    users 012:02989           practitioners 010:03018
    8                the effect 012:02564  the financial services industry 011:03454                the world 011:02297
    9                     firms 012:01979                   the challenges 011:01924
    10         the relationship 011:02148                        countries 010:02793
    11         cryptocurrencies 010:04061                      innovations 010:02582
    12              investments 010:03080                    the potential 010:02255


"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin

from .item_to_cluster import ItemToCluster


class ItemsByCluster(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        mapping = ItemToCluster().update(**self.params.__dict__).run()

        s = pd.Series(mapping)
        df = pd.DataFrame(
            {k: pd.Series(v.tolist()) for k, v in s.groupby(s).groups.items()}
        )

        return df.fillna("")

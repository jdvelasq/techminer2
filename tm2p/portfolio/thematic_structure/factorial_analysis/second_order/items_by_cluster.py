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
    >>> from tm2p.papers.thematic.second_order_factors import ItemsByCluster
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
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.to_string())  # doctest: +NORMALIZE_WHITESPACE
                                       0                                  1                               2                                          3
    0                  fintech 157:34856                  finance 050:10972  financial technology 052:09484                       regulators 012:02416
    1                    china 033:06419               innovation 033:07734   financial inclusion 022:04623  the financial services industry 011:03454
    2       financial services 031:07105               technology 026:04985              the role 015:02528                      innovations 010:02582
    3                    banks 031:06740  sustainable development 018:02898         the emergence 010:01933
    4                     data 026:05921               blockchain 017:04405
    5          the development 026:05689                 research 014:03510
    6                  banking 025:04625  artificial intelligence 014:02936
    7               the impact 021:04968           sustainability 014:02486
    8                 evidence 018:03900   the financial industry 011:04250
    9                consumers 017:03475                the world 011:02297
    10     fintech development 015:03625         cryptocurrencies 010:04061
    11       fintech companies 014:03279     the financial sector 010:03244
    12                 the use 013:03451              investments 010:03080
    13           green finance 013:03038            practitioners 010:03018
    14               customers 013:02933
    15        fintech services 013:02241
    16            policymakers 013:01987
    17                services 012:03614
    18                   users 012:02989
    19  financial institutions 012:02923
    20              the effect 012:02564
    21                covid-19 012:02097
    22                   firms 012:01979
    23         economic growth 012:01976
    24  information technology 011:03183
    25        the relationship 011:02148
    26          the challenges 011:01924
    27               countries 010:02793
    28           the potential 010:02255


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

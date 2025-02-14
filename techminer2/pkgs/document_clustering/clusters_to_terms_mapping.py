# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Clusters to Terms Mapping
===============================================================================


>>> from sklearn.cluster import KMeans
>>> kmeans = KMeans(
...     n_clusters=4,
...     init="k-means++",
...     n_init=10,
...     max_iter=300,
...     tol=0.0001,
...     algorithm="lloyd",
...     random_state=0,
... )
>>> from techminer2.pkgs.document_clustering import ClustersToTermsMapping
>>> mapping = (
...     ClustersToTermsMapping()
...     #
...     # FIELD:
...     .with_field("descriptors")
...     .having_terms_in_top(50)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # COUNTERS:
...     .using_term_counters(True)
...     #
...     # TFIDF:
...     .using_binary_term_frequencies(False)
...     .using_row_normalization(None)
...     .using_idf_reweighting(False)
...     .using_idf_weights_smoothing(False)
...     .using_sublinear_tf_scaling(False)
...     #
...     # CLUSTERING:
...     .using_clustering_estimator_or_dict(kmeans)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... )
>>> import pprint
>>> pprint.pprint(mapping)
{0: ['THIS_PAPER 14:2240',
     'BANKS 09:1133',
     'THE_FINANCIAL_SERVICES_INDUSTRY 06:1237',
     'CONSUMERS 06:0804',
     'ENTREPRENEURS 04:0744',
     'INVESTMENT 04:0581',
     'THE_POTENTIAL 04:0547'],
 1: ['FINTECH 46:7183',
     'FINANCE 21:3481',
     'FINANCIAL_TECHNOLOGY 17:2359',
     'THIS_STUDY 14:1737',
     'INNOVATION 13:2394',
     'TECHNOLOGY 13:1594',
     'FINANCIAL_SERVICES 11:1862',
     'THE_FINANCIAL_INDUSTRY 09:2006',
     'SERVICES 09:1527',
     'REGULATORS 08:0974',
     'DATA 07:1086',
     'THE_DEVELOPMENT 07:1073',
     'BANKING 07:0851',
     'THIS_ARTICLE 06:1360',
     'THE_FIELD 06:1031',
     'CHINA 06:0673',
     'THE_FINANCIAL_SECTOR 05:1147',
     'THE_IMPACT 05:0787',
     'VALUE 05:0612',
     'BUSINESS_MODELS 04:1441',
     'BLOCKCHAIN 04:1116',
     'TRADING 04:1050',
     'FINANCIAL_SERVICE 04:1036',
     'INFORMATION_TECHNOLOGY 04:0995',
     'THE_USE 04:0953',
     'PRACTITIONERS 04:0832',
     'FINTECH_COMPANIES 04:0758',
     'THE_AUTHOR 04:0735',
     'FINANCIAL_INSTITUTIONS 04:0722',
     'ELSEVIER_B_._V 04:0718',
     'USERS 04:0687',
     'THE_EMERGENCE 04:0664',
     'CUSTOMERS 04:0599',
     'ALL_RIGHTS_RESERVED 04:0586',
     'SURVEYS 04:0580',
     'INNOVATIONS 04:0518'],
 2: ['THE_PURPOSE 06:1046',
     'DESIGN_METHODOLOGY_APPROACH 04:0555',
     'EMERALD_PUBLISHING_LIMITED 04:0555',
     'ORIGINALITY_VALUE 04:0555',
     'THIS_RESEARCH 04:0540'],
 3: ['THE_RESEARCH 05:0839', 'INFORMATION_SYSTEMS 04:0830']}


"""
from ...internals.mixins import ParamsMixin
from .term_occurrence_by_cluster import TermOccurrenceByCluster


class ClustersToTermsMapping(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        contingency_table = (
            TermOccurrenceByCluster().update_params(**self.params.__dict__).build()
        )

        themes = contingency_table.idxmax(axis=1)

        mapping = {}
        for word, theme in zip(themes.index, themes):
            if theme not in mapping:
                mapping[theme] = []
            mapping[theme].append(word)

        return mapping

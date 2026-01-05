# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Clusters to Terms Mapping
===============================================================================


Example:
    >>> from techminer2.packages.networks.co_authorship.countries import ClustersToTermsMapping
    >>> mapping = (
    ...     ClustersToTermsMapping()
    ...     #
    ...     # FIELD:
    ...     .having_terms_in_top(20)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(True)
    ...     #
    ...     # NETWORK:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     .using_association_index("association")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping)
    {0: ['United States 16:3189',
         'China 08:1085',
         'South Korea 06:1192',
         'Sweden 01:0160',
         'Kazakhstan 01:0121',
         'Belgium 01:0101'],
     1: ['Germany 07:1814',
         'Netherlands 03:0300',
         'Denmark 02:0330',
         'Singapore 01:0576',
         'France 01:0258'],
     2: ['Australia 05:0783', 'United Kingdom 03:0636', 'Hong Kong 01:0178'],
     3: ['Switzerland 04:0660'],
     4: ['Latvia 02:0163'],
     5: ['Spain 01:0225'],
     6: ['Indonesia 01:0102'],
     7: ['Slovenia 01:0102'],
     8: ['Brunei Darussalam 01:0090']}


"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.packages.networks.co_occurrence.user.clusters_to_terms_mapping import (
    ClustersToTermsMapping as UserClustersToTermsMapping,
)


class ClustersToTermsMapping(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserClustersToTermsMapping()
            .update(**self.params.__dict__)
            .with_field("countries")
            .run()
        )

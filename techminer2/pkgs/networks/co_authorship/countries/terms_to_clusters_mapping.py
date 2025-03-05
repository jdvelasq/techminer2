# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms to Cluster Mapping
===============================================================================


>>> from techminer2.pkgs.networks.co_authorship.countries import TermsToClustersMapping
>>> mapping = (
...     TermsToClustersMapping()
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
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_range_is(None, None)
...     .where_record_citations_range_is(None, None)
...     .where_records_match(None)
...     #
...     .run()
... )
>>> from pprint import pprint
>>> pprint(mapping)
{'Australia 05:0783': 2,
 'Belgium 01:0101': 0,
 'Brunei Darussalam 01:0090': 8,
 'China 08:1085': 0,
 'Denmark 02:0330': 1,
 'France 01:0258': 1,
 'Germany 07:1814': 1,
 'Hong Kong 01:0178': 2,
 'Indonesia 01:0102': 6,
 'Kazakhstan 01:0121': 0,
 'Latvia 02:0163': 4,
 'Netherlands 03:0300': 1,
 'Singapore 01:0576': 1,
 'Slovenia 01:0102': 7,
 'South Korea 06:1192': 0,
 'Spain 01:0225': 5,
 'Sweden 01:0160': 0,
 'Switzerland 04:0660': 3,
 'United Kingdom 03:0636': 2,
 'United States 16:3189': 0}

 
>>> mapping = (
...     TermsToClustersMapping()
...     #
...     # FIELD:
...     .having_terms_in_top(20)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # COUNTERS:
...     .using_term_counters(False)
...     #
...     # NETWORK:
...     .using_clustering_algorithm_or_dict("louvain")
...     .using_association_index("association")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_range_is(None, None)
...     .where_record_citations_range_is(None, None)
...     .where_records_match(None)
...     #
...     .run()
... )
>>> from pprint import pprint
>>> pprint(mapping)
{'Australia': 2,
 'Belgium': 0,
 'Brunei Darussalam': 8,
 'China': 0,
 'Denmark': 1,
 'France': 1,
 'Germany': 1,
 'Hong Kong': 2,
 'Indonesia': 6,
 'Kazakhstan': 0,
 'Latvia': 4,
 'Netherlands': 1,
 'Singapore': 1,
 'Slovenia': 7,
 'South Korea': 0,
 'Spain': 5,
 'Sweden': 0,
 'Switzerland': 3,
 'United Kingdom': 2,
 'United States': 0}


"""
from ....._internals.mixins import ParamsMixin
from ...co_occurrence.user.terms_to_clusters_mapping import (
    TermsToClustersMapping as UserTermsToClusterMapping,
)


class TermsToClustersMapping(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserTermsToClusterMapping()
            .update(**self.params.__dict__)
            .with_field("countries")
            .run()
        )

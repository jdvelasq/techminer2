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

>>> # where_records_ordered_by: date_newest, date_oldest, global_cited_by_highest, 
>>> #                           global_cited_by_lowest, local_cited_by_highest, 
>>> #                           local_cited_by_lowest, first_author_a_to_z, 
>>> #                           first_author_z_to_a, source_title_a_to_z, 
>>> #                           source_title_z_to_a
>>> from techminer2.pkgs.networks.co_occurrence.keywords import DocumentsByClusterMapping
>>> documents_by_cluster = (
...     DocumentsByClusterMapping()
...     #
...     # FIELD:
...     .having_terms_in_top(20)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
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
...     .where_records_ordered_by("date_newest")
...     #
...     .run()
... )
>>> print(len(documents_by_cluster))

>>> print(documents_by_cluster[0][0])





"""
from ....._internals.mixins import ParamsMixin
from ..user.documents_by_cluster_mapping import (
    DocumentsByClusterMapping as UserDocumentsByClusterMapping,
)


class DocumentsByClusterMapping(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserDocumentsByClusterMapping()
            .update(**self.params.__dict__)
            .with_field("keywords")
            .run()
        )

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms by Cluster Frame
===============================================================================

>>> from techminer2.pkgs.networks.citation.authors import TermsByClusterDataFrame
>>> (
...     TermsByClusterDataFrame()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(30)
...     .having_citation_threshold(0)
...     .having_occurrence_threshold(2)
...     .having_terms_in(None)
...     #
...     # CLUSTERING:
...     .using_clustering_algorithm_or_dict("louvain")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... ).head()
                      0                    1                   2
0      Gomber P. 2:1065     Haddad C. 1:0258  Jagtiani J. 3:0317
1     Koch J.-A. 1:0489  Puschmann T. 1:0253   Lemieux C. 2:0253
2     Siering M. 1:0489     Hornuf L. 2:0358                    
3  Kauffman R.J. 1:0576                                         
4      Parker C. 1:0576                                         


"""
from ....._internals.mixins import ParamsMixin
from .._internals.from_others.terms_by_cluster_data_frame import (
    TermsByClusterDataFrame as OtherTermsByClusterDataFrame,
)


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            OtherTermsByClusterDataFrame()
            .update(**self.params.__dict__)
            .unit_of_analysis("authors")
            .build()
        )

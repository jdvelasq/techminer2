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


>>> from techminer2.pkgs.networks.co_authorship.authors import TermsByClusterDataFrame
>>> (
...     TermsByClusterDataFrame()
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
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... )
                      0              1  ...                 5                 6
0      Gomber P. 2:1065  Gai K. 2:0323  ...     Lee I. 1:0557  Hornuf L. 2:0358
1  Kauffman R.J. 1:0576  Qiu M. 2:0323  ...  Shin Y.J. 1:0557                  
2      Parker C. 1:0576  Sun X. 2:0323  ...                                    
3     Weber B.W. 1:0576                 ...                                    
4     Koch J.-A. 1:0489                 ...                                    
5     Siering M. 1:0489                 ...                                    
<BLANKLINE>
[6 rows x 7 columns]


"""
from .....internals.mixins import ParamsMixin
from ...co_occurrence.user.terms_by_cluster_data_frame import (
    TermsByClusterDataFrame as UserTermsByClusterDataFrame,
)


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        return (
            UserTermsByClusterDataFrame()
            .update_params(**self.params.__dict__)
            .with_field("authors")
            .build()
        )

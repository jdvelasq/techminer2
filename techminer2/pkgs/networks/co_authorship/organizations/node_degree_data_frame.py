# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Node Degree Frame
===============================================================================

>>> from techminer2.pkgs.networks.co_authorship.organizations import NodeDegreeDataFrame
>>> (
...     NodeDegreeDataFrame()
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
... ).head()



"""
from .....internals.mixins import InputFunctionsMixin
from ...co_occurrence.user.node_degree_data_frame import (
    NodeDegreeDataFrame as UserNodeDegreeDataFrame,
)


class NodeDegreeDataFrame(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        return (
            UserNodeDegreeDataFrame()
            .update_params(**self.params.__dict__)
            .with_field("organizations")
            .build()
        )

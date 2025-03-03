# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Treemap
===============================================================================

>>> from techminer2.pkgs.networks.co_occurrence.descriptors import Treemap
>>> plot = (
...     Treemap()
...     #
...     # FIELD:
...     .with_field("descriptors")
...     .having_terms_in_top(20)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # NETWORK:
...     .using_association_index("association")
...     #
...     # PLOT:
...     .using_title_text(None)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_range_is(None, None)
...     .where_record_citattions_range_is(None, None)
...     .where_records_match(None)
...     #
...     .build()
... )
>>> plot.write_html("sphinx/_generated/pkgs/networks/co_occurrence/descriptors/treemap.html")

.. raw:: html

    <iframe src="../../_generated/pkgs/networks/co_occurrence/descriptors/treemap.html" 
    height="800px" width="100%" frameBorder="0"></iframe>

"""
from ....._internals.mixins import ParamsMixin
from ..user.treemap import Treemap as UserTreemap


class Treemap(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        return (
            UserTreemap()
            .update(**self.params.__dict__)
            .with_field("descriptors")
            .build()
        )

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

>>> from techminer2.packages.networks.co_authorship.countries import Treemap
>>> plot = (
...     Treemap()
...     #
...     # FIELD:
...     .with_field("countries")
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
...     .where_record_citations_range_is(None, None)
...     .where_records_match(None)
...     #
...     .run()
... )
>>> plot.write_html("docs_source/_generated/px.packages.networks.co_authorship.countries.treemap.html")

.. raw:: html

    <iframe src="../_generated/px.packages.networks.co_authorship.countries.treemap.html"
    height="800px" width="100%" frameBorder="0"></iframe>

"""
from ....._internals.mixins import ParamsMixin
from ...co_occurrence.user.treemap import Treemap as UserTreemap


class Treemap(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserTreemap().update(**self.params.__dict__).with_field("countries").run()
        )

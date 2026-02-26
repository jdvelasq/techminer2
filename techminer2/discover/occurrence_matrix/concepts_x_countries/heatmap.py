"""
Heatmap
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.discover.occurrence_matrix.concepts_x_countries.heatmap.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from techminer2 import CorpusField, ItemsOrderBy
    >>> from techminer2.discover.occurrence_matrix.concepts_x_countries import Heatmap
    >>> fig = (
    ...     Heatmap()
    ...     #
    ...     # COLUMNS:
    ...     .having_column_items_in_top(10)
    ...     .having_column_items_ordered_by(ItemsOrderBy.OCC)
    ...     .having_column_item_occurrences_between(None, None)
    ...     .having_column_item_citations_between(None, None)
    ...     .having_column_items_in(None)
    ...     #
    ...     # ROWS:
    ...     .having_index_items_in_top(15)
    ...     .having_index_items_ordered_by(ItemsOrderBy.OCC)
    ...     .having_index_item_occurrences_between(0, None)
    ...     .having_index_item_citations_between(None, None)
    ...     .having_index_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_item_counters(True)
    ...     #
    ...     # PLOT:
    ...     .using_title_text(None)
    ...     .using_colormap("Blues")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> type(fig).__name__
    'Figure'
    >>> fig.write_html("docsrc/_generated/px.discover.occurrence_matrix.concepts_x_countries.heatmap.html")


"""

from techminer2 import CorpusField
from techminer2._internals import ParamsMixin

from .._internals import Heatmap as BaseHeatmap


class Heatmap(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return (
            BaseHeatmap()
            .with_params(self.params)
            .with_column_field(CorpusField.CONCEPT_NORM)
            .with_index_field(CorpusField.COUNTRY)
            .run()
        )

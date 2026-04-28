"""
Heatmap
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.thematic_struct.co_occur.first_order_network.heatmap.html"
    height="600px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, Field, UnitOrderBy
    >>> from tm2p.portfolio.thematic_struct.co_occur.direct_similarity_network import Heatmap
    >>> fig = (
    ...     Heatmap()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_top_n_units(10)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION)
    ...     #
    ...     # PLOT:
    ...     .using_title_text(None)
    ...     .using_colormap("Blues")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert type(fig).__name__ == 'Figure'    >>> fig.write_html("docsrc/_generated/px.portfolio.thematic_struct.co_occur.first_order_network.heatmap.html")




"""

from tm2p._intern import ParamsMixin
from tm2p._intern.plots.basic.heatmap import heatmap

from ..dir_simil_netw.dir_matrix import DirectMatrix


class Heatmap(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        data_frame = DirectMatrix().update(**self.params.__dict__).run()
        fig = heatmap(self.params, data_frame)
        return fig

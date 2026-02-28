"""
Concept Grid Plot
===============================================================================


## >>> from tm2p.co_occurrence_network.keywords import ConceptGridPlot
## >>> plot = (
## ...     ConceptGridPlot()
## ...     #
## ...     # FIELD:
## ...     .having_items_in_top(30)
## ...     .having_items_ordered_by("OCC")
## ...     .having_item_occurrences_between(None, None)
## ...     .having_item_citations_between(None, None)
## ...     .having_items_in(None)
## ...     #
## ...     # COUNTERS:
## ...     .using_term_counters(True)
## ...     #
## ...     # NETWORK:
## ...     .using_clustering_algorithm_or_dict("louvain")
## ...     .using_association_index("association")
## ...     #
## ...     # DATABASE:
## ...     .where_root_directory("tests/fintech/")
## ...     .where_database("main")
## ...     .where_record_years_range(None, None)
## ...     .where_record_citations_range(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .run()
## ... )
## >>> plot.render("sphinx/images/co_occurrence_network/concept_grid_plot", format="png")


# .. image:: /images/co_occurrence_network/concept_grid_plot.png
#     :width: 900px
#     :align: center

"""

from tm2p._intern import ParamsMixin
from tm2p.synthes.concept_struct.co_occur.usr.concept_grid_plot import (
    ConceptGridPlot as UserConceptGridPlot,
)


class ConceptGridPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserConceptGridPlot()
            .update(**self.params.__dict__)
            .with_source_field("author_keywords")
            .run()
        )

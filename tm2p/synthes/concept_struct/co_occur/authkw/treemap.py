"""
Treemap
===============================================================================



Smoke tests:
    >>> #
    >>> # TEST PREPARATION
    >>> #
    >>> from tm2p.refine.thesaurus_old.descriptors import ApplyThesaurus, InitializeThesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()
    >>> ApplyThesaurus(root_directory="examples/fintech/", quiet=True).run()


    >>> #
    >>> # CODE TESTED
    >>> #
    >>> from tm2p.co_occurrence_network.author_keywords import Treemap
    >>> plot = (
    ...     Treemap()
    ...     #
    ...     # FIELD:
    ...     .with_field("author_keywords")
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index("association")
    ...     #
    ...     # PLOT:
    ...     .using_title_text(None)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docsrc/_generated/px.packages.networks.co_occurrence.author_keywords.treemap.html")

.. raw:: html

    <iframe src="../_generated/px.packages.networks.co_occurrence.author_keywords.treemap.html"
    height="800px" width="100%" frameBorder="0"></iframe>


"""

from tm2p._internals import ParamsMixin
from tm2p.synthes.concept_struct.co_occur.usr.treemap import Treemap as UserTreemap


class Treemap(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserTreemap()
            .update(**self.params.__dict__)
            .with_source_field("author_keywords")
            .run()
        )

"""
StemMatch
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.match import StemMatch
    >>> (
    ...     StemMatch()
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import AnalysisUnit, Field, ThFile, UnitOrderBy
from tm2p.refine._intern.match import BaseStemMatch


class StemMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:
        """:meta private:"""

        return (
            BaseStemMatch()
            .update(**self.params.__dict__)
            #
            .with_thesaurus_file(ThFile.CONCEPT)
            .with_source_field(Field.DESCRIPTOR_NORM)
            .with_analysis_unit(AnalysisUnit.DESCRIPTOR)
            #
            .having_top_n_units(None)
            .having_units_ordered_by(UnitOrderBy.OCC)
            .having_unit_occurrence_between(None, None)
            .having_unit_global_citation_between(None, None)
            .having_units_in(None)
            #
            .where_record_years_range(None, None)
            .where_record_global_citations_range(None, None)
            .where_records_match(None)
            #
            .run()
        )


if __name__ == "__main__":

    StemMatch().where_root_directory("./").run()

"""
FuzzyZeroExactMatch
===============================================================================

Smoke test:
    >>> from tm2p.refine.concept.match import FuzzyZeroExactMatch
    >>> (
    ...     FuzzyZeroExactMatch()
    ...     .using_similarity_cutoff(90)
    ...     .using_fuzzy_threshold(0)
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import AnalysisUnit, Field, ThFile
from tm2p.refine._intern.match import BaseFuzzyZeroExactMatch


class FuzzyZeroExactMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:
        """:meta private:"""

        return (
            BaseFuzzyZeroExactMatch()
            .update(**self.params.__dict__)
            #
            .with_thesaurus_file(ThFile.CONCEPT)
            .with_source_field(Field.DESCRIPTOR_NORM)
            .with_analysis_unit(AnalysisUnit.DESCRIPTOR)
            #
            .where_record_years_range(None, None)
            .where_record_global_citations_range(None, None)
            .where_records_match(None)
            #
            .run()
        )


if __name__ == "__main__":

    FuzzyZeroExactMatch().where_root_directory("./").run()

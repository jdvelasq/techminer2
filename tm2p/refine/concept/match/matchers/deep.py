"""
DeepMatch
===============================================================================

Smoke test:
    >>> from tm2p.refine.concept.match import FuzzyOneExactMatch
    >>> (
    ...     FuzzyOneExactMatch()
    ...     .using_similarity_cutoff(88)
    ...     .using_fuzzy_threshold(80)
    ...     .where_root_directory("tests/regtech-scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import AnalysisUnit, Field, ThFile
from tm2p.refine._intern.match import BaseSharedWordsMatch


class DeepMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:
        """:meta private:"""

        return (
            BaseSharedWordsMatch()
            .update(**self.params.__dict__)
            #
            .with_thesaurus_file(ThFile.CONCEPT)
            .with_source_field(Field.CONCEPT_NORM)
            .with_analysis_unit(AnalysisUnit.CONCEPT)
            #
            .where_record_years_range(None, None)
            .where_record_global_citations_range(None, None)
            .where_records_match(None)
            #
            .run()
        )


if __name__ == "__main__":

    core_area = input("Core Area > ").strip().lower()
    print()
    BaseSharedWordsMatch().where_root_directory("./").with_core_area(
        core_area
    ).with_thesaurus_file(ThFile.CONCEPT).with_analysis_unit(AnalysisUnit.CONCEPT).run()

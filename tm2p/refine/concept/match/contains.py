"""
ContainsMatch
===============================================================================

Smoke test:
    >>> from tm2p.refine.concept.match import ContainsMatch
    >>> (
    ...     ContainsMatch()
    ...     .having_text_matching("firm")
    ...     .using_similarity_cutoff(88)
    ...     .using_fuzzy_threshold(80)
    ...     .where_root_directory("tests/regtech-scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import AnalysisUnit, ThFile
from tm2p.refine._intern.match import BaseContainsMatch


class ContainsMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:
        """:meta private:"""

        return (
            BaseContainsMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CONCEPT)
            .with_analysis_unit(AnalysisUnit.DESCRIPTOR)
            .run()
        )

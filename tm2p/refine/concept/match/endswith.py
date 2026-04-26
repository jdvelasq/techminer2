"""
EndsWithMatch
===============================================================================

Smoke test:
    >>> from tm2p.refine.concept.match import EndsWithMatch
    >>> (
    ...     EndsWithMatch()
    ...     .having_text_matching("ion")
    ...     .using_similarity_cutoff(88)
    ...     .using_fuzzy_threshold(80)
    ...     .where_root_directory("tests/regtech-scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import AnalysisUnit, ThFile
from tm2p.refine._intern.match import BaseEndsWithMatch


class EndsWithMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:
        """:meta private:"""

        return (
            BaseEndsWithMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CONCEPT)
            .with_analysis_unit(AnalysisUnit.DESCRIPTOR)
            .run()
        )

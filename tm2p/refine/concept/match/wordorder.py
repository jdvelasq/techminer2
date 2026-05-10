"""
WordOrderMatch
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.match import WordOrderMatch
    >>> (
    ...     WordOrderMatch()
    ...     .where_root_directory("tests/regtech-scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import AnalysisUnit, ThFile
from tm2p.refine._intern.match import BaseWordOrderMatch


class WordOrderMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:
        """:meta private:"""

        return (
            BaseWordOrderMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CONCEPT)
            .with_analysis_unit(AnalysisUnit.CONCEPT)
            .run()
        )

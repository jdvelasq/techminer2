"""
SeparatorMatch
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.match import SeparatorMatch
    >>> (
    ...     SeparatorMatch()
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import AnalysisUnit, ThFile
from tm2p.refine._intern.match import BaseSeparatorMatch


class SeparatorMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:
        """:meta private:"""

        return (
            BaseSeparatorMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CONCEPT)
            .with_analysis_unit(AnalysisUnit.CONCEPT)
            .run()
        )

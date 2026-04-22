"""
ExpressionMatch
===============================================================================

Smoke test:
    >>> from tm2p.refine.concept.match import ExpressionMatch
    >>> (
    ...     ExpressionMatch()
    ...     .having_text_matching("firm")
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import AnalysisUnit, Field, ThFile
from tm2p.refine._intern.match import BaseExpressionMatch


class ExpressionMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:
        """:meta private:"""

        return (
            BaseExpressionMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CONCEPT)
            .with_source_field(Field.DESCRIPTOR_NORM)
            .with_analysis_unit(AnalysisUnit.DESCRIPTOR)
            .run()
        )


if __name__ == "__main__":

    print()
    pattern = input("Enter a pattern to match > ")
    ExpressionMatch().having_text_matching(pattern).where_root_directory("./").run()
    print()

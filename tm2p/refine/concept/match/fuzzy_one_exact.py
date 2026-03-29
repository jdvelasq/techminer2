"""
FuzzyOneExactMatch
===============================================================================

Smoke test:
    >>> from tm2p.refine.concept.match import FuzzyOneExactMatch
    >>> (
    ...     FuzzyOneExactMatch()
    ...     .using_similarity_cutoff(88)
    ...     .using_fuzzy_threshold(80)
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field, ThFile
from tm2p.refine._intern.match import BaseFuzzyOneExactMatch


class FuzzyOneExactMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:
        """:meta private:"""

        return (
            BaseFuzzyOneExactMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CONCEPT)
            .with_source_field(Field.DESCRIPTOR_NORM)
            .run()
        )

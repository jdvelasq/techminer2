"""
FuzzyZeroExactMatch
===============================================================================

Smoke test:
    >>> from tm2p.refine.org.match import FuzzyZeroExactMatch
    >>> (
    ...     FuzzyZeroExactMatch()
    ...     .using_similarity_cutoff(90)
    ...     .using_fuzzy_threshold(0)
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... ) # doctest: +SKIP

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field, ThFile
from tm2p.refine._intern.match import BaseFuzzyZeroExactMatch


class FuzzyZeroExactMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseFuzzyZeroExactMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.ORG)
            .with_source_field(Field.ORG)
            .run()
        )

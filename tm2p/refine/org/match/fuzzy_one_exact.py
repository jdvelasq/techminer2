"""
FuzzyOneExactMatch
===============================================================================

Smoke test:
    >>> from tm2p.refine.organization.match import FuzzyOneExactMatch
    >>> (
    ...     FuzzyOneExactMatch()
    ...     .using_similarity_cutoff(88)
    ...     .using_fuzzy_threshold(80)
    ...     .where_root_directory("tests/tinyml-scopus/")
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

    def run(self):
        """:meta private:"""

        return (
            BaseFuzzyOneExactMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.ORG)
            .with_source_field(Field.ORG)
            .run()
        )

"""
EndsWithMatch
===============================================================================

Smoke test:
    >>> from tm2p.refine.country.match import EndsWithMatch
    >>> (
    ...     EndsWithMatch()
    ...     .having_text_matching("ion")
    ...     .using_similarity_cutoff(88)
    ...     .using_fuzzy_threshold(80)
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p._intern.enum import Field, ThFile
from tm2p.refine._intern.match import BaseEndsWithMatch


class EndsWithMatch(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseEndsWithMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CTRY)
            .with_source_field(Field.CTRY)
            .run()
        )

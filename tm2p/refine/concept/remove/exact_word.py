"""
ExactWord
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.replace import ExactWord
    >>> (
    ...     ExactWord()
    ...     .having_word("business")
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

    >>> from tm2p.refine.concept.reset import Reset
    >>> (
    ...     Reset()
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p._intern.enum import ThFile
from tm2p.refine._intern.remove import BaseExactWord


class ExactWord(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseExactWord()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CONCEPT)
            .run()
        )

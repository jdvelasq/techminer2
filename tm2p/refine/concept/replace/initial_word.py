"""
InitialWord
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.replace import InitialWord
    >>> (
    ...     InitialWord()
    ...     .having_word("business")
    ...     .having_replacement("BUSINESS")
    ...     .where_root_directory("examples/scopus/")
    ...     .run()
    ... )

    >>> from tm2p.refine.concept.reset import Reset
    >>> (
    ...     Reset()
    ...     .where_root_directory("examples/scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import ThFile
from tm2p.refine._intern.replace import BaseFirstWord


class InitialWord(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseFirstWord()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CONCEPT)
            .run()
        )

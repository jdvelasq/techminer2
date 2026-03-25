"""
RemoveInitialWord
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.replace import RemoveInitialWord
    >>> (
    ...     RemoveInitialWord()
    ...     .having_word("business")
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

    >>> from tm2p.refine.concept.reset import Reset
    >>> (
    ...     ReplaceInitialWord()
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import ThFile
from tm2p.refine._intern.remove import BaseRemoveInitialWord


class RemoveInitialWord(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseRemoveInitialWord()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CONCEPT)
            .run()
        )

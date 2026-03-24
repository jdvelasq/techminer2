"""
ReplaceWord
===============================================================================


Smoke tests:
    >>> from tm2p.refine.org.replace import ReplaceWord
    >>> (
    ...     ReplaceWord()
    ...     .having_word("UNIV")
    ...     .having_replacement("univ")
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

    >>> (
    ...     ReplaceWord()
    ...     .having_word("univ")
    ...     .having_replacement("UNIV")
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )


"""

from tm2p._intern import ParamsMixin
from tm2p.enum import ThFile
from tm2p.refine._intern.replace import BaseReplaceWord


class ReplaceWord(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseReplaceWord()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.ORG)
            .run()
        )

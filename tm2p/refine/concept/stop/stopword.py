"""
StopWord
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.replace import StopWord
    >>> (
    ...     StopWord()
    ...     .having_word("business")
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )

    >>> from tm2p.refine.concept.reset import Reset
    >>> (
    ...     Reset()
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import ThFile
from tm2p.refine._intern.stop import BaseStopWord


class StopWord(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        from ..apply import Apply

        (
            BaseStopWord()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CONCEPT)
            .run()
        )

        return Apply().where_root_directory(self.params.root_directory).run()


def run():

    preferred = None

    print()
    while True:

        preferred = input("Prefered > ").strip()
        if preferred == "":
            break

        StopWord().having_word(preferred).where_root_directory("./").run()
        print("\n\n")


if __name__ == "__main__":
    run()

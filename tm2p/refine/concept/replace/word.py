"""
Word
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.replace import Word
    >>> (
    ...     Word()
    ...     .having_word("business")
    ...     .having_replacement("BUSINESS")
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
from tm2p.refine._intern.replace import BaseExactWord


class Word(
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


def run():

    from ..apply import Apply
    from ..group import Group

    preferred = None
    variant = None

    print()
    while True:

        preferred = input("Prefered > ").strip()
        if preferred == "":
            break

        variant = input("Variant > ").strip()
        if variant == "":
            break

        (
            Word()
            .having_word(preferred)
            .having_replacement(variant)
            .where_root_directory("./")
            .run()
        )

        Group().where_root_directory("./").run()
        Apply().where_root_directory("./").run()

        print("\n\n")


if __name__ == "__main__":
    run()

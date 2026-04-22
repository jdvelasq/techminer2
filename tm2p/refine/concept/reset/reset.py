"""
Reset
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.reset import Reset
    >>> (
    ...     Reset()
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import ThFile
from tm2p.refine._intern.reset import BaseReset


class Reset(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseReset()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CONCEPT)
            .run()
        )


if __name__ == "__main__":

    Reset().where_root_directory("./").run()

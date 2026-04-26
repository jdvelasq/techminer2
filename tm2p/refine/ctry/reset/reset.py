"""
Reset
===============================================================================

Smoke tests:
    >>> from tm2p.refine.ctry.reset import Reset
    >>> (
    ...     Reset()
    ...     .where_root_directory("tests/regtech-scopus/")
    ...     .run()
    ... ) # doctest: +SKIP

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
            .with_thesaurus_file(ThFile.CTRY)
            .run()
        )

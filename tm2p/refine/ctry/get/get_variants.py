"""
GetVariants
===============================================================================

Smoke tests:
    >>> from tm2p.refine.ctry.oper import GetVariants
    >>> terms = (
    ...     GetVariants()
    ...     .having_text_matching(
    ...         (
    ...             "Azerbaijan",
    ...             "Bahrain",
    ...         )
    ...     )
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(terms[:5])
    ['Azerbaijan State University of Economics (UNEC), Baku, Azerbaijan',
     'Accounting Finance & Banking Department, Ahlia University, Manama, Bahrain',
     'College of Business Administration, University of Bahrain, Zallaq, Bahrain',
     'Department of Banking and Finance, Ahlia University, Manama, Bahrain',
     'Department of Finance and Accounting, Kingdom University, Riffa, Bahrain']







"""

from tm2p.enum import ThFile
from tm2p.refine._intern.get import BaseGetVariants


class GetVariants(
    BaseGetVariants,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            BaseGetVariants()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.CTRY)
            .run()
        )

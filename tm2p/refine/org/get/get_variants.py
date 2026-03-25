"""
GetVariants
===============================================================================

Smoke tests:
    >>> from tm2p.refine.org.oper import GetVariants
    >>> terms = (
    ...     GetVariants()
    ...     .having_text_matching(
    ...         (
    ...             "Addis Ababa University",
    ...             "Ahlia University",
    ...         )
    ...     )
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(terms[:5])
    ['Addis Ababa University, Addis Ababa, Ethiopia',
     'Accounting Finance & Banking Department, Ahlia University, Manama, Bahrain',
     'Department of Banking and Finance, Ahlia University, Manama, Bahrain']






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
            .with_thesaurus_file(ThFile.ORG)
            .run()
        )

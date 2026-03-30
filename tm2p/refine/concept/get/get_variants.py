"""
GetVariants
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.get import GetVariants
    >>> terms = (
    ...     GetVariants()
    ...     .having_text_matching(
    ...         (
    ...             "fintech",
    ...             "fintech technology",
    ...         )
    ...     )
    ...     .where_root_directory("examples/scopus/")
    ...     .run()
    ... )
    >>> terms[:5]
    ['fintech', 'fintech technology']

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
            .with_thesaurus_file(ThFile.CONCEPT)
            .run()
        )

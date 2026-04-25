"""
GetVariants
===============================================================================

Smoke tests:
    >>> from tm2p.refine.organization.get import GetVariants
    >>> terms = (
    ...     GetVariants()
    ...     .having_text_matching(
    ...         (
    ...             "ADDIS ABABA UNIV",
    ...             "AIN UNIV",
    ...         )
    ...     )
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )
    >>> terms[:5]
    ['Addis Ababa University, Addis Ababa, Ethiopia', 'College of Business, Al Ain University, Al Ain, Abu Dhabi, United Arab Emirates']

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

"""
GetVariants
===============================================================================

Smoke tests:
    >>> from tm2p.refine.org.get import GetVariants
    >>> terms = (
    ...     GetVariants()
    ...     .having_text_matching(
    ...         (
    ...             "AIN SHAMS UNIV",
    ...             "AL-BAYT UNIV",
    ...         )
    ...     )
    ...     .where_root_directory("tests/regtech-scopus/")
    ...     .run()
    ... )
    >>> terms[:5]
    ['Ain Shams University, Cairo, Egypt', 'Department of Business Administration, Business School, Al al-Bayt University, Al-Mafraq, Jordan', 'Department of Computer Science, Faculty of Information Technology, Al Al-Bayt University, Al-Mafraq, Jordan']


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

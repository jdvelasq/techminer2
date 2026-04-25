"""
Smoke tests:
    >>> from tm2p.enum import ThFile
    >>> from tm2p.refine._intern.oper import BaseGetVariants
    >>> terms = (
    ...     BaseGetVariants()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .having_text_matching(
    ...         (
    ...             "fintech",
    ...             "fintech technology",
    ...         )
    ...     )
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )
    >>> terms[:5]
    ['fintech', 'fintech technology']




"""

from tm2p._intern import ParamsMixin
from tm2p.enum import ThField
from tm2p.refine._intern.data_access import load_thesaurus_as_dataframe


class BaseGetVariants(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        if isinstance(self.params.pattern, str):
            pattern = (self.params.pattern,)
        else:
            pattern = self.params.pattern

        df = load_thesaurus_as_dataframe(params=self.params)
        df = df[df[ThField.PREFERRED.value].isin(pattern)].copy()
        series = df[ThField.VARIANT.value].str.split("; ").explode().str.strip()
        series = series.to_list()

        return series

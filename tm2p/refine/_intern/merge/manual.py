"""
Smoke tests:
    >>> from tm2p.enum import ThFile, Field
    >>> from tm2p.refine._intern.merge import BaseManual
    >>> (
    ...     BaseManual()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .having_text_matching(
    ...         (
    ...             "fintech innovation",
    ...             "fin-tech innovation",
    ...         )
    ...     )
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )
    1

"""

from tm2p import ThField
from tm2p._intern import ParamsMixin
from tm2p.refine._intern.data_access import (
    load_thesaurus_as_dataframe,
    save_dataframe_as_thesaurus,
)

PREFERRED = ThField.PREFERRED.value
VARIANT = ThField.VARIANT.value


class BaseManual(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = load_thesaurus_as_dataframe(params=self.params)

        df[VARIANT] = df[VARIANT].str.split("; ")
        df = df.explode(VARIANT)  #  type: ignore
        df[VARIANT] = df[VARIANT].str.strip()

        lead = self.params.pattern[0]
        candidates = self.params.pattern[1:]

        for candidate in candidates:
            df.loc[df[PREFERRED] == candidate, PREFERRED] = lead

        grouped_df = df.groupby(PREFERRED, as_index=False).agg({VARIANT: list})

        grouped_df[VARIANT] = grouped_df[VARIANT].apply(sorted)
        grouped_df[VARIANT] = grouped_df[VARIANT].str.join("; ")

        save_dataframe_as_thesaurus(
            params=self.params,
            df=grouped_df,  # type: ignore
        )

        return 1

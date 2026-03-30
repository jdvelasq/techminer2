"""
Smoke tests:
    >>> from tm2p.enum import ThFile
    >>> from tm2p.refine._intern.sort import BaseSortByAlphabetLeftToRight
    >>> (
    ...     BaseSortByAlphabetLeftToRight()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .where_root_directory("examples/scopus/")
    ...     .run()
    ... )
    7722


"""

from tm2p._intern import ParamsMixin
from tm2p.enum import ThField
from tm2p.refine._intern.data_access import (
    load_thesaurus_as_dataframe,
    save_dataframe_as_thesaurus,
)


class BaseSortByAlphabetLeftToRight(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        df = load_thesaurus_as_dataframe(params=self.params)

        df = df.sort_values(
            by=[ThField.PREFERRED.value, ThField.VARIANT.value],
            ascending=[True, True],
        ).reset_index(drop=True)

        save_dataframe_as_thesaurus(
            params=self.params,
            df=df,
        )

        return len(df)

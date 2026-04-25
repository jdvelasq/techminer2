"""
Smoke tests:
    >>> from tm2p.enum import ThFile
    >>> from tm2p.refine._intern.sort import BaseSortByCharacterLength
    >>> (
    ...     BaseSortByCharacterLength()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .where_root_directory("tests/tinyml-scopus/")
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


class BaseSortByCharacterLength(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        df = load_thesaurus_as_dataframe(params=self.params)

        df["_key_length_"] = df[ThField.PREFERRED.value].str.len()

        df = df.sort_values(
            by=["_key_length_", ThField.PREFERRED.value, ThField.VARIANT.value],
            ascending=[False, True, True],
        ).reset_index(drop=True)

        df = df.drop(columns=["_key_length_"])

        save_dataframe_as_thesaurus(
            params=self.params,
            df=df,
        )

        return len(df)

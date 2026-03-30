"""
Smoke tests:
    >>> from tm2p.enum import ThFile
    >>> from tm2p.refine._intern.sort import BaseSortByMaxTokenLength
    >>> (
    ...     BaseSortByMaxTokenLength()
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


class BaseSortByMaxTokenLength(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        df = load_thesaurus_as_dataframe(params=self.params)

        df["_length_"] = df[ThField.PREFERRED.value].str.split(" ")
        df["_length_"] = df["_length_"].apply(lambda x: max(len(word) for word in x))

        df = df.sort_values(
            by=["_length_", ThField.PREFERRED.value, ThField.VARIANT.value],
            ascending=[False, True, True],
        ).reset_index(drop=True)

        df = df.drop(columns=["_length_"])

        save_dataframe_as_thesaurus(
            params=self.params,
            df=df,
        )

        return len(df)

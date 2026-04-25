"""
Smoke tests:
    >>> from tm2p.enum import ThFile
    >>> from tm2p.refine._intern.group import BaseGroup
    >>> (
    ...     BaseGroup()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )



"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p.enum import ThField
from tm2p.refine._intern.data_access import (
    load_thesaurus_as_dataframe,
    save_dataframe_as_thesaurus,
)


class BaseGroup(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        df = load_thesaurus_as_dataframe(params=self.params)
        df = _explode_variants(df)
        df = _group_variants(df)

        save_dataframe_as_thesaurus(
            params=self.params,
            df=df,  # type: ignore
        )


def _explode_variants(
    df: pd.DataFrame,
) -> pd.DataFrame:

    df[ThField.VARIANT.value] = df[ThField.VARIANT.value].str.split("; ")
    df = df.explode(ThField.VARIANT.value)  #  type: ignore
    df[ThField.VARIANT.value] = df[ThField.VARIANT.value].str.strip()

    return df


def _group_variants(df):

    grouped_df = df.groupby(ThField.PREFERRED.value, as_index=False).agg(
        {ThField.VARIANT.value: list}
    )
    grouped_df[ThField.VARIANT.value] = grouped_df[ThField.VARIANT.value].apply(sorted)

    grouped_df[ThField.VARIANT.value] = grouped_df[ThField.VARIANT.value].str.join("; ")

    return grouped_df

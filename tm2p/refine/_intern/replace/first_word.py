"""
Smoke tests:
    >>> from tm2p.enum import ThFile
    >>> from tm2p.refine._intern.replace import BaseFirstWord
    >>> (
    ...     BaseFirstWord()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .having_word("business")
    ...     .having_replacement("BUSINESS")
    ...     .where_root_directory("examples/scopus/")
    ...     .using_colored_output(False)
    ...     .run()
    ... )

    >>> from tm2p.refine.concept.reset import Reset
    >>> (
    ...     Reset()
    ...     .where_root_directory("examples/scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import ThField
from tm2p.refine._intern.data_access import (
    load_thesaurus_as_dataframe,
    save_dataframe_as_thesaurus,
)


class BaseFirstWord(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        df = load_thesaurus_as_dataframe(params=self.params)
        df = df[
            [
                ThField.PREFERRED.value,
                ThField.VARIANT.value,
            ]
        ]
        df[ThField.PREFERRED.value] = df[ThField.PREFERRED.value].apply(
            lambda x: f" {x} " if isinstance(x, str) else x
        )
        df[ThField.PREFERRED.value] = df[ThField.PREFERRED.value].str.replace(
            f"^ {self.params.word} ",
            f" {self.params.replacement} ",
            regex=True,
        )
        df[ThField.PREFERRED.value] = df[ThField.PREFERRED.value].str.strip()
        df = df.explode(ThField.VARIANT.value)  #  type: ignore
        grouped_df = df.groupby(ThField.PREFERRED.value, as_index=False).agg(
            {ThField.VARIANT.value: list}
        )
        grouped_df[ThField.VARIANT.value] = grouped_df[ThField.VARIANT.value].str.join(
            "; "
        )
        save_dataframe_as_thesaurus(
            params=self.params,
            df=grouped_df,  # type: ignore
        )

"""
Replace Abbreviations
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.acronym import Replace
    >>> (
    ...     Replace()
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )  # doctest: +SKIP
    >>> from tm2p.refine.concept.reset import Reset
    >>> (
    ...     Reset()
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import ThField, ThFile
from tm2p.refine._intern.data_access import (
    load_thesaurus_as_dataframe,
    save_dataframe_as_thesaurus,
)

PREFERRED = ThField.PREFERRED.value
VARIANT = ThField.VARIANT.value


class Replace(
    ParamsMixin,
):
    """:meta private:"""

    def _load_acronyms_thesaurus_as_dataframe(self):

        mixin = (
            ParamsMixin()
            .update(**self.params.__dict__)
            .with_thesaurus_file(ThFile.ACRONYM)
        )
        df = load_thesaurus_as_dataframe(params=mixin.params)
        return df

    def _merge(self, df):

        df[VARIANT] = df[VARIANT].str.split("; ")
        df = df.explode(VARIANT)  #  type: ignore
        df[VARIANT] = df[VARIANT].str.strip()

        grouped_df = df.groupby(PREFERRED, as_index=False).agg({VARIANT: list})
        grouped_df[VARIANT] = grouped_df[VARIANT].apply(sorted)
        grouped_df[VARIANT] = grouped_df[VARIANT].str.join("; ")

        return grouped_df

    def _replace_acronyms(self, acronyms, df):

        for _, row in acronyms.iterrows():

            abbr = row[PREFERRED]
            value = row[VARIANT].split("; ")[0].strip()

            df[PREFERRED] = df[PREFERRED].str.replace(
                " " + abbr + " ",
                " " + value + " ",
                regex=False,
            )

        return df

    def _add_padding(self, df):

        df = df.copy()
        df[PREFERRED] = " " + df[PREFERRED] + " "
        return df

    def _remove_padding(self, df):

        df = df.copy()
        df[PREFERRED] = df[PREFERRED].str.strip()
        return df

    def run(self) -> None:

        from ..apply import Apply

        self.with_thesaurus_file(ThFile.CONCEPT)

        acronyms = self._load_acronyms_thesaurus_as_dataframe()
        df = load_thesaurus_as_dataframe(params=self.params)
        df = self._add_padding(df=df)  # type: ignore
        df = self._replace_acronyms(acronyms=acronyms, df=df)
        df = self._remove_padding(df=df)
        df = self._merge(df=df)

        save_dataframe_as_thesaurus(
            params=self.params,
            df=df,  # type: ignore
        )

        Apply().where_root_directory(self.params.root_directory).run()


if __name__ == "__main__":

    Replace().where_root_directory("./").run()

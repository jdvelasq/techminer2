"""
Smoke tests:
    >>> from tm2p.enum import ThFile
    >>> from tm2p.refine._intern.replace import BaseStopWord
    >>> (
    ...     BaseStopWord()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .having_word("business")
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .using_colored_output(False)
    ...     .run()
    ... )

    >>> from tm2p.refine.concept.reset import Reset
    >>> (
    ...     Reset()
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )

"""

import sys

from duckdb import df

from tm2p._intern import ParamsMixin
from tm2p._intern.packag_data.word_lists.update_stopwords import update_stopwords
from tm2p.enum import ThField
from tm2p.refine._intern.data_access import (
    load_thesaurus_as_dataframe,
    save_dataframe_as_thesaurus,
)

PREFERRED = ThField.PREFERRED.value
VARIANT = ThField.VARIANT.value


class BaseGenericStopword(
    ParamsMixin,
):
    """:meta private:"""

    def _load_thesaurus(self):

        df = load_thesaurus_as_dataframe(params=self.params)
        df = df[[PREFERRED, VARIANT]]

        return df

    def _update_stopwords(self, df):

        variants = df.loc[df[PREFERRED] == self.params.word].copy()
        variants = variants[VARIANT].str.split("; ").explode().str.strip().tolist()
        answer = update_stopwords(self.params.word, variants)

        if answer == "no":
            sys.stderr.write("domain-specific stopword.\n")
        elif answer == "common":
            sys.stderr.write("common-and-basic stopword.\n")
        elif answer == "scientific":
            sys.stderr.write("scientific-and-academic stopword.\n")
        sys.stderr.flush()

    def _transform_to_stopword(self, df):

        df[PREFERRED] = df[PREFERRED].apply(
            lambda x: "#domain_specific_stopwords" if x == self.params.word else x
        )

        df[VARIANT] = df[VARIANT].str.split("; ")
        df = df.explode(VARIANT)  #  type: ignore
        df[VARIANT] = df[VARIANT].str.strip()

        grouped_df = df.groupby(PREFERRED, as_index=False).agg({VARIANT: list})

        grouped_df[VARIANT] = grouped_df[VARIANT].apply(sorted)
        grouped_df[VARIANT] = grouped_df[VARIANT].str.join("; ")

        save_dataframe_as_thesaurus(
            params=self.params,
            df=grouped_df,  # type: ignore
        )

    def run(self):
        """:meta private:"""

        df = self._load_thesaurus()
        self._update_stopwords(df)
        self._transform_to_stopword(df)

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

from tm2p._intern import ParamsMixin
from tm2p.enum import ThField
from tm2p.refine._intern.data_access import (
    load_thesaurus_as_dataframe,
    save_dataframe_as_thesaurus,
)


class BaseStopWord(
    ParamsMixin,
):
    """:meta private:"""

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
            lambda x: f"#{self.params.word}" if x == self.params.word else x
        )

        df[ThField.PREFERRED.value] = df[ThField.PREFERRED.value].str.strip()
        save_dataframe_as_thesaurus(
            params=self.params,
            df=df,  # type: ignore
        )

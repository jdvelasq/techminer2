"""
Concordance Records
=========================================================================================

Smoke test:
    >>> from pprint import pprint
    >>> from techminer2.analyze.concordances import ConcordanceRecords
    >>> from techminer2 import RecordsOrderBy
    >>> mapping = (
    ...     ConcordanceRecords()
    ...     #
    ...     .having_text_matching("FINTECH")
    ...     #
    ...     .where_root_directory("examples/fintech-with-references/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by(RecordsOrderBy.PUBYEAR_NEWEST)
    ...     .run()
    ... )
    >>> assert isinstance(mapping, list)
    >>> assert len(mapping) > 0
    >>> assert all(isinstance(r, dict) for r in mapping)
    >>> assert 'AR' in mapping[0]
    >>> assert 'AU' in mapping[0]
    >>> pprint(mapping[0])


"""

import re

import pandas as pd  # type: ignore
from textblob import TextBlob  # type: ignore

from techminer2 import CorpusField
from techminer2._internals import ParamsMixin
from techminer2._internals.data_access.load_filtered_main_data import (
    load_filtered_main_data,
)
from techminer2._internals.record_builders import records_to_dicts

__reviewed__ = "2026-01-29"


class ConcordanceRecords(ParamsMixin):
    """:meta private:"""

    def _filter_by_concordance(
        self, dataframe: pd.DataFrame, search_for: str
    ) -> pd.DataFrame:

        found = (
            dataframe[CorpusField.ABS_TOK.value]
            .astype(str)
            .str.contains(search_for, regex=True)
        )
        dataframe = dataframe[found]
        return dataframe

    def _process_abstracts(
        self, dataframe: pd.DataFrame, search_for: str
    ) -> pd.DataFrame:

        dataframe = dataframe.copy()

        dataframe[CorpusField.ABS_TOK.value] = dataframe[CorpusField.ABS_TOK.value].map(
            lambda x: list(TextBlob(x).sentences)
        )
        dataframe[CorpusField.ABS_TOK.value] = dataframe[CorpusField.ABS_TOK.value].map(
            lambda x: [str(y) for y in x]
        )
        dataframe[CorpusField.ABS_TOK.value] = dataframe[CorpusField.ABS_TOK.value].map(
            lambda x: [y[:-2] if y[-2:] == " ." else y for y in x]
        )
        dataframe[CorpusField.ABS_TOK.value] = dataframe[CorpusField.ABS_TOK.value].map(
            lambda x: [y for y in x if re.search(search_for, y)]
        )
        dataframe[CorpusField.ABS_TOK.value] = dataframe[CorpusField.ABS_TOK.value].map(
            " . ".join
        )

        return dataframe

    def run(self) -> list[dict]:

        search_for = r"\b" + self.params.pattern.lower().replace("_", " ") + r"\b"
        dataframe = load_filtered_main_data(params=self.params)
        dataframe = self._filter_by_concordance(dataframe, search_for)
        dataframe = self._process_abstracts(dataframe, search_for)
        mapping = records_to_dicts(dataframe)

        return mapping

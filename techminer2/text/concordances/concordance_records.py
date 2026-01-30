"""
Concordance Records
=========================================================================================

Smoke test:
    >>> from pprint import pprint
    >>> from techminer2.text.concordances import ConcordanceRecords
    >>> from techminer2 import RecordsOrderBy
    >>> mapping = (
    ...     ConcordanceRecords()
    ...     #
    ...     .having_text_matching("FINTECH")
    ...     #
    ...     .where_root_directory("examples/small/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by(RecordsOrderBy.DATE_NEWEST)
    ...     .run()
    ... )
    >>> assert isinstance(mapping, list)
    >>> assert len(mapping) > 0
    >>> assert all(isinstance(r, dict) for r in mapping)
    >>> assert 'AR' in mapping[0]
    >>> assert 'AU' in mapping[0]
    >>> pprint(mapping[0])  # doctest: +SKIP
    {'AB': 'there is currently NO_CONSENSUS about what THE_TERM_FINTECH means . '
           'this paper explores THE_COMPLEXITY of FINTECH , and attempts '
           'A_DEFINITION , drawn from A_PROCESS of reviewing more than 200 '
           'scholarly articles referencing THE_TERM_FINTECH and covering A_PERIOD '
           'of more than 40 years . the_objective_of_this study is to offer '
           'A_DEFINITION which is distinct as_well_as succinct in '
           'ITS_COMMUNICATION , yet sufficiently broad in ITS_RANGE of APPLICATION '
           '. as THE_ORIGINS of THE_TERM can neither be unequivocally placed in '
           'ACADEMIA nor in PRACTICE , THE_DEFINITION concentrates on extracting '
           'out THE_QUINTESSENCE of FINTECH using BOTH_SPHERES . applying '
           'SEMANTIC_ANALYSIS and BUILDING on THE_COMMONALITIES of 13 peerreviewed '
           'DEFINITIONS of THE_TERM , it is concluded that FINTECH is '
           'A_NEW_FINANCIAL_INDUSTRY that APPLIES_TECHNOLOGY to improve '
           'FINANCIAL_ACTIVITIES . THE_IMPLICATIONS as_well_as THE_SHORTCOMINGS of '
           'THIS_DEFINITION are discussed . 2021 journal of innovation management '
           '. all rights reserved .',
     'AR': 'Schueffel, 2016, J INNOV MANAG, V4, P32',
     'AU': 'Schueffel P.',
     'DE': 'Banking; Financial institution; Financial services; Innovation; '
           'Research; Technology; Terminology',
     'ID': nan,
     'PY': 2016,
     'SO': 'J. Innov. Manag.',
     'TC': 389,
     'TI': 'Taming the beast: A scientific definition of fintech',
     'UT': 13}


"""

import re

import pandas as pd  # type: ignore
from textblob import TextBlob  # type: ignore

from techminer2 import Field
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
            dataframe[Field.ABS_TOK.value]
            .astype(str)
            .str.contains(search_for, regex=True)
        )
        dataframe = dataframe[found]
        return dataframe

    def _process_abstracts(
        self, dataframe: pd.DataFrame, search_for: str
    ) -> pd.DataFrame:

        dataframe = dataframe.copy()

        dataframe[Field.ABS_TOK.value] = dataframe[Field.ABS_TOK.value].map(
            lambda x: TextBlob(x).sentences
        )
        dataframe[Field.ABS_TOK.value] = dataframe[Field.ABS_TOK.value].map(
            lambda x: [str(y) for y in x]
        )
        dataframe[Field.ABS_TOK.value] = dataframe[Field.ABS_TOK.value].map(
            lambda x: [y[:-2] if y[-2:] == " ." else y for y in x]
        )
        dataframe[Field.ABS_TOK.value] = dataframe[Field.ABS_TOK.value].map(
            lambda x: [y for y in x if re.search(search_for, y)]
        )
        dataframe[Field.ABS_TOK.value] = dataframe[Field.ABS_TOK.value].map(" . ".join)

        return dataframe

    def run(self) -> list[dict]:

        search_for = r"\b" + self.params.pattern.lower().replace("_", " ") + r"\b"
        dataframe = load_filtered_main_data(params=self.params)
        dataframe = self._filter_by_concordance(dataframe, search_for)
        dataframe = self._process_abstracts(dataframe, search_for)
        mapping = records_to_dicts(dataframe)

        return mapping

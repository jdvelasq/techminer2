"""
KWICConcordance
=========================================================================================

Smoke test:
    >>> from tm2p.enum import Field, RecordOrderBy
    >>> from tm2p.explore.concordance import KWICConcordance
    >>> contexts = (
    ...     KWICConcordance()
    ...     #
    ...     .with_source_field(Field.ABSTR_RAW)
    ...     .having_text_matching("FINTECH")
    ...     #
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by(RecordOrderBy.YEAR_NEWEST)
    ...     #
    ...     .run()
    ... )
    >>> assert isinstance(contexts, list)
    >>> assert len(contexts) > 0
    >>> assert all(isinstance(c, str) for c in contexts)
    >>> for t in contexts[:20]: print(t)
                                                                 FINTECH is touted as a game changing, disruptive innovation capab…
                                                                 FINTECH can be used to facilitate the green economy by allowing g…
                                                                 FINTECH , as the fusion of finance and technology, has not only t…
                                                                 FINTECH service providers should insure that their products are e…
                                                                 FINTECH is a newly emerged service that combines innovative finan…
                                                                 FINTECH companies can be differentiated in several areas, based o…
                                                                 FINTECH appears and develops rapidly in various business models t…
                                                                 FINTECH offers several services, such as funding, payment (includ…
                                                                 FINTECH companies are generally small to medium sized startups tr…
                                                                 FINTECH innovations are enabling access to financial services thr…
                                                                 FINTECH is a new economic industry, comprised of companies that a…
                                                                 FINTECH has important implications for digital transformation of…
                                                                 FINTECH is viewed as a game changer to bring finance to the unrea…
                                                                 FINTECH adoption optimization expands the financial access to for…
                                                                 FINTECH affects consumption, savings, and investment decisions in…
                                                                 FINTECH platforms are one of the most important elements in the r…
                                                                 FINTECH is a dynamic and innovative field that fully benefits fro…
                                                                 FINTECH , particularly the blockchain, has the potential to be di…
                                                                 FINTECH has a potential to disrupt and to create new types of risk
                                                                 FINTECH , ESG performance, and corporate strategy

"""

import re

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p.enum import Field

__reviewed__ = "2026-01-29"


class KWICConcordance(
    ParamsMixin,
):
    """:meta private:"""

    def _extract_context_phrases(self, dataframe: pd.DataFrame) -> pd.Series:

        pattern = self.params.pattern
        if isinstance(pattern, tuple):
            pattern = pattern[0]

        search_for = pattern.lower().replace("_", " ")

        dataframe = dataframe.set_index(
            pd.Index(
                dataframe[Field.REC_ID.value] + " / " + dataframe[Field.TITLE_RAW.value]
            )
        )

        dataframe["_found_"] = (
            dataframe[self.params.source_field.value]
            .astype(str)
            .str.contains(r"\b" + search_for + r"\b", regex=True, flags=re.IGNORECASE)
        )

        dataframe = dataframe[dataframe["_found_"]].copy()  # type: ignore[assignment]
        abstracts = dataframe[self.params.source_field.value]
        phrases = abstracts.str.replace(";", ".").str.split(".").explode().str.strip()
        context_phrases = phrases[
            phrases.str.contains(
                r"\b" + search_for + r"\b", regex=True, flags=re.IGNORECASE
            )
        ].reset_index(  # type: ignore[attr-defined]
            drop=True
        )

        return context_phrases

    # -------------------------------------------------------------------------
    def _create_contexts_dataframe(self, context_phrases: pd.Series) -> pd.DataFrame:

        pattern = self.params.pattern
        if isinstance(pattern, tuple):
            pattern = pattern[0]

        search_for = pattern.lower().replace("_", " ")

        regex = r"\b" + search_for + r"\b"
        contexts = context_phrases.str.extract(
            r"(?P<left_context>[\s \S]*)" + regex + r"(?P<right_context>[\s \S]*)",
            flags=re.IGNORECASE,
        )

        contexts["left_context"] = contexts["left_context"].fillna("")
        contexts["left_context"] = contexts["left_context"].str.strip()

        contexts["right_context"] = contexts["right_context"].fillna("")
        contexts["right_context"] = contexts["right_context"].str.strip()

        contexts = contexts[
            contexts["left_context"].map(lambda x: x != "")
            | contexts["right_context"].map(lambda x: x != "")
        ]

        contexts["criteria"] = (
            contexts["left_context"].str.lower().str.replace("_", " ", regex=False)
        )
        contexts["criteria"] = contexts["criteria"].str[::-1]
        contexts = contexts.sort_values(by="criteria", ascending=True)  # type: ignore[call-arg]
        contexts.drop(columns=["criteria"], inplace=True)

        return contexts.reset_index(drop=True)  # type: ignore[return-value]

    # -------------------------------------------------------------------------
    def _transform_context_dataframe_to_texts(
        self, contexts: pd.DataFrame
    ) -> list[str]:

        search_for = self.params.pattern
        if isinstance(search_for, tuple):
            search_for = search_for[0]

        contexts = contexts.copy()
        contexts["left_r"] = contexts["left_context"].str[::-1]

        contexts["left_context"] = contexts["left_context"].map(
            lambda x: "<<<" + x[-57:] if len(x) > 60 else x
        )
        contexts["right_context"] = contexts["right_context"].map(
            lambda x: x[:57] + ">>>" if len(x) > 60 else x
        )

        contexts["left_context"] = contexts["left_context"].str.replace(
            r"(<<<\s*)", "\u2026", regex=True
        )

        contexts["right_context"] = contexts["right_context"].str.replace(
            r"(\s*>>>)", "\u2026", regex=True
        )

        texts = []
        for _, row in contexts.iterrows():
            text = (
                f"{row['left_context']:>60} {search_for.upper()} {row['right_context']}"
            )
            texts.append(text)

        return texts

    # -------------------------------------------------------------------------
    def run(self) -> list[str]:

        assert self.params.source_field in [
            Field.ABSTR_RAW,
            Field.ABSTR_TOK,
            Field.ABSTR_UPPER,
        ]

        dataframe = load_filtered_main_csv_zip(params=self.params)
        context_phrases = self._extract_context_phrases(dataframe=dataframe)
        contexts_dataframe = self._create_contexts_dataframe(context_phrases)
        texts = self._transform_context_dataframe_to_texts(contexts_dataframe)

        return texts

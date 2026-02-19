"""
Extract Abstract Suffixes
===============================================================================

Smoke test:
    >>> from techminer2.ingest.review import ExtractAbstractSuffixes
    >>> text = (
    ...     ExtractAbstractSuffixes()
    ...     .having_text_matching(None)
    ...     .having_n_chars(90)
    ...     .where_root_directory("examples/tests/")
    ...     .run()
    ... )
    >>> assert isinstance(text, list)
    >>> assert all(isinstance(t, str) for t in text)
    >>> assert all(len(t) <= 90 for t in text)
    >>> assert len(text) > 0
    >>> for t in text[:10]: print(t)
    th THE_DEMANDS of INDUSTRY . 2010 edsig ( education special interest group of the aitp ) .
    TORS , REGULATORS , etc . ) , who explore THE_FIELD of FINTECH . 2016 , the author ( s ) .
    how COMPANIES_COLLABORATE or compete in SPECIFIC_FINTECH_AREAS . 2016 , the author ( s ) .
    HADOW has been brought to THE_LIGHT . springer international publishing switzerland 2016 .
    _LENDING and CROWDFUNDING platforms . springer international publishing switzerland 2016 .
    SOCIAL_ENVIRONMENT . 2016 . faculty of management , warsaw university of technology 2016 .
    we provide OBJECTIVE_UNDERSTANDING of FINTECH , how it is reflected in THE_POPULAR_MEDIA .
    ANKING , CASH , CREDIT , and DEBIT_CARDS in DIFFERENT_COUNTRIES and REGIONS of THE_WORLD .
    examining CONCEPTS such_as THE_DEVELOPMENT of BUSINESS_APPLICATIONS that use embedded AI .
    ORMATION . 4 ) OUR_RESULTS inform PRACTITIONERS how to time THE_DECISION of MONETIZATION .



"""

from techminer2._internals import ParamsMixin
from techminer2.ingest.records.record_mapping import RecordMapping  # type: ignore

__reviewed__ = "2026-01-28"


class ExtractAbstractSuffixes(
    ParamsMixin,
):
    """:meta private:"""

    def _sort_by_suffix(self, texts: list[str]) -> list[str]:
        reversed_texts = [text[::-1] for text in texts]
        sorted_reversed = sorted(reversed_texts)
        return [text[::-1] for text in sorted_reversed]

    def run(self) -> list[str]:

        docs = RecordMapping().update(**self.params.__dict__).run()

        abstracts = [doc["AB"] for doc in docs if isinstance(doc["AB"], str)]
        suffixes = [text[-self.params.n_chars :] for text in abstracts]

        suffixes_grouped_by_ending = self._sort_by_suffix(suffixes)

        if self.params.pattern is not None:
            suffixes_grouped_by_ending = [
                text
                for text in suffixes_grouped_by_ending
                if self.params.pattern in text
            ]

        return suffixes_grouped_by_ending

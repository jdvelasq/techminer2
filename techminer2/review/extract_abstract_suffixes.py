"""
Extract Abstract Suffixes
===============================================================================

Smoke test:
    >>> from techminer2.review import ExtractAbstractSuffixes
    >>> text = (
    ...     ExtractAbstractSuffixes()
    ...     .having_text_matching(None)
    ...     .having_n_chars(90)
    ...     .where_root_directory("examples/small/")
    ...     .run()
    ... )
    >>> assert isinstance(text, list)
    >>> assert all(isinstance(t, str) for t in text)
    >>> assert all(len(t) <= 90 for t in text)
    >>> assert len(text) > 0
    >>> sorted_check = text == sorted([t[::-1] for t in text], key=lambda x: x[::-1])
    >>> assert sorted_check
    >>> for t in text[:5]: print(t) # doctest: +SKIP
    th THE_DEMANDS of INDUSTRY . 2010 edsig ( EDUCATION_SPECIAL_INTEREST_GROUP of THE_AITP ) .
    TORS , REGULATORS , etc . ) , who explore THE_FIELD of FINTECH . 2016 , the author ( s ) .
    how COMPANIES_COLLABORATE or compete in SPECIFIC_FINTECH_AREAS . 2016 , the author ( s ) .
    HADOW has been brought to THE_LIGHT . springer international publishing switzerland 2016 .
    _LENDING and CROWDFUNDING platforms . springer international publishing switzerland 2016 .

"""

from techminer2._internals import ParamsMixin
from techminer2.explore.record_mapping import RecordMapping  # type: ignore

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

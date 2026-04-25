"""
ExtractAbstractSuffixes
===============================================================================

Smoke test:
    >>> from tm2p.ingest.rev import ExtractAbstractSuffixes
    >>> text = (
    ...     ExtractAbstractSuffixes()
    ...     .having_n_chars(90)
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )
    >>> assert isinstance(text, list)
    >>> assert all(isinstance(t, str) for t in text)
    >>> assert all(len(t) <= 90 for t in text)
    >>> assert len(text) > 0
    >>> for t in text[:10]: print(t)  # doctest: +NORMALIZE_WHITESPACE +SKIP
    resents a THOROUGH_DISCUSSION of MEC_BASED_IOMT_HEALTHCARE_SYSTEMS . 2022 the_author ( s )
    e with PRECAUTIONARY_REMARKS and guidelines for FUTURE_RESEARCHERS . 2022 the_author ( s )
    DEVICES and an alternative for CONNECTION to 2g/3g MOBILE_NETWORKS . 2023 the_author ( s )
    ution toward REAL_WORLD_DEPLOYMENT of FACE_MASKS_DETECTION_SYSTEMS . 2023 the_author ( s )
    m achieve ACCURACY comparable to when trained on BALANCED_DATASETS . 2023 the_author ( s )
     t246187 and ta120 t246189 is 528 BYTES and 744 BYTES respectively . 2023 the_author ( s )
    ERSPECTIVE on this CHALLENGING_AND_RAPIDLY_EVOLVING_RESEARCH_FIELD . 2024 the_author ( s )
    ork have been meticulously benchmarked on 13 OPEN_SOURCED_DATASETS . 2024 the_author ( s )
    efits and challenges of this kind of TINYML_ANALYSIS are described . 2024 the_author ( s )
    hes EDUCATIONAL_PROGRAMS by encouraging INTERDISCIPLINARY_LEARNING . 2025 the_author ( s )

"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field
from tm2p.ingest.rec.rec_map import RecordMapping  # type: ignore

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

        docs = (
            RecordMapping()
            .update(**self.params.__dict__)
            .with_source_field(Field.ABSTR_UPPER)
            .where_record_years_range(None, None)
            .where_record_global_citations_range(None, None)
            .where_records_match(None)
            .run()
        )

        abstracts = [doc["AB"] for doc in docs if isinstance(doc["AB"], str)]
        suffixes = [text[-self.params.n_chars :] for text in abstracts]

        suffixes_grouped_by_ending = self._sort_by_suffix(suffixes)

        if "pattern" in self.params.__dict__ and self.params.pattern is not None:
            suffixes_grouped_by_ending = [
                text
                for text in suffixes_grouped_by_ending
                if self.params.pattern in text  # type: ignore
            ]

        return suffixes_grouped_by_ending


if __name__ == "__main__":

    ExtractAbstractSuffixes().having_n_chars(130).where_root_directory("./").run()

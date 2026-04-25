"""
ExtractAbstractPrefixes
===============================================================================

Smoke test:
    >>> from tm2p.ingest.rev import ExtractAbstractPrefixes
    >>> text = (
    ...     ExtractAbstractPrefixes()
    ...     .having_n_chars(90)
    ...     .where_root_directory("tests/regtech-scopus/")
    ...     .run()
    ... )
    >>> assert isinstance(text, list)
    >>> assert all(isinstance(t, str) for t in text)
    >>> assert all(len(t) <= 90 for t in text)
    >>> assert len(text) > 0
    >>> for t in text[:10]: print(t)  # doctest: +NORMALIZE_WHITESPACE +SKIP
    ACCURATE_DATA_ANNOTATION is essential to successfully implementing MACHINE_LEARNING ( ML )
    ARTIFICIAL_INTELLIGENCE ( AI ) is being applied across all areas of BUSINESS_AND_SOCIETY .
    ARTIFICIAL_INTELLIGENCE ( AI ) is transforming MODERN_LIFE by driving INNOVATION and effic
    ARTIFICIAL_INTELLIGENCE and MACHINE_LEARNING have numerous key roles to play in_the_future
    BANKS are dedicated to SERVING the real ECONOMY . in_recent_years , REGULATORY_TECHNOLOGY
    BIODIVERSITY and indigenous KNOWLEDGE_SYSTEMS present numerous opportunities to advance th
    BLOCKCHAIN and MACHINE_LEARNING_INTEGRATION has changed the_area_of REGULATORY_TECHNOLOGY
    BLOCKCHAIN holds promise for reshaping INSURANCE_OPERATIONS by enhancing TRANSPARENCY , AU
    BLOCKCHAIN s technological characteristics , such as DECENTRALIZATION , robustness , and a
    CHAPTER 8 will analyze how CHINA_APPLIES REGTECH to REGULATION . in addition , this_chapte



"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field
from tm2p.ingest.rec.rec_map import RecordMapping  # type: ignore

__reviewed__ = "2026-01-28"


class ExtractAbstractPrefixes(
    ParamsMixin,
):
    """:meta private:"""

    def _sort_by_prefix(self, texts: list[str]) -> list[str]:
        sorted_texts = sorted(texts)
        return sorted_texts

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
        prefixes = [text[: self.params.n_chars] for text in abstracts]

        prefixes_grouped_by_begining = self._sort_by_prefix(prefixes)

        if "pattern" in self.params.__dict__ and self.params.pattern is not None:
            prefixes_grouped_by_begining = [
                text
                for text in prefixes_grouped_by_begining
                if self.params.pattern in text  # type: ignore
            ]

        return prefixes_grouped_by_begining


if __name__ == "__main__":

    ExtractAbstractPrefixes().having_n_chars(130).where_root_directory("./").run()

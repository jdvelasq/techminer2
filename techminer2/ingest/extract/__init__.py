"""Private API."""

from techminer2.ingest.extract.contains import ContainsExtractor
from techminer2.ingest.extract.difference import DifferenceExtractor
from techminer2.ingest.extract.ends_with import EndsWithExtractor
from techminer2.ingest.extract.full_match import FullMatchExtractor
from techminer2.ingest.extract.intersection import IntersectionExtractor
from techminer2.ingest.extract.match import MatchExtractor
from techminer2.ingest.extract.starts_with import StartsWithExtractor
from techminer2.ingest.extract.stemming_and import StemmingAndExtractor
from techminer2.ingest.extract.stemming_or import StemmingOrExtractor
from techminer2.ingest.extract.top_terms import TopTermsExtractor

__all__ = [
    "ContainsExtractor",
    "EndsWithExtractor",
    "DifferenceExtractor",
    "IntersectionExtractor",
    "FullMatchExtractor",
    "MatchExtractor",
    "StartsWithExtractor",
    "StemmingAndExtractor",
    "StemmingOrExtractor",
    "TopTermsExtractor",
]

from .acro import ExtractAcronyms
from .header import ExtractSectionHeaders
from .phrase import ReprocessNounPhrases
from .prefix import ExtractAbstractPrefixes

__all__ = [
    "ExtractAcronyms",
    "ExtractSectionHeaders",
    "ExtractAbstractPrefixes",
    "ReprocessNounPhrases",
]


def __getattr__(name):
    if name == "ExtractAbstractSuffixes":
        from .suffix import ExtractAbstractSuffixes

        return ExtractAbstractSuffixes
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

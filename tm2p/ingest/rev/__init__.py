from .acro import ExtractAcronyms
from .header import ExtractSectionHeaders
from .phrase import ReprocessNounPhrases

__all__ = [
    "ExtractAcronyms",
    "ExtractSectionHeaders",
    "ReprocessNounPhrases",
]


def __getattr__(name):
    if name == "ExtractAbstractSuffixes":
        from .suffix import ExtractAbstractSuffixes

        return ExtractAbstractSuffixes
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

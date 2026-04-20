from .acronyms import ExtractAcronyms
from .headers import ExtractSectionHeaders
from .phrases import ReprocessNounPhrases

__all__ = [
    "ExtractAcronyms",
    "ExtractSectionHeaders",
    "ReprocessNounPhrases",
]


def __getattr__(name):
    if name == "ExtractAbstractSuffixes":
        from .suffixes import ExtractAbstractSuffixes

        return ExtractAbstractSuffixes
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

from functools import lru_cache

from nltk.stem import PorterStemmer  # type: ignore

stemmer = PorterStemmer()


@lru_cache(maxsize=None)
def internal__apply_porter_stemmer(word: str) -> str:
    """Apply Porter stemming algorithm with caching."""
    return stemmer.stem(word)

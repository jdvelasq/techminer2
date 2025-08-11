"""Porter stemmer."""
from functools import lru_cache  # type: ignore

from nltk.stem import PorterStemmer  # type: ignore

stemmer = PorterStemmer()


@lru_cache(maxsize=None)
def internal__apply_porter_stemmer(word):
    return stemmer.stem(word)

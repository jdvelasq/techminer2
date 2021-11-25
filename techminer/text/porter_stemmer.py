import re
import string

from nltk.stem import PorterStemmer


def porter_stemmer(text):
    """Returns the stemmer transformation of the string."""
    if text is None:
        return None
    text = text.strip().lower()
    text = re.sub("-", " ", text)
    text = re.sub("[" + string.punctuation + "]", "", text)
    s = PorterStemmer()
    text = sorted(set([s.stem(w) for w in text.split()]))
    return " ".join(text)

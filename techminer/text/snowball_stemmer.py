import re
import string

from nltk.stem import SnowballStemmer


def snowball_stemmer(x):
    """Computes the stemmer transformation of string x.

    Examples
    ----------------------------------------------------------------------------------------------

    >>> stemmer_snowball('neural net')
    'net neural'


    """
    if x is None:
        return None
    x = x.strip().lower()
    x = re.sub("-", " ", x)
    x = re.sub("[" + string.punctuation + "]", "", x)
    # x = remove_accents(x)
    s = SnowballStemmer("english")
    x = sorted(set([s.stem(w) for w in x.split()]))
    return " ".join(x)

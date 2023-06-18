import re
import string

from nltk.stem import PorterStemmer


def porter_stemmer(text):
    """
    Apply Porter stemming algorithm to the input text.

    Args:
        text (str): The input text to be stemmed.

    Returns:
        str: The stemmed version of the input text.
    """
    if text is None:
        return None

    # Convert to lowercase and remove leading/trailing whitespace
    text = text.strip().lower()

    # Replace hyphens with spaces and remove punctuation
    text = re.sub("-", " ", text)
    text = re.sub("[" + string.punctuation + "]", "", text)

    # Apply stemming to each word in the text
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in text.split()]

    # Return a sorted, deduplicated list of stemmed words
    unique_stems = sorted(set(stemmed_words))
    return " ".join(unique_stems)

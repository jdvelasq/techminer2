"""
Stopwords
=========
"""

from os.path import isfile


def load_stopwords(directory_or_list):
    """
    Loads the stopwords from the given directory.

    :param directory: The directory where the stopwords are stored.
    """
    if directory_or_list is None:
        return []

    if isinstance(directory_or_list, str):
        if directory_or_list[-1] != "/":
            directory_or_list += "/"
        filename = directory_or_list + "stopwrods.txt"
        if not isfile(filename):
            raise FileNotFoundError(f"The file '{filename}' does not exist.")

        with open(filename, "r", encoding="utf-8") as f:
            stopwords = f.read().splitlines()

        return stopwords

    if isinstance(directory_or_list, list):
        values = [isinstance(element, str) for element in directory_or_list]
        if not all(values):
            raise TypeError("The list must contain only strings.")
        return directory_or_list

    raise TypeError("The parameter must be a string or a list of strings.")

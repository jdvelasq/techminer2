from os.path import isfile


def load_stopwords(directory):
    """
    Loads the stopwords from the given directory.

    :param directory: The directory where the stopwords are stored.
    """

    if directory[-1] != "/":
        directory += "/"
    filename = directory + "stopwrods.txt"
    if not isfile(filename):
        raise FileNotFoundError(f"The file '{filename}' does not exist.")

    with open(filename, "r") as f:
        stopwords = f.read().splitlines()

    return stopwords

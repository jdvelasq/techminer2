import os


def load_stopwords(directory):
    """
    Loads stopwords from the project directory.

    """
    filename = os.path.join(directory, "processed", "stopwords.txt")
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
    return [
        line.strip()
        for line in open(
            filename,
            "r",
            encoding="utf-8",
        ).readlines()
    ]

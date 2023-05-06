"""Loads user stopwords from the project directory."""
import os


def load_stopwords(directory):
    """Load user stopwords from the specified directory."""

    stopwords_file_path = os.path.join(directory, "processed", "stopwords.txt")

    if not os.path.isfile(stopwords_file_path):
        raise FileNotFoundError(f"The file '{stopwords_file_path}' does not exist.")

    with open(stopwords_file_path, "r", encoding="utf-8") as file:
        stopwords = [line.strip() for line in file.readlines()]

    return stopwords

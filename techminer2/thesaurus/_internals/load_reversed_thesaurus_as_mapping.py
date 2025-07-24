"""
This module implement generic thesaurus functions.


"""

import os.path


def internal__load_reversed_thesaurus_as_mapping(file_path):
    """Load existence thesaurus as a dataframe."""

    value_phrases = []
    key_phrases = []
    key_phrase = None

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.replace("\t", "    ")
            if not line.startswith(" "):
                key_phrase = line.strip()
            else:
                value_phrase = line.strip()
                value_phrases.append(value_phrase)
                key_phrases.append(key_phrase)

    mapping = dict(zip(value_phrases, key_phrases))
    mapping = {k: v for k, v in mapping.items() if k != ""}

    return mapping

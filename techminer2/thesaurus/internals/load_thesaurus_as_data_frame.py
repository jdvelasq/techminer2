"""Thesaurus internal functions"""

import pandas as pd  # type: ignore


def internal__load_thesaurus_as_data_frame(file_path):
    """Load existence thesaurus as a dataframe."""

    value_phrases = []
    key_phrases = []
    key_phrase = None
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if not line.startswith(" "):
                key_phrase = line.strip()
            else:
                value_phrase = line.strip()
                value_phrases.append(value_phrase)
                key_phrases.append(key_phrase)

    frame = pd.DataFrame(
        {
            "key": key_phrases,
            "value": value_phrases,
        }
    )

    return frame

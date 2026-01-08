import os.path
from typing import Dict, List, Optional


def internal__load_reversed_thesaurus_as_mapping(file_path: str) -> Dict[str, str]:
    """Load existence thesaurus as a mapping."""

    value_phrases: List[str] = []
    key_phrases: List[str] = []
    key_phrase: Optional[str] = None

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.replace("\t", "    ")
            if not line.startswith(" "):
                key_phrase = line.strip()
            else:
                value_phrase = line.strip()
                # skip value lines that appear before any key header
                if key_phrase is None:
                    continue
                value_phrases.append(value_phrase)
                key_phrases.append(key_phrase)

    mapping = dict(zip(value_phrases, key_phrases))
    mapping = {k: v for k, v in mapping.items() if k != ""}

    return mapping

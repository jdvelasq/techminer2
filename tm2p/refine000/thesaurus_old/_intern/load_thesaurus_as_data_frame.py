import pandas as pd  # type: ignore


def internal__load_thesaurus_as_data_frame(file_path: str) -> pd.DataFrame:
    """Load thesaurus file as a dataframe."""

    indent = " " * 4

    value_phrases = []
    key_phrases = []
    key_phrase = None
    order = -1
    mapping = {}
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:

            # Normalize tabs to spaces for consistent indentation detection
            line = line.replace("\t", indent)

            if not line.startswith(" "):
                key_phrase = line.strip()
                order += 1
                mapping[key_phrase] = order
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

    frame = (
        frame.groupby("key", as_index=False).agg({"value": list}).reset_index(drop=True)
    )
    frame["value"] = frame["value"].str.join("; ")
    frame["order"] = frame["key"].map(mapping)
    frame = frame.sort_values("order").drop(columns=["order"]).reset_index(drop=True)

    return frame

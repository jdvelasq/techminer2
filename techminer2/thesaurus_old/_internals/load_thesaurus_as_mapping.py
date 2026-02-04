from typing import Dict, List

from techminer2.thesaurus_old._internals.load_thesaurus_as_data_frame import (
    internal__load_thesaurus_as_data_frame,
)


def internal__load_thesaurus_as_mapping(file_path: str) -> Dict[str, List[str]]:
    """Load existence thesaurus as a dataframe."""

    frame = internal__load_thesaurus_as_data_frame(file_path)
    frame = frame.groupby("key", as_index=False).agg(list)
    return dict(zip(frame.key, frame.value))

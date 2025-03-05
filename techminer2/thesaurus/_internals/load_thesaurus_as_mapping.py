"""
This module implement generic thesaurus functions.


"""

from .load_thesaurus_as_data_frame import internal__load_thesaurus_as_data_frame


def internal__load_thesaurus_as_mapping(file_path):
    """Load existence thesaurus as a dataframe."""

    frame = internal__load_thesaurus_as_data_frame(file_path)
    frame = frame.groupby("key", as_index=False).agg(list)
    return dict(zip(frame.key, frame.value))

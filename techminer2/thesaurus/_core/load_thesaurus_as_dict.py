"""
This module implement generic thesaurus functions.


"""

from .load_thesaurus_as_frame import load_thesaurus_as_frame


def load_thesaurus_as_dict(file_path):
    """Load existence thesaurus as a dataframe."""

    frame = load_thesaurus_as_frame(file_path)
    frame = frame.groupby("key", as_index=False).agg(list)
    return dict(zip(frame.key, frame.value))

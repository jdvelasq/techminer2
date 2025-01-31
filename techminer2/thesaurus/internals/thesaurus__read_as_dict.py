"""
This module implement generic thesaurus functions.


"""

from .thesaurus__read_as_dataframe import thesaurus__read_as_dataframe


def thesaurus__read_as_dict(file_path):
    """Load existence thesaurus as a dataframe."""

    frame = thesaurus__read_as_dataframe(file_path)
    frame = frame.groupby("key", as_index=False).agg(list)
    return dict(zip(frame.key, frame.value))

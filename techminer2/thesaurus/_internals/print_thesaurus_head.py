"""Thesaurus internal functions"""

import sys

from .load_thesaurus_as_data_frame import internal__load_thesaurus_as_data_frame


def internal__print_thesaurus_head(
    file_path,
    n=8,
):
    """Print the head of the thesaurus."""

    data_frame = internal__load_thesaurus_as_data_frame(file_path)
    keys = data_frame.key
    keys = keys.drop_duplicates().head(n).tolist()
    data_frame = data_frame.groupby("key", as_index=False).agg({"value": list})
    data_frame = data_frame.loc[data_frame.key.isin(keys), :]
    data_frame["value"] = data_frame["value"].str.join("; ")

    #
    sys.stderr.write(f"\nINFO  Thesaurus head {file_path}.")
    for _, row in data_frame.iterrows():
        #
        key = row.key
        if len(key) > 30:
            key = key[:26] + " ..."
        key = f"{key:>30s}"
        #
        value = row.value
        if len(value) > 50:
            value = row.value[:46] + " ..."
        value = f"{value:<50s}"
        #
        sys.stderr.write(f"\n        {key} : {value}")

    sys.stderr.flush()


# =============================================================================

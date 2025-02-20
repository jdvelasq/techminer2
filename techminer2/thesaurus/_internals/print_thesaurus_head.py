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
    data_frame = data_frame.set_index("key").loc[keys, :].reset_index()

    data_frame["key"] = data_frame["key"].map(
        lambda x: x[:50] + "..." if len(x) > 50 else x
    )
    data_frame["value"] = data_frame["value"].str.join("; ")
    data_frame["value"] = data_frame["value"].map(
        lambda x: x[:70] + "..." if len(x) > 70 else x
    )

    sys.stdout.write(f"Printing thesaurus header\n")
    sys.stdout.write(f"  Loading {file_path} thesaurus file\n")
    sys.stdout.write(f"  Header:\n")

    for _, row in data_frame.iterrows():
        sys.stdout.write(f"    {row.key}\n")
        sys.stdout.write(f"      {row.value}\n")
    sys.stdout.flush()


# =============================================================================

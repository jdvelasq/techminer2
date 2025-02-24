"""Thesaurus internal functions"""

import sys

from .load_thesaurus_as_data_frame import internal__load_thesaurus_as_data_frame


def internal__print_thesaurus_header(
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
        lambda x: x[:75] + "..." if len(x) > 75 else x
    )
    data_frame["value"] = data_frame["value"].str.join("; ")
    data_frame["value"] = data_frame["value"].map(
        lambda x: x[:71] + "..." if len(x) > 74 else x
    )

    sys.stderr.write(f"\nPrinting thesaurus header\n  File : {file_path}\n")
    for _, row in data_frame.iterrows():
        sys.stderr.write(f"\n    {row.key}")
        sys.stderr.write(f"\n      {row.value}")
    sys.stderr.write(f"\n")
    sys.stderr.flush()


# =============================================================================

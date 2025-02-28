"""Thesaurus internal functions"""

import sys

from .load_thesaurus_as_data_frame import internal__load_thesaurus_as_data_frame


def internal__print_thesaurus_header(
    thesaurus_path,
    n=8,
):
    """:meta private:"""

    data_frame = internal__load_thesaurus_as_data_frame(thesaurus_path)

    keys = data_frame.key
    keys = keys.drop_duplicates().head(n).tolist()

    data_frame = data_frame.groupby("key", as_index=False).agg({"value": list})
    data_frame["value"] = data_frame.value.str.join("; ")
    data_frame = data_frame.loc[data_frame.key.isin(keys), :]
    data_frame = data_frame.set_index("key").loc[keys, :].reset_index()

    data_frame["key"] = data_frame["key"].map(
        lambda x: x[:77] + "..." if len(x) > 80 else x
    )
    data_frame["value"] = data_frame["value"].map(
        lambda x: x[:73] + "..." if len(x) > 76 else x
    )

    sys.stdout.write(f"Printing thesaurus header\n  File : {thesaurus_path}\n\n")
    for _, row in data_frame.iterrows():
        sys.stdout.write(f"    {row.key}\n")
        sys.stdout.write(f"      {row.value}\n")
    sys.stdout.write("\n")
    sys.stdout.flush()


# =============================================================================

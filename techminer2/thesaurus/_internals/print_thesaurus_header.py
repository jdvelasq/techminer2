"""Thesaurus internal functions"""

import sys

from colorama import Fore, init

from .load_thesaurus_as_data_frame import internal__load_thesaurus_as_data_frame

init(autoreset=True)


def internal__print_thesaurus_header(
    thesaurus_path,
    n=8,
    use_colorama=True,
):
    """:meta private:"""

    data_frame = internal__load_thesaurus_as_data_frame(thesaurus_path)
    if data_frame.empty:
        return

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

    msg = f"Printing thesaurus header\n  File : {thesaurus_path}\n\n"
    if use_colorama:
        filename = str(thesaurus_path).split("/")[-1]
        msg = msg.replace("File :", f"{Fore.LIGHTBLACK_EX}File :")
        msg = msg.replace(filename, f"{Fore.RESET}{filename}")
    sys.stderr.write(msg)

    for _, row in data_frame.iterrows():
        sys.stderr.write(f"    {row.key}\n")
        if use_colorama:
            sys.stderr.write(f"      {Fore.LIGHTBLACK_EX}{row.value}{Fore.RESET}\n")
        else:
            sys.stderr.write(f"      {row.value}\n")
    sys.stderr.write("\n")
    sys.stderr.flush()


# =============================================================================

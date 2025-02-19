""""Thesaurus common functions."""

from ..._internals.log_message import internal__log_message
from . import (
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_data_frame,
)


class ThesaurusMixin:

    def print_thesaurus_head(self, n=8):
        """Print the head of the thesaurus."""

        file_path = internal__generate_user_thesaurus_file_path(self.params)
        data_frame = internal__load_thesaurus_as_data_frame(file_path)
        keys = data_frame.key
        keys = keys.drop_duplicates().head(n).tolist()
        data_frame = data_frame.groupby("key", as_index=False).agg({"value": list})
        data_frame = data_frame.loc[data_frame.key.isin(keys), :]
        data_frame["value"] = data_frame["value"].str.join("; ")

        lines = [
            "  " + "-" * 35 + " Thesaurus head " + "-" * 35,
        ]

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
            lines.append(f"    {key} : {value}")

        lines.append("  " + "-" * 84)
        internal__log_message(msgs=lines, prompt_flag=-1)

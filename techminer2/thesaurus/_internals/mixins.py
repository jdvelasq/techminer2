""""Thesaurus common functions."""

import pandas as pd
from textblob import Word
from tqdm import tqdm  # type: ignore

from ...database._internals.io import internal__load_filtered_database
from . import (
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_mapping,
)

tqdm.pandas()


class ThesaurusMixin:

    # -------------------------------------------------------------------------
    def internal__build_thesaurus_path(self):
        self.thesaurus_path = internal__generate_user_thesaurus_file_path(
            params=self.params
        )

    # -------------------------------------------------------------------------
    def internal__create_thesaurus_data_frame_from_field(self):

        keys = self.filtered_records[self.params.field].dropna()
        keys = keys.str.split("; ")
        keys = keys.explode()
        keys = keys.str.strip()
        keys = keys.drop_duplicates()

        data_frame = pd.DataFrame(
            {
                "key": keys,
                "value": keys,
            }
        )

        self.data_frame = data_frame

    # -------------------------------------------------------------------------
    def internal__extract_findings(self):
        if self.data_frame is None:
            self.findings = {}
            return
        keys = self.data_frame.key.drop_duplicates()
        findings = {key: self.mapping[key] for key in sorted(keys)}
        self.findings = findings

    # -------------------------------------------------------------------------
    def internal__group_values_by_key(self):

        self.data_frame["value"] = self.data_frame["value"].str.split("; ")
        self.data_frame = self.data_frame.explode("value")
        self.data_frame["value"] = self.data_frame["value"].str.strip()
        self.data_frame = self.data_frame.groupby("key").agg({"value": list})
        self.data_frame["value"] = self.data_frame["value"].map(
            lambda x: sorted(set(x))
        )
        self.data_frame["value"] = self.data_frame["value"].str.join("; ")

    # -------------------------------------------------------------------------
    def internal__load_filtered_records(self):
        self.filtered_records = internal__load_filtered_database(params=self.params)

    # -------------------------------------------------------------------------
    def internal__load_thesaurus_as_mapping(self):
        mapping = internal__load_thesaurus_as_mapping(self.thesaurus_path)
        self.mapping = {key: "; ".join(value) for key, value in mapping.items()}

    # -------------------------------------------------------------------------
    def internal__reduce_keys(self):

        particles = [
            "aided",
            "and the",
            "and",
            "applied to",
            "assisted",
            "at",
            "based",
            "for",
            "in",
            "like",
            "of the",
            "of using",
            "of",
            "on",
            "s",
            "sized",
            "to",
            "under",
            "using",
        ]

        # Based on the basic TheVantagePoint algorithm to group terms
        data_frame = self.data_frame.copy()
        data_frame["fingerprint"] = data_frame["key"].copy()

        # hyphen-insensitive matching
        data_frame["fingerprint"] = (
            data_frame["fingerprint"].str.replace("_", " ").replace("-", " ")
        )

        # case-insensitive matching
        data_frame["fingerprint"] = data_frame["fingerprint"].str.lower()

        # particles remotion
        for particle in particles:
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                f" {particle} ", " "
            )
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                f"^{particle} ", ""
            )
            data_frame["fingerprint"] = data_frame["fingerprint"].str.replace(
                f" {particle}$", ""
            )

        # singular and plural matching
        data_frame["fingerprint"] = data_frame["fingerprint"].str.strip()
        data_frame["fingerprint"] = data_frame["fingerprint"].str.split(" ")
        data_frame["fingerprint"] = data_frame["fingerprint"].map(
            lambda x: [w.strip() for w in x]
        )
        data_frame["fingerprint"] = data_frame["fingerprint"].map(
            lambda x: [Word(w).singularize().singularize().singularize() for w in x]
        )

        # word order insensitive matching
        data_frame["fingerprint"] = data_frame["fingerprint"].map(
            lambda x: sorted(set(x))
        )

        # final fingerprint
        data_frame["fingerprint"] = data_frame["fingerprint"].str.join(" ")

        # preserve the key with the largest number of values
        data_frame["count"] = data_frame["value"].map(lambda x: len(x.split("; ")))
        data_frame = data_frame.sort_values(
            by=["fingerprint", "count", "key"], ascending=False
        )

        # mapping
        mapping = data_frame[["key", "fingerprint"]].copy()
        mapping = mapping.drop_duplicates()
        mapping = mapping.set_index("fingerprint")
        mapping = mapping["key"].to_dict()

        data_frame["key"] = data_frame["fingerprint"].apply(lambda x: mapping[x])

        self.data_frame = data_frame[["key", "value"]].copy()

    # -------------------------------------------------------------------------
    def internal__sort_data_frame_by_key(self):
        self.data_frame = self.data_frame.sort_values("key")

    # -------------------------------------------------------------------------
    def internal__transform_thesaurus_mapping_to_data_frame(self):
        keys = list(self.mapping.keys())
        values = list(self.mapping.values())
        self.data_frame = pd.DataFrame(
            {
                "key": keys,
                "value": values,
            }
        )

    # -------------------------------------------------------------------------
    def internal__write_thesaurus_data_frame_to_disk(self):

        with open(self.thesaurus_path, "w", encoding="utf-8") as file:
            for key, row in self.data_frame.iterrows():
                file.write(key + "\n")
                for value in row["value"].split("; "):
                    file.write(f"    {value}\n")

    # -------------------------------------------------------------------------
    def internal__write_thesaurus_mapping_to_disk(self):

        for key in self.findings.keys():
            self.mapping.pop(key)

        with open(self.thesaurus_path, "w", encoding="utf-8") as file:

            # write the found keys
            for key in sorted(self.findings.keys()):
                file.write(key + "\n")
                for item in self.findings[key].split("; "):
                    file.write("    " + item + "\n")

            # write the remaining keys
            for key in sorted(self.mapping.keys()):
                file.write(key + "\n")
                for item in self.mapping[key].split("; "):
                    file.write("    " + item + "\n")


# =============================================================================

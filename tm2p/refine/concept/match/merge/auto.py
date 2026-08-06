"""
Auto
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.match import Auto
    >>> (
    ...     Auto()
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )  # doctest: +SKIP

"""

import json
import os
import time
from pathlib import Path

import openai
from openai import OpenAI

from tm2p._intern import ParamsMixin
from tm2p._intern.packag_data import update_core_thesaurus
from tm2p._intern.packag_data.templates.load_builtin_template import (
    load_builtin_template,
)
from tm2p.enum import ThField, ThFile
from tm2p.refine._intern.data_access import (
    load_thesaurus_as_dataframe,
    save_dataframe_as_thesaurus,
)

PREFERRED = ThField.PREFERRED.value
VARIANT = ThField.VARIANT.value


class Auto(
    ParamsMixin,
):
    """:meta private:"""

    def _explode(self, df):

        df[VARIANT] = df[VARIANT].str.split("; ")
        df = df.explode(VARIANT)  #  type: ignore
        df[VARIANT] = df[VARIANT].str.strip()

        return df

    def _merge(self, df):

        grouped_df = df.groupby(PREFERRED, as_index=False).agg({VARIANT: list})
        grouped_df[VARIANT] = grouped_df[VARIANT].apply(sorted)
        grouped_df[VARIANT] = grouped_df[VARIANT].str.join("; ")

        return grouped_df

    def _run_auto(self, df):

        filepath = (
            Path(self.params.root_directory)
            / "refine"
            / "thesaurus"
            / "candidate_matches.txt"
        )
        if not filepath.exists():
            return df

        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        preferred = None
        n_lines = len(lines)
        print(f"Processing {n_lines} lines...")

        for idx, line in enumerate(lines):

            time.sleep(0.5)

            if line.startswith("    "):

                variant = line.strip()
                variant = " ".join(variant.split(" ")[:-1])

                if preferred is None:
                    raise ValueError("Variant found before preferred term.")

                preferred = preferred.strip()
                variant = variant.strip()
                if preferred == "" or variant == "":
                    raise ValueError("Preferred or variant term is empty.")

                print(f"{idx}/{n_lines}  '{preferred}' <---- '{variant}'", flush=True)

                choice = update_core_thesaurus(
                    preferred=preferred,
                    variant=variant,
                )

                if choice is True:
                    df[PREFERRED] = df[PREFERRED].replace(variant, preferred)

            else:
                preferred = line.strip()
                preferred = " ".join(preferred.split(" ")[:-1])

        return df

    def run(self) -> None:
        """:meta private:"""

        from ...apply import Apply
        from ...group import Group

        self.with_thesaurus_file(ThFile.CONCEPT)
        df = load_thesaurus_as_dataframe(params=self.params)
        df = self._explode(df=df)  # type: ignore
        df = self._run_auto(df=df)
        df = self._merge(df=df)

        save_dataframe_as_thesaurus(
            params=self.params,
            df=df,  # type: ignore
        )

        Group().where_root_directory(self.params.root_directory).run()
        Apply().where_root_directory(self.params.root_directory).run()


if __name__ == "__main__":

    Auto().where_root_directory("./").run()

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


class AutoMerge(
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

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        core_area = self.params.core_area

        system_prompt = load_builtin_template(
            "shell.thesaurus.descriptors.match.synonyms.system.txt"
        )

        user_template = load_builtin_template(
            "shell.thesaurus.descriptors.match.synonyms.user.txt"
        )

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

                choice = self._ask(
                    idx=idx,
                    n_lines=n_lines,
                    preferred=preferred,
                    variant=variant,
                    client=client,
                    user_template=user_template,
                    system_prompt=system_prompt,
                )

                if choice == "yes":
                    df[PREFERRED] = df[PREFERRED].replace(variant, preferred)
                    print("✓ Synonym.\n")
                elif choice == "no":
                    print("✗ Not a synonym.\n")
                    continue
                else:
                    print("✗ Skipped.\n")
                    continue

            else:
                preferred = line.strip()
                preferred = " ".join(preferred.split(" ")[:-1])

        return df

    def _ask(
        self,
        idx,
        n_lines,
        preferred,
        variant,
        client,
        user_template,
        system_prompt,
        indent=4,
    ):

        core_area = self.params.core_area

        pad = " " * indent
        min_len = min(len(preferred), len(variant))
        diff_pos = next(
            (i for i in range(min_len) if preferred[i] != variant[i]), min_len
        )
        len1_tail = len(preferred) - diff_pos
        len2_tail = len(variant) - diff_pos
        marker = " " * diff_pos

        print(f"{idx+1}/{n_lines}\n")
        if len1_tail >= len2_tail:
            print(marker + "v")
        print(preferred)
        print(pad + variant)
        if len2_tail >= len1_tail:
            print(pad + marker + "^")
        else:
            print()

        user_prompt = user_template.format(
            lead_term=preferred,
            candidate_term=variant,
            core_area=core_area,
        )

        try:

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                        "cache_control": {"type": "ephemeral"},
                    },  # type: ignore
                    {
                        "role": "user",
                        "content": user_prompt,
                    },
                ],
                temperature=0,
                response_format={"type": "json_object"},
            )

        except openai.OpenAIError as e:
            print(f"Error processing the query: {e}")
            raise ValueError("API error") from e

        answer = response.choices[0].message.content
        answer = answer.strip()  # type: ignore
        answer = json.loads(answer)
        answer = answer["answer"]
        choice = answer.lower().strip()

        return choice

    def run(self) -> None:
        """:meta private:"""

        from ..apply import Apply
        from ..group import Group

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

    AutoMerge().where_root_directory("./").with_core_area("Food Analytics").run()

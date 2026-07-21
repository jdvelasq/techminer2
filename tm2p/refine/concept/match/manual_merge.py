"""
Shell
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.match import Shell
    >>> (
    ...     Shell()
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )  # doctest: +SKIP

"""

from pathlib import Path

from tm2p._intern import ParamsMixin
from tm2p.enum import ThField, ThFile
from tm2p.refine._intern.data_access import (
    load_thesaurus_as_dataframe,
    save_dataframe_as_thesaurus,
)

PREFERRED = ThField.PREFERRED.value
VARIANT = ThField.VARIANT.value


class ManualMerge(
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

    def _run_shell(self, df):

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

            if line.startswith("    "):

                variant = line.strip()
                variant = " ".join(variant.split(" ")[:-1])

                if preferred is None:
                    raise ValueError("Variant found before preferred term.")

                choice = self._show_diff(
                    idx=idx, n_lines=n_lines, preferred=preferred, variant=variant
                )

                if choice == "y":
                    df[PREFERRED] = df[PREFERRED].replace(variant, preferred)
                    print("✓ Merged.\n")
                elif choice == "q":
                    break
                else:
                    print("✗ Skipped.\n")
                    continue

            else:
                preferred = line.strip()
                preferred = " ".join(preferred.split(" ")[:-1])

        return df

    def _show_diff(self, idx, n_lines, preferred, variant, indent=4):

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

        print()
        print("Merge? (y/[n]/q) : ", end="")
        choice = input().strip().lower()
        print()

        return choice

    def run(self) -> None:
        """:meta private:"""

        from ..apply import Apply
        from ..group import Group

        self.with_thesaurus_file(ThFile.CONCEPT)
        df = load_thesaurus_as_dataframe(params=self.params)
        df = self._explode(df=df)  # type: ignore
        df = self._run_shell(df=df)
        df = self._merge(df=df)

        save_dataframe_as_thesaurus(
            params=self.params,
            df=df,  # type: ignore
        )

        Group().where_root_directory(self.params.root_directory).run()
        Apply().where_root_directory(self.params.root_directory).run()


if __name__ == "__main__":

    ManualMerge().where_root_directory("./").run()

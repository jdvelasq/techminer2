"""
Replace
===============================================================================

Smoke tests:
    >>> from tm2p.refine.acron import Replace
    >>> (
    ...     Replace()
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )  # doctest: +SKIP
    >>> from tm2p.refine.concept.reset import Reset
    >>> (
    ...     Reset()
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )  # doctest: +SKIP 

"""

import sys

from anyio import Path

from tm2p._intern import ParamsMixin
from tm2p.enum import ThField, ThFile
from tm2p.refine._intern.data_access import (
    load_thesaurus_as_dataframe,
    save_dataframe_as_thesaurus,
)

PREFERRED = ThField.PREFERRED.value
VARIANT = ThField.VARIANT.value


class Replace(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:

        df = self._load_thesaurus_as_dataframe()
        df = self._padding_add(df)  # type: ignore
        df = self._replace_acronyms(df)
        df = self._padding_remove(df)
        df = self._merge(df)

        self._save_thesaurus_from_dataframe(df)

    def _replace_acronyms(self, df):

        acronyms = self._load_acronyms()

        for key, value in acronyms.items():

            df[PREFERRED] = df[PREFERRED].str.replace(
                f" {key} ",
                f" {value[0]} ",
                regex=False,
            )

        return df

    def _load_acronyms(self):

        import sys

        acronym_filepath = self._get_acronyms_thesaurus_filepath()

        if not acronym_filepath.exists():
            raise FileNotFoundError(
                f"Acronym thesaurus file not found: '{acronym_filepath}'"
            )

        mapping = {}
        with open(acronym_filepath, "r", encoding="utf-8") as file:
            for line in file:
                line = line.replace("\t", " " * 4)
                if not line.startswith(" "):
                    preferred = line.strip()
                    mapping[preferred] = []
                    sys.stderr.write(f"{preferred}\n")
                    sys.stderr.flush()
                else:
                    if preferred is None:
                        raise ValueError("Variant found before any preferred term")
                    variant = line.strip()
                    mapping[preferred].append(variant)

                    sys.stderr.write(f"  '{preferred}' --> '{variant}'\n")
                    sys.stderr.flush()

        for key, values in mapping.items():
            if len(values) != 1:
                raise ValueError(
                    f"Multiple variants for preferred term '{key}': {values}"
                )

        return mapping

    def _load_thesaurus_as_dataframe(self):
        self.with_thesaurus_file(ThFile.CONCEPT)
        return load_thesaurus_as_dataframe(params=self.params)

    def _save_thesaurus_from_dataframe(self, df):

        save_dataframe_as_thesaurus(
            params=self.params,
            df=df,  # type: ignore
        )

    def _padding_add(self, df):
        df = df.copy()
        df[PREFERRED] = " " + df[PREFERRED] + " "
        return df

    def _padding_remove(self, df):

        df = df.copy()
        df[PREFERRED] = df[PREFERRED].str.strip()
        return df

    def _merge(self, df):

        df[VARIANT] = df[VARIANT].str.split("; ")
        df = df.explode(VARIANT)  #  type: ignore
        df[VARIANT] = df[VARIANT].str.strip()

        grouped_df = df.groupby(PREFERRED, as_index=False).agg({VARIANT: list})
        grouped_df[VARIANT] = grouped_df[VARIANT].apply(sorted)
        grouped_df[VARIANT] = grouped_df[VARIANT].str.join("; ")

        return grouped_df

    def _get_acronyms_thesaurus_filepath(self):

        return (
            Path(self.params.root_directory)
            / "refine"
            / "thesaurus"
            / "acronyms.the.txt"
        )


if __name__ == "__main__":

    Replace().where_root_directory("./").run()

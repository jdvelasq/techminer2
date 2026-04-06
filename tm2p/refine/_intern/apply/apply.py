"""
BaseApply
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field, ThFile
    >>> from tm2p.refine._intern.apply import BaseApply
    >>> (
    ...     BaseApply()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .with_source_field(Field.DESCRIPTOR_RAW)
    ...     .with_target_field(Field.DESCRIPTOR_NORM)
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )

"""

import sys

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p._intern.enum import ThField
from tm2p.refine._intern.data_access import load_thesaurus_as_dataframe

PREFERRED = ThField.PREFERRED.value
VARIANT = ThField.VARIANT.value


class BaseApply(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self) -> None:
        """:meta private:"""

        SOURCE = self.params.source_field.value
        TARGET = self.params.target_field.value

        df = load_main_csv_zip(root_directory=self.params.root_directory)

        th_df = load_thesaurus_as_dataframe(params=self.params)
        th_df[VARIANT] = th_df[VARIANT].str.split("; ")
        th_df = th_df.explode(VARIANT)
        th_df[VARIANT] = th_df[VARIANT].str.strip()
        mapping = dict(zip(th_df[VARIANT], th_df[PREFERRED]))

        df[TARGET] = df[SOURCE].str.split("; ")

        df[TARGET] = df[TARGET].map(
            lambda x: [mapping.get(item, item) for item in x],
            na_action="ignore",
        )

        df[TARGET] = df[TARGET].map(set, na_action="ignore")
        df[TARGET] = df[TARGET].map(sorted, na_action="ignore")
        df[TARGET] = df[TARGET].str.join("; ")

        save_main_csv_zip(df=df, root_directory=self.params.root_directory)

        sys.stderr.write(
            f"\nUsing {self.params.thesaurus_file.value} to update {self.params.target_field.value}"
        )
        sys.stderr.flush()

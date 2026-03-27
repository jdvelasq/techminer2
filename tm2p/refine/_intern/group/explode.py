"""
Smoke tests:
    >>> from tm2p.enum import ThFile
    >>> from tm2p.refine._intern.group import BaseExplode
    >>> (
    ...     BaseExplode()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )


"""

import sys

from tm2p._intern import ParamsMixin
from tm2p.refine._intern.data_access import (
    load_thesaurus_as_dataframe,
    save_dataframe_as_thesaurus,
)

from .group import _explode_variants


class BaseExplode(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:
        """:meta private:"""

        df = load_thesaurus_as_dataframe(params=self.params)
        df = _explode_variants(df)

        save_dataframe_as_thesaurus(
            params=self.params,
            df=df,  # type: ignore
        )

        sys.stderr.write(
            f"\nExploded {self.params.thesaurus_file.value} variants into separate records\n"
        )
        sys.stderr.flush()

"""
Smoke tests:
    >>> from tm2p.enum import ThFile
    >>> from tm2p.refine._intern.reset import Reset
    >>> (
    ...     Reset()
    ...     .with_thesaurus_file(ThFile.CONCEPT)
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )



"""

from tm2p._intern import ParamsMixin
from tm2p.refine._intern.data_access.get_thesaurus_path import get_thesaurus_path


class BaseReset(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        filepath_txt = get_thesaurus_path(
            root_directory=self.params.root_directory,
            file=self.params.thesaurus_file,
        )

        filepath_bak = filepath_txt.with_suffix(".bak")
        filepath_txt.write_text(
            filepath_bak.read_text(encoding="utf-8"), encoding="utf-8"
        )

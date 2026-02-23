"""
Print Header
===============================================================================


Smoke tests:
    >>> # Reset the thesaurus to initial state
    >>> from techminer2.refine.thesaurus_old.user import InitializeThesaurus
    >>> (
    ...     InitializeThesaurus(quit=True)
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .with_field("raw_descriptors")
    ...     .where_root_directory("tests/data/")
    ... ).run()

    >>> from techminer2.refine.thesaurus_old.user import PrintHeader
    >>> (
    ...     PrintHeader()
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .using_colored_output(False)
    ...     .where_root_directory("tests/data/")
    ... ).run()





"""

import sys

from techminer2._internals import ParamsMixin
from techminer2.refine.thesaurus_old._internals import ThesaurusMixin
from techminer2.refine.thesaurus_old._internals.load_thesaurus_as_data_frame import (
    internal__load_thesaurus_as_data_frame,
)


class PrintHeader(
    ParamsMixin,
    ThesaurusMixin,
):
    def internal__load_thesaurus_as_data_frame(self):
        self.data_frame = internal__load_thesaurus_as_data_frame(
            file_path=self.thesaurus_path,
        )

    def run(self):

        self._build_user_thesaurus_path()
        self.internal__load_thesaurus_as_data_frame()
        self.internal__print_thesaurus_header_to_stream(n=8, stream=sys.stdout)


# =============================================================================

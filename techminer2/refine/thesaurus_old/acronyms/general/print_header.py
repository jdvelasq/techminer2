"""
Print Header
===============================================================================


Example:
    >>> # Reset the thesaurus to initial state
    >>> from techminer2.refine.thesaurus_old.acronyms.general import InitializeThesaurus
    >>> (
    ...     InitializeThesaurus(quit=True)
    ...     .where_root_directory("examples/small/")
    ... ).run()

    >>> from techminer2.refine.thesaurus_old.acronyms.general import PrintHeader
    >>> (
    ...     PrintHeader()

    ...     .using_colored_output(False)
    ...     .where_root_directory("examples/small/")
    ... ).run()





"""

from techminer2._internals import ParamsMixin
from techminer2.refine.thesaurus_old.user import PrintHeader as UserPrintHeader


class PrintHeader(
    ParamsMixin,
):

    def run(self):

        (
            UserPrintHeader()
            .update(**self.params.__dict__)
            .with_thesaurus_file("acronyms.the.txt")
            .run()
        )


# =============================================================================

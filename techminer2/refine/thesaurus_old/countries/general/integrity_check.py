"""
Integrity Check
===============================================================================

Smoke tests:
    >>> from techminer2.refine.thesaurus_old.countries import InitializeThesaurus
    >>> (
    ...     InitializeThesaurus()
    ...     .where_root_directory("tests/fintech/")
    ... ).run()


    >>> from techminer2.refine.thesaurus_old.countries import IntegrityCheck
    >>> (
    ...     IntegrityCheck()
    ...     .where_root_directory("tests/fintech/")
    ... ).run()


"""

from techminer2._internals import ParamsMixin
from techminer2.refine.thesaurus_old.user import IntegrityCheck as UserIntegrityCheck


class IntegrityCheck(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        (
            UserIntegrityCheck()
            .update(**self.params.__dict__)
            .update(
                thesaurus_file="countries.the.txt",
                field="affiliations",
                root_directory=self.params.root_directory,
            )
            .run()
        )


# =============================================================================

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Integrity Check
===============================================================================

Example:
    >>> from techminer2.thesaurus_old.countries import InitializeThesaurus
    >>> (
    ...     InitializeThesaurus()
    ...     .where_root_directory("examples/small/")
    ... ).run()


    >>> from techminer2.thesaurus_old.countries import IntegrityCheck
    >>> (
    ...     IntegrityCheck()
    ...     .where_root_directory("examples/small/")
    ... ).run()


"""
from techminer2._internals import ParamsMixin
from techminer2.thesaurus_old.user import IntegrityCheck as UserIntegrityCheck


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

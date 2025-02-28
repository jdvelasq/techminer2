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

>>> from techminer2.thesaurus.countries import CreateThesaurus
>>> CreateThesaurus(root_directory="example/", quiet=True).run()




>>> from techminer2.thesaurus.countries import IntegrityCheck
>>> (
...     IntegrityCheck()
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... )
Thesaurus integrity check
  File : example/thesaurus/countries.the.txt
  106 terms checked
  Integrity check completed successfully
<BLANKLINE>



"""
from ...._internals.mixins import ParamsMixin
from ...user import IntegrityCheck as UserIntegrityCheck


class IntegrityCheck(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        (
            UserIntegrityCheck(
                thesaurus_file="countries.the.txt",
                field="affiliations",
                root_directory=self.params.root_directory,
            ).run()
        )


# =============================================================================

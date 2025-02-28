# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Check Thesaurus Integrity
===============================================================================

>>> from techminer2.thesaurus.organizations import IntegrityCheck
>>> (
...     IntegrityCheck()
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... )
Thesaurus integrity check
  File : example/thesaurus/organizations.the.txt
  106 terms checked
  Integrity check completed successfully
<BLANKLINE>


"""

from ...._internals.mixins import ParamsMixin
from ...user import IntegrityCheck as UserIntegrityCheck


#
#
class IntegrityCheck(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        (
            UserIntegrityCheck()
            .with_thesaurus_file("organizations.the.txt")
            .with_field("affiliations")
            .where_root_directory_is(self.params.root_directory)
            .run()
        )

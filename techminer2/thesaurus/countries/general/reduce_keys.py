# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Cleanup Thesaurus
===============================================================================


>>> from techminer2.thesaurus.countries import CreateThesaurus
>>> CreateThesaurus(root_directory="example/", quiet=True).run()


>>> from techminer2.thesaurus.countries import ReduceKeys
>>> (
...     ReduceKeys()
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... )
Reducing thesaurus keys
  File : example/thesaurus/countries.the.txt
  Keys reduced from 24 to 24
  Keys reduction completed successfully
<BLANKLINE>



"""
from ...._internals.mixins import ParamsMixin
from ...user import ReduceKeys as UserReduceKeys


class ReduceKeys(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        (
            UserReduceKeys(
                thesaurus_file="countries.the.txt",
                root_directory=self.params.root_directory,
            ).run()
        )


# =============================================================================

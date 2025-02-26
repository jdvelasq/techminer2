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


>>> from techminer2.thesaurus.countries import CleanupThesaurus
>>> (
...     CleanupThesaurus()
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .build()
... )
<BLANKLINE>
Thesaurus cleanup completed successfully for file: ...esaurus/countries.the.txt
<BLANKLINE>
Thesaurus application completed successfully for file: ...rus/countries.the.txt
Thesaurus application completed successfully for file: ...try_to_region.the.txt
Thesaurus application completed successfully for file: ..._to_subregion.the.txt

"""
from ..._internals.log_message import internal__log_message
from ..._internals.mixins import ParamsMixin
from ..user import CleanupThesaurus as CleanupUserThesaurus
from .apply_thesaurus import ApplyThesaurus


class CleanupThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        (
            CleanupUserThesaurus()
            .update(**self.params.__dict__)
            .with_thesaurus_file("countries.the.txt")
            .build()
        )

        ApplyThesaurus().update(**self.params.__dict__).build()

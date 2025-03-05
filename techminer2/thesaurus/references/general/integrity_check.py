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


>>> #
>>> # TEST PREPARATION
>>> #
>>> import sys
>>> from io import StringIO
>>> old_stderr = sys.stderr
>>> sys.stderr = StringIO()
>>> #
>>> # CODE:
>>> #
>>> from techminer2.thesaurus.references import IntegrityCheck
>>> (
...     IntegrityCheck()
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... )
>>> #
>>> # TEST EXECUTION
>>> #
>>> output = sys.stderr.getvalue()
>>> sys.stderr = old_stderr
>>> print(output)


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
            .with_thesaurus_file("references.the.txt")
            .with_field("global_references")
            .where_root_directory_is(self.params.root_directory)
            .run()
        )

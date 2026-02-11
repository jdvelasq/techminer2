# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Get Values
===============================================================================


Smoke tests:
    >>> # Redirecting stderr to avoid messages during doctests
    >>> import sys
    >>> from io import StringIO
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Reset the thesaurus to initial state
    >>> from techminer2.refine.thesaurus_old.descriptors import InitializeThesaurus
    >>> InitializeThesaurus(
    ...     root_directory="examples/fintech/",
    ...     quiet=True,
    ... ).run()

    >>> # Creates, configures, an run the exploder
    >>> from techminer2.refine.thesaurus_old.descriptors import GetValues
    >>> terms = (
    ...     GetValues()
    ...     .with_patterns(["FINTECH", "FINANCIAL_TECHNOLOGIES"])
    ...     .where_root_directory("examples/small/")
    ...     .run()
    ... )
    >>> terms[:5]
    ['FINANCIAL_TECHNOLOGIES', 'FINANCIAL_TECHNOLOGY', 'FINTECH', 'FINTECHS']




"""
from techminer2._internals import ParamsMixin
from techminer2.refine.thesaurus_old.user import GetValues as UserGetValues


#
#
class GetValues(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return (
            UserGetValues()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )

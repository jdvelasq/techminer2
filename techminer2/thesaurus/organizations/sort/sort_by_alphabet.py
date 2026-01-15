# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Alphabet
===============================================================================


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.organizations import InitializeThesaurus, SortByAlphabet

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Create and run the sorter
    >>> sorter = (
    ...     SortByAlphabet()
    ...     .having_keys_ordered_by("alphabetical")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/fintech/")
    ... )
    >>> sorter.run()

>>> from techminer2.thesaurus.organizations import PrintHeader
    >>> (
    ...     PrintHeader()
    ...     .using_colored_output(False)
    ...     .where_root_directory("examples/fintech/")
    ... ).run()





"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.thesaurus.user import SortByAlphabet as UserSortByAlphabet


class SortByAlphabet(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            UserSortByAlphabet()
            .update(**self.params.__dict__)
            .with_thesaurus_file("organizations.the.txt")
            .run()
        )

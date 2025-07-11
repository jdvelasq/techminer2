# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Word Length
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.countries import CreateThesaurus, SortByWordLength

    >>> # Redirect stderr to capture output
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> # Sort thesaurus by alphabetical order
    >>> sorter = (
    ...     SortByWordLength()
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()


"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByWordLength as UserSortByWordLength


class SortByWordLength(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            UserSortByWordLength()
            .update(**self.params.__dict__)
            .with_thesaurus_file("countries.the.txt")
            .run()
        )

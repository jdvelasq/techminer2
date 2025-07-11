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
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import CreateThesaurus, SortByAlphabet

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> # Configure and run the sorter
    >>> sorter = (
    ...     SortByAlphabet()
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = StringIO()
    >>> print(output)
    Reducing thesaurus keys
      File : example/data/thesaurus/descriptors.the.txt
      Keys reduced from 1726 to 1726
      Reduction process completed successfully
    <BLANKLINE>
    Sorting thesaurus alphabetically
      File : example/data/thesaurus/descriptors.the.txt
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        ACADEMIA
          ACADEMIA
        ACADEMICS
          ACADEMICS
        ACADEMIC_OBSERVERS
          ACADEMIC_OBSERVERS
        ACADEMIC_RESEARCH
          ACADEMIC_RESEARCH
        ACCELERATE_ACCESS
          ACCELERATE_ACCESS
        ACCEPTANCE_MODELS
          ACCEPTANCE_MODELS
        ACCESS
          ACCESS
        ACCESS_LOANS
          ACCESS_LOANS
    <BLANKLINE>
    <BLANKLINE>




"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByAlphabet as UserSortByAlphabet


class SortByAlphabet(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            UserSortByAlphabet()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )


# =============================================================================

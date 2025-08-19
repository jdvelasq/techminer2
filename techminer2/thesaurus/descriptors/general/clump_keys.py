# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Clump Keys
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import ClumpKeys, InitializeThesaurus

    >>> # Redirect stderr to capture output
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Clump the thesaurus
    >>> (
    ...     ClumpKeys(tqdm_disable=True, use_colorama=False)
    ...     .where_root_directory_is("examples/fintech/")
    ...     .run()
    ... )


    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Clumping thesaurus keys...
                      File : examples/fintech/data/thesaurus/descriptors.the.txt
      Keys reduced from 1721 to 1721
      Clumping process completed successfully
    <BLANKLINE>
    <BLANKLINE>






"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.thesaurus.user import ClumpKeys as UserClumpKeys


#
#
class ClumpKeys(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        (
            UserClumpKeys()
            .update(**self.params.__dict__)
            .update(
                field="raw_descriptors",
                thesaurus_file="descriptors.the.txt",
                root_directory=self.params.root_directory,
                tqdm_disable=self.params.tqdm_disable,
                quiet=self.params.quiet,
            )
            .run()
        )

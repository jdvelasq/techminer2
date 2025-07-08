# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Compress Thesaurus
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import CompressThesaurus, CreateThesaurus

    >>> # Redirect stderr to capture output
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> # Compress the thesaurus
    >>> compressor = (
    ...     CompressThesaurus(tqdm_disable=True)
    ...     .where_root_directory_is("example/")
    ... )
    >>> compressor.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Compressing thesaurus keys
                      File : example/data/thesaurus/descriptors.the.txt
      Keys reduced from 1726 to 1726
      Keys compressing completed successfully
    <BLANKLINE>
    <BLANKLINE>






"""

from ...._internals.mixins import ParamsMixin
from ...user import CompressThesaurus as UserCompressThesaurus


#
#
class CompressThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        (
            UserCompressThesaurus(
                field="raw_descriptors",
                thesaurus_file="descriptors.the.txt",
                root_directory=self.params.root_directory,
                tqdm_disable=self.params.tqdm_disable,
                quiet=self.params.quiet,
            ).run()
        )

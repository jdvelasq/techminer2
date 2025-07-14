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
    >>> from techminer2.thesaurus.descriptors import CompressThesaurus, InitializeThesaurus

    >>> # Redirect stderr to capture output
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="example/", quiet=True).run()

    >>> # Compress the thesaurus
    >>> compressor = (
    ...     CompressThesaurus(tqdm_disable=True, use_colorama=False)
    ...     .where_root_directory_is("example/")
    ... )
    >>> compressor.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Compressing thesaurus keys...
                      File : example/data/thesaurus/descriptors.the.txt
      Keys reduced from 1723 to 1723
      Compression process completed successfully
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
            UserCompressThesaurus()
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

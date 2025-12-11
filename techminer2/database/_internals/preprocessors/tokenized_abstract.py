# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import sys


def internal__preprocess_tokenized_abstract(root_dir):
    """:meta private:"""

    from techminer2.database._internals.operators.tokenize import internal__tokenize

    sys.stderr.write("INFO: Creating 'tokenized_abstract' column\n")
    sys.stderr.flush()

    internal__tokenize(
        source="raw_abstract",
        dest="tokenized_abstract",
        root_dir=root_dir,
    )


#
